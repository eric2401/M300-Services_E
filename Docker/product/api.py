#Product Service
 
 from flask import Flask 
 from flask_restful import Rescource, Api

 app = Flask(_name_)
 api = Api(app)

 class Product(Rescource):
     def get(self):
         return{
             'product':
                [
                    'Ice cream'
                    'Chocolate'
                    'Fruit'
                ]         
}

api.add_resource(Product, '/')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=80, debug=True)
