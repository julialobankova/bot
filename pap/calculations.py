from input import input_number,input_operation
from operations import sum, mult, sub, div 
from log import write_log
def calculation():
    a = input_number()
    b = input_number()
    op = input_operation()
    if op == '1':
        res = sum(a,b)
    elif op == '2':
        res = sub(a,b)
    elif op == '3':
        res = mult(a,b)
    elif op == '4':
        res = div(a,b)
    print(res)
    write_log(a,b,op,res)