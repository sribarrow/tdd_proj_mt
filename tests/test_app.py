import unittest
from tdd_proj.app import mumble_letter

class sampleTests(unittest.TestCase):
    def test_mumble_letter_one(self):
        self.assertEquals(mumble_letter("a"),'A')

    def test_mumble_letter_two(self):
        self.assertEquals(mumble_letter("ab"),'A-Bb')

    def test_mumble_letter_four(self):
        self.assertEquals(mumble_letter("abcd"),'A-Bb-Ccc-Dddd')