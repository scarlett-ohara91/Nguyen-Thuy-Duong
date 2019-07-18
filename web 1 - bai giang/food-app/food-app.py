from flask import Flask, render_template       

app = Flask(__name__)

all_foods = [
        {'title':'Trà sữa trân châu đường đen',
        'description':'ngọt ngào dễ uống',
        'type': 'food',
        'link':'https://thuonghieuvietnoitieng.com/image/cache/admin/b6e81d47956a4d244614d5ec42bb9e35a74aa7bf/Tocotoco/xTRA-SUA-TRAN-CHAU-HOANG-GIA-5-445x445.jpg.pagespeed.ic.uANmujFmL5.jpg'
        },
         {'title':'Caramen trà xanh',
        'description':'nhẹ nhàng thanh mát',
        'type': 'drink',
        'link':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFcZH-kNB9nK6mkCjCAW9kjosNnkN7Lz8-OoKA62RA2oYzzFT2'
        }
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

if __name__ == '__main__':
    app.run(debug ='True')      