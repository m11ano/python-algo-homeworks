class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = []
    postfix = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        elif char in precedence:
            while (
                stack and stack[-1] != "(" and precedence[stack[-1]] >= precedence[char]
            ):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)


def build_expression_tree(postfix_expression):
    stack = []
    for char in postfix_expression:
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
    if node.left or node.right:
        return f"({left}{node.value}{right})"
    return f"{node.value}"


expression = "(a+b)*(c*(d+e+f))+g*(i+j^2)"

postfix_expression = infix_to_postfix(expression)
print("Post expression:", postfix_expression)

tree = build_expression_tree(postfix_expression)

result = inorder_traversal(tree)
print("Recovered expression:", result)
