# 모르스 코드 결정트리
"""
모르스 부호란?

- 점과 선의 조합으로 구성된 메시지 전달용 부호

- 인코딩 : 알파벳에서 모르스 코드로 변환
    > 모르스 부호 표에서 바로 찾음 O(1)

- 디코딩 : 표에서 순차 탐색 O(n)

- 디코딩 방법 개선 => 결정트리
    > 결정트리(decision tree)
        . 여러 단계의 복잡한 조건을 갖는 문제에 대해
          조건과 그에 따른 해결방법을 트리 형태로 나타낸 것

"""


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 모르스 부호 표
table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..')]

# 결정 트리 알고리즘
def make_morse_tree():
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1]                                            # 모르스 코드
        node = root
        for c in code:                                          # 맨 마지막 문자 이전까지 이동
            if c == '.':                                        # 왼쪽으로 이동
                if node.left == None:                           # 비었으면 빈 노드 만들기
                    node.left = TNode(None, None, None)
                node = node.left                                # 왼쪽으로 이동
            elif c == '-':                                      # 오른쪽으로 이동
                if node.right == None:                          # 비었으면 빈 노드 만들기
                    node.right = TNode(None, None, None)
                node = node.right                               # 오른쪽으로 이동
        node.data = tp[0]                                       # 코드의 알파벳
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]


# 테스트
morse = make_morse_tree()
str = input(' 입력 문장 : ')
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print('Morse Code: ', mlist)
print('Decoding : ', end = '')
for code in mlist:
    ch = decode(morse, code)
    print(ch, end = '')
print()
                