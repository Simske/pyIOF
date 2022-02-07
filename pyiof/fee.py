import datetime
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from .base import Id, LanguageString


@dataclass
class Account:
    """The bank account of an organisation or an event.

    Attributes:
        account (str): account information
        type (str, optional): The account type.
    """

    account: str
    type: Optional[str] = None


@dataclass
class Amount:
    """Defines a monetary amount.

    Attributes:
        amount (decimal.Decimal)
        currency (str, optional)
    """

    amount: Decimal
    currency: Optional[str] = None


class FeeType(Enum):
    normal = "Normal"
    late = "Late"


@dataclass
class Fee:
    """A fee that applies when entering a class at a race or ordering a service.

    Attributes:
        id (Id)
        name (list[LanguageString]): A describing name of the fee,
            e.g. 'Late entry fee', at least one entry
        amount (Amount, optional): The fee amount, optionally including currency code.
            This element must not be present if a Percentage element exists.
        taxable_amount (Amount, optional): The fee amount that is taxable,
            i.e. considered when calculating taxes for an event. This element must
            not be present if a Percentage element exists,
            or if an Amount element does not exist.
        percentage (double, optional): The percentage to increase or decrease already
            existing fees in a fee list with. This element must not be present
            if an Amount element exists.
        taxable_percentage (double, optional): The percentage to increase or decrease
            already existing taxable fees in a fee list with. This element must not
            be present if an Amount element exists, or if a Percentage element
            does not exist.
        valid_from_time (datetime.datetime, optional):  The time when the
            fee takes effect.
        valid_to_time (datetime.datetime, optional): The time when the fee expires.
        from_birth_date (datetime.date, optional): The start of the birth date interval
            that the fee should be applied to. Omit if no lower birth date restriction.
        to_birth_date (datetime.date, optional): The end of the birth date interval
            that the fee should be applied to. Omit if no upper birth date restriction.
        type (str, optional): The type of Fee. Allowed values: Normal, Late.
            Default=Normal
    """

    name: List[LanguageString]
    id: Optional[Id] = None
    amount: Optional[Amount] = None
    taxable_amount: Optional[Amount] = None
    percentage: Optional[float] = None
    taxable_percentage: Optional[float] = None
    valid_from_time: Optional[datetime.datetime] = None
    valid_to_time: Optional[datetime.datetime] = None
    from_date_of_birth: Optional[datetime.date] = None
    to_date_of_birth: Optional[datetime.date] = None
    type: Optional[FeeType] = None

    def __post_init__(self):
        if self.amount is not None and self.percentage is not None:
            raise RuntimeError("Fee: only one of amount or percentage can be defined")
        if self.taxable_amount is not None and self.amount is None:
            raise RuntimeError(
                "Fee: taxable_amount only applicable if amount is defined"
            )
        if self.taxable_percentage is not None and self.amount is None:
            raise RuntimeError(
                "Fee: taxable_percentage only applicable if percentage is defined"
            )


@dataclass
class AssignedFee:
    """Contains information about a fee that has been assigned to a
    competitor or a team, and the amount that has been paid.

    Attributes:
        fee (Fee): The fee that has been assigned to the competitor or the team.
        paid_amount (Amount, optional): The amount that has been paid,
            optionally including currency code.
    """

    fee: Fee
    paid_amount: Optional[Amount] = None
    modifyTime: Optional[datetime.datetime] = None
