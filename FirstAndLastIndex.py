'''Famous Problem of Leetcode to find the first and last index of a target value in the given sorted array'''

### Brute Force: O(n)   (Applying Linear Seach)
# L=list(map(int,input().strip().split()))
# key=int(input())
# c=0
# for i in range(0,len(L)):
#     if L[i]==key and c== 0:
#         c += 1
#         x=i
#         y=i
#     elif L[i]==key:
#         y=i
#         c += 1
#     else:
#         pass

# R=[x,y]
# print(R)

### Optimized Approach: O(log n) (Applying Binary Search)
L=list(map(int,input().strip().split()))
key=int(input())
# For finding the first index
start=0
end=len(L)-1
first_index=-1
while(start<=end):
    mid=int((start+end)/2)
    if L[mid]==key: # This can be the first occurence or the first occurrence would be on the left side
        first_index=mid
        end=mid-1   # Checking on left side if there is the first occurrence
    elif key<L[mid]:
        end=mid-1
    else:
        start=mid+1

# For finding the last  occurence index
start=0
end=len(L)-1
last_index=-1
while(start<=end):
    mid=int((start+end)/2)
    if key==L[mid]: #This can be the index of last occurrence or the last occurrene woul be at the right side
        last_index=mid
        start=mid+1 #Checking the right side if there is another(last) occurrence
    elif key<L[mid]:
        end=mid-1
    else:
        start=mid+1

R=[first_index, last_index]
print(R)
