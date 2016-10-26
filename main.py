from katalyst.katalyst import Katalyst
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IO_DIR = os.path.join(BASE_DIR, 'io')
RES_DIR = os.path.join(IO_DIR, 'res')
SVG_DIR = os.path.join(IO_DIR, 'svg')

if __name__ == '__main__':
	svg_file = os.path.join(SVG_DIR, 'mockup.svg')
	if os.path.isfile(svg_file) is not True:
		sys.exit(svg_file + ' file not found')

	katalyst = Katalyst(svg_file)
	katalyst.write_android_res()

	print('Mockup converted to Android res')