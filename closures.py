# Function closures: Inner functions defined in non-global scope remember their enclosed namespaces when definition.

# Basic Example
# def outer():
#     x = 1
#     def inner():
#         print x # 1
#     return inner
# foo = outer()
# # print foo.func_closure
#
# foo()


# Similar to...
# def outer(x):
#     def inner():
#         print x # 1
#     return inner
# print1 = outer(1)
# print2 = outer(2)
# print1()
# print2()
