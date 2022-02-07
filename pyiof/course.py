import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from .base import GeoPosition, Id, LanguageString, MapPosition


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
