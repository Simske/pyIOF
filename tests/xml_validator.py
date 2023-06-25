from pathlib import Path

from lxml import etree

iof_xml_schema = etree.XMLSchema(etree.parse(Path(__file__).parent.parent / "IOF.xsd"))
