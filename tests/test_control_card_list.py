import pathlib

from lxml import etree
from polyfactory.factories.pydantic_factory import ModelFactory

from pyiof import ControlCardList


class ControlCardListFactory(ModelFactory[ControlCardList]):
    __model__ = ControlCardList


iof_xml_schema = etree.XMLSchema(
    etree.parse(pathlib.Path(__file__).parent.parent / "IOF.xsd")
)


def test_control_card_list_schema():
    ccl = ControlCardListFactory.build()
    iof_xml_schema.assertValid(ccl.to_xml_tree())
