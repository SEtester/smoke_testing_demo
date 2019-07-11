#!/usr/bin/env python3
# encoding:utf-8

import unittest
import pytest

class TestUittestCase2(unittest.TestCase):

    @pytest.mark.smoke
    def test_case_with_unittest_3(self):
        '''冒烟测试'''
        pass

    def test_case_with_unittest_4(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)