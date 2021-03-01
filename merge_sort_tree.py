A = [5,2,8,1,4,9,10,14,16,3,7,6]
n=len(A)
tree = [[] for i in range(4*n-1)]
print (n)
def build_tree(cur,l,r):
    if l==r :
        tree[cur].append(A[l])
        #return
    else:
        mid = (l+r)//2
        build_tree(2*cur+1,l,mid) 
        build_tree(2*cur+2,mid+1,r)
        tree[cur] = tree[2*cur+1]+tree[2*cur+2] # //Merging the two sorted arrays

def merge(left,right):
    myList=[]
    i=0
    j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            myList.append(left[i])
            i += 1
        else:
            myList.append(right[j])
            j += 1
    while i < len(left):
        myList.append(left[i])
        i += 1
    while j < len(right):
        myList.append(right[j])
        j += 1
    return myList

build_tree(0,0,n-1)
print (tree)