from models.product import ProductModel
from flask_restful import Resource, reqparse
import datetime as dt 

import time
from models.entradas import EntradasModel
#from models.salida import SalidaModel

_product_parse = reqparse.RequestParser()
_product_parse.add_argument('nombre_producto',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('fecha_vencimiento',
    #type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'),
    type=lambda x: dt.datetime.strptime(x, "%Y-%m-%d").date(),
    #type=str,
    required=False,
    help="cannot be blank"
)
_product_parse.add_argument('cantidad',
    type=int,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('unidad',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('price_entrada',
    type=float,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('price_salida',
    type=float,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('entrada_id',
    type=int,
    required=True,
    help="cannot be blank"
)

class RegisterProduct(Resource):
    def post(self):
        request_data = _product_parse.parse_args()
        #print("sadad: {}".format(request_data))
        if ProductModel.find_by_nameproduct(request_data['nombre_producto']):
            return {"message": "el producto '{}' ya existe".format(request_data['nombre_producto'])}, 400
        

        product = ProductModel(**request_data)
        #a = "entrada de productos a la botica, mas abajo se detallan el nombre del producto y la cantidad que esta ingresando"

        #print(request_data['entrada_id'])
        #entrada = EntradasModel(a)
        #intentos = 0
        #while itentos < 10:
        #    d = request_data['entrada_id']
        #    entrada.save_to_db()s
        try:
            
            product.save_to_db()
            #salida.save_to_db()
        except:
            return {'message':'ah ocurrido un error al insertar el producto'}, 500
        
        return product.json(), 201


class ProductListOne(Resource):
    def get(self, nombre_producto):
        producto = ProductModel.find_by_nameproduct(nombre_producto)
        if producto:
            return producto.json()
        else:
            return {'message':'no se pudo encontrar el producto'}, 404

class ProductoList(Resource):
    def get(self):
        producto = [x.json() for x in ProductModel.find_all()]
        return {'productos':producto}

class ProductEnd(Resource):
    def get(self):
        times = time.strftime("%Y-%m-%d")
        producto = [x.json() for x in ProductModel.find_all()]
        #ss = producto[0]
        #productoend = [prduct['fecha_vencimiento'] for prduct in producto]
        aa = [produs['fecha_vencimiento'] for produs in producto] #if str(produs)==str(times)]
        #print("ssssssssssssssssss: {} and {}---------- {}".format(times, ss, aa))
        #if times == productoend:
        varialbe = [x for x in aa if x<=times]
        #query = ProductModel.find_by_date(str(varialbe))
        #ss = [y.json() for y in ProductModel.find_by_date(times)]
        a = []
        for i in varialbe:
            #print("ttt: {}".format(i))
            ss = [y.json() for y in ProductModel.find_by_date(i)]
            #tt = ProductModel.find_by_date(i)
            a.append(ss)
        return {"productos":a}
        










        #if varialbe:
        #    return query.json()
        #return {'message': query.json()}
        #   return {'message':'sss'}
        #return {'message': 'todos estan al dia'}

        
        
    
