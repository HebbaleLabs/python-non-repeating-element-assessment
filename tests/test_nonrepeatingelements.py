import unittest
from parameterized import parameterized
from nonrepeatingelements import findnonrepeatingelements

class NonRepeatingElementsTest(unittest.TestCase):

  @parameterized.expand([
    ("Array single element non repeatable", [1], {1}),
    ("Array multiple unique element multiple non repeatable", [1,2,3], {1,2,3})
  ])
  def test_find_unique_nonrepeating_elements(self, name, input_value, expected):
    self.longMessage = True
    actual = findnonrepeatingelements(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)

  @parameterized.expand([
    ("Array multiple element single non repeatable", [1,2,3,2,1], {3}),
    ("Array multiple element multiple non repeatable", [1, 2, 2, 3, 1, 4, 1, 3, 67], {4, 67})
  ])
  def test_find_nonrepeating_elements_among_duplicates(self, name, input_value, expected):
    self.longMessage = True
    actual = findnonrepeatingelements(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)

  @parameterized.expand([
    ("Array multiple element single repeatable", [1,1], set())
  ])
  def test_find_duplicate_elements(self, name, input_value, expected):
    self.longMessage = True
    actual = findnonrepeatingelements(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)
