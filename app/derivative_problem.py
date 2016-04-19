from sympy import latex
import sympy as sym
import sympy.functions.elementary.trigonometric as trig
from sympy import simplify, cos, sin, expand, factor, Poly
import sympy.functions.elementary.exponential as exp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations,\
implicit_multiplication_application, function_exponentiation, convert_xor
from random import randint
from numpy import  arange


x = sym.symbols('x')
n = sym.symbols('n')
funcs = [exp.exp, exp.log, trig.sin, trig.cos, trig.tan]
rationals = [(lambda x: x**n) for n in arange(-10,10,1)]

funcs += rationals
print(arange(-10,10,1))
print([func(x) for func in rationals])

transformations = (standard_transformations +
        (implicit_multiplication_application, function_exponentiation,
            convert_xor))


def derivative_string():
    func = funcs[randint(0,len(funcs)-1)]
    coeff = randint(1,4)
    expression = func(coeff * x)
    expression_string = "\\frac{{d}}{{dx}}\\left( {} \\right) = ".format(latex(expression))

    answer = expression.diff(x)
    return expression_string, answer

def evaluate_derivative(solution, answer):
    if solution == None or answer == None:
        return None
    attempt = parse_expr(solution, transformations=transformations)
    return expand(simplify(answer - attempt), trig=True) == 0

