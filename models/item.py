from db import db

#mapping between a row in a table to a python class an therefore a python objects
class ItemModel(db.Model):
    __tablename__ = "items" #creamos una tabla llamada items
    id= db.Column(db.Integer, primary_key=True) #creamos una columna llamada id
    name= db.Column(db.String(80), unique=True, nullable=False) #creamos una columna llamada name
    price= db.Column(db.Float(precision=2), unique=False, nullable=False) #creamos una columna llamada price
    store_id= db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False) #creamos una columna llamada store_id
    store= db.relationship("StoreModel", back_populates="items") #creamos la relacion entre store y store_id