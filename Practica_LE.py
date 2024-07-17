class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)

class Priority_Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Mostrar_cola(self):
        if self.head == None:
            return print("La Sala de Urgencias está vacía, no hay pacientes para mostrar")
        node = self.head
        while node != None:  #Es igual a decir while node is not None:
            print(node.value)
            node = node.next

    def append(self, value, node):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return
        if node.next == None:
            new_node = Node(value)
            node.next = new_node
            new_node.prev = node
            self.tail = new_node
            self.size += 1
            return
        self.append(value, node.next)
    
    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return
        if self.head != None:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = new_node
            self.size += 1
            return
    

class Paciente():
    def __init__(self, nombre, edad, descripcion, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __repr__(self):
        return str(f"{self.nombre} - {self.descripcion} - {self.prioridad}")
    
def Crear_paciente(ll):
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    descripcion = input("Ingrese una descripción breve de la condición del paciente: ")
    prioridad = int(input("Ingrese el nivel de prioridad del paciente: "))
    paciente = Paciente(nombre, edad, descripcion, prioridad)
    new_node = Node(paciente)
    Insercion(ll, ll.head, new_node, paciente)

def Insercion(ll, node, new_node, paciente):
    if ll.head == None:
        ll.append(paciente, ll.head)
        ll.size += 1
        return ll
    elif node.next == None:
        if paciente.prioridad < ll.head.value.prioridad:
            ll.prepend(paciente)
            ll.size += 1
            return ll   
        elif paciente.prioridad < node.value.prioridad:
            nodo_a_desplazar = node
            nodo_a_desplazar.prev.next = new_node
            new_node.prev = nodo_a_desplazar.prev
            nodo_a_desplazar.prev = new_node
            new_node.next = nodo_a_desplazar
            ll.size += 1
            return ll
        else:
            ll.append(paciente, ll.head)
            ll.size += 1
            return ll
    elif paciente.prioridad < ll.head.value.prioridad:
        ll.prepend(paciente)
        ll.size += 1
        return ll
    elif paciente.prioridad < node.value.prioridad:
        nodo_a_desplazar = node
        nodo_a_desplazar.prev.next = new_node
        new_node.prev = nodo_a_desplazar.prev
        nodo_a_desplazar.prev = new_node
        new_node.next = nodo_a_desplazar
        ll.size += 1
        return ll
    Insercion(ll, node.next, new_node, paciente)

def Atención(ll):
    if ll.head == None:
        return print("No hay pacientes en la Sala de Urgencias para atender")
    print(ll.head.value)
    ll.head = ll.head.next
    if ll.head != None:
        ll.head.prev = None
    ll.size -= 1

def Actualizar_prioridad(ll, node):
    nombre_paciente = input("Ingrese el nombre del paciente para actualizar su prioridad: ")
    if ll.head == None:
        return print("La Sala de Urgencias está vacía, no hay pacientes para actualizar su prioridad")
    for i in range(ll.size):
        if nombre_paciente == node.value.nombre:
            if node.prev != None:
                node.prev.next = node.next
            if node.prev == None:
                ll.head = node.next
            if node.next != None:
                node.next.prev = node.prev
            if node.next == None:
                ll.tail == node.prev
            node.next = None
            node.prev = None
            nueva_prioridad = int(input("Ingrese la nueva prioridad para el paciente: "))
            node.value.prioridad = nueva_prioridad
            paciente = Paciente(node.value.nombre, node.value.edad, node.value.descripcion, node.value.prioridad)
            new_node = Node(paciente)
            Insercion(ll, ll.head, new_node, paciente)
        node = node.next
        if node == None:
            return ll

def Borrar(ll, nodo_a_borrar):
    if ll.head is None:
        return

    if ll.head == nodo_a_borrar:
        ll.head = ll.head.next
        if ll.head is not None:
            ll.head.prev = None
        else:
            ll.tail = None
    elif ll.tail == nodo_a_borrar:
        ll.tail = ll.tail.prev
        if ll.tail is not None:
            ll.tail.next = None
        else:
            ll.head = None
    else:
        nodo_a_borrar.prev.next = nodo_a_borrar.next
        nodo_a_borrar.next.prev = nodo_a_borrar.prev

    ll.size -= 1

def Atención_por_prioridad(ll, prioridad, cantidad):
    node = ll.head
    while node is not None and cantidad > 0:
        if node.value.prioridad == prioridad:
            print(f"El paciente {node.value.nombre} de prioridad {prioridad} ha sido atendido")
            next_node = node.next
            Borrar(ll, node)
            cantidad -= 1
            node = next_node
        else:
            node = node.next

def Atender_Mitad_De_Cada_Lote(ll):
    if ll.head is None:
        print("No hay pacientes en la Sala de Urgencias para atender")
        return

    prioridad_actual = ll.head.value.prioridad
    contador = 0
    node = ll.head

    while node is not None:
        if node.value.prioridad == prioridad_actual:
            contador += 1
        else:
            Atención_por_prioridad(ll, prioridad_actual, contador // 2)
            prioridad_actual = node.value.prioridad
            contador = 1
        node = node.next

    # Atender a los pacientes de la última prioridad
    Atención_por_prioridad(ll, prioridad_actual, contador // 2)
        
# def Atención_Por_Lotes(ll, node, prioridad_grupo_mayor=0, contador = 1, cantidad_grupo_mayor = 1):
#     if ll.head == None:
#         return print("No hay pacientes en la Sala de Urgencias para atender")
#     if node == None:
#         print(prioridad_grupo_mayor)
#         return
#     else:
#         if node.next == None:
#             Atención_Por_Lotes(ll, node.next, prioridad_grupo_mayor, contador)
#         elif node.next.value.prioridad == node.value.prioridad:
#             contador += 1
#             prioridad_grupo_mayor = node.value.prioridad
#             Atención_Por_Lotes(ll, node.next, prioridad_grupo_mayor, contador)
#         if contador > cantidad_grupo_mayor:
#             cantidad_grupo_mayor = contador
#         Atención_Por_Lotes(ll, node.next, prioridad_grupo_mayor, contador=1)
        
        
            
    """node == ll.head
    for i in range(ll.size):
        if node.value.prioridad == prioridad_grupo_mayor:
            if node == ll.head:
                Atención(ll)
            elif node == ll.tail:
                print(node.value)
                ll.tail == node.prev
                ll.tail.next == None
                ll.size -= 1
            elif node != ll.head and node != ll.tail:
                print(node.value)
                nodo_proximo = node.next
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None
                node = nodo_proximo
                ll.size -= 1
        if node.next != None:
            node = node.next
        return ll"""
        


Sala_de_Urgencias = Priority_Queue()
p1 = Paciente("Juan", 20, "Brazo roto", 1)
p2 = Paciente("Andres", 3, "Brazo lesionado", 1)
p3 = Paciente("Jose", 30, "Clavícula rota", 2)
p4 = Paciente("Sofia", 18, "Disparo de bala en su costado", 2)
p5 = Paciente("Ramiro", 30, "Uña torcida", 2)
p6 = Paciente("Samuel", 30, "Dolor de diente", 2)
p7 = Paciente("Santi", 30, "Dolor de Muela", 2)
p8 = Paciente("Tomi", 30, "Dolor de cabeza", 3)
p9 = Paciente("Joshua", 30, "Dolor de pierna", 3)
p10 = Paciente("Alejo", 30, "Dolor de dedo", 3)
p11 = Paciente("Sara", 30, "Dolor de pelo", 4)
p12 = Paciente("Vale", 30, "Dolor de espalda", 4)
p13 = Paciente("Jon", 30, "Dolor de espalda", 4)
p14 = Paciente("Juanchito", 30, "Dolor de espalda", 4)

node1 = Node(p1)
node2 = Node(p2)
node3 = Node(p3)
node4 = Node(p4)
node5 = Node(p5)
node6 = Node(p6)
node7 = Node(p7)
node8 = Node(p8)
node9 = Node(p9)
node10 = Node(p10)
node11 = Node(p11)
node12 = Node(p12)
node13 = Node(p13)
node14 = Node(p14)
# Crear_paciente(Sala_de_Urgencias)
# Crear_paciente(Sala_de_Urgencias)
# Crear_paciente(Sala_de_Urgencias)
# Crear_paciente(Sala_de_Urgencias)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node1, p1)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node2, p2)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node3, p3)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node4, p4)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node5, p5)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node6, p6)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node7, p7)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node8, p8)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node9, p9)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node10, p10)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node11, p11)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node12, p12)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node12, p13)
Insercion(Sala_de_Urgencias, Sala_de_Urgencias.head, node12, p14)
# Sala_de_Urgencias.Mostrar_cola()


Atender_Mitad_De_Cada_Lote(Sala_de_Urgencias)
Sala_de_Urgencias.Mostrar_cola()
# print("\n")
# Atención(Sala_de_Urgencias)
# Actualizar_prioridad(Sala_de_Urgencias, Sala_de_Urgencias.head)
# print("\n")

# Sala_de_Urgencias.append(p1, Sala_de_Urgencias.head)
# Sala_de_Urgencias.append(p2, Sala_de_Urgencias.head)
# Sala_de_Urgencias.append(p3, Sala_de_Urgencias.head)
# Sala_de_Urgencias.append(p4, Sala_de_Urgencias.head)

# Sala_de_Urgencias.Mostrar_cola()