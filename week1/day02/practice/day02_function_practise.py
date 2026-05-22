#utf-8

# 接收3个参数，返回一元二次方程 ax*x+bx+c=0的两个解
import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise ValueError("bad operand type")
    deleta = b * b - 4 * a * c
    x1 = (-b + math.sqrt(deleta)) / (2 * a)
    x2 = (-b - math.sqrt(deleta)) / (2 * a)
    return x1, x2
