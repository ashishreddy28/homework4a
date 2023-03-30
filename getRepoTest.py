"""
Name: Bala Ashish Yeruva
Subject: SSW 567
HW 05a - Isolate External Dependencies
"""

import unittest

from getRepo import getRepo


class TestGithubAPI(unittest.TestCase):
    def testGithub1(self):
        self.assertEqual(getRepo('ashishreddy28'), True)

    def testGithub2(self,fakeResponse):
        self.assertEqual(getRepo('ashishreddy28'),fakeResponse, True)



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
