from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, UserLogin
from resources.product import ProductListOne, RegisterProduct, ProductoList, ProductEnd, ProductPoracAbarce
from resources.entradas import RegistrarEntradas, EntradaGet, EntradasList
from resources.stock import RegistarStock,ListEstock


app = Flask(__name__)
app.secret_key='ken'
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTIONS']=True

@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWTManager(app)

api.add_resource(UserRegister,'/register')
api.add_resource(UserLogin, '/login')
api.add_resource(ProductListOne, '/producto/<string:nombre_producto>')
api.add_resource(RegisterProduct, '/producto')
api.add_resource(ProductoList, '/productos')
api.add_resource(ProductEnd, '/productoVencidos')
api.add_resource(RegistrarEntradas, '/entrada')
api.add_resource(EntradaGet, '/entrada/<int:entrada_id>')
api.add_resource(EntradasList, '/entradas')
api.add_resource(RegistarStock,'/estock')
api.add_resource(ListEstock, '/stocks')
api.add_resource(ProductPoracAbarce, '/ProductPoracAbarce')


if __name__=='__main__':
	from db import db
	db.init_app(app)
	app.run(debug=True)