edad = int(input("Digite su edad: "))
genero= input("Digite su sexo , H para hombre, M para mujer")

if edad>19:
    if genero in 'Hh':
        print("Señor. Usted es mayor de edad")
    elif genero in 'Mm':
        print("Señorita. Usted es mayor de edad")
    else:
        print("Dato incorrecto")


else:
    if genero in 'Hh':
        print("Señora. Usted es mayor de edad")
    elif genero in 'Mm':
        print("Señor. Usted es mayor de edad")
    else:
        print("Dato incorrecto")
        
    
    
