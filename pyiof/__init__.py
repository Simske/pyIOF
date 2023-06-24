import importlib.metadata

__version__ = importlib.metadata.version(__package__ or __name__)

del importlib.metadata

from .message_elements import (
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
