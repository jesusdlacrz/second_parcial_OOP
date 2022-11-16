from parqueadero import Carros,Parqueadero
parking = Parqueadero(total_puestos= 200, puestos_disp= 10, puestos_van =2,puestos_SUV= 3,puestos_compact= 4)
carros = Carros(tipo_carro = "van", horas_parqueo= 4)
carros.hora_parqueo(hora_ent=5.00)
carros.precio_parq()
