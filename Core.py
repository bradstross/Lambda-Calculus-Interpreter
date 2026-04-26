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
# for every phrase in our grammar.
#   TODO: What is an adequate way to capture applications? Very hard with this lexer style

def E(tokens):
    node = Node(None)
    for i, tk in enumerate(tokens):
        if tk.type == T.VAR:
            node.token = tk
            tokens.pop(0)
            return node
        elif tk.type == T.LAM:
            node.token = tk
            tokens.pop(0)
            node.left = E(tokens)
            # we need an if block here in case of multiple arguments; we want to make new lambdas if yes, move on if no
            if tokens[i+2] == T.VAR: 
                newlam = Token(T.LAM, "\\")
                node.right = E([newlam] + tokens)
            else:
                node.right = E(tokens)
        elif tk.type == T.DOT:
            tokens.pop(0)
            return E(tokens)
    return

test = [1, 2, 3]
test2 = [2]
test = test2 + test
# test3 = 
print([test.pop(0)])

# test = lex("(\\x.(\\y.x))")

# print(test[3])

