import datetime
from typing import List, Literal, Optional, Set

from pydantic_xml import BaseXmlModel, attr, element

from .base import GeoPosition, Id, Image, LanguageString, MapPosition


class Leg(BaseXmlModel):
    """Defines extra information for a relay leg.

    Attributes:
        name (str, optional): The name of the leg, if not sequentially named.
        min_number_of_competitors (int, default=1): The minimum number of competitors
            in case of a parallel leg.
        max_number_of_competitors (int, default=1): The maximum number of competitors
            in case of a parallel leg.
    """

    name: Optional[str] = element(tag="Name")
    min_number_of_competitors: Optional[int] = attr(name="minNumberOfCompetitors")
    max_number_of_competitors: Optional[int] = attr(name="maxNumberOfCompetitors")


class SimpleCourse(BaseXmlModel):
    """Defines a course, excluding controls.

    Attributes:
        id (Id)
        name (str, optional): The name of the course.
        course_family (str, optional): The family or group of forked courses
            that the course is part of.
        length (float, optional): The length of the course, in meters.
        climb (float, optional): The climb of the course, in meters, along the
            expected best route choice.
        number_of_controls (int, optional): The number of controls in the course,
            excluding start and finish.
    """

    id: Optional[Id] = element(tag="Id")
    name: Optional[str] = element(tag="Name")
    course_family: Optional[str] = element(tag="CourseFamily")
    length: Optional[float] = element(tag="Length")
    climb: Optional[float] = element(tag="Climb")
    number_of_controls: Optional[int] = element(tag="NumberOfControls")


"""The type of a control: (ordinary) control, start, finish,
    crossing point or end of marked route.

Valid values:
    control
    start
    finish
    crossing_point
    end_of_marked_route
"""
ControlType = Literal[
    "control", "start", "finish", "crossing_point", "end_of_marked_route"
]


class Control(BaseXmlModel):
    """Defines a control, without any relationship to a particular course.

    Attributes:
        id (Id, optional): The code of the control.
        punching_unit_id (list[Id], optional): If the control has multiple punching
        units with separate codes, specify all these codes using elements of this kind.
        Omit this element if there is a single punching unit whose code is
        the same as the control code.
        name (list[LanguageString], optional): The name of the control, used for
            e.g. online controls ('spectator control', 'prewarning').
        position (GeoPosition, optional): The geographical position of the control.
        map_position (MapPosition, optional): The position of the control according
            to the map's coordinate system.
        type (ControlType): The type of the control: (ordinary) control, start, finish,
            crossing point or end of marked route. This attribute can be overridden
            on the CourseControl level. Defaults to ControlType.control
        modifytime (datetime.datetime, optional)
    """

    id: Id = element(tag="Id")
    punching_unit_id: Set[Id] = element(tag="PunchingUnitId", default_factory=list)
    name: Set[LanguageString] = element(tag="Name", default_factory=list)
    position: Optional[GeoPosition] = element(tag="Position")
    map_position: Optional[MapPosition] = element(tag="MapPosition")
    type: ControlType = attr(default="control")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class SimpleRaceCourse(SimpleCourse):
    """Defines a course for a certain race, excluding controls.

    Attributes:
        id (Id)
        name (str, optional): The name of the course.
        course_family (str, optional): The family or group of forked courses
            that the course is part of.
        length (float, optional): The length of the course, in meters.
        climb (float, optional): The climb of the course, in meters, along the
            expected best route choice.
        number_of_controls (int, optional): The number of controls in the course,
            excluding start and finish.
        raceNumber (int, optional): The ordinal number of the race that the
            information belongs to for a multi-race event, starting at 1.
    """

    race_number: Optional[int] = attr(name="raceNumber")


class ControlAnswer(BaseXmlModel):
    """Defines the the selected answer, the correct answer and the time used on a Trail-O control.

    Attributes:
        answer (str): The answer that the competitor selected. If the
            competitor did not give any answer, use an empty string.
        correct_answer (str): The correct answer. If no answer is correct, use an empty string.
        time (float, optional): The time in seconds used to give the answer, in case of a timed
            control. Fractions of seconds (e.g. 258.7) may be used if the time resolution is
            higher than one second.
    """

    answer: str = element(tag="Answer")
    correct_answer: str = element(tag="CorrectAnswer", default="")
    time: Optional[float] = element(tag="Time")


class CourseControl(BaseXmlModel):
    """A control included in a particular course.

    control (list[str]): The code(s) of the control(s), without course-specific information.
        Specifying multiple control codes means that the competitor is required to punch one
        of the controls, but not all of them.

    """

    control: List[str] = element(tag="Control")
    map_text: Optional[str] = element(tag="MapText")
    map_text_position: Optional[MapPosition] = element(tag="MapTextPosition")
    leg_length: Optional[float] = element(tag="LegLength")
    score: Optional[float] = element(tag="Score")
    type: Optional[ControlType] = attr()
    random_order: bool = attr(name="randomOrder", default=False)
    special_instruction: Optional[
        Literal[
            "None",
            "TapedRoute",
            "FunnelTapedRoute",
            "MandatoryCrossingPoint",
            "MandatoryOutOfBoundsAreaPassage",
        ]
    ] = attr(name="specialInstruction", default="None")
    taped_route_length: Optional[float] = attr(name="tapedRouteLength")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class Course(BaseXmlModel):
    """Defines a course, i.e. a number of controls including start and finish."""

    id: Optional[Id] = element(tag="Id")
    name: str = element(tag="Name")
    course_family: Optional[str] = element(tag="CourseFamily")
    length: Optional(float) = element(tag="Length")
    climb: Optional(float) = element(tag="Climb")
    course_controls: list[CourseControl] = element(tag="CourseControl")
    map_id: Optional[int] = element(tag="MapId")
    number_of_competitors: Optional[int] = attr(name="numberOfCompetitors")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class Map(BaseXmlModel):
    """Map information, used in course setting software with regard to the "real" map."""

    id: Optional[Id] = element(tag="Id")
    image: Optional[Image] = element(tag="Image")
    scale: float = element(tag="Scale")
    map_position_top_left: MapPosition = element(tag="MapPositionTopLeft")
    map_position_bottom_right: MapPosition = element(tag="MapPositionBottomRight")


class Route(BaseXmlModel):
    """Defines a route, i.e. a number of geographical positions (waypoints) describing a competitor's navigation throughout a course."""

    base64: str


class PersonCourseAssignment(BaseXmlModel):
    """Element that connects a course with an individual competitor. Courses should be
    present in the RaceCourseData element and are matched on course name and/or course
    family. Persons are matched by 1) BibNumber, 2) EntryId.
    """

    entry_id: Optional[Id] = element(tag="EntryId")
    bib_number: Optional[str] = element(tag="BibNumber")
    person_name: Optional[str] = element(tag="PersonName")
    class_name: Optional[str] = element(tag="ClassName")
    course_name: Optional[str] = element(tag="CourseName")
    course_family: Optional[str] = element(tag="CourseFamily")
