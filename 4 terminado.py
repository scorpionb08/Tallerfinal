class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    def itareas(self):
        print(self.tareas)

    def calcular_salario(self):
        salario = self.salario_base
        for tarea in self.tareas:
            tarea1.calcular_costo()
            salario+=tarea1.costo
            
        return int(salario)

    def __str__(self):
        return f"Empleado {self.nombre} con salario base {self.salario_base}"

class Tarea:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    def calcular_costo(self):
        return self.costo

    def __str__(self):
        return f"Tarea {self.nombre} con costo {self.costo}"


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        
    def horasextra(self):
        print("más de 8 horas por dia trabajando de lunes a viernes empiezan a contar extras\n")
        he=int(input("cuantas horas trabajo en la semana\n"))
        q=he-40
        if(he>40):
            print(f"trabajo {q} horas extra\n")
        else:
            return("no trabajo horas extra\n")

    def generar_informe(self):
        print(f"Departamento numero: {self.nombre}")
        for empleado in self.empleados:
            salario = empleado1.calcular_salario()
            print(f"{empleado} con salario {salario}")
            
        print()

    def __str__(self):
        return f"Departamento {self.nombre}"

h=int(input("ingrese la cantidad de empleados que quiere registar\n"))
for i in range(0,h):
    
    x=input("ingrese el nombre del empleado\n")
    y=int(input("ingrese el salario base del empleado\n"))
    empleado1 = Empleado(x, y)
    
    t=input("ingrese la tarea del empleado\n")
    u=int(input("ingrese el salario adiccional de esta tarea\n"))
    tarea1 = Tarea(t, u)
    w=int(input("¿Desea agregar al empleado a un departemento? 1. si  2. no\n"))
    if w==1:
        empleado1.agregar_tarea(tarea1)
        d=input("ingrese el departamento del empleado\n")
        departamento = Departamento(d)
        departamento.agregar_empleado(empleado1)
    
    p=int(input("¿Quiere ver las horas extras que fueron hechas?  1.si  2.no\n"))
    if p==1:
        departamento.horasextra()
    departamento.generar_informe()
    
