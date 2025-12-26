import python_basic.python_module as python_module

print("This is the main script.")

nums = []
vals = nums
vals.append(1)
print(nums)
print(vals)

nums1 = [1,2,3]
data = ('peter',) * (len(nums1) - nums1[::-1][0])
print(data)

t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
t3 = (True, False, None)
t4 = (5.0 , 6.0, 7.0)

t1, t2 = t3, t4
print(t1)
print(t2)

data = ()
print(data.__len__())