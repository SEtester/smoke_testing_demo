# smoke_testing_demo
如果你喜欢我的文章，麻烦点个赞👍

> 前言：之前有一段时间一直用 Python Uittest做自动化测试，觉得Uittest组织冒烟用例比较繁琐，后来康哥提示我使用pytest.mark来组织冒烟用例


本文讲述以下几个内容：  
> 1、Unittest 如何组织冒烟用例    
> 2、Pytest 组织冒烟测试  
> 3、Pytest 执行unittest冒烟用例    

环境准备：  
> Python 3.64   
> Pytest 5.01  


项目目录：
```
smoke_testing_demo
        test_case
            __init__.py
            test_case_with_unittest.py
            test_case_with_pytest.py
        run_unittest_smoke_testing.py
```
<br>

### 一、Unittest如何组织冒烟用例
- 当 import unittest 时 ，会自动导入TestLoader类  
- TestLoader这个类下，封装了 5 种组织用例的方法  
- 本文主要讲解 loadTestsFromNames 
- 更多Uittest组织用例方法可参考《Unittest组织用例的姿势》这篇博文，链接在文末

#### loadTestsFromNames 方法简介
```
$ loader.py 该文件在python3.7已不存在，建议使用python3.64 查看使用方法

class TestLoader(object):
    """
    该类负责根据各种标准加载测试并将它们包装在TestSuite中
    """
    
    def loadTestsFromNames(self, names, module=None):
    """
    返回给定的一组用例名的测试用例的套件
    """    
```

#### loadTestsFromNames 组织冒烟用例 

测试用例
```
$ test_case_with_unittest.py

#!/usr/bin/env python3
# encoding:utf-8

import unittest

class TestUittestCase(unittest.TestCase):

    def test_case_with_unittest_1(self):
        '''冒烟测试用例'''
        print('I am Smoke Testing ')

    def test_case_with_unittest_2(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
```
$ test_case_with_unittest2.py

#!/usr/bin/env python3
# encoding:utf-8

import unittest

class TestUittestCase2(unittest.TestCase):

    def test_case_with_unittest_3(self):
        '''冒烟测试用例'''
        print('I am Smoke Testing ')

    def test_case_with_unittest_4(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
冒烟测试用例集
```
$ run_unittest_smoke_testing.py

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

```
运行结果
```
test_case_with_unittest_3 (test_case.test_case_with_unittest2.TestUittestCase2)
冒烟测试 ... ok
test_case_with_unittest_1 (test_case.test_case_with_unittest.TestUittestCase)
冒烟测试 ... ok
----------------------------------------------------------------------
Ran 2 tests in 0.000s
```
<br>

#### 小结：
- 通过loadTestsFromNames 可以从不同的模块组织特定的用例集
- 使用loadTestsFromNames这个方法,需要传入一个数组
- 数组里面里面的元素必须是字符串
- 数组元素传入格式：'moudleName.testCaseClassName.testCaseName' 
- 执行用例是根据数组元素的的顺序执行

```
ps: 更多通过loadTestsFromNames 使用技巧，
可以查看《Unittest组织用例的姿势》这篇博文，链接在文末
```

<br>

### 二、Pytest 组织冒烟测试  
- pytest 提供了测试用例标记机制
- 一个测试用例允许被多个@pytest.mark进行标记
- 同一个@pytest.mark可以标记多个测试用例
- pytest.mark常用于冒烟测试用例组织

```
ps:更多的pytest.mark用法可以参考乙醇老师《安利一下pytest的mark用法》
```
#### pytest.mark 组织冒烟用例
测试用例
```
$ run_unittest_smoke_testing.py

#!/usr/bin/env python3
# encoding:utf-8

import pytest

@pytest.mark.test_env
def test_case_1():
    pass

@pytest.mark.test_env
@pytest.mark.smoke
def test_case_2():
    ''' 冒烟用例'''
    pass
```
cd 进入 /test_case目录, 
使用命令行运行 test_case_with_pytest.py
```
pytest test_case_with_pytest.py -v -m smoke
```
运行结果
```
collected 2 items
test_case_with_pytest.py::test_case_2 PASSED

============================== 1 tests deselected ==============================
==================== 1 passed, 1 deselected in 0.01 seconds ====================
```
运行被标记test_env的用例
```
pytest test_case_with_pytest.py -v -m test_env
```
运行结果
```
collected 2 items
test_case_with_pytest.py::test_case_1 PASSED
test_case_with_pytest.py::test_case_2 PASSED
=========================== 2 passed in 0.01 seconds ===========================
```
<br>


### 三、Pytest 执行 Unittest冒烟用例    
__Pytest测试框架是兼容Python自带的Unittest__  

修改test_case_with_unittest2.py
```
$ test_case_with_unittest2.py

#!/usr/bin/env python3
# encoding:utf-8

import unittest
import pytest

class TestUittestCase2(unittest.TestCase):

    @pytest.mark.smoke                 
    def test_case_with_unittest_3(self):
        '''冒烟测试用例'''
        print('I am Smoke Testing ')

    def test_case_with_unittest_4(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
命令行运行 test_case_with_unittest2.py
```
pytest test_case_with_unittest2.py -v -m smoke
```
运行结果
```
collected 2 items / 1 deselected / 1 selected
test_case_with_unittest2.py::TestUittestCase2::test_case_with_unittest_3 PASSED [100%]

============== 1 passed, 1 deselected, 1 warnings in 0.01 seconds ==============
```

总结：  
1、Uittest组织冒烟用例，需通过loadTestsFromNames在不同的测试模块里指定测试用例，组装成test suit(测试套件)后，给TextTestRunner运行  

2、Pytest组织冒烟用例，只需给测试用例加上@pytest.mark.key ，使用命令行pytest -m key test_case.py 即可

<br>


### 自动化冒烟测试 Unittest , Pytest 哪家强？
笔者个人见解：  
- 使用Uittest组织冒烟测试，关注点有至少有两个  
1、当编写新功能的冒烟测试，需要去维护冒烟测试用例集  
2、合并代码时，如果有两个人同时修改了这个冒烟用例集，还要解决冲突，防止遗漏冒烟用例

- 使用Pytest组织冒烟测试，关注点在于用例的本身  
当编写新功能的冒烟测试，我只需在给用例加一个编写用例人员约定好的@pytest.mark，例如@pytest.mark.smoke


#### 推荐阅读

[《安利一下pytest的mark用法》](https://mp.weixin.qq.com/s/S5QiTz8gDWxhuJYmjo2oAw)

[《Python Unittest - 根据不同测试环境跳过用例详解》](https://www.cnblogs.com/snailrunning/p/10125596.html#4287840)


<br>

__最后，欢迎同学们留言, 你认为自动化冒烟测试 Unittest , Pytest 哪家强？__  
__文章如有不是，欢迎同学们斧正__
<br>

<br>
