# hay que usar:
# property yes
# decorators yes
# abstract class yes
# exceptions yes
# comentarios yes
import abc
class Parqueadero:
    def __init__(self,total_puestos: int, puestos_disp: int,puestos_van: int,puestos_SUV: int,puestos_compact: int) -> None:
        
        self.total_puestos = total_puestos
        self.puestos_disp = puestos_disp
        self.puestos_van= puestos_van
        self.puestos_SUV= puestos_SUV
        self.puestos_compact= puestos_compact

    def parqueadero_van (self,puestos_van: int):
        if (self.puestos_van >= 1 ):
            self.puestos_van = self.puestos_van - 1
        else: 
            raise Exception("No hay plazas disponibles, vuelva pronto.")
        
    
    def parquedero_SUV (self,puestos_SUV: int):
    
        if (self.puestos_SUV >= 1 ):
            self.puestos_SUV = self.puestos_SUV - 1
        else: 
            raise Exception("No hay plazas disponibles, vuelva pronto.")
    
    def parquedero_compact(self,puestos_compact: int):

        if (self.puestos_compact >= 1 ):
            self.puestos_compact= self.puestos_compact - 1
        else: 
            raise Exception("No hay plazas disponibles, vuelva pronto.")
    
class Automoviles(abc.ABC):
    @abc.abstractmethod
    def hora_parqueo(self):
        ...
    @abc.abstractmethod
    def precio_parq(self):
        ...

class Carros(Automoviles):
    def __init__(self,tipo_carro: str, horas_parqueo = float) -> None:
        
        self.tipo_carro = tipo_carro
        self.horas_parqueo = horas_parqueo

    def hora_parqueo (self,hora_ent: int):
        if (hora_ent>=5.00 and hora_ent<22.00):
            print ("Abierto")
        else: 
            raise Exception("Cerrado, horario de 5:00 a.m - 22:00 pm")
        
        """
        este exception ayudará a que existan horas en las que no se pueda ingresar al
        parqueadero. 
        """
        
    @property
    def  precio_final(self):
        return  (1500* self.horas_parqueo)

    def precio_parq (self):
        
        if (self.tipo_carro == "compact"):
            precio  = self.precio_final* 1.1 
            print (f"el auto compact debe pagar $ {precio}")
        if (self.tipo_carro == "SUV"):
            precio  = self.precio_final* 1.2 
            print (f"el auto SUV pagar $ {precio}")
        if (self.tipo_carro == "van"):
            precio = self.precio_final* 1.3 
            print (f"la van debe pagar $ {precio}")

        """
        se uso el property con el fin de tener un precio fijo que varia
        segun el tipo de carro que ingrese al parqueadero.
        """