def knapsack01(Cap,N,v,w):
    # Base case 0 items left or knapsack is full
    if N == 0 or Cap == 0:
        return 0
    # if weight of current element is less than or equal to capacity we can
    # either include or exclude the item.
    if w[N-1] <= Cap:
         return max(v[N-1]+knapsack01(Cap-w[N-1],N-1,v,w),knapsack01(Cap,N-1,v,w))
    # if weight of current element is greater than the capacity we will
    # not include it thus returning just the ignoring part.
    else:
        return knapsack01(Cap,N-1,v,w)
v = [50, 100, 150, 200]
w = [8, 16, 32, 40]
Cap = 64
N=len(w)
print(knapsack01(Cap, N, v, w))