odd_list = []                           # vuot qua scope???
def get_even_list(int_list):
    odd_list = []
    int_list = [1, 2, 5, 9, -10, 6]
    for i in int_list:
        if i % 2 != 0:                  # no bi nhay cach sau remove ah?
            odd_list = odd_list + [i]     # i dang la int? 
    for j in odd_list:
        int_list.remove(j)       # co remove dc theo list nhu nay ko?
    
    return int_list

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
   print("Your function is correct")
else:
   print("Ooops, bugs detected")
