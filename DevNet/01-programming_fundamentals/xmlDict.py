import xmltodict
import pprint


xml_read = open('xml_example.xml').read()
pprint.pprint(xml_read)

xml_dict = xmltodict.parse(xml_read)
pprint.pprint(xml_dict)


print(xml_dict['interface']['ipv4']['address']['ip'])
