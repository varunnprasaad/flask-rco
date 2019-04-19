from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from app.db import db_handler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C://sqlite//data//test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_query = dict()
    search_query['pickup_location'] = request.form['pickup_location']
    search_query['dropoff_location'] = request.form['dropoff_location']

    search_query['pickup_date'] = request.form['pickup_date']
    search_query['pickup_time'] = request.form['pickup_time']

    search_query['dropoff_date'] = request.form['dropoff_date']
    search_query['dropoff_time'] = request.form['dropoff_time']

    search_results = db_handler.getcars(search_query)

    # return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)
