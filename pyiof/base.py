import datetime
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional


@dataclass
class Id:
    """Identifier element, used extensively. The id should be known
    and common for both systems taking part in the data exchange.

    Attributes:
        type (str, optional): The issuer of the identity, e.g. World Ranking List.
    """

    id: str
    type: Optional[str] = None


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
class ControlCard:
    """ControlCard

    Attributes:
        id (str): The unique identifier of the control card, i.e. card number.
        punchingsystem (str, optional): The manufacturer of the punching
                                        system, e.g. 'SI' or 'Emit'.
        modifytime (datetime, optional)
    """

    id: str
    punchingsystem: Optional[str] = None
    modifytime: Optional[datetime.datetime] = None


@dataclass
class Score:
    """Score

    The score earned in an event for some purpose, e.g. a ranking list.
    Attributes:
        score (double): The actual score
        type (str): Purpose of score, e.g. name of ranking list
    """

    score: float
    type: Optional[str] = None


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
    alt: Optional[float] = None


@dataclass
class Account:
    """The bank account of an organisation or an event.

    Attributes:
        account (str): account information
        type (str, optional): The account type.
    """

    account: str
    type: Optional[str] = None


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
    url: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    resolution: Optional[float] = None


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
    time: Optional[datetime.time] = None


@dataclass
class LanguageString:
    """Defines a text that is given in a particular language.

    Attributes:
        text (str)
        language (str, optional): The ISO 639-1 two-letter code of the language
            as stated in https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes.
    """

    text: str
    language: Optional[str] = None


class EventForm(Enum):
    individual = "Individual"
    team = "Team"
    relay = "Relay"


@dataclass
class ClassType:
    """Defines a class type, which is used to group classes in categories.

    Attributes:
        id (Id, optional)
        name (str): The name of the class type
        modifytime (datetime, optional)
    """

    name: str
    id: Optional[Id] = None
    modifytime: Optional[datetime.datetime] = None


@dataclass
class Leg:
    """Defines extra information for a relay leg.

    Attributes:
        name (str, optional): The name of the leg, if not sequentially named.
        min_number_of_competitors (int, default=1): The minimum number of competitors in case of a parallel leg.
        max_number_of_competitors (int, default=1): The maximum number of competitors in case of a parallel leg.
    """

    name: Optional[str] = None
    min_number_of_competitors: Optional[int] = None
    max_number_of_competitors: Optional[int] = None


@dataclass
class Amount:
    """Defines a monetary amount.

    Attributes:
        amount (decimal.Decimal)
        currency (str, optional)
    """

    amount: Decimal
    currency: Optional[str] = None


class FeeType(Enum):
    normal = "Normal"
    late = "Late"


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
    id: Optional[Id] = None
    amount: Optional[Amount] = None
    taxable_amount: Optional[Amount] = None
    percentage: Optional[float] = None
    taxable_percentage: Optional[float] = None
    valid_from_time: Optional[datetime.datetime] = None
    valid_to_time: Optional[datetime.datetime] = None
    from_date_of_birth: Optional[datetime.date] = None
    to_date_of_birth: Optional[datetime.date] = None
    type: Optional[FeeType] = None

    def __post_init__(self):
        if self.amount is not None and self.percentage is not None:
            raise RuntimeError("Fee: only one of amount or percentage can be defined")
        if self.taxable_amount is not None and self.amount is None:
            raise RuntimeError(
                "Fee: taxable_amount only applicable if amount is defined"
            )
        if self.taxable_percentage is not None and self.amount is None:
            raise RuntimeError(
                "Fee: taxable_percentage only applicable if percentage is defined"
            )


@dataclass
class AssignedFee:
    """Contains information about a fee that has been assigned to a competitor or a team, and the amount that has been paid.

    Attributes:
        fee (Fee): The fee that has been assigned to the competitor or the team.
        paid_amount (Amount, optional): The amount that has been paid, optionally including currency code.
    """

    fee: Fee
    paid_amount: Optional[Amount] = None
    modifyTime: datetime.datetime = None


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

    id: Optional[Id] = None
    name: Optional[str] = None
    course_family: Optional[str] = None
    length: Optional[float] = None
    climb: Optional[float] = None
    number_of_controls: Optional[int] = None


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
    position: Optional[GeoPosition] = None
    map_position: Optional[MapPosition] = None
    type: ControlType = ControlType.control
    modifytime: Optional[datetime.datetime] = None


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
    first_start: Optional[datetime.datetime] = None
    status: Optional[RaceClassStatus] = None
    course: List[SimpleCourse] = field(default_factory=list)
    online_controls: List[Control] = field(default_factory=list)
    race_number: Optional[int] = None
    max_number_of_competitors: Optional[int] = None
    modifytime: Optional[datetime.datetime] = None


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
    """Defines a class in an event

    Attributes:
        name (str): The name of the class
        id: Optional[Id]
        shortname (Optional[str]): The abbreviated name of a class, used when space is limited.
        classtype (List[ClassType]): The class type(s) for the class.
        leg (List[Leg]): Information about the legs, if the class is a relay class. One Leg element per leg must be present.
        team_fee (List[Fee]): The entry fees for a team as a whole taking part in this class. Use the Fee element to specify a fee for an individual competitor in the team. Use the TeamFee subelement of the RaceClass element to specify a fee on race level.
        fee (List[Fee]): The entry fees for an individual competitor taking part in the class. Use the TeamFee element to specify a fee for the team as a whole. Use the Fee subelement of the RaceClass element to specify a fee on race level.
        status (EventClassStatus): The overall status of the class, e.g. if overall results should be considered invalid due to misplaced controls. Defaults to normal
        raceclass (List[RaceClass]): Race-specific information for the class, e.g. course(s) assigned to the class.
        too_few_entries_substitute_class (Optional[Class_]): The class that competitors in this class should be transferred to if there are too few entries in this class.
        too_many_entries_substitue_class (Optional[Class_]): The class that competitors that are not qualified (e.g. due to too low ranking) should be transferred to if there are too many entries in this class.
        min_age (Optional[int]): The lowest allowed age for a competitor taking part in the class.
        max_age (Optional[int]): The highest allowed age for a competitor taking part in the class.
        sex (Optional[Sex])
        min_number_of_team_members (Optional[int]): The minimum number of members in a team taking part in the class, if the class is a team class.
        max_number_of_team_members (Optional[int]): The maximum number of members in a team taking part in the class, if the class is a team class.
        min_team_age (Optional[int]): The lowest allowed age sum of the team members for a team taking part in the class.
        max_team_age (Optional[int]): The highest allowed age sum of the team members for a team taking part in the class.
        number_of_competitors (Optional[int]): The number of competitors in the class. A competitor corresponds to a person (if an individual event) or a team (if a team or relay event).
        max_number_of_competitors (Optional[int]): The maximum number of competitors that are allowed to take part in the class. A competitor corresponds to a person (if an individual event) or a team (if a team or relay event). If the maximum number of competitors varies between races in a multi-day event, use the maxNumberOfCompetitors attribute in the RaceClass element.
        resultlist_mode (ResultListMode): Defines the kind of information to include in the result list, and how to sort it. For example, the result list of a beginner's class may include just "finished" or "did not finish" instead of the actual times.
    """

    name: str
    id: Optional[Id] = None
    shortname: Optional[str] = None
    classtype: List[ClassType] = field(default_factory=list)
    leg: List[Leg] = field(default_factory=list)
    team_fee: List[Fee] = field(default_factory=list)
    fee: List[Fee] = field(default_factory=list)
    status: EventClassStatus = EventClassStatus.normal
    raceclass: List[RaceClass] = field(default_factory=list)
    too_few_entries_substitute_class: Optional["Class_"] = None
    too_many_entries_substitue_class: Optional["Class_"] = None
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    sex: Optional[Sex] = None
    min_number_of_team_members: Optional[int] = None
    max_number_of_team_members: Optional[int] = None
    min_team_age: Optional[int] = None
    max_team_age: Optional[int] = None
    number_of_competitors: Optional[int] = None
    max_number_of_competitors: Optional[int] = None
    resultlist_mode: ResultListMode = ResultListMode.default


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
