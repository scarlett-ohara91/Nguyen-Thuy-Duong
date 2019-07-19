from flask import Flask, render_template, redirect, request

app = Flask(__name__)

all_foods = [
        {'title':'Trà sữa trân châu đường đen',
        'description':'ngọt ngào dễ uống',
        'type': 'food',
        'link':'https://thuonghieuvietnoitieng.com/image/cache/admin/b6e81d47956a4d244614d5ec42bb9e35a74aa7bf/Tocotoco/xTRA-SUA-TRAN-CHAU-HOANG-GIA-5-445x445.jpg.pagespeed.ic.uANmujFmL5.jpg',
        'id':'TSTC'},
        {'title':'Caramen trà xanh',
        'description':'nhẹ nhàng thanh mát',
        'type': 'drink',
        'link':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFcZH-kNB9nK6mkCjCAW9kjosNnkN7Lz8-OoKA62RA2oYzzFT2',
        'id':'CRM'},
        {'title':'Táo đỏ chưng',
        'description':'đầy đủ dinh dưỡng',
        'type': 'food',
        'link':'http://yensaobienviet.com/wp-content/uploads/2018/10/yen-sao-voi-tao-do.jpg',
        'id':'TĐC'}
    ]

@app.route('/foods')

def home():
    # title = 'Trà sữa trân châu đường đen'
    # description = 'ngọt ngào dễ uống'
    # link = 'https://thuonghieuvietnoitieng.com/image/cache/admin/b6e81d47956a4d244614d5ec42bb9e35a74aa7bf/Tocotoco/xTRA-SUA-TRAN-CHAU-HOANG-GIA-5-445x445.jpg.pagespeed.ic.uANmujFmL5.jpg'

    return render_template('new_food.html',ALL_FOODS=all_foods)

@app.route('/foods/<int:index>')

def detailed_web(index):
    food = all_foods[index]
    return render_template('food_detailed.html',food=food)

@app.route('/foods/delete/<int:index>')

def del_web(index):
    del all_foods[index]
    return redirect('/foods')

@app.route('/foods/add_food', methods=['GET','POST'])

# khi truy cập trang tương đương với request GET

def add_food():
    if request.method == 'GET':
        return render_template('add_food.html')
    elif request.method == 'POST':
        form = request.form
        title = form['title']
        description = form['desc']
        link = form['img_link']
        food_type = form['food_type']
        added_food = {
            'title':title,
            'description':description,
            'link':link,
            'type':food_type
        }
        all_foods.append(added_food)
        return redirect('/foods')

@app.route('/foods/edit/<int:index>')
def edit(index):
    

if __name__ == '__main__':
    app.run(debug ='True')      