#!/usr/bin/env python3
# encoding:utf-8

import pytest

@pytest.mark.test_env
def test_case_1():
    pass

@pytest.mark.test_env
@pytest.mark.smoke
def test_case_2():
    '''冒烟用例'''
    pass