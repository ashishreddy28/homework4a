"""
Name: Ashish Reddy Yeruva
Cwid:20012794
Subject: SSW - 567
HW 04a Homework 04a
"""
import unittest

from getRepo import getRepo


class TestGithubAPI(unittest.TestCase):
    def testGithub1(self):
        self.assertEqual(getRepo('ashishreddy28'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
