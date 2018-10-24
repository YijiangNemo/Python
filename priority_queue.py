# Code for insertion into a priority queue
# implemented as a binary tree
#
# Written by *** for COMP9021


from binary_tree import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        def _insert(self,n,height,l):
            if n > height:
                return
            if self:
                l.append([n,self.value])
                _insert(self.left_node,n+1,height,l)
                _insert(self.right_node,n+1,height,l)
        l = []       
        if self.value is None:
            self.value = value
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
            return True
        _insert(self,0,self.height(),l)
        ll = [None]
        for x in range(self.height()+1):

            for i in range(len(l)):
                if l[i][1] is not None:
                    if l[i][0] == x:
                        ll.append(l[i][1])

        ll.append(value)
        
        p = len(ll) - 1
        while p > 1 and ll[p] < ll[(p)//2 ]:
            ll[p], ll[p//2] = ll[p//2 ] , ll[p]
            p //= 2
##        print(ll)
        self.value = ll[1]
        
        if len(ll) <= 4:
            
            t2 = BinaryTree(ll[2])
            if 3 <= len(ll) -1:
                t3 = BinaryTree(ll[3])
            
            self.left_node = t2
            if 3 <= len(ll) -1:
                self.right_node = t3
        if 4 < len(ll) <= 6:
            t4 = BinaryTree(ll[4])
            if 5 <= len(ll) -1:
                t5 = BinaryTree(ll[5])
            
            t2 = BinaryTree(ll[2])
            t3 = BinaryTree(ll[3])
            self.left_node = t2
            self.right_node = t3
            self.left_node.left_node = t4
            if 5 <= len(ll) -1:
                self.left_node.right_node = t5
        if 6 < len(ll) <=8:
            t6 = BinaryTree(ll[6])
            if 7 <= len(ll) - 1:
                t7 = BinaryTree(ll[7])
            t3 = BinaryTree(ll[3])
            t4 = BinaryTree(ll[4])
            t5 = BinaryTree(ll[5])
            t2 = BinaryTree(ll[2])
            self.left_node = t2
            self.right_node = t3
            self.left_node.left_node = t4
            self.left_node.right_node = t5
            self.right_node.left_node = t6
            if 7 <= len(ll) - 1:
                self.right_node.right_node = t7
        if 8 < len(ll) <= 10:
            t6 = BinaryTree(ll[6])
            t7 = BinaryTree(ll[7])
            t3 = BinaryTree(ll[3])
            t4 = BinaryTree(ll[4])
            t5 = BinaryTree(ll[5])
            t2 = BinaryTree(ll[2])
            t8 = BinaryTree(ll[8])
            if 9 <= len(ll) -1:
                t9 = BinaryTree(ll[9])
            self.left_node = t2
            self.right_node = t3
            self.left_node.left_node = t4
            self.left_node.right_node = t5
            self.right_node.left_node = t6
            self.right_node.right_node = t7
            self.left_node.left_node.left_node = t8
            if 9 <= len(ll) -1:
                self.left_node.left_node.right_node = t9
        if 10 < len(ll) <= 12:
            t6 = BinaryTree(ll[6])
            t7 = BinaryTree(ll[7])
            t3 = BinaryTree(ll[3])
            t4 = BinaryTree(ll[4])
            t5 = BinaryTree(ll[5])
            t2 = BinaryTree(ll[2])
            t8 = BinaryTree(ll[8])
            t9 = BinaryTree(ll[9])
            t10 = BinaryTree(ll[10])
            if 11 <= len(ll) -1:
                t11 = BinaryTree(ll[11])
            self.left_node = t2
            self.right_node = t3
            self.left_node.left_node = t4
            self.left_node.right_node = t5
            self.right_node.left_node = t6
            self.right_node.right_node = t7
            self.left_node.left_node.left_node = t8
            self.left_node.left_node.right_node = t9
            self.left_node.right_node.left_node = t10
            if 11 <= len(ll) -1:
                self.left_node.right_node.left_node = t11
            
##        if self.value == value:
##            t = BinaryTree(value)
## #           t.value = value
## #           t.left_node = self
##            self.left_node = t
####            pq = t
## #           return self
####            pq.left.node = self
####            self.print_binary_tree()
####            pq.print_binary_tree()
##        if value < self.value:
##            t = self
## #           t.value = value
##            self.value = value
            

        
 #      BinaryTree.insert_in_bst(self, value)
        # Replace pass above with your code
