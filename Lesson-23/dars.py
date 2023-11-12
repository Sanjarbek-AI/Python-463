# def args_test(*args):
#     max_num = args[0]
#
#     for num in args:
#         if num > max_num:
#             max_num = num
#
#     return max_num
#
#
# result = args_test(2, 23, 4, 6, 43, 1, 3, 45, 323, 2)
# print(result)
def kwargs_test(**kwargs):
    return kwargs


result = kwargs_test()
print(result)

