import datetime
from typing import List, Literal, Optional

from pydantic_xml import BaseXmlModel, attr, element

from .base import GeoPosition, Id, LanguageString
from .class_ import Class_, Race
from .competitor import Organisation, Person, Role
from .contact import EntryReceiver
from .fee import Account, Fee


class EventURL(BaseXmlModel):
    url: str
    type: Literal["Website", "StartList", "ResultList", "Other"] = attr()


class InformationItem(BaseXmlModel):
    """Defines a general-purpose information object containing a title and content."""

    title: str = element(tag="Title")
    content: str = element(tag="Content")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class Service(BaseXmlModel):
    """Defines a general purpose service request, e.g. for rental card or accomodation."""

    id: Optional[Id] = element(tag="Id")
    name: List[LanguageString] = element(tag="Name")
    fee: List[Fee] = element(tag="Fee", default_factory=list)
    description: List[LanguageString] = element(tag="Description", default_factory=list)
    max_number: Optional[float] = element(tag="MaxNumber")
    requested_numebr: Optional[float] = element(tag="RequestedNumber")
    type: Optional[str] = attr()
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class ServiceRequest(BaseXmlModel):
    id: Optional[Id] = element(tag="Id")
    service: Service = element(tag="Service")
    requested_quantity: float = element(tag="RequestedQuantity")
    deliverd_quantity: float = element(tag="DeliveredQuantity")
    comment: Optional[str] = element(tag="Comment")
    assigned_fee: List[Fee] = element(tag="AssignedFee")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class Schedule(BaseXmlModel):
    """Defines the schedule of sub-events that comprise the entire orienteering event, e.g. banquets, social events and awards ceremonies."""

    start_time: datetime.datetime = element(tag="StartTime")
    end_time: Optional[datetime.datetime] = element(tag="EndTime")
    name: str = element(tag="Name")
    venue: Optional[str] = element(tag="Venue")
    position: Optional[GeoPosition] = element(tag="Position")
    details: Optional[str] = element(tag="Details")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


EventStatus = Literal[
    "Planned", "Applied", "Proposed", "Sanctioned", "Canceled", "Rescheduled"
]

EventClassification = Literal["International", "National", "Regional", "Local", "Club"]

EventForm = Literal["Individual", "Team", "Relay"]

RaceDiscipline = Literal["Sprint", "Middle", "Long", "Ultralong", "Other"]


class Event(BaseXmlModel):
    id: Optional[Id] = element(tag="Id")
    name: str = element(tag="Name")
    start_time: Optional[datetime.datetime] = element(tag="StartTime")
    end_time: Optional[datetime.datetime] = element(tag="EndTime")
    event_status: Optional[EventStatus] = element(tag="EventStatus")
    classification: Optional[EventClassification] = element(tag="Classification")
    forms: List[EventForm] = element(tag="Form", default_factory=list)
    organisers: List[Organisation] = element(tag="Organiser", default_factory=list)
    officials: List[Role] = element(tag="Official", default_factory=list)
    classes: List[Class_] = element(tag="Class", default_factory=list)
    races: List[Race] = element(tag="Race", default_factory=list)
    entry_receiver: Optional[EntryReceiver] = element(tag="EntryReceiver")
    services: List[Service] = element(tag="Service", default_factory=list)
    accounts: List[Account] = element(tag="Account", default_factory=list)
    urls: List[EventURL] = element(tag="EventURL", default_factory=list)
    information: List[InformationItem] = element(
        tag="InformationItem", default_factory=list
    )
    schedules: List[Schedule] = element(tag="Schedule", default_factory=list)
    news: List[InformationItem] = element(tag="News", default_factory=list)
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class PersonServiceRequest(BaseXmlModel):
    """Service requests made by a person."""

    person: Person = element(tag="Person")
    service_requests: List[ServiceRequest] = element(tag="ServiceRequests")


class OrganisationServiceRequest(BaseXmlModel):
    """
    Service requests made by an organisation.
    """

    organisation: Organisation = element(tag="Organisation")
    service_requests: List[ServiceRequest] = element(
        tag="ServiceRequest", default_factory=list
    )
    person_service_requests: List[PersonServiceRequest] = element(
        tag="PersonServiceRequest", default_factory=list
    )
