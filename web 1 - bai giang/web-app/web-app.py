from flask import Flask, render_template        # Flask này là cái j

# 1: khởi tạo server - để thực hiện các tính năng mình viết ra
app = Flask(__name__)

# 2: build route
# function building: dính hàm vào 1 cái j đó (route)
@app.route('/')         # thể hiện trang chủ: /
def home():
# Cách 1 - ko dùng dictionary
    # title = 'Bún đậu'              
    # description = 'Rất ngon'
    # link = 'https://andemdanang.com/wp-content/uploads/2018/09/b%C3%BAn-%C4%91%E1%BA%ADu-m%E1%BA%AFm-t%C3%B4m-%C4%91n-600x400.jpg'

# Cách 2:
    # đổ dữ liệu sang template
    food = {'title': 'Bún đậu', 'description': 'Rất ngon', 'link':'https://andemdanang.com/wp-content/uploads/2018/09/b%C3%BAn-%C4%91%E1%BA%ADu-m%E1%BA%AFm-t%C3%B4m-%C4%91n-600x400.jpg'}
    return render_template('all_food.html', FOOD = food) # còn cách nào nữa ko ý nhỉ, mà chỉ dùng FOOD, ko có FOOD [title] bla bla 
    # return render_template('all_food.html', TITLE = title, DESCRIPTION = description, LINK = link)

# @app.route('/say-hi')         # tên hàm fai là unique, tên route cũng vậy
# def say_hi():
#     return 'Chào các mày'

# @app.route('/say-hi/<name>')         # <>: thể hiện biến
# def say_hi_everyone(name):
#     return 'Chào' + ' ' + name

# @app.route('/add/<int:x>/<int:y>')         # <>: chú ý cách convert
# def add(x,y):
#     total = x + y                           # ở đây thì nếu convert vẫn fai để dạng int(x)
#     return str(total)

# 3: run server
# if __name__ == '__main__':
    # app.run(debug ='True')      # cứ lưu là nó tự thay đổi theo. ko cần chạy lại