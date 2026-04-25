# Goal is to eventually make this an interpreter for lambda calculus
# TODO: Parser for lambda caclulus
#   We want to use some kind of formal parsing structure for this.
# Lambda caclulus has a simple structure
# e ::= x | (lam x e) | (e e) 
# gonna do LL(2) because I prefer the grammar
# TODO: abstract syntax tree/parse tree (implement recursive descent?)
# https://en.wikipedia.org/wiki/Recursive_descent_parser


from enum import Enum
from Node import *

class T(Enum):
    VAR = 1
    LAM = 2
    APP = 3

#TODO: let's build a lexer first. Doesn't make sense to implement peeks_sym this way. 

def peek_sym(sng, index):
    if sng[index].isalpha():
        return T.VAR
    elif sng[index:index+2] == "(l":
        return T.LAM
    elif sng[index] == "(" and sng[index+1] != "l":
        return T.APP
    else:
        return "error: not well formed"



print(peek_sym("(f n)", 0))

# def accept(sym, index):
#     if (peek_sym(str, index))

# node = Node("lam", T.LAM)
# nl = Node("x", T.VAR)
# nr = Node("x", T.VAR)
# node.left = nl
# node.right = nr

#print(node.right)

#print("5222"[0])