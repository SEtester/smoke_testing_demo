#!/usr/bin/env python3
# encoding:utf-8

import unittest


class TestUittestCase(unittest.TestCase):

    def test_case_with_unittest_1(self):
        '''冒烟测试'''
        pass

    def test_case_with_unittest_2(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
