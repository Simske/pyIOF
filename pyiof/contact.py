import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from .base import GeoPosition, Id, Image
from .fee import Account


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

    careof: Optional[str] = None
    street: Optional[str] = None
    zipcode: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[Country] = None
    type: Optional[str] = None
    modifytime: Optional[datetime.datetime] = None


class ContactType(Enum):
    phone_number = "PhoneNumber"
    mobile_phone_number = "MobilePhoneNumber"
    fax_number = "FaxNumber"
    email_address = "EmailAddress"
    web_address = "WebAddress"
    other = "Other"


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
    type: ContactType
    modifytime: Optional[datetime.datetime] = None


class Sex(Enum):
    m = "M"
    f = "F"
    b = "B"


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
    birthdate: Optional[datetime.date] = None
    nationality: Optional[Country] = None
    address: List[Address] = field(default_factory=list)
    contact: List[Contact] = field(default_factory=list)
    sex: Optional[Sex] = None
    modifytime: Optional[datetime.datetime] = None


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


class OrganisationType(Enum):
    iof = "IOF"
    iof_region = "IOFRegion"
    national_federation = "NationalFederation"
    national_region = "NationalREgion"
    club = "Club"
    school = "School"
    company = "Company"
    military = "Military"
    other = "Other"


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
    id: Optional[Id] = None
    shortname: Optional[str] = None
    medianame: Optional[str] = None
    parent_organisation_id: Optional[Id] = None
    country: Optional[Country] = None
    address: List[Address] = field(default_factory=list)
    contact: List[Contact] = field(default_factory=list)
    position: Optional[GeoPosition] = None
    account: List[Account] = field(default_factory=list)
    role: List[Role] = field(default_factory=list)
    logotype: List[Image] = field(default_factory=list)
    type: Optional[OrganisationType] = None
    modifytime: Optional[datetime.datetime] = None
