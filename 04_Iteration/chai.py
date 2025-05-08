print('hello')
# Python behind the scenes in loops
# >>> test = "hitesh"
# >>> if not test: 
# ...     print("chai")
# ...     
# >>> test = ""
# >>> if not test: 
# ...     print("chai")
# ...     
# chai
# >>> myList = [1,2,3,4]
# >>> I = iter(myList)
# >>> 
# >>> I
# <list_iterator object at 0x0000021F2F9D8280>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x0000021F2F9D8280>
# >>> i
# Traceback (most recent call last):
#   File "<python-input-41>", line 1, in <module>
#     i
# NameError: name 'i' is not defined. Did you mean: 'I'?
# >>> I.lower()
# Traceback (most recent call last):
#   File "<python-input-42>", line 1, in <module>
#     I.lower()
#     ^^^^^^^
# AttributeError: 'list_iterator' object has no attribute 'lower'
# >>> I
# <list_iterator object at 0x0000021F2F9D8280>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<python-input-47>", line 1, in <module>
#     I.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>> f = open('chai.py')
# >>> iter(f) is f
# True
# >>> iter(f)
# <_io.TextIOWrapper name='chai.py' mode='r' encoding='cp1252'>
# >>> iter(f) is f.__iter__()
# True
# >>> myNewList = [1,2,3]
# >>> iter(myNewList) is f
# False
# >>> iter(myNewList) is myNewList
# False
# >>> D = {'a}
#   File "<python-input-55>", line 1
#     D = {'a}
#          ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> D = {'a':1,'b':2}
# >>> D
# {'a': 1, 'b': 2}
# >>> for key in D.keys()
#   File "<python-input-58>", line 1
#     for key in D.keys()
#                        ^
# SyntaxError: expected ':'
# >>> for key in D.keys():
# ...     print(key)
# ... 
# a
# b
# >>> I = iter(D)
# >>> I
# <dict_keyiterator object at 0x0000021F2FA742C0>
# >>> next(I)
# 'a'
# >>> next(I)
# 'b'
# >>> next(I)
# Traceback (most recent call last):
#   File "<python-input-64>", line 1, in <module>
#     next(I)
#     ~~~~^^^
# StopIteration
# >>> next(I)
# Traceback (most recent call last):
#   File "<python-input-65>", line 1, in <module>
#     next(I)
#     ~~~~^^^
# StopIteration
# >>> next(I.keys())
# Traceback (most recent call last):
#   File "<python-input-66>", line 1, in <module>
#     next(I.keys())
#          ^^^^^^
# AttributeError: 'dict_keyiterator' object has no attribute 'keys'
# >>> for key in D.value():                                                                                   
# ...     print(key)                                                                                          
# ...     
# Traceback (most recent call last):
#   File "<python-input-67>", line 1, in <module>
#     for key in D.value():
#                ^^^^^^^
# AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
# >>> for key in D.values():                                                                                  
# ...     print(key)                                                                                          
# ...     
# 1
# 2
# >>> range(5)
# range(0, 5)
# >>> R = range(5)
# >>> R
# range(0, 5)
# >>> I = iter(R)
# >>> next(I)
# 0
# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last):
#   File "<python-input-78>", line 1, in <module>
#     next(I)
#     ~~~~^^^
# StopIteration
# >>> 
