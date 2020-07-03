from my_app import app

#app.config.from_pyfile('config.py')

app.run(host='0.0.0.0', port='5000')#debug=True
#app.config['debug']=True
#app.debug=True