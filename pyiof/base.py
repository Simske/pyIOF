import datetime
from dataclasses import dataclass, field
from typing import ClassVar, List


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
