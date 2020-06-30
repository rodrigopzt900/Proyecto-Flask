from flask.views import MethodView
from flask import request
from my_app.product.model.product import Product
from my_app.product.model.category import Category
from my_app.rest_api.helper.request import sendResJson

from my_app import app,db
import json #Importamos esta libreria , para transformar el archivo sqlalchemy a un json el cual recien pueden manejar python o flask nativamente

class ProductApi(MethodView):
    def get(self,id=None):
        products = Product.query.all()
        print(products)
        
        if id:
            product = Product.query.get(id)
            res = productToJson(product)
        
        else:
            res= []
            for p in products:
                res.append(productToJson(p))
        return sendResJson(res,None,200)
    
    def post(self):
        if not request.form:                     #Si request.form no existe pues manda return y 403
            return sendResJson(None,"Sin parametro de nombre",403)                                       #
        #Validaciones de nombre
        if not "name" in request.form:
            return sendResJson(None,"Sin parametro de nombre",403)                                       #
        
        if len(request.form['name'])<3:
            return sendResJson(None,"El nombre es demasiado corto",403)                                       #
        #Validaciones de precio
        if not "price" in request.form:
            return sendResJson(None,"Sin parametro en precio",403)                                       #
        
        #if request.form['price'] is not float:     Esta validacion no funciona...
        #    return "Precio no valido",403      #Aplica la de abajo
        
        try:
            float(request.form['price'])            #Se ve raro pero quiere decir que si el numero 'price' se puede convertir a flotante pues lo acepta y si detecta algo como '195.5hola' pues manda el except
        except ValueError:
            return sendResJson(None,"El valor insertado no existe",403)                                       #
        
        #-Validaciones de categoria
        if not "category_id" in request.form:
            return sendResJson(None,"La categoria esta vacia ,creo",403)                                       #
        try:
            int(request.form['category_id'])            #Se ve raro pero quiere decir que si el numero 'price' se puede convertir a flotante pues lo acepta y si detecta algo como '195.5hola' pues manda el except
        except ValueError:
            return sendResJson(None,"La categoria no es valida",403)                                       #
  
        category = Category.query.filter(Category.id == int(request.form['category_id'])  ).all()       #
        #print('Categoria: ',category)                                                                  #   Esta validacion la hiciste tu , si puedes mejorarla pues dale.
        #print('Len de la categoiria:',len(category))                                                   #
        if len(category) == 0 :                                                                         #
            return sendResJson(None,"La categoria no existe",403)                                       #
        
        p.name = (request.form['name'])
        p.price = (request.form['price'])
        p.category_id = (request.form['category_id'])


        db.session.add(p)
        db.session.commit()
        return sendResJson(productToJson(p),None,200)
        
    
    def put(self,id):
        p = Product.query.get(id) #Queremos devolver una respuesta en el json por lo que   "product = Product.query.get_or_404(id)" no es valido
        if not p:
            return sendResJson(None,"Producto no existe",403)
        
        if not request.form:                     #Si request.form no existe pues manda return y 403
            return sendResJson(None,"Sin parametro de nombre",403)                                       #
        #Validaciones de nombre
        if not "name" in request.form:
            return sendResJson(None,"Sin parametro de nombre",403)                                       #
        
        if len(request.form['name'])<3:
            return sendResJson(None,"El nombre es demasiado corto",403)                                       #
        #Validaciones de precio
        if not "price" in request.form:
            return sendResJson(None,"Sin parametro en precio",403)                                       #
        
        #if request.form['price'] is not float:     Esta validacion no funciona...
        #    return "Precio no valido",403      #Aplica la de abajo
        
        try:
            float(request.form['price'])            #Se ve raro pero quiere decir que si el numero 'price' se puede convertir a flotante pues lo acepta y si detecta algo como '195.5hola' pues manda el except
        except ValueError:
            return sendResJson(None,"El valor insertado no existe",403)                                       #
        
        #-Validaciones de categoria
        if not "category_id" in request.form:
            return sendResJson(None,"La categoria esta vacia ,creo",403)                                       #
        try:
            int(request.form['category_id'])            #Se ve raro pero quiere decir que si el numero 'price' se puede convertir a flotante pues lo acepta y si detecta algo como '195.5hola' pues manda el except
        except ValueError:
            return sendResJson(None,"La categoria no es valida",403)                                       #
  
        category = Category.query.filter(Category.id == int(request.form['category_id'])  ).all()       #
        #print('Categoria: ',category)                                                                  #   Esta validacion la hiciste tu , si puedes mejorarla pues dale.
        #print('Len de la categoiria:',len(category))                                                   #
        if len(category) == 0 :                                                                         #
            return sendResJson(None,"La categoria no existe",403)                                       #
        
        p = Product(request.form['name'],request.form['price'],request.form['category_id'])
        db.session.add(p)
        db.session.commit()
        return sendResJson(productToJson(p),None,200)

    
    def delete(self,id):
        product = Product.query.get(id) #Queremos devolver una respuesta en el json por lo que   "product = Product.query.get_or_404(id)" no es valido
        if not product:
            return sendResJson(None,"Producto no existe",403)
        db.session.delete(product)
        db.session.commit()
        return sendResJson('Producto eliminado',None,200)

    
    
def productToJson(product: Product):
    return {
                'id': product.id,
                'name': product.name,
                'category_id': product.category_id,
                'category': product.category.name
            }
    
product_view= ProductApi.as_view('product_view')
app.add_url_rule('/api/products/',view_func=product_view,methods=['GET',"POST"])
app.add_url_rule('/api/products/<int:id>',view_func=product_view,methods=["GET","DELETE","PUT"])