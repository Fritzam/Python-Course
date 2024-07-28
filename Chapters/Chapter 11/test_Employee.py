import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """ Create a set up for Employee class """

        self.singleEmployee = Employee("Michal", "Redacted", "100000")

    def test_assertGiveRaiseGives5000(self):
        self.singleEmployee.give_raise()
        self.assertTrue(self.singleEmployee.annual_salary == 105000)

    def test_assertGiveRaiseGivesCustom(self):
        self.singleEmployee.give_raise("100000")
        self.assertTrue(self.singleEmployee.annual_salary == 200000)
