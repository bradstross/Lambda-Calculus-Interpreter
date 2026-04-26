from enum import Enum

class TType(Enum):
    VAR = 1
    LAM = 2
    APP = 3
    DOT = 4
    LP = 5
    RP = 6

# Lexemes should be the lexed string literals, type should be one of the TType enums
class Token:
    def __init__(self, type, lexeme):
        self.lexeme = lexeme
        self.type = type
    def __str__(self):
        return f"Lex: {self.lexeme} \nType: {self.type}"