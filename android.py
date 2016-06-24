from lxml import etree

class Android:
	def linear_layout(self, attributes={}):
		element = etree.Element('LinearLayout')

		for attribute_key, attribute_value in attributes.items():
			element.set(attribute_key, attribute_value)

		return element
