from lxml import etree

import re

class Magic():
	MULTIPLIER = 1
	# TODO: calculate multiplier

	# def __int__(self):
	# 	Svg.__int__(self)

	def unit_correction(self, number):
		number = float(number)
		return int(number / 4) * 4


	def magic(self):
		art_boards = self.svg_layout_tree.xpath('//ns:svg/ns:g',
		                                        namespaces={'ns': self.SVG_NS})

		art_board_dimensions = []
		for art_board in art_boards:
			for element in art_board.getiterator():
				if element.tag == self.SVG_RECT:
					dimension = {'width': self.unit_correction(element.attrib['width']),
								 'height': self.unit_correction(element.attrib['height'])}

					if 'x' in element.attrib:
						dimension['left'] = float(element.attrib['x'])
					else:
						dimension['left'] = 0

					if 'y' in element.attrib:
						dimension['top'] = float(element.attrib['y'])
					else:
						dimension['top'] = 0

					dimension['right'] = dimension['left'] + dimension['width']
					dimension['bottom'] = dimension['top'] + dimension['height']

					art_board_dimensions.append(dimension)

				if element.getparent() == art_board:
					if element.tag == self.SVG_TEXT:
						print(element.tag)
					else:
						attribute = element.attrib['id'].lower()

						if re.match('layout', attribute):
							print(element.tag)


			print('-')