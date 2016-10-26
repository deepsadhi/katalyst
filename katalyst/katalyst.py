from lxml import etree
from android import Android
from svg import Svg
from writer import Writer
from magic import Magic


import os
import re
import cairo
import rsvg

class Katalyst(Svg, Writer, Magic):
	'''
	Katalyst
	'''
	EXSLT_NS = 'http://exslt.org/regular-expressions'

	def __init__(self, file_path):
		Svg.__init__(self)
		Writer.__init__(self)
		Magic.__init__(self)

		self.io_dir = os.path.dirname(os.path.dirname(os.path.abspath(file_path)))
		self.res_dir = os.path.join(self.io_dir, 'res')

		self.android = Android()

		self.file_path = file_path
		self.parse()


	def parse(self):
		self.svg_layout_tree = etree.parse(self.file_path)


	def parse_color(self):
		self.background_color = set()
		color_fill = self.svg_layout_tree.xpath('//ns:rect', namespaces={'ns': self.SVG_NS})

		for color in color_fill:
			if 'fill' in color.attrib and color.attrib['fill'].lower() != 'none':
				self.background_color.add(color.attrib['fill'])

		self.text_color = set()
		color_fill = self.svg_layout_tree.xpath('//ns:text', namespaces={'ns': self.SVG_NS})
		for color in color_fill:
			if 'fill' in color.attrib and color.attrib['fill'].lower() != 'none':
				self.text_color.add(color.attrib['fill'])


	def parse_action_bar_text(self):
		action_bars_texts = self.svg_layout_tree.xpath('//ns:svg/ns:g/ns:g[re:match(@id, "ActionBar")]/ns:text',
		                                         namespaces={'re': self.EXSLT_NS, 'ns': self.SVG_NS})

		self.action_bars_texts = []
		for action_bars_text in action_bars_texts:
			self.action_bars_texts.append({'name': action_bars_text.getparent().getparent().attrib['id'].lower(),
			                               'text': action_bars_text.text})


	def write_action_bars_text(self):
		self.parse_action_bar_text()

		i = 1
		self.xml_action_bar_resources_tree = self.android.resources()
		for action_bar in self.action_bars_texts:
			self.xml_action_bar_resources_tree.append(self.android.string(action_bar))

		file = os.path.join(self.values_dir, 'strings.xml')
		self.write_to_file(self.xml_action_bar_resources_tree, file)



	def write_color(self):
		self.parse_color()


		# TODO: spacing and comment
		# For color
		self.xml_color_resources_tree = self.android.resources()
		i = 1
		for color in self.background_color:
			attributes = {'name': 'background_color_' + str(i)}
			i = i + 1
			self.xml_color_resources_tree.append(self.android.color(attributes, color))

		i = 1
		for color in self.text_color:
			attributes = {'name': 'text_color_' + str(i)}
			i = i + 1
			self.xml_color_resources_tree.append(self.android.color(attributes, color))

		file = os.path.join(self.values_dir, 'colors.xml')
		self.write_to_file(self.xml_color_resources_tree, file)


	def write_kxml(self):
		self.parse_kxml()

		view_groups = self.kxml_layout.xpath('//Kxml/ViewGroup')
		i = 1
		for view_group in view_groups:
			file = os.path.join(self.layouts_dir, 'activity_' + str(i) + '.xml')
			self.write_to_file(self.android.linear_layout(view_group), file)
			i = i + 1
			# print(etree.tostring(self.android.linear_layout(view_group), pretty_print=True).decode())


	def write_drawable(self, svg, drawable):
		directory = os.path.join(self.res_dir, drawable['name'])
		if not os.path.exists(directory):
			os.makedirs(directory)

		tmp_svg = etree.fromstring(etree.tostring(svg))

		tmp_svg.attrib['height'] = str(float(tmp_svg.attrib['height']) * float(drawable['multiplier']))
		tmp_svg.attrib['width'] = str(float(tmp_svg.attrib['width']) * float(drawable['multiplier']))


		file = os.path.join(directory, 'asset.png')

		img = cairo.ImageSurface(cairo.FORMAT_ARGB32,
		                         int(float(tmp_svg.attrib['height'])),
		                         int(float(tmp_svg.attrib['height'])))
		ctx = cairo.Context(img)
		handle = rsvg.Handle(None, str(etree.tostring(tmp_svg)))
		handle.render_cairo(ctx)
		img.write_to_png(file)


	def write_drawables(self):
		drawables = [{'name': 'drawable-mdpi', 'multiplier': 1},
					 {'name': 'drawable-hdpi', 'multiplier': 1.5},
					 {'name': 'drawable-xhdpi', 'multiplier': 2},
					 {'name': 'drawable-xxhdpi', 'multiplier': 3},
					 {'name': 'drawable-xxxhdpi', 'multiplier': 4}
					]

		for drawable in drawables:
			for svg in self.asset:
				self.write_drawable(svg, drawable)

		# print(etree.tostring(svg, pretty_print=True).decode())


	def write_android_res(self):
		if not os.path.exists(self.res_dir):
			os.makedirs(self.res_dir)

		self.values_dir = os.path.join(self.res_dir, 'values')
		if not os.path.exists(self.values_dir):
			os.makedirs(self.values_dir)

		self.layouts_dir = os.path.join(self.res_dir, 'layout')
		if not os.path.exists(self.layouts_dir):
			os.makedirs(self.layouts_dir)

		self.write_color()
		self.write_action_bars_text()
		self.write_kxml()

		self.write_drawables()


	def convert_to_xml_layout(self):
		groups = self.svg_layout_tree.xpath('//ns:svg/ns:g', namespaces = {'ns': self.SVG_NS})

		self.xml_layout_tree = self.android.linear_layout()
		for group in groups:
			self.xml_layout_tree.append(self.android.linear_layout(group.attrib))




