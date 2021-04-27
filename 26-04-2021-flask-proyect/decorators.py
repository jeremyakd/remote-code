import time

def doblar_numero(func): # recibo una funcion como parametro y devuelvo otra
    print("Entro en la funcion doblar_numero")
    time.sleep(1)
    # PROCESO LOS DATOS

    def numero_doblado(num): # recibo el parametro de la llamada
        print("Entro en la funcion numero_doblado")
        suma = num+num
        time.sleep(1)
        func(suma) # lo duplico y llamo a la funcion

        # DEVUELVO LA "NUEVA FUNCION"
    time.sleep(1)
    print("retorno....")
    return numero_doblado


@doblar_numero # decorador, solo multiplica por 2 el numero
def imprime_numero(num):
    time.sleep(1)
    print("Se llama con 3 y recibe un => ", num)
    time.sleep(1)
    print(num)

imprime_numero(3)


""" 
def authenticate (user):
    # => afir JUAM PEREZ
    # LE PEGO A LA API DE AFIP PARA VER SI EXISTE 
    pass # te hago la validacion

@authenticate 
class User(name, passw):
    def __init__(self) -> None:
        super().__init__()
    pass

"""