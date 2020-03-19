import BTrees
from BTrees.OOBTree import OOBTree

print()
print()
print(BTrees)
print()
a = OOBTree({1:11, 2:22, 3:33})
expected = [3, 2, 1]
b = a.iterkeys(reverse=True)
actual = list(b)
print(actual, expected == actual)
