import argparse
from typing import Optional

from .. import ResultList
from ..result import (
    ClassResult,
    PersonRaceResult,
    PersonResult,
    TeamMemberRaceResult,
    TeamMemberResult,
    TeamResult,
)


def _collect_race_numbers(result_list: ResultList) -> list[Optional[int]]:
    """Collect all distinct race numbers present in the result list."""
    race_numbers: set[Optional[int]] = set()
    for class_result in result_list.class_results:
        for pr in class_result.person_results:
            for rr in pr.results:
                race_numbers.add(rr.race_number)
        for tr in class_result.team_results:
            for tmr in tr.team_member_results:
                for rr in tmr.results:
                    race_numbers.add(rr.race_number)
    # Sort numerically, with None (unknown race number) last
    return sorted(race_numbers, key=lambda x: (x is None, x))


def _recalculate_person_results(person_results: list[PersonResult]) -> list[PersonResult]:
    """Recalculate positions and time_behind for person results, then sort ranked first."""
    ranked_statuses = {"OK", "Finished"}

    ranked: list[tuple[PersonResult, PersonRaceResult]] = []
    unranked: list[tuple[PersonResult, PersonRaceResult | None]] = []

    for pr in person_results:
        rr = pr.results[0] if pr.results else None
        if rr and rr.status in ranked_statuses and rr.time is not None:
            ranked.append((pr, rr))
        else:
            unranked.append((pr, rr))

    ranked.sort(key=lambda x: x[1].time)  # type: ignore[arg-type]
    winner_time = ranked[0][1].time if ranked else None

    updated_ranked: list[PersonResult] = []
    for pr, rr in ranked:
        pos = sum(1 for _, other in ranked if other.time < rr.time) + 1  # type: ignore[operator]
        time_behind = rr.time - winner_time  # type: ignore[operator]
        new_rr = rr.model_copy(
            update={"position": pos, "time_behind": time_behind, "overall_result": None}
        )
        updated_ranked.append(pr.model_copy(update={"results": [new_rr]}))

    updated_unranked: list[PersonResult] = []
    for pr, rr in unranked:
        if rr:
            new_rr = rr.model_copy(
                update={"position": None, "time_behind": None, "overall_result": None}
            )
            updated_unranked.append(pr.model_copy(update={"results": [new_rr]}))
        else:
            updated_unranked.append(pr)

    return updated_ranked + updated_unranked


def _split_for_race(result_list: ResultList, race_number: Optional[int]) -> ResultList:
    """Return a new ResultList containing only results for the given race number."""
    new_class_results: list[ClassResult] = []

    for class_result in result_list.class_results:
        # Filter and strip overall_result from person results
        new_person_results: list[PersonResult] = []
        for pr in class_result.person_results:
            race_results = [rr for rr in pr.results if rr.race_number == race_number]
            if race_results:
                new_person_results.append(pr.model_copy(update={"results": race_results}))

        # Filter and strip overall_result from team member results
        new_team_results: list[TeamResult] = []
        for tr in class_result.team_results:
            new_member_results: list[TeamMemberResult] = []
            for tmr in tr.team_member_results:
                race_results_tm: list[TeamMemberRaceResult] = [
                    rr.model_copy(update={"overall_result": None})
                    for rr in tmr.results
                    if rr.race_number == race_number
                ]
                if race_results_tm:
                    new_member_results.append(tmr.model_copy(update={"results": race_results_tm}))
            if new_member_results:
                new_team_results.append(
                    tr.model_copy(update={"team_member_results": new_member_results})
                )

        if new_person_results:
            new_person_results = _recalculate_person_results(new_person_results)

        if new_person_results or new_team_results:
            new_class_results.append(
                class_result.model_copy(
                    update={"person_results": new_person_results, "team_results": new_team_results}
                )
            )

    return result_list.model_copy(update={"class_results": new_class_results})


def main(input_path: str, output_prefix: str) -> None:
    """Load a resultlist from the input path and split into multiple files according to racenumber.

    Overall results should be removed, and the ranking in the results should be
    adjusted/recalculated and the list resorted.
    """
    result_list = ResultList.read_xml(input_path)
    race_numbers = _collect_race_numbers(result_list)

    for race_number in race_numbers:
        split = _split_for_race(result_list, race_number)
        suffix = str(race_number) if race_number is not None else "unknown"
        output_path = f"{output_prefix}_{suffix}.xml"
        split.write_xml(output_path)
        print(f"Written race {suffix} → {output_path}")


def parse_args():
    """parse arguments for main with argument parser"""
    parser = argparse.ArgumentParser(
        description="Split a MeOS multi-run ResultList XML into one file per race."
    )
    parser.add_argument("input_path", help="Path to the input ResultList XML file")
    parser.add_argument(
        "output_prefix",
        help="Output filename prefix (e.g. 'results' produces 'results_1.xml', 'results_2.xml', …)",
    )
    return parser.parse_args()


def cli() -> None:
    """Entry point for the meos-split console script."""
    args = parse_args()
    main(args.input_path, args.output_prefix)


if __name__ == "__main__":
    cli()
