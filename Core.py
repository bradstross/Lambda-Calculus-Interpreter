# Goal is to eventually make this an interpreter for lambda calculus
# TODO: Parser for lambda caclulus
#   We want to use some kind of formal parsing structure for this.
# Lambda caclulus has a simple structure
# E ::= x | (\x.E) | (E E) 
# Let's change the grammar to make this easier lmao
# E ::= AB | AP
# AB ::= \x.E
# AP ::= Atom { Atom }
# Atom ::= x | (E)
# TODO: abstract syntax tree/parse tree (implement recursive descent?)
# https://en.wikipedia.org/wiki/Recursive_descent_parser

from Node import *
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

# E ::= ABST | APP
# ABST ::= \x.E
# APP ::= Atom { Atom }
# ATOM ::= x | (E)

def ATOM(tokens, i):
    if tokens[i].type == T.VAR:
        term = Node("var")
        term.left = Node(tokens[i].lexeme)
        return term, i + 1 
    if tokens[i].type == T.LP:
        term, j = E(tokens, i + 1)
        return term, (j + 1)  

def APP(tokens, term, j, length):
    if j >= length:
        return term, j
    elif tokens[j].type == T.VAR:
        appterm = Node("app")
        appterm.right, k = ATOM(tokens, j)
        appterm.left = term
        result, l = APP(tokens, appterm, k, length)
        return result, l
    elif tokens[j].type == T.LP:
        appterm = Node("app")
        appterm.right, k = ATOM(tokens, j)
        appterm.left = term
        result, l = APP(tokens, appterm, k, length)
        return result, l
    # add a boolean param that checks whether we have already seen an RP
    elif tokens[j].type == T.RP:
        return term, j
    else:
        return term, j

def ABST(tokens, i):
    term = Node(tokens[i].lexeme)
    term.left, j = ATOM(tokens, i + 1)
    term.right, k = ATOM(tokens, j + 1)
    return term, k

def E(tokens, i):
    length = len(tokens)
    if i > length:
        return None, i
    elif tokens[i].type == T.VAR:
        term, j = ATOM(tokens, i)
        term, j = APP(tokens, term, j, length)
        return term, j
    elif tokens[i].type == T.LP:
        term, j = ATOM(tokens, i)
        term, j = APP(tokens, term, j, length)
        return term, j
    elif tokens[i].type == T.DOT:
        return E(tokens, i + 1)
    elif tokens[i].type == T.LAM:
        #TODO: ABST tests/APP syntax
        term, j = ABST(tokens, i)
        term, j = APP(tokens, term, j, length)
        return term, j  
    elif tokens[i].type == T.RP:
        return E(tokens, i + 1)        
    return
    
# test = [1, 2, 3]
# testvar = test.pop(0)
# test.pop(0)
# test3 = 

test, j = E(lex("(\\x.(\\y.(x y))) z"), 0)
Node.in_order(test)
# print(f"{test}, {j}")
# print(f"{test.left.left}")
# print(f"{test.right.left}")
# print(test.left.left)
# print(test.right.left)

# test = lex("(\\x.(\\y.x))")

# print(test[3])

