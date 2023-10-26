from db import db

class StoreModel(db.Model):
    __tablename__ = "stores" #creamos una tabla llamada items
    id= db.Column(db.Integer, primary_key=True) #creamos una columna llamada id
    name= db.Column(db.String(80), unique=True, nullable=False) #creamos una columna llamada name
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic" , cascade="all, delete") #creamos la relacion entre store y store_id
    tags = db.relationship("TagsModel", back_populates="store", lazy="dynamic")