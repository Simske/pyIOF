import pydantic_xml
from pydantic_xml import attr, element  # noqa: F401


class BaseXmlModel(  # type: ignore
    pydantic_xml.BaseXmlModel,
    nsmap={
        "": "http://www.orienteering.org/datastandard/3.0",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    },
):
    def to_xml_tree(self, skip_empty: bool = True, **kwargs):
        return super().to_xml_tree(skip_empty=True, **kwargs)

    def to_xml(self, pretty_print: bool = True, **kwargs):
        return super().to_xml(
            pretty_print=True, xml_declaration=True, encoding="utf8", **kwargs
        )

    @classmethod
    def read_xml(cls, path: str):
        with open(path, "rb") as f:
            return cls.read_xml(f)
