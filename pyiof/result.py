import datetime
from enum import Enum
from typing import List, Optional

from dataclass import dataclass, field

from .base import Id


class ResultStatus(Enum):
    """Enum: The result status of the person or team at the time of the result generation.

    Attributes:
        ok: Finished and validated.
        finished: Finished but not yet validated.
        missing_punch: Missing punch.
        disqualified: Disqualified (for some other reason than a missing punch).
        did_not_finishDid not finish (i.e. conciously cancelling the race after having started, in contrast to MissingPunch).
        active: Currently on course.
        inactive: Has not yet started.
        over_time: Overtime, i.e. did not finish within the maximum time set by the organiser.
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
