from urllib.request import urlopen
from bs4 import BeautifulSoup   
from collections import OrderedDict     

# 1 open connection: tạo variable để lưu đường link
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read().decode('utf8')    

# f = open('scafef.html','wb')
# f.write(html_content)
# f.close()

# 2 find ROI
soup = BeautifulSoup(html_content,'html.parser')
table = soup.find('table',id="tableContent") 

# 3 extract ROI: lấy ra từng tin một: 
trs = table.find_all('tr')      

# 4 save excel
empty_list = []
for tr in trs:
    tds = tr.find_all('td')
    if tds and tds[0].string is not None:
        title =  tds[0].string.strip()    
        quy4_2016 = tds[1].string
        quy1_2017 = tds[2].string
        quy2_2017 = tds[3].string
        quy3_2017 = tds[4].string

    dic = OrderedDict({'Truoc Sau': title,'Quy 4 - 2016': quy4_2016,'Quy 1 - 2017': quy1_2017,'Quy 2 - 2017': quy2_2017,'Quy 3 - 2017': quy3_2017})

    empty_list.append(dic)            # ko còn bị lặp lại

# 4 save data: lưu vào excel
# import pyexcel
# make sure you had pyexcel-xls installed

# pyexcel.save_as(records=empty_list, dest_file_name="your_file50.xls")