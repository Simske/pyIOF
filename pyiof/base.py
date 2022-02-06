import datetime
from dataclasses import dataclass, field
from typing import ClassVar, List
from decimal import Decimal
from enum import Enum


@dataclass
class Id:
    """Identifier element, used extensively. The id should be known
    and common for both systems taking part in the data exchange.

    Attributes:
        type (str, optional): The issuer of the identity, e.g. World Ranking List.
    """

    id: str
    type: str = None


@dataclass
class PersonName:
    family: str
    given: str


@dataclass
class Country:
    """Defines the name of the country

    Attributes:
        name: Name of the country
        code: The International Olympic Committee's 3-letter code of the country
              as stated in https://en.wikipedia.org/wiki/List_of_IOC_country_codes.
              Note that several of the IOC codes are different from the standard
              ISO 3166-1 alpha-3 codes.
    """

    name: str
    code: str


@dataclass
class Address:
    """The postal address of a person or organisation.

    Attributes:
        careof (str, optional)
        street (str, optional)
        zipcode (str, optional)
        city (str, optional)
        state (str, optional)
        country (Country, optional)
        type (str, optional): The address type, e.g. visitor address or invoice address.
    """

    careof: str = None
    street: str = None
    zipcode: str = None
    city: str = None
    state: str = None
    country: Country = None
    type: str = None
    modifytime: datetime.datetime = None


@dataclass
class Contact:
    """Contact information for a person, organisation or other entity.

    Attributes:
        contact (str): contact information
        type (str): type of contact, one of {PhoneNumber, MobilePhoneNumber, FaxNumber,
                    EmailAddress, WebAddress, Other}
        modifyTime (datetime, optional)
    """

    contact: str
    type: str
    modifytime: datetime.datetime = None
    allowed_types: ClassVar = (
        "PhoneNumber",
        "MobilePhoneNumber",
        "FaxNumber",
        "EmailAddress",
        "WebAddress",
        "Other",
    )

    def __post_init__(self):
        if self.type not in self.allowed_types:
            raise RuntimeError(f"Invalid Type {self.type} for `Contact`")


@dataclass
class Person:
    """Represents a person.
    This could either be a competitor (see the Competitor element)
    or contact persons in an organisation (see the Organisation element).

    Attributes:
        Id
    """

    id: List[Id]
    name: PersonName
    birthdate: datetime.date = None
    nationality: Country = None
    address: List[Address] = field(default_factory=list)
    contact: List[Contact] = field(default_factory=list)
    sex: str = None
    modifytime: datetime.datetime = None


@dataclass
class ControlCard:
    """ControlCard

    Attributes:
        id (str): The unique identifier of the control card, i.e. card number.
        punchingsystem (str, optional): The manufacturer of the punching
                                        system, e.g. 'SI' or 'Emit'.
        modifytime (datetime, optional)
    """

    id: str
    punchingsystem: str = None
    modifytime: datetime.datetime = None


@dataclass
class Score:
    """Score

    The score earned in an event for some purpose, e.g. a ranking list.
    Attributes:
        score (double): The actual score
        type (str): Purpose of score, e.g. name of ranking list
    """

    score: float
    type: str = None


@dataclass
class GeoPosition:
    """Defines a geographical position, e.g. of a control.

    Attributes:
        lng (double): The longitude
        lat (double): The latitude
        alt (double): The altitude (elevation above sea level), in meters
    """

    lng: float
    lat: float
    alt: float = None


@dataclass
class Account:
    """The bank account of an organisation or an event.

    Attributes:
        account (str): account information
        type (str, optional): The account type.
    """

    account: str
    type: str = None


@dataclass
class Role:
    """Role

    A role defines a connection between a person and some kind of task,
    responsibility or engagement, e.g. being a course setter at an event.

    Attributes:
        person (Person): person which has the role
        type (str): The type of role
    """

    person: Person
    type: str


@dataclass
class Image:
    """Image file

    Defines an image file, either as a link (use the url attribute)
    or as base64-encoded binary data.

    Attributes:
        data: base64 encoded data
        mediatype (str): The type of the image file, e.g. image/jpeg. Refer to
                   https://www.iana.org/assignments/media-types/media-types.xhtml#image
                   for available media types.
        width (int, optional): The width of the image in pixels.
        height (int, optional): The height of the image in pixels.
        resolution (double, optional): The resolution of the image in dpi.
    """

    data: str
    mediatype: str
    url: str = None
    width: int = None
    height: int = None
    resolution: float = None


@dataclass
class Organisation:
    """Organisation

    Information about an organisation, i.e. address, contact person(s) etc.
    An organisation is a general term including federations, clubs, etc.

    Attributes:
        id (Id, optional)
        name (str): Full name of the organisation
        shortname
    """

    name: str
    id: Id = None
    shortname: str = None
    medianame: str = None
    parent_organisation_id: Id = None
    country: Country = None
    address: List[Address] = field(default_factory=list)
    contact: List[Contact] = field(default_factory=list)
    position: GeoPosition = None
    account: List[Account] = field(default_factory=list)
    role: List[Role] = field(default_factory=list)
    logotype: List[Image] = field(default_factory=list)
    type: str = None
    modifytime: datetime.datetime = None
    allowed_types: ClassVar = (
        "IOF",
        "IOFRegion",
        "NationalFederation",
        "NationalREgion",
        "Club",
        "School",
        "Company",
        "Military",
        "Other",
    )

    def __post_init__(self):
        if self.type not in self.allowed_types:
            raise RuntimeError(f"Invalid Type {self.type} for `Organisation`")


@dataclass
class DateAndOptionalTime:
    """Defines a point in time which either is known by date and time,
    or just by date. May be used for event dates, when the event date is
    decided before the time of the first start.

    Attributes:
        date (datetime.date): The date part, expressed in ISO 8601 format.
        time (datetime.time, optional): The time part, expressed in ISO 8601 format.
    """

    date: datetime.date
    time: datetime.time = None


@dataclass
class LanguageString:
    """Defines a text that is given in a particular language.

    Attributes:
        text (str)
        language (str, optional): The ISO 639-1 two-letter code of the language
            as stated in https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes.
    """


@dataclass
class EventForm:
    form: str
    allowed_forms: ClassVar = ("Individual", "Team", "Relay")

    def __post_init__(self):
        if self.type not in self.allowed_forms:
            raise RuntimeError(f"Invalid form {self.type} for Event")

@dataclass
class ClassType:
    """Defines a class type, which is used to group classes in categories.

    Attributes:
        id (Id, optional)
        name (str): The name of the class type
        modifytime (datetime, optional)
    """
    name: str
    id: Id = None
    modifytime: datetime.datetime = None

@dataclass
class Leg:
    """Defines extra information for a relay leg.

    Attributes:
        name (str, optional): The name of the leg, if not sequentially named.
        min_number_of_competitors (int, default=1): The minimum number of competitors in case of a parallel leg.
        max_number_of_competitors (int, default=1): The maximum number of competitors in case of a parallel leg.
    """
    name: str = None
    min_number_of_competitors: int = 1
    max_number_of_competitors: int = 1

@dataclass
class Amount:
    """Defines a monetary amount.

    Attributes:
        amount (decimal.Decimal)
        currency (str, optional)
    """
    amount: Decimal
    currency: str = None

@dataclass
class Fee:
    """A fee that applies when entering a class at a race or ordering a service.

    Attributes:
        id (Id)
        name (list[LanguageString]): A describing name of the fee, e.g. 'Late entry fee', at least one entry
        amount (Amount, optional): The fee amount, optionally including currency code. This element must not be present if a Percentage element exists.
        taxable_amount (Amount, optional): The fee amount that is taxable, i.e. considered when calculating taxes for an event. This element must not be present if a Percentage element exists, or if an Amount element does not exist.
        percentage (double, optional): The percentage to increase or decrease already existing fees in a fee list with. This element must not be present if an Amount element exists.
        taxable_percentage (double, optional): The percentage to increase or decrease already existing taxable fees in a fee list with. This element must not be present if an Amount element exists, or if a Percentage element does not exist.
        valid_from_time (datetime.datetime, optional):  The time when the fee takes effect.
        valid_to_time (datetime.datetime, optional): The time when the fee expires.
        from_birth_date (datetime.date, optional): The start of the birth date interval that the fee should be applied to. Omit if no lower birth date restriction.
        to_birth_date (datetime.date, optional): The end of the birth date interval that the fee should be applied to. Omit if no upper birth date restriction.
        type (str, optional): The type of Fee. Allowed values: Normal, Late. Default=Normal
    """
    name: List[LanguageString]
    id: Id = None
    amount: Amount = None
    taxable_amount: Amount = None
    percentage: float = None
    taxable_percentage: float = None
    valid_from_time: datetime.datetime = None
    valid_to_time: datetime.datetime = None
    from_date_of_birth: datetime.date = None
    to_date_of_birth: datetime.date = None
    type: str = None
    allowed_types: ClassVar[List[str]] = ["normal", "late"]

    def __post_init__(self):
        if self.type not in self.allowed_types:
            raise RuntimeError(f"Invalid type {self.type} for Fee")
        if self.amount is not None and self.percentage is not None:
            raise RuntimeError(f"Fee: only one of amount or percentage can be defined")
        if self.taxable_amount is not None and self.amount is None:
            raise RuntimeError(f"Fee: taxable_amount only applicable if amount is defined")
        if self.taxable_percentage is not None and self.amount is None:
            raise RuntimeError(f"Fee: taxable_percentage only applicable if percentage is defined")

class EventClassStatus(Enum):
    """The status of the class - enum

    Attributes:
        normal: The default status.
        divided: The class has been divided in two or more classes due to a large number of entries.
        joined: The class has been joined with another class due to a small number of entries.
        invalidated: The results are considered invalid due to technical issues such as misplaced controls. Entry fees are not refunded.
        invalidated_not_fee: The results are considered invalid due to technical issues such as misplaced controls. Entry fees are refunded.
    """
    normal = "Normal"
    divided = "Divided"
    joined = "Joined"
    invalidated = "Invalidated"
    invalidated_no_fee = "InvalidatedNoFee"

class RaceClassStatus(Enum):
    """The status of a certain race in the class.

    Attributes:
        start_times_not_allocated: The start list draw has not been made for this class in this race
        start_times_allocated: The start list draw has been made for this class in this race.
        not_used: The class is not organised in this race, e.g. for classes that are organised in only some of the races in a multi-race event.
        completed: The result list is complete for this class in this race.
        invalidated: The results are considered invalid due to technical issues such as misplaced controls. Entry fees are not refunded.
        invalidated_no_fee: The results are considered invalid due to technical issues such as misplaced controls. Entry fees are refunded.
    """
    start_times_not_allocated = "StartTimesNotAllocated"
    start_times_allocated = "StartTimesAllocated"
    not_used = "NotUsed"
    completed = "Completed"
    invalidated = "Invalidated"
    invalidated_no_fee = "InvalidatedNoFee"
