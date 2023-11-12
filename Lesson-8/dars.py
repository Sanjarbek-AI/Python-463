# lists = [-1, -2, 3, -4, 1, 0, 5, -3, 8]
# mus = []
# man = []
# for i in lists:
#     if i >= 0:
#         mus.append(i)
#     else:
#         man.append(i)
# for iii in range(len(man)):
#     for ii in range(len(man)):
#         try:
#             i = man[ii]
#             i1 = man[ii+1]
#             if i > i1:
#                 del man[ii+1]
#                 man.insert(ii, i1)
#         except:
#             pass
# for iii in range(len(mus)):
#     for ii in range(len(mus)):
#         try:
#             i = mus[ii]
#             i1 = mus[ii+1]
#             if i < i1:
#                 del mus[ii+1]
#                 mus.insert(ii, i1)
#         except:
#             pass
# for i in mus:
#     man.append(i)
# print(man)

# nums = ["Salom", "Ayubxon", "Bobur"]
# nums1 = [1, 2, 3]
#
# nums.extend(nums1)
# print(nums + nums1 + nums1 + nums1)

nums = [-1, 12, -4, 12, 22, 44, -89, -65, 12, 22, 444, -876, 21]
max_num = 0
min_num = 0
for num in nums:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

max_num_index = nums.index(max_num)
min_num_index = nums.index(min_num)

nums[max_num_index] = min_num
nums[min_num_index] = max_num

print(nums)