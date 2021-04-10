
'''
문제) 자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 
꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자
를 출력합니다.

▣ 입력예제 1 
3
125 15232 97

▣ 출력예제 1
97
'''

import sys

# 실행시 파일을 읽어옴
# sys.stdin = open("input.txt", "rt")

# 숫자를 입력
n = int(input())
num_list = list(map(int, input().split()))

# 자릿수의 합을 반환하는 함수
def digit_sum(num):
    # 자릿수의 합을 저장할 변수
    sum = 0

    # num을 숫자로 이용하는 경우
    while num > 0:
        # num을 10으로 나눈 나머지를 더함
        sum += num%10
        # num에는 num을 10으로 나눈 몫을 저장
        num = num//10

    # num을 문자로 이용하는 경우
    '''
    for i in str(num):
        sum += int(i)
    '''

    return sum

max = 0
# 입력받은 숫자의 개수만큼 반복
for n in num_list:
    if max < digit_sum(n):
        max = digit_sum(n)
        result = n

print(result)