# sets=list(map(int,input().split()))
# out=[]
# for i in range(len(sets)):
# 	if sum(sets[0:i])==sum(sets[i+1:-1]): out.append(i)
# print(*out)
# O(n*2)

# sets=list(map(int,input().split()))
# out=[]
# total_sum=sum(sets)
# sum_before_i=0
# for i in range(len(sets)):
# 	if sum_before_i==total_sum-sum_before_i-sets[i]: out.append(i)
# 	sum_before_i+=sets[i]
# print(*out)
# O(n)
















































































