from .model_factories import *
from .xml_validator import iof_xml_schema


def test_competitor_list_schema():
    iof_xml_schema.assertValid(CompetitorListFactory.build().to_xml_tree())


def test_organisation_list_schema():
    iof_xml_schema.assertValid(OrganisationListFactory.build().to_xml_tree())


def test_event_list_schema():
    iof_xml_schema.assertValid(EventListFactory.build().to_xml_tree())


def test_class_list_schema():
    iof_xml_schema.assertValid(ClassListFactory.build().to_xml_tree())


def test_entry_list_schema():
    iof_xml_schema.assertValid(EntryListFactory.build().to_xml_tree())


def test_course_data_schema():
    iof_xml_schema.assertValid(CourseDataFactory.build().to_xml_tree())


def test_start_list_schema():
    iof_xml_schema.assertValid(StartListFactory.build().to_xml_tree())


def test_result_list_schema():
    iof_xml_schema.assertValid(ResultListFactory.build().to_xml_tree())


def test_service_request_list_schema():
    iof_xml_schema.assertValid(ServiceRequestListFactory.build().to_xml_tree())


def test_control_card_list_schema():
    iof_xml_schema.assertValid(ControlCardListFactory.build().to_xml_tree())
