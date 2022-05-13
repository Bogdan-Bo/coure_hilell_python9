#1 All
"""
1) a = ["hello", "world", "goodbye"]
print(all(a))     # True
2) a = ["hello", "", "goodbye"]
print(all(a))     # False
3) a = [1, 2, 3]
print(all(a))    # True
4) a = [(1, 2, 3), (),(4, 8, 9)]
print(all(a)) # False
5) z = 100
   b = z % 2 ==0
   c = z > 50
   v = z < 1000
print(all([b, c, v])) #True
#2 Any
1) a = ["hello", "", "goodbye"]
print(any(a)) #True
2) a = ["", "", ""]
print(any(a)) #False
3) a = [(),(),()]
print(any(a)) #False
4) z = 100
b = z % 2 ==0
c = z > 50
v = z < 1000
print(any([b, c, v])) #True
#3 Filter
1) def fil(x):
    return x > 10
a = [1, 3, 5, 55, 66, 23,102]
b = list(filter(fil, a))
print(b)
2) a = [1, 3, 5, 55, 66, 23,102]
b = [i for i in a if 10 < i < 100]
print(b)
3) a = ["How", "Car", "Morning", "Tomorrow", "Yesterday"]
b = list(filter(lambda x: len(x) > 5, a))
print(b)"""

