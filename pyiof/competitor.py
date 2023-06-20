import datetime
from typing import List, Literal, Optional

from pydantic_xml import BaseXmlModel, attr, element

from .base import Id, Score
from .class_ import Class_
from .contact import Organisation, Person
from .course import ControlAnswer, Route, SimpleCourse
from .fee import AssignedFee
from .misc import ServiceRequest


class ControlCard(BaseXmlModel):
    """ControlCard

    Attributes:
        id (str): The unique identifier of the control card, i.e. card number.
        punchingsystem (str, optional): The manufacturer of the punching
                                        system, e.g. 'SI' or 'Emit'.
        modifytime (datetime, optional)
    """

    id: str
    punchingsystem: Optional[str] = attr(name="punchingSystem")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class Competitor(BaseXmlModel):
    """Represents information about a person in a competition context,
    i.e. including organisation and control card.

    Attributes:
        person: Person
        organisation (List[Organisation]): The organisations that the
            person is member of.
        controlcards (List[ControlCard]): The default control cards of the competitor.
        class_ (List[Claas_]): The default classes of the competitor.
        score (List[Score]): Any scores, e.g. ranking scores, for the person.
        modifytime (datetime.datetime, optional)
    """

    person: Person = element(tag="Person")
    organisation: List[Organisation] = element(tag="Organisation", default_factory=list)
    controlcards: List[ControlCard] = element(tag="ControlCard", default_factory=list)
    class_: List[Class_] = element(tag="Class", default_factory=list)
    score: List[Score] = element(tag="Class", default_factory=list)
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class StartTimeAllocationRequest(BaseXmlModel):
    """Used to state start time allocation requests. It consists of a possible
    reference Organisation or Person and the allocation request, e.g. late start
    or grouped with the reference Organisation/Person. This way it is possible
    to state requests to the event organizer so that e.g. all members of an
    organisation has start times close to each other - or parents have start
    times far from each other. It is totally up to the event software and
    organizers whether they will support such requests.
    """

    organisation: Optional[Organisation] = element(tag="Organisation")
    person: Optional[Person] = element(tag="Person")
    type: Optional[
        Literal["Normal", "EarlyStart", "LateStart", "SeparatedFrom", "GroupedWith"]
    ] = attr(default="Normal")


class PersonEntry(BaseXmlModel):
    """
    Defines an event entry for a person.
    """

    id: Optional[Id] = element(name="Id")
    person: Person = element(name="Person")
    organisation: Optional[Organisation] = element(tag="Organisation")
    controlcards: List[ControlCard] = element(tag="ControlCard", default_factory=list)
    scores: List[Score] = element(tag="Score", default_factory=list)
    classes: List[Class_] = element(tag="Class", default_factory=list)
    race_number: List[int] = element(tag="RaceNumber", default_factory=list)
    assigned_fee: List[AssignedFee] = element(tag="AssignedFee", default_factory=list)
    service_requests: List[ServiceRequest] = element(
        tag="ServiceRequest", default_factory=list
    )
    starttime_allocation_request: Optional[StartTimeAllocationRequest] = element(
        tag="StartTimeAllocationRequest"
    )
    entry_time: Optional[datetime.datetime] = element(tag="EntryTime")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class TeamEntryPerson(BaseXmlModel):
    """Defines a person that is part of a team entry."""

    person: Optional[Person] = element(tag="Person")
    organisation: Optional[Organisation] = element(tag="Organisation")
    leg: Optional[int] = element(tag="Leg")
    leg_order: Optional[int] = element(tag="LegOrder")
    control_card: List[ControlCard] = element(tag="ControlCard", default_factory=list)
    score: List[Score] = element(tag="Score", default_factory=list)
    assigned_fees: List[AssignedFee] = element(tag="AssignedFee", default_factory=list)


class TeamEntry(BaseXmlModel):
    """Defines an event entry for a team."""

    id: Optional[Id] = element(tag="Id")
    name: str = element(tag="Name")
    organisations: List[Organisation] = element(
        tag="Organisation", default_factory=list
    )
    team_entry_persons: List[TeamEntryPerson] = element(
        tag="TeamEntryPerson", default_factory=list
    )
    class_: List[Class_] = element(tag="Class", default_factory=list)
    race: List[int] = element(tag="Race", default_factory=list)
    assigned_fees: List[AssignedFee] = element(tag="AssignedFee", default_factory=list)
    service_requests: List[ServiceRequest] = element(
        tag="ServiceRequest", default_factory=list
    )
    start_time_allocation_request: Optional[StartTimeAllocationRequest] = element(
        tag="StartTimeAllocationRequest"
    )
    contact_information: Optional[str] = element(tag="ContactInformation")
    entry_time: Optional[datetime.datetime] = element(tag="EntryTime")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class PersonRaceStart(BaseXmlModel):
    """Start information for a person in a race."""

    bib_number: Optional[str] = element(tag="BibNumber")
    start_time: Optional[datetime.datetime] = element(tag="StartTime")
    course: Optional[SimpleCourse] = element(tag="Course")
    control_card: List[ControlCard] = element(tag="ControlCard", default_factory=list)
    assigned_fees: List[AssignedFee] = element(tag="AssignedFee", default_factory=list)
    service_requests: List[ServiceRequest] = element(
        tag="ServiceRequest", default_factory=list
    )
    race_number: Optional[int] = attr(name="raceNumber")


class PersonStart(BaseXmlModel):
    """
    Start information for an individual competitor, including e.g. start time and bib number.
    """

    entry_id: Optional[Id] = element(tag="EntryId")
    person: Optional[Person] = element(tag="Person")
    organisation: Optional[Organisation] = element(tag="Organisation")
    starts: List[PersonRaceStart] = element(tag="Start")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


"""The result status of the person or team at the time of the result generation."""
ResultStatus = Literal[
    "OK",
    "Finished",
    "MissingPunch",
    "Disqualified",
    "DidNotFinish",
    "Active",
    "Inactive",
    "OverTime",
    "SportingWithdrawal",
    "NotCompeting",
    "Moved",
    "MovedUp",
    "DidNotStart",
    "DidNotEnter",
    "Cancelled",
]


class OverallResult(BaseXmlModel):
    time: Optional[float] = element(tag="Time")
    time_behind: Optional[float] = element(tag="TimeBehind")
    position: Optional[int] = element(tag="Position")
    status: ResultStatus = element(tag="Status")
    scores: List[Score] = element(tag="Score", default_factory=list)


class SplitTime(BaseXmlModel):
    """Defines a split time at a control."""

    control_card: str = element(tag="ControlCode")
    time: Optional[float] = element(tag="Time")
    status: Literal["OK", "Missing", "Additional"] = element(tag="Status", default="OK")


class PersonRaceResult(BaseXmlModel):
    """Result information for a person in a race."""

    bib_number: Optional[str] = element(tag="BibNumber")
    start_time: Optional[datetime.datetime] = element(tag="StartTime")
    finish_time: Optional[datetime.datetime] = element(tag="FinishTime")
    time: Optional[float] = element(tag="Time")
    time_behind: Optional[float] = element(tag="TimeBehind")
    position: Optional[int] = element(tag="Position")
    status: ResultStatus = element(tag="Status")
    scores: List[Score] = element(tag="Score", default_factory=list)
    overall_result: Optional[OverallResult] = element(tag="OverallResult")
    course: Optional[SimpleCourse] = element(tag="Course")
    split_time: List[SplitTime] = element(tag="SplitTime")
    control_answers: List[ControlAnswer] = element(
        tag="ControlAnswer", default_factory=list
    )
    route: Optional[Route] = element(tag="Route")
    control_card: List[ControlCard] = element(tag="ControlCard", default_factory=list)
    assigned_fees: List[AssignedFee] = element(tag="AssignedFee", default_factory=list)
    service_requests: List[ServiceRequest] = element(
        tag="ServiceRequest", default_factory=list
    )
    race_number: Optional[int] = attr(name="raceNumber")
