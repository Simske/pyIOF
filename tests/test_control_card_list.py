from .model_factories import ControlCardListFactory
from .xml_validator import iof_xml_schema


def test_control_card_list_schema():
    iof_xml_schema.assertValid(ControlCardListFactory.build().to_xml_tree())
