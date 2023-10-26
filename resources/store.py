import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import StoreSchema
from db import db
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("store",__name__, description="Operations on stores")

@blp.route("/store")
class StoreList(MethodView):
	@blp.response(200, StoreSchema(many=True))
	def get(self):
		return StoreModel.query.all()
	

	@blp.arguments(StoreSchema)
	@blp.response(201, StoreSchema)
	def post(self, store_data):
		store= StoreModel(**store_data)
		try:
			db.session.add(store)
			db.session.commit()

		except IntegrityError:
			abort(409, message="Store already exists")
		except SQLAlchemyError:
			abort(500, message="Internal server error")

		return store, 201

@blp.route("/store/<string:store_id>")
class Store(MethodView):
	@blp.response(200, StoreSchema)
	def get(self, store_id):
		item = StoreModel.query.get_or_404(store_id)
		return item
	
	def delete(self, store_id):
		store= StoreModel.query.get_or_404(store_id)
		db.session.delete(store)
		db.session.commit()
		return "deleted!", 204