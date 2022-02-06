import datetime
from dataclasses import dataclass, field
from typing import ClassVar, List, Optional
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

@dataclass
class SimpleCourse:
    """Defines a course, excluding controls.

    Attributes:
        id (Id)
        name (str, optional): The name of the course.
        course_family (str, optional): The family or group of forked courses that the course is part of.
        length (float, optional): The length of the course, in meters.
        climb (float, optional): The climb of the course, in meters, along the expected best route choice.
        number_of_controls (int, optional): The number of controls in the course, excluding start and finish.
    """
    id: Id = None
    name: str = None
    course_family: str = None
    length: float = None
    climb: float = None
    number_of_controls: int = None

class Unit(Enum):
    """Enum class for units

    Attributes:
        mm: Millimeters, used when the map is represented by a printed piece of paper.
        px: Pixels, used when the map is represented by a digital image.
    """
    mm = "mm"
    px = "px"

@dataclass
class MapPosition:
    """Defines a position in a map's coordinate system.

    Attributes:
        x (float): The number of units right of the center of the coordinate system.
        y (float): The number of units below the center of the coordinate system.
        unit (Unit, optional): The type of unit used, defaults to Unit.mm
    """
    x: float
    y: float
    unit: Unit = Unit.mm

class ControlType(Enum):
    """The type of a control: (ordinary) control, start, finish, crossing point or end of marked route.

    Attributes:
        control
        start
        finish
        crossing_point
        end_of_marked_route
    """
    control = "Control"
    start = "Start"
    finish = "Finish"
    crossing_point = "CrossingPoint"
    end_of_marked_route = "EndOfMarkedRoute"

@dataclass
class Control:
    """Defines a control, without any relationship to a particular course.

    Attributes:
        id (Id, optional): The code of the control.
        punching_unit_id (list[Id], optional): If the control has multiple punching units with separate codes, specify all these codes using elements of this kind. Omit this element if there is a single punching unit whose code is the same as the control code.
        name (list[LanguageString], optional): The name of the control, used for e.g. online controls ('spectator control', 'prewarning').
        position (GeoPosition, optional): The geographical position of the control.
        map_position (MapPosition, optional): The position of the control according to tha map's coordinate system.
        type (ControlType): The type of the control: (ordinary) control, start, finish, crossing point or end of marked route. This attribute can be overridden on the CourseControl level. Defaults to ControlType.control
        modifytime (datetime.datetime, optional)
    """
    id: Id
    punching_unit_id: List[Id] = field(default_factory=list)
    name: List[LanguageString] = field(default_factory=list)
    position: GeoPosition = None
    map_position: MapPosition = None
    type: ControlType = ControlType.control
    modifytime: datetime.datetime = None

@dataclass
class RaceClass:
    """Information about a class with respect to a race.

    Attributes:
        punching_system (list[str]): The punching system used for the class at the race. Multiple punching systems can be specified, e.g. one for punch checking and another for timing.
        team_fee (list[Fee]): The entry fees for a team as a whole taking part in this class. Use the Fee element to specify a fee for an individual competitor in the team. Use the TeamFee subelement of the Class element to specify a fee on event level.
        fee (list[Fee]): The entry fees for an individual competitor taking part in the race class. Use the TeamFee element to specify a fee for the team as a whole. Use the Fee subelement of the Class element to specify a fee on event level.
        first_start (datetime.datetime, optional)
        status (RaceClassStatus, optional): The status of the race, e.g. if results should be considered invalid due to misplaced constrols.
        course (list[SimpleCourse]): The courses assigned to this class. For a mass-start event or a relay event, there are usually multiple courses per class due to the usage of spreading methods.
        online_controls (list[Control]): The controls that are online controls for this class.
        race_number (int, optional): The ordinal number of the race that the information belongs to for a multi-race event, starting at 1.
        max_number_of_competitors (int, optional): The maximum number of competitors that are allowed to take part in the race class. A competitor corresponds to a person (if an individual event) or a team (if a team or relay event). This attribute overrides the maxNumberOfCompetitors attribute in the Class element.
        modifytime (datetime.datetime, optional)
    """
    punching_system: List[str] = field(default_factory=list)
    team_fee: List[Fee] = field(default_factory=list)
    fee: List[Fee] = field(default_factory=list)
    first_start: datetime.datetime = None
    status: RaceClassStatus = None
    course: List[SimpleCourse] = field(default_factory=list)
    online_controls: List[Control] = field(default_factory=list)
    race_number: int = None
    max_number_of_competitors: int = None
    modifytime: datetime.datetime = None


class Sex(Enum):
    m = "M"
    f = "F"
    b = "B"

class ResultListMode(Enum):
    """Defines the kind of information to include in the result list, and how to sort it. For example, the result list of a beginner's class may include just 

    Attributes:
        default: The result list should include place and time for each competitor, and be ordered by place.
        unordered: The result list should include place and time for each competitor, but be unordered with respect to times (e.g. sorted by competitor name).
        unordered_no_times: The result list should not include any places and times, and be unordered with respect to times (e.g. sorted by competitor name).
    """
    default = "Default"
    unordered = "Unordered"
    unordered_no_times = "UnorderedNoTimes"

@dataclass
class Class_:
    name: str
    id: Id = None
    shortname: str = ""
    classtype: List[ClassType] = field(default_factory=list)
    leg: List[Leg] = field(default_factory=list)
    team_fee: List[Fee] = field(default_factory=list)
    fee: List[Fee] = field(default_factory=list)
    status: EventClassStatus = EventClassStatus.normal
    raceclass: List[RaceClass] = field(default_factory=list)
    too_few_entries_substitute_class: Class_ = None
    too_many_entries_substitue_class: Class_ = None
    min_age: int = None
    max_age: int = None
    sex: Sex = None
    min_number_of_team_members: int = None
    max_number_of_team_members: int = None
    min_team_age: int = None
    max_team_age: int = None
    number_of_competitors: int = None
    max_number_of_competitors: int = None
    resultlist_mode: ResultListMode

@dataclass
class Score:
    """The score earned in an event for some purpose, e.g. a ranking list.
    The 'type' attribute is used to specify which purpose.
    """
    score: float
    type: Optional[str] = None




@dataclass
class Competitor:
    """Represents information about a person in a competition context, i.e. including organisation and control card.

    Attributes:
        person: Person
        organisation (List[Organisation]): The organisations that the person is member of.
        controlcards (List[ControlCard]): The default control cards of the competitor.
        class_ (List[Claas_]): The default classes of the competitor.
        score (List[Score]): Any scores, e.g. ranking scores, for the person.
        modifytime (datetime.datetime, optional)
    """
    person: Person
    organisation: List[Organisation] = field(default_factory=list)
    controlcards: List[ControlCard] = field(default_factory=list)
    class_: List[Class_] = field(default_factory=list)
    score: List[Score] = field(default_factory=list)
    modifytime: Optional[datetime.datetime] = None
