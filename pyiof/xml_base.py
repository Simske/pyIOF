import datetime
import re
from typing import Annotated, Self, cast

import pydantic_xml
from pydantic import BeforeValidator
from pydantic_xml import attr, element  # noqa: F401


def _normalize_datetime_str(v: object) -> object:
    if isinstance(v, str) and "T" in v:
        date_part, time_part = v.split("T", 1)
        time_part = re.sub(r"^(\d{2})\.(\d{2})\.(\d{2})", r"\1:\2:\3", time_part)
        return f"{date_part}T{time_part}"
    return v


def _normalize_time_str(v: object) -> object:
    if isinstance(v, str):
        return re.sub(r"^(\d{2})\.(\d{2})\.(\d{2})", r"\1:\2:\3", v)
    return v


FlexDatetime = Annotated[datetime.datetime, BeforeValidator(_normalize_datetime_str)]
FlexTime = Annotated[datetime.time, BeforeValidator(_normalize_time_str)]


class BaseXmlModel(  # type: ignore
    pydantic_xml.BaseXmlModel,
    nsmap={
        "": "http://www.orienteering.org/datastandard/3.0",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    },
):
    def to_xml_tree(self, exclude_none: bool = True, **kwargs):
        return super().to_xml_tree(exclude_none=exclude_none, **kwargs)

    def to_xml(self, pretty_print: bool = True, **kwargs) -> bytes:
        return cast(
            bytes,
            super().to_xml(
                pretty_print=pretty_print,
                xml_declaration=True,
                encoding="UTF-8",
                skip_empty=True,
                **kwargs,
            ),
        )

    @classmethod
    def read_xml(cls, path: str) -> Self:
        with open(path, "rb") as f:
            return cls.from_xml(f.read())

    def write_xml(self, path: str) -> None:
        with open(path, "wb") as f:
            f.write(self.to_xml())
