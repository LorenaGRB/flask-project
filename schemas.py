from marshmallow import Schema, fields

#creamos PainItemSchema y PlainStoreSchema para que no se haga referencia circular en ItemSchema y StoreSchema
#ya que ItemSchema y StoreSchema se hacen referencia mutuamente
#por ejemplo en ItemSchema se hace referencia a StoreSchema y en StoreSchema se hace referencia a ItemSchema
#por lo tanto se crean PlainItemSchema y PlainStoreSchema para que no se haga referencia circular


#en los schemas se deben refejar las relaciones entre las tablas (que estan en los models)
#para que se puedan hacer las consultas de forma correcta
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str(required=True)
        
class PlainTagsSchemas(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True) #dump only que aparece cuando envia data no cuando recibe

class ItemUpdateSchema(Schema):
	id = fields.Int()
	name = fields.Str()
    

class StoreSchema(PlainStoreSchema):
	items = fields.Nested(PlainItemSchema(), dump_only=True)
	tags = fields.Nested(PlainTagsSchemas(), dump_only=True)   

class TagsSchema(PlainTagsSchemas):
	store = fields.Nested(PlainStoreSchema(), dump_only=True)
	store_id = fields.Int(required=True, load_only=True)
