nums = [1,3,2]

#multi = lambda a, b : a * b
#so above line will not work with list
#we need to take one element and multiply it by 2

result1 = list(map(lambda x : x*2, nums))
print(result1)

result2 = list(filter(lambda x : x%2==0, nums))
print(result2)

result3 = sorted(nums)
print(result3)


nums1 = [10,20,30,40,50]
#list comprehension
result4 = [x*2 for x in nums1]
print(result4)


result5 = []