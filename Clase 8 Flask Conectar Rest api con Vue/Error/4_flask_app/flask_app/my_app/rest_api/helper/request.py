import json

def sendResJson(data,msj,code):  #La data se va a enviar cuando la respuesta sea correcta y el mensaje cuando no sea correcta
    #La data como tal puede ser una data como tal    o un mensaje
    if code != 200:             #El codigo 200 en el http significa que la peticion se realizo correctamente
        return json.dumps(
            {
                'code': code,
                'msj': msj 
            }
        ),code                  #Devolvemos el codigo afuera de la lista, por siacaso , esto Code no se va a mostrar cuando hagamos en post
    else:
        return json.dumps(
            {
                'code':code,
                'data':data             #El data debe tener su formato correcto , no podemos pasarle un objeto de SQLAlchemy 
            }
        ),code                  #Devolvemos el codigo afuera de la lista, por siacaso , esto Code no se va a mostrar cuando hagamos en post