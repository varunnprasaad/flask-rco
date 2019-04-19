from sqlalchemy import Column, Integer, String, Date, Text

from app import db


class Base(db.Model):
    __abstract__ = True

    def __repr__(self):
        items = ['%s=%r' % (col.name, getattr(self, col.name))
                 for col in self.__table__.columns]
        return "<%s.%s[object at %x] {%s}>" % (self.__class__.__module__,
                                               self.__class__.__name__,
                                               id(self), ','.join(items))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    brand = Column(String)
    model = Column(String)
    mileage = Column(String)
    color = Column(String)
    production_year = Column(Integer)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    driver_license_number = Column(String)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(45))
    city = Column(String(45))
    state = Column(String(45))
    zipcode = Column(Integer)
    country = Column(String(20))


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(Integer)


class Insurance(Base):
    __tablename__ = 'insurance'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    policy = Column(Integer)


class RentalInsurance(Base):
    __tablename__ = 'rental_insurance'
    id = Column(Integer, primary_key=True)
    rental_id = Column(Integer)
    insurance_id = Column(Integer)


class Rental(Base):
    __tablename__ = 'rental'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    car_id = Column(Integer)
    pickup_location = Column(Integer)
    dropoff_location = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    remarks = Column(Text)
