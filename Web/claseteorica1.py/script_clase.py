import requests 
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/")
print(pedido)
print(pedido.json())
print(len(pedido.json()))

pedido = requests.get("https://macowins-server.herokuapp.com/prendas/404")
print(pedido.headers)
#el header me dice toda la metadata-- toda la informacion relativa a ese pedido. La fecha, que tipo de informacion trae(content type)
print(pedido.status_code) 
#me devuelve un error 404-- es decir que no existe
#status code:  habla de como fue la conexion, el estado de ese pedido. En este caso es 404
#request---- status code
        # ------ jason, trae la informacion del pedido 