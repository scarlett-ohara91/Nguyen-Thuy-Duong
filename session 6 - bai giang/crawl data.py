from urllib.request import urlopen
from bs4 import BeautifulSoup   # de xac dinh ROI
from collections import OrderedDict     # ko xep theo alphabe

# 1 open connection: tạo variable để lưu đường link
url = "https://dantri.com.vn"
conn = urlopen(url)             # tao ra con duong noi lien may minh va server
raw_data = conn.read()          # lam du lieu chay ve may minh
content = raw_data.decode('utf8')     # sắp xếp lại dữ liệu thành dạng phổ thông

# print(content)

# 2 find ROI
soup = BeautifulSoup(content,'html.parser')
ul = soup.find('ul','ul1 ulnew')    # tao variable luu tru the ul: argu 1: tag name, argu 2: dac diem nhan dang: riêng class thi mới đc viet giá trị thôi, còn những cái khác, ví dụ id thì phải ghi đủ id=..
# print(ul.prettify())

# 3 extract ROI: lấy ra từng tin một: lấy từng cái thẻ li
li_list = ul.find_all('li')     # hàm find luôn trả về 1 list

empty_list = []
for li in li_list:
    # dic = {'Title':'','Link':''}
    
    h4 = li.h4                      # lấy ra h4 của thẻ li
    # print(h4)

    a = h4.a                        # lấy ra a của h4
    # print(a)

    title =  a.string.strip()       # lấy tiêu đề và bỏ hết space
    # print(title)            

    link = a['href']
    # print(link)                   # a như 1 cái dictionary thôi

    link2 = url + a['href']
    # print(link2)
    dic = OrderedDict({'Title': title,'Link': link2})
    # dic['Title'] = title
    # dic['Link'] = link2

    empty_list.append(dic)

print(empty_list)

# 4 save data: lưu vào excel
import pyexcel
# make sure you had pyexcel-xls installed

pyexcel.save_as(records=empty_list, dest_file_name="your_file2.xls")

