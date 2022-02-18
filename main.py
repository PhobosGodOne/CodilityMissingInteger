# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = sorted(A)
    minNum = 1
    if A[-1] < 0:
        return 1
    for i in range(0,len(A)):

        if i<len(A)-1 and A[i] == A[i+1]:
            continue
        if A[i] == minNum:
            minNum +=1
    return minNum






print(solution([1,3, 2]))


