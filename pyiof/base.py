import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Optional


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
