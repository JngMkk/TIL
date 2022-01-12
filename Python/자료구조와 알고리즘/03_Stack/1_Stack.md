# 스택

> 파이썬으로 쉽게 풀어쓴 자료구조 참고

## 스택이란?

- 먼저 들어 온 데이터가 나중에 나가는 형식의 자료구조

  <img src="https://user-images.githubusercontent.com/87686562/149066497-eadba4de-5af9-4ea1-8ee0-dd93ad095e6c.png" alt="image" style="zoom:67%;" />

- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있음

- 스택의 용도

  - 되돌리기, 함수호출, 괄호 검사, 계산기(후위 표기식 계산, 중위 표기식의 후위 표기식 변환), 미로 탐색 등

- Stack ADT

  ```
  데이터 : FILO의 접근 방법을 유지하는 항목들의 모음
  
  연산
  - Stack() : 비어 있는 새로운 선택을 만듦
  - isEmpty() : 스택이 비어있으면 True 아니면 False
  - push(item) : item을 스택의 맨 위에 추가
  - pop() : 스택의 맨 위에 있는 항목을 꺼내 반환(삭제)
  - peek() : 스택의 맨 위에 있는 항목을 삭제하지 않고 반환
  - size() : 스택내의 모든 항목들의 개수 반환
  - clear() : 스택을 공백상태로 만듦
  ```

- 함수버전 스택의 구현

  ```python
  top = []
  def isEmpty():
      return len(top) == 0        # True / False
  def push(item):
      top.append(item)
  def pop():
      if not isEmpty():           # 공백상태가 아니면
          return top.pop(-1)      # 리스트 맨 뒤에서 하나 꺼내고 반환
  def peek():
      if not isEmpty():
          return top[-1]
  def size():
      return len(top)
  def clear():
      global top
      top = []
  ```

- 함수버전 스택의 구현2 (스택의 크기가 정해져 있는 경우)

  ```python
  SIZE = 5
  stack = [None] * SIZE
  top = -1
  
  def isFull():
      global top, stack, SIZE
      if top >= SIZE - 1:
          return True
      return False
  def push(data):
      global top, stack, SIZE
      if isFull():
          print('Stack is Full')
          return None
      top += 1
      stack[top] = data
  def isEmpty():
      global top, stack, SIZE
      if top == -1:
          return True
      return False
  def pop():
      global top, stack, SIZE
      if isEmpty():
          print('Stack is Empty')
          return None
      data = stack[top]
      stack[top] = None
      top -= 1
      return data
  def peek():
      global top, stack, SIZE
      if isEmpty():
          print('Stack is Empty')
          return None
      return stack[top]
  ```

- 클래스버전 스택의 구현

  ```python
  class Stack:
      def __init__(self):
          self.top = []
  
      def isEmpty(self):
          return len(self.top) == 0
      def size(self):
          return len(self.top)
      def push(self, item):
          self.top.append(item)
      def pop(self):
          if not self.isEmpty():
              return self.top.pop(-1)
      def peek(self):
          if not self.isEmpty():
              return self.top[-1]
      def __str__(self):
          return str(self.top[::-1])  # 처음부터 끝까지 역순으로 나타내어라.
  ```


---

## 스택의 응용 : 괄호 검사

- 괄호의 종류 : [], {}, ()

  - 조건 1 : 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함
  - 조건 2 : 같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 함
  - 조건 3 : 서로 다른 타입의 괄호 쌍이 서로를 교차하면 안됨

- 알고리즘

  ```python
  def checkBrackets(statement):
      stack = Stack()
      for ch in statement:
          if ch in ('{', '[', '('):	# if ch in '{[('을 써도 같은 결과
              stack.push(ch)		# 왼쪽 괄호를 만나면 stack에 삽입
          elif ch in ('}', ']', ')'):	# 오른쪽 괄호를 만나면 stack에서 최근에 삽입된 괄호 pop
              if stack.isEmpty():		# 스택이 비었으면
                  return False		# 조건 2 위반
              else:
                  left = stack.pop()		# 꺼낸 괄호가 오른쪽 괄호와 짝이 맞지 않으면
                  if ch == '}' and left != '{' or \
                      ch == ']' and left != '[' or \
                      ch == ')' and left != '(':
                      return False
      return stack.isEmpty()		# False면 조건 1위반
  ```

---

## 스택의 응용 : 수식의 계산

- 수식의 표기 방법 3가지

  | 전위(prefix)               | 중위(infix)                | 후위(postfix)              |
  | -------------------------- | -------------------------- | -------------------------- |
  | 연산자 피연산자1 피연산자2 | 피연산자1 연산자 피연산자2 | 피연산자1 피연산자2 연산자 |
  | + A B                      | A + B                      | A B +                      |
  | + 5 * A B                  | 5 + A * B                  | 5 A B * +                  |

  ![image](https://user-images.githubusercontent.com/87686562/149144932-60c00ba5-fe43-49b4-8508-b8374bc8094f.png)



- 후위표기 수식의 계산 방법

  <img src="https://user-images.githubusercontent.com/87686562/149145076-5dab73d5-6f52-4345-b52d-d098a1a2333f.png" alt="image" style="zoom:80%;" />

- 후위 표기 수식 계산 알고리즘

  ```python
  def evalPostfix(expr):
      s = Stack()
      for token in expr:
          if token in "+-*/":		# 항목이 연산자면
              val2 = s.pop()		# 피연산자2
              val1 = s.pop()		# 피연산자1
              if token == '+':
                  s.push(val1 + val2)
              elif token == '-':
                  s.push(val1 - val2)
              elif token == '*':
                  s.push(val1 * val2)
              elif token == '/':
                  s.push(val1 / val2)
          else:				# 항목이 피연산자이면
              s.push(float(token))	# 실수로 변경해서 스택에 저장
      return s.pop()
  ```

- 중위 표기 수식의 후위 표기 변환 ( 2 + 3 * 4 --> 2 3 4 * + )

  - 중위표기와 후위표기
    - 공통점 : 피연산자의 순서
    - 다른점 : 연산자의 순서
    - 후위 표기식의 연산자의 출력순서
      - 중위표기 수식의 연산자 우선순위 관계와 괄호에 의해 결정됨

- 알고리즘

  - 피연산자를 만나면 그대로 출력
  - 연산자를 만나면 스택에 저장했다가 스택보다 우선 순위가 낮은 연산자가 나오면 그때 출력
  - 왼쪽 괄호는 우선순위가 가장 낮은 연산자로 취급
  - 오른쪽 괄호가 나오면 스택에서 왼쪽 괄호위에 쌓여있는 모든 연산자를 출력

- 중위 -> 후위 변환 (A + B * C)

  <img src="https://user-images.githubusercontent.com/87686562/149146476-e39d6e67-ef4a-44bb-848d-8ed5d57fe289.png" alt="image" style="zoom: 67%;" />

- 중위 -> 후위 변환 (A * B + C)

  <img src="https://user-images.githubusercontent.com/87686562/149146852-44b405dc-e4ec-4c60-9872-7d6076c4a3b4.png" alt="image" style="zoom:67%;" />

- 중위 -> 후위 변환 (A + B) * C

  <img src="https://user-images.githubusercontent.com/87686562/149147014-58498556-7ff1-4e9d-89d4-f436a48aa20d.png" alt="image" style="zoom:67%;" />

- 알고리즘

  ```python
  def precedence(op):
      if op == '(' or op == ')':
          return 0
      elif op == '+' or op == '-':
          return 1
      elif op == '*' or op == '/':
          return 2
      else:
          return -1
  
  def Infix2Postfix(expr):                    # expr 입력(중위 표기식)
      s = Stack()
      output = []                             # output(후위 표기식)
      for term in expr:
          if term in '(':                     # 왼쪽 괄호이면
              s.push('(')                     # 스택에 삽입
          elif term in ')':                   # 오른쪽 괄호이면
              while not s.isEmpty():
                  op = s.pop()
                  if op == '(':               # 왼쪽 괄호가 나올 때까지
                      break                   # 스택에서 연산자를 꺼내 출력
                  else:
                      output.append(op)
          elif term in '+-*/':                # 연산자이면
              while not s.isEmpty():          # 우선순위가 높거나 같은 연산자를
                  op = s.peek()               # 스택에서 모두 꺼내 출력
                  if precedence(term) <= precedence(op):
                      output.append(op)
                      s.pop()
                  else:
                      break
              s.push(term)                    # 마지막으로 현재 연산자 삽입
          else:                               # 피연산자이면
              output.append(term)             # 바로 출력
  
      while not s.isEmpty():                  # 처리가 끝났으면 스택에 남은 항목을
          output.append(s.pop())              # 모두 output에 추가
  
      return output
  ```

---

## 스택의 응용 : 미로 탐색

- 미로 탐색이란?

  - 미로의 입구에서 시작해서 출구를 찾아 가는 문제

  <img src="https://user-images.githubusercontent.com/87686562/149148450-6ffc2755-f3c6-4516-bc9f-58aa73796e13.png" alt="image" style="zoom:67%;" />

- 시행착오를 이용하는 탐색방법

  - 하나의 경로를 시도해 보고 막히면 다시 다른 경로를 시도
  - 가던 길이 막히면 가장 최근 갈림길로 돌아가서 다른 길을 찾자

- 깊이우선탐색(DFS, Depth First Search) 알고리즘

  - 스택에 지나온 경로를 저장

  <img src="https://user-images.githubusercontent.com/87686562/149148631-3aae1047-559e-4e2b-83a2-bf9cb4ef281d.png" alt="image" style="zoom:67%;" />

- 알고리즘

  ```python
  def isValidPos(x, y):
      """ (x, y)가 갈 수 있는 방인지 검사하는 함수 """
      if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
          return False			# (x, y)가 미로 밖이면 갈 수 없음
      else:				# 출구('x')이거나 방('0')이면 갈 수 있음
          return map[y][x] == '0' or map[y][x] == 'x'
  
  def DFS():
      stack = Stack()
      stack.push((0, 1))				# 시작위치 삽입(튜플)
      print('DFS : ')
  
      while not stack.isEmpty():			# 공백이 아닐 동안
          here = stack.pop()				# 항목을 꺼냄
          print(here, end = '->')
          (x, y) = here
          if map[y][x] == 'x':			# 출구이면 탐색 성공. True 반환
              return True
          else:
              map[y][x] = '.'				# 현재위치를 지나왔다고 . 표시
              """ 4방향의 이웃을 검사해 갈 수 있으면 스택에 삽입 """
              if isValidPos(x, y - 1):
                  stack.push((x, y - 1))          # 상
              if isValidPos(x, y + 1):
                  stack.push((x, y + 1))          # 하
              if isValidPos(x - 1, y):
                  stack.push((x - 1, y))          # 좌
              if isValidPos(x + 1, y):
                  stack.push((x + 1, y))          # 우
          print('현재 스택 : ', stack)
      return False				# 탐색 실패. False 반환
  ```

  