from katalyst import Katalyst
import os
import sys
# from android import Layout

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IO_DIR = os.path.join(BASE_DIR, 'io')
RES_DIR = os.path.join(IO_DIR, 'res')
SVG_DIR = os.path.join(IO_DIR, 'svg')

if __name__ == '__main__':
	svg_file = os.path.join(SVG_DIR, 'katalyst_mockup.svg')
	if os.path.isfile(svg_file) is not True:
		sys.exit(svg_file + ' file not found')

	katalyst = Katalyst(svg_file)
	katalyst.write_android_res()

	# parse color
	# katalyst.parse_color()

	# Layout conversion
	# katalyst.convert_to_xml_layout()
	# katalyst.write_to_file(katalyst.xml_layout_tree, 'layout.xml')
	# print(katalyst.to_string(katalyst.xml_layout_tree))



	# l = Layout()
	# attrib = {'name':'deepak', 'work':'lf'}
	# print(l.linear_layout(attrib).attrib)

	# for e in katalyst.all_elements():
	# 	print(e.tag)

	# katalyst.convert_to_xml_layout()

	# for e in katalyst.all_elements():
	# 	print (e.tag)

	# print(katalyst.to_string())
	# katalyst.write_to_file('android.xml')
	# katalyst.get_attrib()
	# katalyst.convert_to_xml_layout()