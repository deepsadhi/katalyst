from lxml import etree
from android import Android
from svg import Svg
from writer import Writer

class Katalyst(Svg, Writer):
	'''
	Katalyst
	'''
	def __init__(self, file_path):
		Svg.__init__(self)
		Writer.__init__(self)

		self.android = Android()

		self.file_path = file_path
		self.parse()


	def parse(self):
		self.svg_layout_tree = etree.parse(self.file_path)


	def convert_to_xml_layout(self):
		groups = self.svg_layout_tree.xpath('//ns:svg/ns:g', namespaces = {'ns': self.SVG_NS})

		self.xml_layout_tree = self.android.linear_layout()
		for group in groups:
			self.xml_layout_tree.append(self.android.linear_layout(group.attrib))




