from lxml import etree

class Writer:
	def __init__(self):
		pass

	def to_string(self, xml):
		return etree.tostring(xml,
		                      xml_declaration=True, encoding='utf-8',
		                      pretty_print=True).decode()

	def write_to_file(self, xml, file_name):
		with open(file_name, 'wb') as file:
			# TODO: check decode() required or not
		    file.write(etree.tostring(xml,
		                              xml_declaration=True,
		                              encoding='utf-8',
		                              pretty_print=True))
		file.close()