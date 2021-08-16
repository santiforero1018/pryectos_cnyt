""" Probador de libreria de operaciones con numeros complejos

"""

import Libreria_numeros_complejos as nc


def main():
    """ Funcion principal

    :return: None
    """
    print("Hola usuario, este es un programa que rea liza operaciones con numeros complejos usando una libreria"
          "de operaciones basicas con numeros complejos, por favor, seguir las instrucciones para el buen"
          "funcionamiento del programa \n")
    print("si el numero b de la parte imaginaria es negativo, digite el numero de la siguiente manera:")
    print("a-b*i\n")
    numero_complejo1 = input("ingrese un numero complejo (a+b*i): ")
    numero_complejo2 = input("ingrese un numero complejo (a+b*i): ")
    par_complejo1 = [int(numero_complejo1[0]), int(numero_complejo1[1:-2])]
    par_complejo2 = [int(numero_complejo2[0]), int(numero_complejo2[1:-2])]
    print(par_complejo1, par_complejo2)
    print()
    print("elija la operacion que desee realizar con numeros complejos\n")
    operador = "0"
    while operador != "A":
        operador = input("Digite +,-,*,/ para realizar una operacion basica con numeros complejos, Digite A"
                         "para finalizar las operaciones: ")
        if operador == "+":
            resultado = nc.suma_complejos(par_complejo1, par_complejo2)
            print("El resultado de la suma de los numeros compejos es: ", resultado, "\n")
        elif operador == "-":
            resultado = nc.resta_complejos(par_complejo1, par_complejo2)
            print("El resultado de la resta de los numeros compejos es: ", resultado, "\n")
        elif operador == "*":
            resultado = nc.multiplicacion_complejos(par_complejo1, par_complejo2)
            print("El resultado de la multiplicación de los numeros compejos es: ", resultado, "\n")
        else:
            resultado = nc.division_complejos(par_complejo1, par_complejo2)
            print("El resultado de la división de los numeros compejos es: ", resultado, "\n")


main()
