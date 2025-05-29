from pathlib import Path

import pytest

import pyiof


@pytest.mark.parametrize(
    ("base_object", "example_file_dir"),
    [
        (pyiof.CompetitorList, "competitorlist"),
        (pyiof.OrganisationList, "organisationlist"),
        (pyiof.EventList, "eventlist"),
        (pyiof.ClassList, "classlist"),
        (pyiof.EntryList, "entrylist"),
        (pyiof.CourseData, "coursedata"),
        (pyiof.StartList, "startlist"),
        (pyiof.ResultList, "resultlist"),
        (pyiof.ServiceRequestList, "servicerequestlist"),
        (pyiof.ControlCardList, "controlcardlist"),
    ],
)
def test_parsing_xml(base_object, example_file_dir: str):
    base_path = Path(__file__).parents[0] / "testdata" / example_file_dir
    for path in base_path.iterdir():
        base_object.read_xml(str(path))
