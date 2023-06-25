from typing import Generic, TypeVar

from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory

import pyiof


class CustomFaker(Faker):
    custom_faker_base = Faker()

    def pylist(self, **kwargs):
        return Faker().pylist(3, **kwargs)


T = TypeVar("T")


class CustomModelFactory(Generic[T], ModelFactory[T]):
    __is_base_factory__ = True
    __faker__ = CustomFaker()
    __batch_size__ = lambda: __random__.randint(1, 3)


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
