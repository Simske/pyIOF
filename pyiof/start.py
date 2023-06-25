import datetime
from typing import List, Optional

from pydantic import conlist

from .base import Id
from .class_ import Class_
from .competitor import ControlCard, Organisation, Person
from .course import SimpleCourse, SimpleRaceCourse, StartName
from .fee import AssignedFee
from .misc import ServiceRequest
from .xml_base import BaseXmlModel, attr, element


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
    starts: conlist(item_type=PersonRaceStart, min_items=1) = element(tag="Start")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class TeamMemberRaceStart(BaseXmlModel):
    """Start information for a team member in a race."""

    leg: Optional[int] = element(tag="Leg")
    leg_order: Optional[int] = element(tag="LegOrder")
    bib_number: Optional[str] = element(tag="BibNumber")
    start_time: Optional[datetime.datetime] = element(tag="StartTime")
    course: Optional[SimpleCourse] = element(tag="Course")
    control_card: List[ControlCard] = element(tag="ControlCard", default_factory=list)
    assigned_fees: List[AssignedFee] = element(tag="AssignedFee", default_factory=list)
    service_requests: List[ServiceRequest] = element(
        tag="ServiceRequest", default_factory=list
    )
    race_number: Optional[int] = attr(name="raceNumber")


class TeamMemberStart(BaseXmlModel):
    """Start information for an individual competitor, including e.g. start time
    and bib number.
    """

    entry_id: Optional[Id] = element(tag="EntryId")
    person: Optional[Person] = element(tag="Person")
    organisation: Optional[Organisation] = element(tag="Organisation")
    starts: conlist(item_type=TeamMemberRaceStart, min_items=1) = element(tag="Start")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class TeamStart(BaseXmlModel):
    """Start information for a team, including e.g. team name, start times
    and bib numbers.
    """

    entry_id: Optional[Id] = element(tag="EntryId")
    name: Optional[str] = element(tag="Name")
    organisations: List[Organisation] = element(
        tag="Organisation", default_factory=list
    )
    bib_number: Optional[str] = element(tag="BibNumber")
    team_member_starts: List[TeamMemberStart] = element(
        tag="TeamMemberStart", default_factory=list
    )
    assigned_fees: List[AssignedFee] = element(tag="AssignedFee", default_factory=list)
    service_requests: List[ServiceRequest] = element(
        tag="ServiceRequest", default_factory=list
    )
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class ClassStart(BaseXmlModel):
    """The start list of a single class containing either individual start times
    or team start times.
    """

    class_: Class_ = element(tag="Class")
    courses: List[SimpleRaceCourse] = element(tag="Course", default_factory=list)
    start_name: List[StartName] = element(tag="StartName", default_factory=list)
    person_starts: List[PersonStart] = element(tag="PersonStart", default_factory=list)
    team_starts: List[TeamStart] = element(tag="TeamStart", default_factory=list)
    time_resolution: float = attr(name="timeResolution", default=1)
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")
