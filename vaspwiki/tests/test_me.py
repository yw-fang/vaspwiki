from unittest import TestCase
from vaspwiki import vaspwiki
# The testme.py file is my first test file.
# Although it’s overkill for now, we’ll use a
# unittest.TestCase subclass to provide infrastructure for later development.

"""
Test method 1
to run this test
$ cd tests/
$ pip install nose
$ nosetests
"""

class TestPlaygroud(TestCase):
    def test_open_browser(self):
        requested_pattern = 'INCAR'
        if vaspwiki.help_function(requested_pattern):
            self.assertTrue(True)

# class TestConsole(TestCase):
#     def test_basic(self):
#         pass

"""
Test method 2

To integrate above with our setup.py,
and ensure that Nose is installed when we run the tests, we’ll add a few lines to setup():

setup(
    ...
    test_suite='nose.collector',
    tests_require=['nose'],
)

To run this tests, we can do by:

$ python setup.py test

We can also update the .travis.yml so that the travis CI will examine the unit test

add the following to the .travis.yml, pip install -r requirements.txt is used for
installation of the markdown and nose modules.
install:
  - pip install -r requirements.txt
# command to run tests
script:
      - pytest

Note that, the test scripts must begin with test_ like this current file named 'test_me.py'
"""
