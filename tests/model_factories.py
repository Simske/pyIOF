from polyfactory.factories.pydantic_factory import ModelFactory

import pyiof


class ClassListFactory(ModelFactory[pyiof.ClassList]):
    __model__ = pyiof.ClassList


class CompetitorListFactory(ModelFactory[pyiof.CompetitorList]):
    __model__ = pyiof.CompetitorList


class ControlCardListFactory(ModelFactory[pyiof.ControlCardList]):
    __model__ = pyiof.ControlCardList


class CourseDataFactory(ModelFactory[pyiof.CourseData]):
    __model__ = pyiof.CourseData


class EntryListFactory(ModelFactory[pyiof.EntryList]):
    __model__ = pyiof.EntryList


class EventListFactory(ModelFactory[pyiof.EventList]):
    __model__ = pyiof.EventList


class OrganisationListFactory(ModelFactory[pyiof.OrganisationList]):
    __model__ = pyiof.OrganisationList


class ResultListFactory(ModelFactory[pyiof.ResultList]):
    __model__ = pyiof.ResultList


class ServiceRequestListFactory(ModelFactory[pyiof.ServiceRequestList]):
    __model__ = pyiof.ServiceRequestList


class StartListFactory(ModelFactory[pyiof.StartList]):
    __model__ = pyiof.StartList
