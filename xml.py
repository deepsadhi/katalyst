class Xml:
	'''
	Xml base class
	'''
	def to_string(self):
		return etree.tostring(self.svg_tree, pretty_print=True).decode()

	def write_to_file(self, file_name):
		with open(file_name, 'wb') as file:
			# TODO: check decode() required or not
		    file.write(etree.tostring(self.svg_tree, pretty_print=True))
		file.close()

	def all_elements(self):
		elements = []
		for element in self.svg_tree.iter():
			elements.append(element)
		return elements

	def get_attrib(self):
		element = self.svg_tree.getroot().attrib
		for key, value in element.items():
			print (key + ' => ' + value)