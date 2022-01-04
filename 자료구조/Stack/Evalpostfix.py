from Stack import Stack
# 후위 표기 수식 계산 알고리즘
def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in '+-*/':     # 항목이 연산자이면
            val2 = s.pop()      # 피연산자2
            val1 = s.pop()      # 피연산자1
            if token == '+':
                s.push(val1 + val2)
            elif token == '-':
                s.push(val1 - val2)
            elif token == '*':
                s.push(val1 * val2)
            elif token == '/':
                s.push(val1 / val2)
        else:                   # 항목이 피연산자이면
            s.push(float(token))    # 실수로 변경해서 스택에 저장
    return s.pop()

# 테스트
expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
print(expr1, ' --> ', evalPostfix(expr1))
print(expr2, ' --> ', evalPostfix(expr2))

# 중위 표기 수식의 후위 표기 변환
# 후위 표기식의 연산자의 출럭 순서: 중위표기 수식의 연산자 우선순위 관계와 괄호에 의해 결정됨. 스택 사용.
# 알고리즘
# 피연산자를 만나면 그대로 출력
# 연산자를 만나면 스택에 저장했다가 스택보다 우선 순위가 낮은 연산자가 나오면 그때 출력
# 왼쪽 괄호는 우선순위가 가장 낮은 연산자로 취급
# 오른쪽 괄호가 나오면 스택에서 왼쪽 괄호 위에 쌓여있는 모든 연산자를 출력
def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def Infix2Postfix(expr):
    s = Stack()
    output = []
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output

# 테스트
infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)
print('  중위표기: ', infix1)
print('  후위표기: ', postfix1)
print('  계산결과: ', result1, end='\n\n')
print('  중위표기: ', infix2)
print('  후위표기: ', postfix2)
print('  계산결과: ', result2)