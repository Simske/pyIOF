import datetime
from dataclasses import dataclass, field
from typing import List, Optional

from .base import Score
from .class_ import Class_
from .contact import Organisation, Person


@dataclass
class ControlCard:
    """ControlCard

    Attributes:
        id (str): The unique identifier of the control card, i.e. card number.
        punchingsystem (str, optional): The manufacturer of the punching
                                        system, e.g. 'SI' or 'Emit'.
        modifytime (datetime, optional)
    """

    id: str
    punchingsystem: Optional[str] = None
    modifytime: Optional[datetime.datetime] = None


@dataclass
class Competitor:
    """Represents information about a person in a competition context, i.e. including organisation and control card.

    Attributes:
        person: Person
        organisation (List[Organisation]): The organisations that the person is member of.
        controlcards (List[ControlCard]): The default control cards of the competitor.
        class_ (List[Claas_]): The default classes of the competitor.
        score (List[Score]): Any scores, e.g. ranking scores, for the person.
        modifytime (datetime.datetime, optional)
    """

    person: Person
    organisation: List[Organisation] = field(default_factory=list)
    controlcards: List[ControlCard] = field(default_factory=list)
    class_: List[Class_] = field(default_factory=list)
    score: List[Score] = field(default_factory=list)
    modifytime: Optional[datetime.datetime] = None
