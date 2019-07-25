

peso = float(input ("Introduzca su peso"))
altura = float(input ("Introduzca su altura"))
IMC = (peso)/(altura**2)


if IMC<=18.0:
    print ("Peso demasiado bajo")
elif IMC<=24.9:
    print ("Su peso es normal felicidades")
elif IMC<=29.9:
    print ("Tiene sobrepeso, vigile su dieta")
elif IMC>29.9:
    print ("Obesidad grave, consulte su médico")
