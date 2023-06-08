import datetime
from typing import Literal, Optional, Set

from pydantic_xml import BaseXmlModel, attr, element

from .base import GeoPosition, Id, LanguageString, MapPosition


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
    name: Set[LanguageString] = element(default_factory=list)
    position: Optional[GeoPosition] = element(tag="Position")
    map_position: Optional[MapPosition] = element(tag="MapPosition")
    type: ControlType = attr(dewfault="control")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")
