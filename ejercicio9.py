class Empleado:
    def __init__(self):
        self.codigo = ""
        self.nombres = ""
        self.apellidos = ""
        self.salario_base = ""



    def calcular_retencion(self):
        total = (self.salario_base * 0.1)
        return total

    def salario_neto(self):
        if((self.salario_base -(self.salario_base*0.1)) <= 828116):
            total1 = (self.salario_base + 97032)
            return total1
        else:
            total1 = (self.salario_base)-(self.salario_base*0.1)
            return total1
            

    def datos_empleado(self):
        datos_empleado = self.nombres + " " + self.apellidos
        return datos_empleado
        

emp = Empleado()
emp.nombres = input("Ingrese Nombre: ")
emp.apellidos = input("Ingresar Apelido: ")
emp.salario_base = float(input("Ingresar salario: "))
print (emp.calcular_retencion())
print (emp.salario_neto())
print (emp.datos_empleado())
            
