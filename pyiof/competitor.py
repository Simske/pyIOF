import datetime
from typing import List, Optional

from pydantic_xml import BaseXmlModel, attr, element

from .base import Score
from .class_ import Class_
from .contact import Organisation, Person


class ControlCard(BaseXmlModel):
    """ControlCard

    Attributes:
        id (str): The unique identifier of the control card, i.e. card number.
        punchingsystem (str, optional): The manufacturer of the punching
                                        system, e.g. 'SI' or 'Emit'.
        modifytime (datetime, optional)
    """

    id: str
    punchingsystem: Optional[str] = attr(name="punchingSystem")
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")


class Competitor(BaseXmlModel):
    """Represents information about a person in a competition context,
    i.e. including organisation and control card.

    Attributes:
        person: Person
        organisation (List[Organisation]): The organisations that the
            person is member of.
        controlcards (List[ControlCard]): The default control cards of the competitor.
        class_ (List[Claas_]): The default classes of the competitor.
        score (List[Score]): Any scores, e.g. ranking scores, for the person.
        modifytime (datetime.datetime, optional)
    """

    person: Person = element(tag="Person")
    organisation: List[Organisation] = element(tag="Organisation", default_factory=list)
    controlcards: List[ControlCard] = element(tag="ControlCard", default_factory=list)
    class_: List[Class_] = element(tag="Class", default_factory=list)
    score: List[Score] = element(tag="Class", default_factory=list)
    modify_time: Optional[datetime.datetime] = attr(name="modifyTime")
