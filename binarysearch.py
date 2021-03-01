def binsr(ar,tar,start,end):
    mid = (start+end)//2
    if ar[mid] == tar:
        return mid
    while ar[mid]!=tar:
        if tar<ar[mid]:
            return binsr(ar,tar,start,mid)
        else :
            return binsr(ar,tar,mid,end)
        

arr = [1,3,5,7,8,10,11,12,13,888,8888,656565,656565656,5656565,6565656565656,565656565]

print(binsr(arr,12,0,10)) #7
