# inter=sorted([list(map(int,input().split())) for _ in range(int(input()))],key=lambda x:x[1])
# itog=[]
# itog.append(inter.pop(0))
# for i in range(len(inter)):
# 	a,b=inter[i]
# 	if a>itog[-1][1]: itog.append(inter[i])
# print(len(itog))

# n,m=map(int,input().split())
# if n%2==0 and m%2==0: print('Lose')
# else: print('Win')

n,m=map(int,input().split())
def nim_sum(n, m): return n ^ m
def optimal_move(n, m):
    for i in range(n + 1):
        for j in range(m + 1):
            if nim_sum(n - i, m - j) == 0: return i, j
def play_game(n, m):
    while n > 0 or m > 0:
        i, j = optimal_move(n, m)
        n, m = n - i, m - j
        if n == 0 and m == 0:
            print("Lose" if nim_sum(n, m) == 0 else "Win")
play_game(n,m)

































































































