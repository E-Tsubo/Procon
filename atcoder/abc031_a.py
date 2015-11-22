import sys

def main():

	a,d = map( int, input().split( " ") )
	ans = max( (a+1)*d, a*(d+1) )
	print(ans)

if __name__ == '__main__':
	main()