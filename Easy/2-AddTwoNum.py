# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = len(l1) - 1
        n2 = len(l2) - 1
        lista1 = 0
        lista2 = 0
        while n1 != -1 or n2 != -1:
            if n1 != -1:
                lista1 = lista1*10
                lista1 = lista1 + l1[n1]
                n1 -= 1
            elif n2 != -1:
                lista2 = lista2*10
                lista2 = lista2 + l2[n2]
                n2 -= 1

        resultado = lista1 + lista2
        temp = resultado
        reversed_result = []
        while temp != 0:
            digit = temp % 10
            reversed_result.append(digit)
            temp //= 10

        return reversed_result