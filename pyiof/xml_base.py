import pydantic_xml
from pydantic_xml import attr, element


class BaseXmlModel(
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
