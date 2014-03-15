\reverse \spjoin \print_fst \clear reverse spjoin pln func

Welcome to Fifth, a stack-based programming language. pln
This tutorial will help you get started with the basics of Fifth. pln
Incidentally, it is written in Fifth. pln pln

Let's start out with pushing some things onto the stack. pln
Try running the following code: pln
Hello, world! pln

>>> getln eval print clear

Great! In case you hadn't noticed, the tutorial will \print the contents of pln
stack whenever you write any code. The stack is also cleared often, so be pln
careful in this tutorial. You can \clear the stack using the "clear" function, pln
\and \print it with the "print" function. Let's try it now. Run this code: pln
Hello, world! \clear \print pln

>>> getln eval

Note that nothing was printed when you ran the "print" function! This is because pln
you cleared the stack. Note that things which are not defined as functions are pushed pln
onto the stack. If you don't want this to happen, prefix the data with the "\" pln
character. Let's try it now: pln
I want to push \\print onto the stack. pln

>>> getln eval print clear

Great! Notice that the literal string "print" was pushed on the stack. pln
When we start to define functions, this will be really useful -- unless you pln
want to substitute the result of a function into your definition, you'll pln
need to escape function calls in function definitions. Sounds confusing? pln
Read the definition of the \pln function at the top of this tutorial. pln pln

Anyway, variables are a pretty important concept. Let's define one: pln
100 myNumber \define pln

>>> getln eval clear

\myNumber 100.0 \= reverse spjoin check_mynum func
clear Uh-oh! Looks like you didn't set \\myNumber to 100. Let's try that again. \pln reverse spjoin fail_mynum func
>>> \getln \eval \clear reverse spjoin retry_mynum func
check_mynum \fail_mynum \retry_mynum \check_mynum reverse spjoin while

Great! Looks like you've set your first variable! pln
