#!/usr/bin/python3


import sys
if(len(sys.argv) != 4):
    # Si el n argumentos es incorrecto, termino programa
    print("Número incorrecto de argumentos. Prueba:")
    print("calcu.py <operacion> <a> <b>")
    sys.exit()


_, operacion, numero1, numero2 = sys.argv
    # Con _, descartas el primer elemento de una lista-> es como llamarlo "_" y no usarlo mas
    # lo podrias haber llamado  de cualquier otra forma
if (operacion == 'multi'):
    operacion = '*'
    resultado = float(numero1) * float(numero2)
elif(operacion == 'entre'):
    operacion = '/'
    try:
        resultado = float(numero1)/float(numero2)
    except ZeroDivisionError:
        sys.exit("Error al dividir entre 0")
elif(operacion == 'mas'):
    operacion = '+'
    resultado = float(numero1)+float(numero2)
elif(operacion == 'menos'):
    operacion = '-'
    resultado = float(numero1)-float(numero2)

print("El resultado de la operacion es:")
print(numero1, operacion, numero2, "=", resultado)
