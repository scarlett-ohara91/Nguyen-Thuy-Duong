from flask import Flask, render_template, redirect, request
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://admin:admin@c4e34-cluster-gnal4.mongodb.net/test?retryWrites=true&w=majority')

first_database = client.bike_database

first_collection = first_database['bike_collection']

app = Flask(__name__)

all_bikes = []

@app.route('/new_bike', methods=['GET','POST'])

def add_bike():
    if request.method == 'GET':
        return render_template('add_bike.html')
    elif request.method == 'POST':
        form = request.form
        model = form['model']
        daily_fee = form['daily_fee']
        img_link = form['img_link']
        year = form['year']
        added_bike = {
            'model':model,
            'daily_fee':daily_fee,
            'img_link':img_link,
            'year':year
        }
        all_bikes.append(added_bike)
        first_collection.insert_one(added_bike)

        return render_template('mine_bikes.html',ALL_BIKES=all_bikes)


if __name__ == '__main__':
    app.run(debug ='True')      