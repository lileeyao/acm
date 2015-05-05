"""
Thoughts:

<> Surely we can merge, it takes O(n) time and O(n) space.

<> divide-and-conquer

To find kth node:

        +---------+---------+
Array A | part1   | part2   |
        +---------+---------+
        +---------------+---------------+
Array B | part3         | part4         |
        +---------------+---------------+


each time compare the k/2 th node in A and B arrays.
m = len(A) n = len(B)

If (m/2+n/2+1) > k && am/2 > bn/2 , drop Section 2
If (m/2+n/2+1) > k && am/2 < bn/2 , drop Section 4
If (m/2+n/2+1) < k && am/2 > bn/2 ,  drop Section 3
If (m/2+n/2+1) < k && am/2 < bn/2 ,  drop Section 1

"""


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        na, nb = len(A), len(B)
        # the total num of A and B: 1. if odd: pick (m+n)/2 + 1; 2. if even, pick ((m+n)/2 + (m+n)/2+1)/2.
        if (na + nb) % 2 == 0:
            return (self.gen(A, B, (na + nb)/2) + self.gen(A, B, (na + nb)/2 + 1))/2.0
        else:
            return self.gen(A, B, (na + nb)/2 + 1)

    def gen(self, A, B, k):
        na, nb = len(A), len(B)
        # if length becomes 0, means the median is not in the array.
        if na == 0:
            return B[k - 1]
        if nb == 0:
            return A[k - 1]
        # k <= 1, means there are two elems left, either the first elem in A or B.
        if k <= 1:
            return min(A[0], B[0])

        if B[nb/2] >= A[na/2]:
            if (na / 2 + nb / 2 + 1) >= k:
                #drop the right part of B
                return self.gen(A, B[:nb/2], k)
            else:
                #drop the right part of A
                return self.gen(A[(na/2 + 1):], B, k - (na/2+1))
        else:
            if (na / 2 + nb / 2 + 1) >= k:
                #drop the left part of A
                return self.gen(A[:na/2], B, k)
            else:
                #drop the left part of B
                return self.gen(A, B[nb/2+1:], k - (nb/2 + 1))



sol = Solution()
A = [1,9,9,9,10,11,13]
B = [2,2,3,6,7,9,10]

print sol.findMedianSortedArrays(A,B)