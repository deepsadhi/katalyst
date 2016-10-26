from lxml import etree

class Android:
	def linear_layout(self, attributes={}):
		element = etree.Element('LinearLayout')

		for attribute_key, attribute_value in attributes.items():
			element.set(attribute_key, attribute_value)

		return element

	def resources(self, attributes={}):
		element = etree.Element('resources')

		for attribute_key, attribute_value in attributes.items():
			element.set(attribute_key, attribute_value)

		return element

	def color(self, attributes={}, text=''):
		element = etree.Element('color')
		element.text = text

		for attribute_key, attribute_value in attributes.items():
			element.set(attribute_key, attribute_value)

		return element

	def string(self, attributes={}):
		element = etree.Element('string')
		element.text = attributes['text']
		element.set('name', 'activity_' + attributes['name'])

		return element

	def generate_xml(self, element):
		if element.tag == 'TextView':
			self.xml_layout.feed('<TextView android:layout_width="%s" android:layout_height="%s" android:text="%s" android:textColor="%s" android:textSize="%ssp" />' % ('wrap_content', 'wrap_content', element.attrib['text'], element.attrib['text-color'], element.attrib['font-size']))
		elif element.tag == 'Button':
			self.xml_layout.feed('<Button android:layout_gravity="bottom|end" android:text="%s" android:layout_width="wrap_content" android:background="%s" android:layout_height="wrap_content" />' % (element.attrib['text'], element.attrib['fill']))
		elif element.tag == 'InputField':
			self.xml_layout.feed('<EditText android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="%s"/>' % (element.attrib['hint']))
		elif element.tag == 'Image':
			self.xml_layout.feed('<ImageView android:layout_gravity="center" android:layout_width="200dp" android:layout_height="200dp" android:id="@+id/imageView2" android:src="@mipmap/ic_android" />')
		elif element.tag == 'ViewGroup':
			self.xml_layout.feed('<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent" android:layout_height="match_parent" android:paddingBottom="@dimen/activity_vertical_margin" android:paddingLeft="@dimen/activity_horizontal_margin" android:paddingRight="@dimen/activity_horizontal_margin" android:paddingTop="@dimen/activity_vertical_margin" android:orientation="vertical" tools:context="com.iusmaharjan.katalyst.MainActivity">')

			for node in element.getiterator():
				if node.getparent() == element:
					self.generate_xml(node)

			self.xml_layout.feed('</LinearLayout>')


	def linear_layout(self, view_group):
		self.xml_layout = etree.XMLParser()

		self.generate_xml(view_group)

		return self.xml_layout.close()




