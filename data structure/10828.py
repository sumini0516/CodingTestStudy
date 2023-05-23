import sys


def push(x):
    stack.append(x)


def pop():
    if (len(stack) == 0):
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    if (len(stack) == 0):
        return 1
    else:
        return 0


def top():
    if (len(stack) == 0):
        return -1
    else:
        return stack[-1]


x = int(input())
stack = []
for i in range(x):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == "push":
        push(str[1])
    elif str[0] == "pop":
        print(pop())
    elif str[0] == "empty":
        print(empty())
    elif str[0] == "size":
        print(size())
    elif str[0] == "top":
        print(top())