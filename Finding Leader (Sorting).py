#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Finding Leaders for an Unsorted Array
def find_leaders(arr):
    n = len(arr)
    max_right = arr[n-1]
    leaders = [max_right]

    for i in range(n-2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            leaders.insert(0, max_right)

    return leaders

arr = [7, 10, 4, 10, 6, 5, 2]
result = find_leaders(arr)
print(result)


# In[7]:


# Buy and Sell Stock
def max_profit(prices):
    if not prices or len(prices) == 1:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

result1 = max_profit(prices1)
result2 = max_profit(prices2)

print("Output for prices1:", result1)
print("Output for prices2:", result2)


# In[9]:


# Sum of All Subset XOR Totals
def XOR(nums):
    total_xor_sum = 0

    for i in range(1 << len(nums)):
        subset_xor = 0
        for j in range(len(nums)):
            if (i & (1 << j)) != 0:
                subset_xor ^= nums[j]
        total_xor_sum += subset_xor

    return total_xor_sum

nums1 = [1, 3]
nums2 = [5, 1, 6]

result1 = XOR(nums1)
result2 = XOR(nums2)

print("Output for nums1:", result1)
print("Output for nums2:", result2) 


# In[ ]:




