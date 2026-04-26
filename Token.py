from enum import Enum

class TType(Enum):
    VAR = 1
    LAM = 2
    DOT = 3
    LP = 4
    RP = 5

# Lexemes should be the lexed string literals, type should be one of the TType enums
class Token:
    def __init__(self, type, lexeme):
        self.lexeme = lexeme
        self.type = type
    def __str__(self):
        return f"Lex: {self.lexeme} \nType: {self.type}"