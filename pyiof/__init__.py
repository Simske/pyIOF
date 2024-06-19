import importlib.metadata

from .class_ import Class_
from .competitor import *
from .contact import *
from .message_elements import (  # noqa: F401
    ClassList,
    CompetitorList,
    ControlCardList,
    CourseData,
    EntryList,
    EventList,
    OrganisationList,
    ResultList,
    ServiceRequestList,
    StartList,
)

__version__ = importlib.metadata.version(__package__ or __name__)
del importlib.metadata
