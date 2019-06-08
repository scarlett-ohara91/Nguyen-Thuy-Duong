# # list1 = ['anh','em','chi']

# def search_A(haystack,needle):
#     for item in haystack:
#         if item == needle:
#             print('True')   
#         print('False')            

# search_A(list1,'ai')

list1 = ['anh','em','chi','anh','chi','anh','em','chi','anh']

def search_A(haystack,needle):
    count = 0
    for item in haystack:
        if item == needle:
            count += 1
            print(count)
            return True
    print(count)
    return False            # hereeeee

search_A(list1,'anh')


# list1 = ['anh','em','chi','anh','em','chi','anh','em','chi']

# def search_A(haystack,needle):
#     count = 0
#     ret_val = False
#     for item in haystack:
#         if item == needle:
#             ret_val = True
#             count += 1
#     print(count)
#     return(ret_val)
#     # print(count)               # ko ra là sao =))

# search_A(list1,'anh')

# # list1 = ['anh','chi','em']
# # def search_A(haystack,needle):
# #     ret_val = False
# #     for item in haystack:
# #         if item == needle:
# #             ret_val = True
# #         # else:
#         #     ret_val = False
#     print(ret_val)

# search_A(list1,'anh')
