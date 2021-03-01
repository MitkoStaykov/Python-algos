import math
import os
import random
import re
import sys


import bisect

class Multiset:
    l = list()
    def add(self, val):
        #self.l.append(val)
        #self.l.sort()
        ind = bisect.bisect(self.l,val,0,len(self))                
        self.l.insert(ind,val)
    def remove(self, val):
        if len(self)==0:
            return
        if not (self.searchh(val,0,len(self)-1)):
            return False
        ind = bisect.bisect(self.l,val,0,len(self))
        #for i in range(len(self.l)):
            #if(self.l[i] == val):                 
        del self.l[ind-1]
                #return
    def searchh (self,val,start,end):
        mid = (start+end)//2
        print (start,end)
        if (val == self.l[start] or val == self.l[end]) :
            return True
        if start+1==end:
            return False
        elif start == end :
            return False
        elif val < self.l[mid]:
            return self.searchh(val,start,mid)
        elif val > self.l[mid]:
            return self.searchh(val,mid,end)
        elif val == self.l[mid]:
            return True
        
    def __contains__(self, val):
        if len(self)==0:
            return False
        return self.searchh(val,0,len(self)-1)
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.l)
if __name__ == '__main__': 
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()