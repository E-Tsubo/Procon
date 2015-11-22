import sys

def main():

	L,H = map( int, input().split( " ") )
	N = int(input())
	ans = []
	
	for i in range(N):
		tmp = int(input())
		if H < tmp:
			ans.append(-1)
		elif L <= tmp and tmp <= H:
			ans.append(0)
		else:
			ans.append(L-tmp)
			
	for x in range(len(ans)):
		print(ans[x])
	
if __name__ == '__main__':
	main()