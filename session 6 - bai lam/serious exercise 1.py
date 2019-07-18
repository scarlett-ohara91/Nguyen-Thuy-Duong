# 2.1: Save to excel:
from urllib.request import urlopen
from bs4 import BeautifulSoup   
from collections import OrderedDict     

# 1 open connection: tạo variable để lưu đường link
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)          
raw_data = conn.read()         
content = raw_data.decode('utf8')     

# print(content)

# 2 find ROI
soup = BeautifulSoup(content,'html.parser')
div = soup.find('div',id='main')                   # cho các phần còn lại như role vào nữa đc ko? bằng cách nào? lấy 1 vùng nhỏ đc ko?
                                                   # thử cái 1 img trên trang https://stackoverflow.com/questions/20649048/display-text-from-img-alt-tag-with-beautifulsoup 
# print(div.prettify())                            # cai prettify này làm j? cho cái ul $0 được ko

# 3 extract ROI: lấy ra từng tin một: lấy từng cái thẻ li
# 3.a: lấy ra name:
li_list = div.find_all('li')       

empty_list = []

for li in li_list:   
    h3 = li.h3 
    a = h3.a                        
    title = a.string.strip()      

# 3.b: lấy ra artist:
    h4 = li.h4 
    a = h4.a                        
    artist = a.string.strip()      

    dic = OrderedDict({'Title': title,'Artist': artist})
    empty_list.append(dic)

# # 4 save data: lưu vào excel
# import pyexcel
# make sure you had pyexcel-xls installed

# pyexcel.save_as(records=empty_list, dest_file_name="Itunes_table.xls")

# 2.2: Download youtube:
from youtube_dl import YoutubeDL

options = {

    'default_search': 'ytsearch', 

    'max_downloads': 1, 

    'format': 'bestaudio/audio'

}

dl = YoutubeDL(options)

# print(empty_list)

for li in empty_list: 
    dl.download([li['Title'] + li['Artist']])        # sao ko tải đc hết nhở