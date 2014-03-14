from fifth_functions import definitions, exec_with_stack
import sys

global stack
stack = []

def exec_one_line(l):
    global stack
    stack = exec_with_stack(stack, l)

if len(sys.argv) < 2:
    while True:
        exec_one_line(input(">>> "))
else:
    code = open(sys.argv[1]).read().split()
    exec_one_line(code)
