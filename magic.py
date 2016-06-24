from lxml import etree

import re

class Magic():
	MULTIPLIER = 1
	# TODO: calculate multiplier

	def unit_correction(self, number):
		number = float(number)
		return int(number / 4) * 4

	def recursion_magic(self, element):
		if element.tag == self.SVG_TEXT:
			print(element.tag)
		elif element.tag == self.SVG_G:
			attribute = element.attrib['id'].lower()
			if re.match('image', attribute):
				print(attribute)
			elif re.match('inputfield', attribute):
				print(attribute)
			elif re.match('button', attribute):
				print(attribute)
			else:
				for node in element.getiterator():
					if node.getparent() == element:
						self.recursion_magic(node)

	def magic(self):
		art_boards = self.svg_layout_tree.xpath('//ns:svg/ns:g',
		                                        namespaces={'ns': self.SVG_NS})

		art_board_dimensions = []
		for art_board in art_boards:
			for element in art_board.getiterator():
				if element.getparent() == art_board:
					if 'id' in element.attrib:
						attribute = element.attrib['id'].lower()
						if element.tag == self.SVG_G and (re.match('statusbar', attribute) or re.match('actionbar', attribute)):
							continue
						else:
							self.recursion_magic(element)
			print('-')


