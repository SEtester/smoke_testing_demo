#!/usr/bin/env python3
# encoding:utf-8

import unittest

cases = [
    'test_case.test_case_with_unittest2.TestUittestCase2.test_case_with_unittest_3',
    'test_case.test_case_with_unittest.TestUittestCase.test_case_with_unittest_1'
]
test_suit = unittest.TestLoader().loadTestsFromNames(cases)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suit)
