class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_expression_tree(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(Node(char))
        elif char in "+-*/^":
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[0]


def inorder_traversal(node):
    if node is None:
        return ""
    left = inorder_traversal(node.left)
    right = inorder_traversal(node.right)
    return f"({left}{node.value}{right})"


postfix_expression = "ab+cd+e+f*gi+j^*+"

tree = build_expression_tree(postfix_expression)

result = inorder_traversal(tree)

print("Обратное выражение:", result)
