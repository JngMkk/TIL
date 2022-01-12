from Stack_class import Stack

def checkBracket(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if ch == '}' and left != '{' or \
                    ch == ']' and left != '[' or \
                    ch == ')' and left != '(':
                    return False
    return stack.isEmpty()


# 테스트
str = ("{ A[(i+1)] = 0; }", "if( (i==0) && (j==0 )", "A[ (i+1] ) = 0;")
for s in str:
    m = checkBracket(s)
    print(s, " ---> ", m)
