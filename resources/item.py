from sqlite3 import IntegrityError
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import ItemSchema,ItemUpdateSchema, PlainItemSchema
from models import ItemModel #para poder usar la importacion de models así era necesario el __init__.py
from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("item",__name__, description="Operations on items")

@blp.route("/item")
class ItemList(MethodView):
	@blp.response(200, ItemSchema(many=True))
	def get(self):
		return ItemModel.query.all()
	
	@blp.arguments(ItemSchema)
	@blp.response(201, ItemSchema)
	def post(self, item_data):
		print('item data',item_data)
		item= ItemModel(**item_data)
		try: 
			db.session.add(item) #agrega el item a la sesion
			db.session.commit() #guarda el item en la base de datos

		except IntegrityError:
			abort(409, message="Item already exists")
		except SQLAlchemyError:
			abort(500, message="Internal server error")
		print('tiem',item)
		return item, 201

@blp.route("/item/<string:item_id>")
class Item(MethodView):
	@blp.response(200, ItemSchema)
	def get(self, item_id):
		item = ItemModel.query.get_or_404(item_id)
		return item

	def delete(self, item_id):
		item= ItemModel.query.get_or_404(item_id)
		db.session.delete(item)
		db.session.commit()
		return item
	
	@blp.arguments(PlainItemSchema)
	@blp.response(200, ItemSchema)
	def put(self, item_data, item_id): #item_id viene del path y item_data del body
		item = ItemModel.query.get(item_id)
		print(item,  item_data, item_id)
		#si el id existe entonces se actualiza el item indicado , si no se crea un nuevo item
		if item:
			item.price = item_data["price"]
			item.name = item_data["name"]
		else:
			item = ItemModel(id=item_id ,**item_data)
		
		db.session.add(item)
		db.session.commit()
		return item, 200