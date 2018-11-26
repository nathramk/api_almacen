from db import db
from datetime import datetime
import time

class ProductModel(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.Integer, primary_key=True)
	nombre_producto = db.Column(db.String(80))
	fecha_vencimiento = db.Column(db.Date, nullable=False)#, default=datetime.utcnow)#, default=datetime.utcnow)
	cantidad = db.Column(db.Integer)
	unidad = db.Column(db.String(30))
	price_entrada = db.Column(db.Float(precision=2))
	price_salida = db.Column(db.Float(precision=2))
	entrada_id = db.Column(db.Integer, db.ForeignKey('entradas.id'))

	entrada = db.relationship('EntradasModel')

	def __init__(self, nombre_producto,fecha_vencimiento,cantidad,unidad,price_entrada, price_salida,entrada_id):
		self.nombre_producto = nombre_producto
		self.fecha_vencimiento = fecha_vencimiento
		self.cantidad = cantidad
		self.unidad = unidad
		self.price_entrada = price_entrada
		self.price_salida = price_salida
		self.entrada_id = entrada_id
	
	def json(self):
		return {
			'id': self.id,
			'nombre_producto': self.nombre_producto,
			'fecha_vencimiento': str(self.fecha_vencimiento),
			'cantidad': self.cantidad,
			'unidad': self.unidad,
			'price_entrada': self.price_entrada,
			'price_salida': self.price_salida,
			'entrada_id': self.entrada_id
		}

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	
	@classmethod
	def find_by_nameproduct(cls, nombre_producto):
		producto = cls.query.filter_by(nombre_producto=nombre_producto).first()
		return producto
	
	@classmethod
	def find_by_productId(cls, _id):
		producto = cls.query.filter_by(id=_id).first()
		return producto
	
	@classmethod
	def find_all(cls):
		producto = cls.query.all()
		return producto

	@classmethod	
	def find_by_date(cls, fecha_vencimiento):
		
		product = cls.query.filter_by(fecha_vencimiento=fecha_vencimiento).all()
		
		return product