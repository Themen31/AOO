# Capa de Acceso a Datos
class ClienteDAO:
    def __init__(self):
        self.clientes = {}  # Simulando una base de datos con un diccionario

    def guardar_cliente(self, id_cliente, nombre):
        self.clientes[id_cliente] = nombre

    def obtener_cliente(self, id_cliente):
        return self.clientes.get(id_cliente, None)

# Capa de Lógica de Negocio
class ClienteServicio:
    def __init__(self, dao):
        self.dao = dao

    def registrar_cliente(self, id_cliente, nombre):
        self.dao.guardar_cliente(id_cliente, nombre)

    def obtener_nombre_cliente(self, id_cliente):
        return self.dao.obtener_cliente(id_cliente)

# Capa de Presentación
class ClienteControlador:
    def __init__(self, servicio):
        self.servicio = servicio

    def agregar_cliente(self, id_cliente, nombre):
        self.servicio.registrar_cliente(id_cliente, nombre)
        print(f"Cliente '{nombre}' agregado con éxito.")

    def mostrar_cliente(self, id_cliente):
        nombre = self.servicio.obtener_nombre_cliente(id_cliente)
        if nombre:
            print(f"Cliente: {nombre}")
        else:
            print("Cliente no encontrado.")

# Creando las instancias y conectando las capas
cliente_dao = ClienteDAO()
cliente_servicio = ClienteServicio(cliente_dao)
cliente_controlador = ClienteControlador(cliente_servicio)

# Uso de la aplicación
cliente_controlador.agregar_cliente(1, "Juan Pérez")
cliente_controlador.mostrar_cliente(1)
cliente_controlador.mostrar_cliente(2)