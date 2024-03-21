## Diccionario de mensajes de error
def get_error(n):
    errorsDic = {
            1: "Dividir por 0 no es cool :_( ",
            2: "¿¿Qué operador es ese?? O.o ",
            3: "Eso no se puede usar para calcular!! >:P "
            }
    return errorsDic[n]

## Función de suma
def add(a,b):
    return str(a + b)

## Función de resta
def subs(a, b):
    return str(a - b)

## Función de multiplicación
def mul(a,b):
    return str(a * b)

## Función de división
def div(a,b):
    if b == 0:
        return get_error(1) 
    else:    
        return str(a / b)

## Función de módulo
def mod(a,b):
    if b == 0:
        return get_error(1)
    else:
        return str(a % b)

## Gestión de los mensajes de error
def error(msg, n):
    return msg + ": " + get_error(n)

## Salida de la aplicación
def logout():
    print("Vuelve cuando quieras!")
    exit()

## Check del tipo de operación elegida por el usuario
def check_operator(operator):
    if operator.lower() == "exit":
        logout()

    match operator:
        case "+":
            return "add" 
        case "-":
            return "subs" 
        case "*":
            return "mul" 
        case "/":
            return "div"
        case "%":
            return "mod" 
        case _:
            return "Error" 

## Check de valores validos introducidos por el usuario
def check_value(value):
    if value.lower() == "exit":
        logout()
    try:
        val = int(value)
        return True 
    except ValueError:
        try:
            val = float(value)
            return True 
        except ValueError:
            return False

## Muestra el menú de interacción con el usuario
def show_menu():
    operationsDic = {
            "add": add,
            "subs": subs,
            "mul": mul,
            "div": div,
            "mod": mod,
            "Error": error
            }
    calc_checker = "Error"

    print("\n**********************************************")
    print("*********>>> RETRO SNEAKY CALC <<*************")
    print("**********************************************")
    print("\nLos operadores disponibles son:")
    print("+ => suma")
    print("- => resta")
    print("* => multiplicación")
    print("/ => división")
    print("% => módulo, resto de la división")
    print("\nSi quieres salir, escribe: exit")
    print("\n****>>> Introduce los valores: <<<****")
    print("VALOR1 OPERADOR VALOR2")

    a = input("\nValor 1: ")
    if check_value(a):
        a = float(a)
        operator = input("Operación: ")
        calc_checker = check_operator(operator)
        if calc_checker.find("Error") == -1:
            b = input("Valor 2: ")
            if check_value(b):
                b = float(b)
            else:
                a = calc_checker = "Error" 
                b = 3
        else:
            a = calc_checker
            b = 2
    else:
        a = calc_checker
        b = 3

    result = operationsDic[calc_checker](a,b)
    print("\n###>> Resultado: " + result)

    more = input("\nPulsa S/s para salir.Enter para hacer otra operación... ")
    if more.lower() == "s":
        logout()
    show_menu()

show_menu()
