import datetime
from typing import List, Literal, Optional

from pydantic_xml import BaseXmlModel, attr, element

from .base import GeoPosition, Id, LanguageString
from .fee import Fee


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
