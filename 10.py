class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def enviar_mensaje(self, mensaje,sala):
        sala.recibir_mensaje(mensaje, self)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} ha recibido el mensaje: {mensaje}")


class Mensaje:
    def __init__(self, contenido):
        self.contenido = contenido


class SalaDeChat:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def enviar_mensaje(self, mensaje, usuario):
        for u in self.usuarios:
            if u != usuario:
                u.recibir_mensaje(mensaje.contenido)

    def recibir_mensaje(self, mensaje, usuario):
        print(f"{usuario.nombre} ha enviado el mensaje")
        self.enviar_mensaje(mensaje, usuario)
        
# Creamos algunos usuarios
usuario1 = Usuario("Juan")
usuario2 = Usuario("Maria")
usuario3 = Usuario("Pedro")

# Creamos una sala de chat
sala_de_chat = SalaDeChat()

# Agregamos los usuarios a la sala de chat
sala_de_chat.agregar_usuario(usuario1)
sala_de_chat.agregar_usuario(usuario2)
sala_de_chat.agregar_usuario(usuario3)

# Los usuarios envían mensajes en la sala de chat
usuario1.enviar_mensaje(Mensaje("Hola a todos"),sala_de_chat)
usuario2.enviar_mensaje(Mensaje("Hola Juan"),sala_de_chat)
usuario3.enviar_mensaje(Mensaje("Hola Maria"),sala_de_chat)
