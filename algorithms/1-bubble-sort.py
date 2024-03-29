# https://github.com/minsuk-heo/problemsolving/blob/master/sort/BubbleSort.py

import unittest

# def bubblesort(alist):
#     for i in range(len(alist)-1):
#         for j in range(len(alist)-1):
#             if alist[j] > alist[j+1]:
#                 alist[j], alist[j+1] = alist[j+1], alist[j]
#     return alist

def bubblesort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(n-i-1):
            print (j)

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([4, 6, 1, 3, 5, 2]))
        # self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([6, 4, 3, 1, 2, 5]))
        # self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([6, 5, 4, 3, 2, 1]))

if __name__ == '__main__':
   unittest.main()