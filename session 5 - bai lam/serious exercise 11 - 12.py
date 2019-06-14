def is_inside(point_index, rec_index):              # ko de format nhu the nay dc ah?
    confirm_index = False
    if rec_index[0] <= point_index[0] <= rec_index[0] + rec_index[2] and rec_index[1] <= point_index[1] <= rec_index[1] + rec_index[3]:
        confirm_index = True

    return confirm_index

tester = is_inside([200, 120], [140, 60, 100, 200]) 

if tester == True:
   print("Your function is correct")
else:
   print("Ooops, bugs detected")