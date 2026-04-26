# Goal is to eventually make this an interpreter for lambda calculus
# TODO: Parser for lambda caclulus
#   We want to use some kind of formal parsing structure for this.
# Lambda caclulus has a simple structure
# E ::= x | (\x.E) | (E E) 
# Let's change the grammar to make this easier lmao
# E ::= AB | AP
# AB ::= \VAR.E
# AP ::= Atom ( Atom )
# Atom ::= VAR | (E)
# TODO: abstract syntax tree/parse tree (implement recursive descent?)
# https://en.wikipedia.org/wiki/Recursive_descent_parser

from Node import *
from Term import * 
from enum import Enum
from Token import TType as T
from Token import Token

def lex(str):
    tokens = []
    token = None
    length = len(str)
    i = 0
    while i < length:
        if str[i] == "(":
            token = Token(T.LP, "(")
            tokens.append(token)
            i += 1
        elif str[i] == ")":
            token = Token(T.RP, ")")
            tokens.append(token)
            i += 1
        elif str[i] == "\\":
            token = Token(T.LAM, "\\")
            tokens.append(token)
            i += 1
        elif str[i].isalpha():
            token =  Token(T.VAR, str[i])
            tokens.append(token)
            i += 1
        elif str[i] == ".":
            token =  Token(T.DOT, ".")
            tokens.append(token)
            i += 1            
        else:
            i += 1
    return tokens

# TODO: Now that we've got a lexer, we want a parser. This will require objects
# for every term in our grammar.
#   TODO: What is an adequate way to capture applications? Very hard with this lexer style

# we gotta go back to the drawing board. Nodes should be params args and instructions
def E(tokens):
    length = len(tokens)
    if tokens == []:
        return 
    elif tokens[0].type == T.VAR:
        term = VarExp(tokens[0].lexeme)
        tokens.pop(0)
        return term
    elif tokens[0].type == T.LP and tokens[1].type == T.LAM:
        tokens.pop(0)
        lam = tokens.pop(0)
        # auto-currying multiple arguments below
        if tokens[0].type == T.VAR and tokens[1].type == T.DOT:
            term = LambdaExp(E(tokens), E(tokens[1::]))
            return term
        elif tokens[0].type == T.VAR and tokens[1].type == T.VAR:
            term = LambdaExp(E(tokens), E([lam] + tokens[1::]))
            return term
        else:
            return "Error: expression not well-formed"
    elif tokens[0].type == T.LP and tokens[1].type == T.VAR:
        tokens.pop(0)
        term = AppExp(E(tokens), E(tokens[1::]))
        return term
    elif tokens[0] == T.RP:
        tokens.pop(0)
        return E(tokens) 
    elif tokens[0].type == T.DOT:
        tokens.pop(0)
        return E(tokens)
    return

# def E(tokens):
#     node = Node(None)
#     length = len(tokens)
#     i=0
#     while i < length:
#         if tokens[i].type == T.VAR:
#             node.token = tokens[i]
#             tokens.pop(0)
#             return node
#         elif tokens[i].type == T.LP and tokens[i+1].type == T.LAM:
#             node.token = tokens[i+1]
#             tokens.pop(0)
#             tokens.pop(0)
#             node.left = E(tokens)
#             # we need an if block here in case of multiple parameters; we want to make new lambdas if yes, move on if no
#             if tokens[i+2].type == T.VAR: 
#                 newlam = Token(T.LAM, "\\")
#                 node.right = E([newlam] + tokens)
#             else:
#                 node.right = E(tokens)
#         elif tokens[i].type == T.DOT:
#             tokens.pop(0)
#             return E(tokens)
#             # this is a bit problematic; how do we model applications on a parse tree?
#         elif tokens[i].type == T.LP and tokens[i+1].type == T.VAR:
#             tokens[i+1].type = T.APP
#             node.token = tokens[i+1]
#             tokens.pop(0)
#             tokens.pop(0)
#         else:
#             i += 1
#     return

test = [1, 2, 3]
testvar = test.pop(0)
test.pop(0)
# test3 = 
print(testvar)

# test = lex("(\\x.(\\y.x))")

# print(test[3])

