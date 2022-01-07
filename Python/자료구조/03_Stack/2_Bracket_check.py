"""
괄호 검사 구현

- 조건 1 : 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
- 조건 2 : 같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다.
- 조건 3 : 서로 다른 타입의 괄호 쌍이 서로를 교차하면 안된다.

- 소스파일 괄호검사 가능

"""
from Stack_class import Stack

def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):           # 왼쪽 괄호를 만나면 스택에 삽입한다.
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():             # 오른쪽 괄호를 만나면 pop()연산으로 가장 최근에 삽입된 괄호를 꺼낸다.
                return False                # 이때 스택이 비었으면 조건 2에 위배된다
            else:
                left = stack.pop()          # 꺼낸 괄호가 오른쪽 괄호와 짝이 맞지 않으면 조건 3에 위배된다
                if ch == '}' and left != '{' or \
                    ch == ']' and left != '[' or \
                    ch == ')' and left != '(':
                        return False
    return stack.isEmpty()                  # 끝까지 처리했는데 스택에 괄호가 남아 있으면 조건 1에 위배된다.



# 테스트
str = ("{ A[(i+1)] = 0; }", "if( (i==0) && (j==0 )", "A[ (i+1] ) = 0;")
for s in str:
    m = checkBrackets(s)
    print(s, " ---> ", m)