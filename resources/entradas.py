from models.entradas import EntradasModel
from flask_restful import Resource, reqparse
_entrada_parser = reqparse.RequestParser()

_entrada_parser.add_argument('detalle',
    type=str,
    required=True,
    help="No dberia de estar en blanco"
)

class RegistrarEntradas(Resource):
    def post(self):
        data = _entrada_parser.parse_args()
        #if EntradasModel.find_by_id.
        #entrada = EntradasModel.find_by_id()
        entrada = EntradasModel(**data)
        try:
            entrada.save_to_db()
        except:
            return {"message":"ocurrio un error al isertar una nueva entrada"}, 500

        return entrada.json(),201

class EntradaGet(Resource):
    @classmethod
    def get(cls, entrada_id):
        entrada = EntradasModel.find_by_id(entrada_id)
        if not entrada:
            return {'message':'no se pudo encontrar la entrada'}
        return entrada.json()
        


class EntradasList(Resource):
    def get(self):
        entrada = [x.json() for x in EntradasModel.find_all()]
        return {'entradas': entrada}