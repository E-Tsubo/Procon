# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

# 逆ポーランド計算
# 実装のスピード重視のため、細かいエラーチェックをしていない。
# 入力値の記法が間違っているなどは、別でチェックが必要
def mycalc(a):
	stack = []

	for i in range(0,len(a)):
		#print(*stack)
		if a[i].isdigit() == True:
			stack.append(a[i])
		else:
			tmp1 = stack.pop()
			tmp2 = stack.pop()
			if a[i] == "+":
				stack.append(int(tmp2) + int(tmp1))
			elif a[i] == "-":
				stack.append(int(tmp2) - int(tmp1))
			elif a[i] == "*":
				stack.append(int(tmp2) * int(tmp1))
			else:
				print("Input Error.")

	return stack.pop()

def main():
	# Input Step
	a = input().split(" ")

	# Calc Step
	result = mycalc(a)

	# Output Step
	print(result)

if __name__ == '__main__':
	main()
