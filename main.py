from katalyst import Katalyst
# from android import Layout

if __name__ == '__main__':
	katalyst = Katalyst('mockup.svg')
	katalyst.convert_to_xml_layout()
	katalyst.write_to_file(katalyst.xml_layout_tree, 'layout.xml')
	print(katalyst.to_string(katalyst.xml_layout_tree))



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