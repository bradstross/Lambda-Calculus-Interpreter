class Node:
    def __init__(self, expr, token):
        self.expr = expr
        self.token = token 
        self.left = None
        self.right = None

    def __str__(self):
        return f"Expr: {self.expr} \n Sym: {self.token}"
    
    # def post_order(node):
    #     for child in node.children:
    #         if child is not None:
    #             Node.post_order(child)
    #     print(str(node))

    # def pre_order(node):
    #     print(str(node))
    #     for child in node.children:
    #         if child is not None:
    #             Node.pre_order(child)    