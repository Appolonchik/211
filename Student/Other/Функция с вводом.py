
arg1 = int(input())
arg2 = int(input())
op = int(input())

def arithmetic(arg1, arg2, op):
    if op == '+':
        return(arg1 + arg2)
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return "Неизвестная операция"

