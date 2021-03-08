
'''
문제) K번째 큰 수

현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 
여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
은 22입니다.

▣ 입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력
된다.

▣ 출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.

▣ 입력예제 1 
10 3
13 15 34 23 45 65 33 11 26 42

▣ 출력예제 1
143
'''

import sys

# 실행시 파일을 읽어옴
# sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))

# set은 중복되는 자료를 제거함
res = set()

# 첫번째 카드 뽑기
for i in range(n):
	# 두번째 카드 뽑기
	for j in range(i+1, n):
		# 3번째 카드 뽑기
		for m in range(j+1, n):
			# 뽑힌 카드를 모두 더함
			# 더해진 결과를 set 형태의 데이터에 추가함
			# set 형식은 add를 통해 데이터를 추가함
			# set은 중복 데이터를 허용하지 않음
			# 따라서 중복되는 결과는 자동으로 제거됨
			res.add(a[i] + a[j] + a[m])

# 정렬을 위해 set을 list로 변환
res = list(res)
# 내림차순 정렬
res.sort(reverse=True)
# k 번째 변수 출력
print(res[k-1])
