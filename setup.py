#!/usr/bin/env python

from importlib.metadata import entry_points
import setuptools
import pdf2image_cli

setuptools.setup(
	name="pdf2image-cli",
	version='1.0.0',
	packages=setuptools.find_packages(include=['pdf2image_cli', 'pdf2image_cli.*']),
	entry_points={
		'console_scripts': [
			"pdf2image=pdf2image_cli.__main__:main"
		]
	}
)