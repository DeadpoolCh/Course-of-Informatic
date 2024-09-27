# sets=list(map(int,input().split()))
# # sets=list(map(int,[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]))
# dicts={}
# for i in range(len(sets)):
# 	sums=0
# 	for j in range(i,len(sets)):
# 		sums+=sets[j]
# 		if sums==0:
# 			dicts[i]=(i,j)
# print('Подмассив с нулевой суммой существует' if len(dicts)>0 else '')

# sets=list(map(int,[0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]))
# # sets=list(map(int,input().split()))
# print(list('0'*sets.count(0)+'1'*sets.count(1)+'2'*sets.count(2)))

# sets=list(map(int,input().split()))
# # sets=list(map(int,[1,2,3,4,5,6,7]))
# for i in range(1,len(sets)-1,2):
# 	if sets[i-1]>sets[i]: sets[i],sets[i-1]=sets[i-1],sets[i]
# 	elif sets[i+1]>sets[i]: sets[i],sets[i+1]=sets[i+1],sets[i]
# 	if sets[-2]>sets[-1]: sets[-1],sets[-2]=sets[-2],sets[-1]
# print(*sets,sep=' ')





















































































