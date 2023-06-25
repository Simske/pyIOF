from .model_factories import OrganisationListFactory
from .xml_validator import iof_xml_schema


def test_organisation_list_schema():
    iof_xml_schema.assertValid(OrganisationListFactory.build().to_xml_tree())
