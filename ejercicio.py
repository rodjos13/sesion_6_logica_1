# Implementar una calculadora que pida dos numeros y una operacion, vamos a usar la figura de switch...case y luego con if...elif...else.

# calculadora básica:

num_1 =float(input("Primer numero a consultar:"))

num_2 =float (input ("Segundo numero a consultar:"))

operador =input("Que operacion vas a hacer? (+,-,/,*)" )
                
# como asi que switch y case ?

# switch y case es una forma diferente de escribir condicionales, donde se evalua un parametro, booleano, y se va a direccionar inmediamente segun los casos definidos

# match operador: 
#     case "+":
#         print("Resultado", num_1 + num_2)
#     case "-":
#         print("Resultado", num_1 - num_2)
#     case "*":
#         print("Resultado", num_1 * num_2)
#     case "/":
#         if num_2 != 0: 
#             print("Resultado", num_1 / num_2)
#         else: 
#             print("Resultado no valido")
#     case _:
#         print("Resultado no valido")

if operador == "+": 
    print("Resultado", num_1 + num_2)

elif operador == "-":
    print("Resultado", num_1 - num_2)

elif operador == "*":
    print("Resultado", num_1 * num_2)
elif operador == "/": 
    if num_2 != 0: 
        print("Error dividiendo por cero.")

else:
    print("Operacion no valida.")





