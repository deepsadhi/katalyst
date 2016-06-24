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
