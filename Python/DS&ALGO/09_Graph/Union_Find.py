"""
서로소 집합이란 공통 원소가 없는 두 집합을 의미함

- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

- 서로소 집합 자료구조는 두 종류의 연산을 지원
    - 합집합 : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
    - 찾기 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

- 서로소 집합 자료구조는 합치기 찾기 자료구조라고 불리기도 함

- 여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정
    1. 합집합 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인함
        1. A와 B의 루트 노드 A', B'를 각각 찾음
        2. A'를 B'의 부모 노드로 설정
    2. 모든 합집합 연산을 처리할 때까지 1번의 과정 반복

- 서로소 집합 자료구조에서는 연결성을 통해 손쉽게 집합의 형태를 확인할 수 있음

- 기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없음
    - 루트 노드를 찾기 위해 부모 테이블을 계속해서 확인하며 거슬러 올라가야 함(재귀)

- 서로소 집합 자료구조 기본적인 구현 방법의 문제점
    - 합집합 연산이 편향되게 이루어지는 경우 찾기 함수가 비효율적으로 동작
    - 최악의 경우에는 찾기 함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V)임
    - 해결 방법 : 경로 압축을 이용
        - 찾기 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신함
        - 경로 압축 기법을 적용하면 각 노드에 대하여 찾기 함수를 호출한 이후에 해당 노드의 루트 노드가 바로 부모 노드가 됨
        - 기본적인 방법에 비하여 시간 복잡도가 개선됨
    
"""

# 서로소 집합 자료구조 기본적인 구현 방법
# 특정 원소가 속한 집합을 찾기
def find_parent1(parent, x):
    if parent[x] != x:
        return find_parent1(parent, parent[x])
    return x

# 경로 압축
def find_parent2(parent, x):
    if parent[x] != x:
        parent[x] = find_parent2(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent2(parent, a)
    b = find_parent2(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

"""
입력 예제

6 4
1 4
2 3
2 4
5 6

"""

# 테스트
if __name__ == '__main__':
    v, e = map(int, input().split())
    parent_table = [0] * (v+1)

    for i in range(1, v+1):
        parent_table[i] = i

    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent_table, a, b)

    print('각 원소가 속한 집합 : ', end = '')
    for i in range(1, v+1):
        print(find_parent2(parent_table, i), end = ' ')         # 여기서 parent_table이 한번 더 수정됨
    print()

    print('부모 테이블 : ', end = '')
    for i in range(1, v+1):
        print(parent_table[i], end = ' ')