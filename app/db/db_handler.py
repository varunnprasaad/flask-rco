from app.db import models


def getcars(search_query):
    cars = [car.as_dict() for car in models.Car.query.all()]
    return cars


def db_get_cars_by_category(category):
    cars = [car.as_dict() for car in models.Car.query.filter_by(category_id=category)]
    return cars
