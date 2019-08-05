from flask import Flask, render_template       

app = Flask(__name__)

users = {
	'Huy': {
			'name':'Nguyen Quang Huy','gender':'male',
			'age': 29
       },
'Tuan Anh' : {
			'name':'Huynh Tuan Anh','gender':'male',
			'age': 17
       }
}

name_users = ['Huy','Tuan Anh']

@app.route('/<username>')

# cái return nó ko đi cùng với for đc ah? chỉ hiển thị 1 cái ah

def info_listing(username):
       if username not in name_users:
              return 'This user does not exist 1'
       else:
              person = users[username]
              return render_template('users.html',person_2 = person,name_users=name_users,username=username)

if __name__ == '__main__':
    app.run(debug ='True') 