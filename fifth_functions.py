def exec_with_stack(stack, l):
    for func in l.split():
        if func in definitions:
            stack = definitions[func](stack)
        else:
            if func[0] == '\\':
                stack.append(func[1:])
                continue
            try:
                stack.append(int(func))
            except:
                try:
                    stack.append(float(func))
                except:
                    stack.append(func)
    return stack

definitions = {}

def ffunc(*fname):
    def ffunc_int(func):
        for i in fname:
            definitions[i] = func
        return func
    return ffunc_int

### I/O
@ffunc("print")
def print_stack(stack):
    print(stack)
    return stack

@ffunc("print_fst")
def print_fst(stack):
    print(stack[-1])
    return stack

@ffunc("getln")
def getln(stack):
    stack.append(input(stack.pop() + " "))
    return stack

### Math
@ffunc("add", "+", "concat")
def add(stack):
    stack.append(stack.pop() + stack.pop())
    return stack

@ffunc("sub", "-")
def sub(stack):
    stack.append(stack.pop() - stack.pop())
    return stack

@ffunc("mul", "*")
def mul(stack):
    stack.append(stack.pop() * stack.pop())
    return stack

@ffunc("div", "/")
def div(stack):
    stack.append(stack.pop() / stack.pop())
    return stack

#### Comparisons
@ffunc("eq", "=")
def equals_stack(stack):
    stack.append(stack.pop() == stack.pop())
    return stack

#### Boolean Math
@ffunc("not", "!")
def stack_not(stack):
    v = stack.pop()
    if v == False:
        stack.append(True)
    else:
        stack.append(False)
    return stack

@ffunc("and", "&&")
def stack_and(stack):
    stack.append(stack.pop() and stack.pop())
    return stack

@ffunc("or", "||")
def stack_or(stack):
    stack.append(stack.pop() or stack.pop())
    return stack

@ffunc("boolequiv")
def stack_tobool(stack):
    stack.append(bool(stack.pop()))
    return stack

### Stack Operations
@ffunc("spjoin")
def spjoin(stack):
    return [" ".join([str(i) for i in stack[::-1]])]

@ffunc("reverse")
def reverse_stack(stack):
    return stack[::-1]

@ffunc("clear")
def clear_stack(stack):
    return []

@ffunc("dup", "dupl")
def dupl(stack):
    stack.append(stack[-1])
    return stack

### Loops and Conditions
@ffunc("while")
def while_loop(stack):
    code = stack.pop()
    while len(stack) == 0 or stack[-1]:
        stack = exec_with_stack(stack, code)
    return stack

@ffunc("if")
def if_stack(stack):
    code = stack.pop()
    if stack[-1]:
        stack = exec_with_stack(stack, code)
    return stack

### Defining new actions
@ffunc("define")
def define(stack):
    name = stack.pop()
    value = stack.pop()
    def return_static(stack):
        stack.append(value)
        return stack
    definitions[name] = return_static
    return stack

@ffunc("func")
def func(stack):
    name = stack.pop()
    value = stack.pop()
    def wow(stack):
        return exec_with_stack(stack, value)
    definitions[name] = wow
    return stack

### eval
@ffunc("eval")
def eval(stack):
    code = stack.pop()
    return exec_with_stack(stack, code)
