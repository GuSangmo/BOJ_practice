#2559. 수열
"""
Use sliding window

100 * 10만이니 1000만을 넘지않을 것.

"""

def getmax_partialsum(arr,window_size):
    start=0
    end=window_size    
    window=arr[start:end] #end가 끝나려면, end가 length여야함.
    maximum=maxsum=sum(window)
    while end<len(arr):
        maxsum+=arr[end]
        maxsum-=arr[start]
        maximum=max(maxsum,maximum)        
        start+=1; end+=1
        if end==len(arr): break
    return maximum
    
import sys
input=sys.stdin.readline
N,K=map(int,input().rstrip().split())
arrays=list(map(int,input().rstrip().split()))
print(getmax_partialsum(arrays,K))





