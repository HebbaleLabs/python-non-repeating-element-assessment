import unittest
from delayed_assert import expect, assert_expectations
from nonrepeatingelements import findnonrepeatingelements

class NonRepeatingElementsTest(unittest.TestCase):

  def test_array_singleelement_nonrepeatable(self):
    expect( lambda: self.assertEqual(findnonrepeatingelements([1]), {1}))
    assert_expectations()

  def test_array_multipleuniqueelement_mutliplenonrepeatable(self):
    expect( lambda: self.assertEqual(findnonrepeatingelements([1,2,3]), {1,2,3}))
    assert_expectations()

  def test_array_multipleelement_singlerepeatable(self):
    expect( lambda: self.assertEqual(findnonrepeatingelements([1,1]), set()))
    assert_expectations()

  def test_array_multipleelement_singlenonrepeatable(self):
    expect( lambda: self.assertEqual(findnonrepeatingelements([1,2,3,2,1]), {3}))
    assert_expectations()

  def test_array_multipleelement_multiplenonrepeatable(self):
    expect( lambda: self.assertEqual(findnonrepeatingelements([1,2,2,3,1,4,1,3,67]), {4,67}))
    assert_expectations()
