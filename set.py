# set 생성과 기본 연산
s = {1, 2, 3}
print(s, type(s))

print(len(s))
print(2 in s)
print(4 not in s)

# list의 중복 항목을 제거 할때 유용
l = [1, 2, 3, 2, 2, 4, 5, 5, 6]
s = set(l)
print(s)
l2 = list(s)
for n in l2:
    print(n, end=' ')
else:
    print()

# 메서드
s.add(10)
print(s)

s.add(1)
print(s)

s.discard(10)
print(s)

# 존재하지 아이템 삭제시 예외 발생
# s.remove(20)
# print(s)

s.update({5, 6, 10, 20})
print(s)

s.clear()
print(s)

# 수학 집합과 관련된 메서드
s1 = {1, 2, 3, 4, 5, 6, 7, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s5 = s1.difference(s2)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)

print(s1.issuperset(s4))
print(s5.issuperset(s2))
print(s4.issubset(s1))
