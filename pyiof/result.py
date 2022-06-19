import datetime
from enum import Enum
from typing import List, Optional

from dataclass import dataclass, field

from .base import Id
from .competitor import ControlCard
from .course import SimpleCourse
from .fee import AssignedFee


class ResultStatus(Enum):
    """Enum: The result status of the person or team at the time of
    the result generation.

    Attributes:
        ok: Finished and validated.
        finished: Finished but not yet validated.
        missing_punch: Missing punch.
        disqualified: Disqualified (for some other reason than a missing punch).
        did_not_finishDid not finish (i.e. conciously cancelling the race
            after having started, in contrast to MissingPunch).
        active: Currently on course.
        inactive: Has not yet started.
        over_time: Overtime, i.e. did not finish within the maximum
            time set by the organiser.
        sporting_withdrawal: Sporting withdrawal (e.g. helping an injured competitor).
        not_competing: Not competing (i.e. running outside the competition).
        moved: Moved to another class.
        moved_up: Moved to a "better" class, in case of entry restrictions.
        did_not_start: Did not start (in this race).
        did_not_enter: Did not enter (in this race).
        cancelled: The competitor has cancelled his/hers entry.
    """

    ok = "OK"
    finished = "Finished"
    missing_punch = "MissingPunch"
    disqualified = "Disqualified"
    did_not_finish = "DidNotFinish"
    active = "Active"
    inactive = "Inactive"
    over_time = "OverTime"
    sporting_withdrawal = "SportingWithdrawal"
    not_competing = "NotCompeting"
    moved = "Moved"
    moved_up = "MovedUp"
    did_not_start = "DidNotStart"
    did_not_enter = "DidNotEnter"
    cancelled = "Cancelled"


class Score(double):
    """The score earned in an event for some purpose, e.g. a ranking list.
    Subclass of double

    Attributes:
        type (str, optional): Score purpose
    """

    type: Optional(str) = None


class SplitTimeStatus(Enum):
    """Status enum for SplitTime

    Attributes:
        ok: Control belongs to the course and has been punched
            (either by electronical punching or pin punching).
            If the time is not available or invalid, omit the Time element.
        missing: Control belongs to the course but has not been punched.
        additional: Control does not belong to the course,
            but the competitor has punched it.
    """

    ok = "OK"
    missing = "Missing"
    additional = "Additional"


@dataclass
class SplitTime:
    """Defines a split time at a control.

    Attributes:
        control_code (str): The code of the control.
        time (datetime.timedelta, optional): The time, in seconds, elapsed from start to punching the control.
        status (SplitTimeStatus, optional): Status of control (OK, misssing, additional).
    """

    control_code: str
    time: Optional[datetime.timedelta] = None
    status: Optional[SplitTimeStatus] = None


@dataclass
class OverallResult:
    """Overall result for races with more than one race

    Attributes:
        status (ResultStatus): The status of the result.
        time (timedelta, optional): The time that is shown in the result list.
        time_behind (timedelta, optional): The time that the the person or team is
            behind the leader or winner.
        position (int, optional): The position in the result list for the person or
            team that the result belongs to. This element should only be present
            when the Status element is set to OK.
        score (list[Score], optional): Any scores that are attached to the result,
            e.g. World Ranking points.
    """

    status: ResultStatus
    time: Optional[datetime.timedelta] = None
    time_behind: Optional[datetime.timedelta] = None
    position: Optional[int] = None
    score: Optional[List[Score]] = None
