from models.product import ProductModel
from flask_restful import Resource, reqparse
import datetime as dt 

import time
from models.entradas import EntradasModel
from models.stock import StockModel
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
_product_parse.add_argument('detalle_cantidad',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('unidad',
    type=int,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('detalle_unidad',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('tipo_medicamento',
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
        #if ProductModel.find_by_nameproduct(request_data['nombre_producto']):
        #    return {"message": "el producto '{}' ya existe".format(request_data['nombre_producto'])}, 400
        #z = request_data["price_entrada"]+300
        #print("[0]::::: {}".format(request_data["nombre_producto"])) 
        #print("[1]::::: {}".format(request_data["fecha_vencimiento"]))
        #print("[2]::::: {}".format(request_data["cantidad"]))
        #print("[3]::::: {}".format(request_data["detalle_cantidad"]))
        #print("[4]::::: {}".format(request_data["unidad"]))
        #print("[5]::::: {}".format(request_data["detalle_unidad"]))
        #print("[6]::::: {}".format(z))
        #print("[7]::::: {}".format(request_data["price_salida"]))
        #print("[8]::::: {}".format(request_data["entrada_id"]))

        psearch_if = [g.json() for g in ProductModel.find_all()]
        product = ProductModel.find_by_nameproduct(request_data['nombre_producto'])
        if product:
            #req = ProductModel.fin_by_pricesalid(request_data['nombre_producto'], request_data['price_salida'])
            
            aaa = product.json()['cantidad']
            iddddd = product.json()['id']
            print("resss: {}".format(iddddd))
            product.cantidad = request_data['cantidad'] + aaa
            #stock = StockModel(request_data["cantidad"], request_data["detalle_unidad"], request_data['price_salida'], request_data["entrada_id"])

        else:
            product = ProductModel(**request_data)
                
        


        
        #a = "entrada de productos a la botica, mas abajo se detallan el nombre del producto y la cantidad que esta ingresando"
        #print(request_data['entrada_id'])
        #entrada = EntradasModel(a)
        #intentos = 0
        #while itentos < 10:
        #    d = request_data['entrada_id']
        #    entrada.save_to_db()s
        
        try:
            #stock.save_to_db()
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
class ProductPoracAbarce(Resource):
    def get(self):

        producto = [x.json() for x in ProductModel.find_all()]
        #if x['cantidad'] <= 20 and x['cantidad'] > 0
        

        zz = [produss['cantidad'] for produss in producto]

        poco = [x for x in zz if x<=20 and x>0]
        a = []
        for i in poco:
            #print("ttt: {}".format(i))
            #ss = [y.json() for y in ProductModel.fin_by_cantidad(i)]
            #tt = ProductModel.find_by_date(i)
            tt = ProductModel.fin_by_cantidad(i)
            a.append(tt.json())
                
        return {"productos":a}
        #print("ssss: {}".format(poco))

        #return {'producto vencidos': producto}


class ProductEnd(Resource):
    def get(self):
        times = time.strftime("%Y-%m-%d")
        producto = [x.json() for x in ProductModel.find_all()]
        #ss = producto[0]a
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
            #ss = [y.json() for y in ProductModel.find_by_date(i)]
            tt = ProductModel.find_by_date(i)
            a.append(tt.json())
        return {"productos":a}

        










        #if varialbe:
        #    return query.json()
        #return {'message': query.json()}
        #   return {'message':'sss'}
        #return {'message': 'todos estan al dia'}

        
        
    
