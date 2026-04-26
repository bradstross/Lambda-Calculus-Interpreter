# Goal is to eventually make this an interpreter for lambda calculus
# TODO: Parser for lambda caclulus
#   We want to use some kind of formal parsing structure for this.
# Lambda caclulus has a simple structure
# E ::= x | (\x.E) | (E E) 
# gonna do LL(2) because I prefer the grammar
# TODO: abstract syntax tree/parse tree (implement recursive descent?)
# https://en.wikipedia.org/wiki/Recursive_descent_parser

from Node import *
from Token import TType as T
from Token import Token

# class TType(Enum):
#     VAR = 1
#     LAM = 2
#     APP = 3

# TODO: Let's build a lexer first. 
#   We will lex with the parentheses and simply omit them when building the parse tree
#   Lexer will split input strings and build a stack of tokens

# TODO: Now that we've got a lexer, we want a parser. This will require objects
# for every phrase in our grammar.

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

#make the string skip

test = lex("(\\x.x)")

print(test[5])

# def peek_sym(sng, index):
#     if sng[index].isalpha():
#         return T.VAR
#     elif sng[index:index+2] == "(l":
#         return T.LAM
#     elif sng[index] == "(" and sng[index+1] != "l":
#         return T.APP
#     else:
#         return "error: not well formed"



# print(peek_sym("(f n)", 0))

# def accept(sym, index):
#     if (peek_sym(str, index))

# node = Node("lam", T.LAM)
# nl = Node("x", T.VAR)
# nr = Node("x", T.VAR)
# node.left = nl
# node.right = nr

#print(node.right)

#print("5222"[0])