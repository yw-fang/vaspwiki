from vaspwiki import __version__
import io
import os
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.rst')
with io.open(readme_path, encoding='utf-8') as readme_file:
	long_description = readme_file.read()


def readme():
	with open('README.rst') as f:
		return (f.read())


setup(name='vaspwiki',
	  version='1.1.1',
	  description='The VASP manual',
	  long_description=long_description,
	  long_description_content_type='text/x-rst',
	  keywords='python vasp manual',
	  url='https://github.com/yw-fang/vaspwiki',
	  author='Yue-Wen FANG',
	  author_email='fyuewen@gmail.com',
	  license='MIT LICENSE',
	  packages=['vaspwiki'],
	  install_requires=[
	  ],
	  test_suite='nose.collector',
	  tests_require=['nose'],
	  entry_points = {
		  'console_scripts': ['vaspwiki=vaspwiki.vaspwiki_command:vaspwiki_command'],
	  },
	  include_package_data=True,
	  zip_safe=False)
