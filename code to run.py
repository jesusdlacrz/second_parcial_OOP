from parqueadero import Carros,Parqueadero
parking = Parqueadero(nombre_cliente="Juan", puestos_van =2,puestos_SUV= 3,puestos_compact= 4)
parking.registro(nombre_cliente= "Juan" ,total_puestos= 200,puestos_disp= 10)

carros = Carros(tipo_carro = "van", horas_parqueo= 4)
carros.hora_parqueo(hora_ent=5.00)
carros.precio_parq()
#regis.registro(,total_puestos=200,puestos_disp=10)
