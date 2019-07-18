from flask import Flask, redirect       

app = Flask(__name__)

@app.route('/about-me')
def about_me():
    return 'My name is Duong, from Vietnam. :) \nI am 28 years old and currently working as an auditor. ~~~ \nI love playing guitar and love shopping the mostttt'

@app.route('/school')
def school():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
    app.run(debug ='True') 