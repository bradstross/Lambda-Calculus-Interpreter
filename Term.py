class VarExp:
    def __init__(self, var):
        self.var = var

class LambdaExp:
    def __init__(self, var, body):
        self.var = var
        self.body = body

class AppExp:
    def __init__(self, op, rand):
        self.op = op
        self.rand = rand