from lxml import etree

import re

class Magic():
	MULTIPLIER = 1
	# TODO: calculate multiplier

	def unit_correction(self, number):
		number = float(number)
		return int(number / 4) * 4


	def calculate_font_height(self, font_size=16, font_family='Roboto-Regular', text='k'):
		return font_size * 1.5


	def recursion_magic(self, element, parent_dimension):
		dimension = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0, 'height': 0, 'width': 0}

		if element.tag == self.SVG_TEXT:
			print(element.tag)

		elif element.tag == self.SVG_G:
			rect = element.getchildren()[0]
			dimension['width'] = float(rect.attrib['width'])
			dimension['height'] = float(rect.attrib['height'])

			if 'x' in rect.attrib:
				dimension['left'] = float(rect.attrib['x'])

			if 'y' in rect.attrib:
				dimension['top'] = dimension['top'] + float(rect.attrib['y'])

			dimension['right'] = dimension['left'] + dimension['width']
			dimension['bottom'] = dimension['top'] + dimension['height']

			print(dimension)

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
						self.recursion_magic(node, dimension)

	def magic(self):
		art_boards = self.svg_layout_tree.xpath('//ns:svg/ns:g',
		                                        namespaces={'ns': self.SVG_NS})

		art_board_dimensions = []
		for art_board in art_boards:
			dimension = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0, 'height': 0, 'width': 0}

			for element in art_board.getiterator():
				if element.getparent() == art_board:
					if 'id' in element.attrib:
						attribute = element.attrib['id'].lower()
						if element.tag == self.SVG_G and (re.match('statusbar', attribute) or re.match('actionbar', attribute)):
							height = float(element.getchildren()[0].attrib['height'])
							dimension['top'] = dimension['top'] + height

						elif element.tag == self.SVG_RECT:
							dimension['width'] = float(element.attrib['width'])
							dimension['height'] = float(element.attrib['height'])

							if 'x' in element.attrib:
								dimension['left'] = float(element.attrib['x'])

							tmp_y = 0
							if 'y' in element.attrib:
								tmp_y = float(element.attrib['y'])
								dimension['top'] = dimension['top'] + float(element.attrib['y'])

							dimension['right'] = dimension['left'] + dimension['width']
							dimension['bottom'] = tmp_y + dimension['height']

						else:
							self.recursion_magic(element, dimension)
			print('-')




