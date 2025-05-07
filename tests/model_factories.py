from typing import Generic, TypeVar

from polyfactory import Ignore
from polyfactory.factories.base import T
from polyfactory.factories.pydantic_factory import ModelFactory

import pyiof


class CustomModelFactory(ModelFactory[T]):  # type: ignore
    __is_base_factory__ = True

    __randomize_collection_length__ = True
    __min_collection_length__ = 2
    __max_collection_length__ = 5

    # ignore values for pyiof.class_.Class_ because of recursion
    too_few_entries_substitute_class = Ignore()
    too_many_entries_substitute_class = Ignore()


class ClassListFactory(CustomModelFactory[pyiof.ClassList]):
    __model__ = pyiof.ClassList


class CompetitorListFactory(CustomModelFactory[pyiof.CompetitorList]):
    __model__ = pyiof.CompetitorList


class ControlCardListFactory(CustomModelFactory[pyiof.ControlCardList]):
    __model__ = pyiof.ControlCardList


class CourseDataFactory(CustomModelFactory[pyiof.CourseData]):
    __model__ = pyiof.CourseData


class EntryListFactory(CustomModelFactory[pyiof.EntryList]):
    __model__ = pyiof.EntryList


class EventListFactory(CustomModelFactory[pyiof.EventList]):
    __model__ = pyiof.EventList


class OrganisationListFactory(CustomModelFactory[pyiof.OrganisationList]):
    __model__ = pyiof.OrganisationList


class ResultListFactory(CustomModelFactory[pyiof.ResultList]):
    __model__ = pyiof.ResultList


class ServiceRequestListFactory(CustomModelFactory[pyiof.ServiceRequestList]):
    __model__ = pyiof.ServiceRequestList


class StartListFactory(CustomModelFactory[pyiof.StartList]):
    __model__ = pyiof.StartList
