# def delete_digits(string: str) -> str:
#     for char in string:
#         if char.isdigit(): string=string.replace(char,'')
#     result = string
#     return result
#
#
# def delete_letters(string: str) -> str:
# 	for char in string:
# 		if char.isalpha(): string=string.replace(char,'')
# 	result = string
# 	return result
#
# assert delete_digits('123abnd4FDhj32') == 'abndFDhj'
# assert delete_letters('123abnd4FDhj32') == '123432'


# def encode(word: str, permutation: list[int]) -> str:
# 	for i in range(len(permutation)):
# 		if
# 	result = word
# 	return result
#
# permutation = [
#     122, 98, 99, 100, 101, 102, 103, 104, 105,
#     106, 107, 108, 109, 110, 111, 112, 113, 114,
#     115, 116, 117, 118, 119, 120, 121, 97
# ]
#
# word = 'aboba'
# print(encode(word,permutation))
#
# assert 'zbobz' == encode(word, permutation)


def swap_words(sentence: str) -> str:
	words=sorted(sentence.split(),key=len,reverse=True)
	words[0],words[1]=words[1],words[0]
	space_count,k=[],0
	for i in range(len(sentence)):
		if sentence[i]==' ':k+=1
		else: space_count.append(k); k=0
		if i==len(sentence)-1: space_count.append(k)
	space_count.remove(0)
	temp=''
	for i in range(len(words)):
		temp+=' '*space_count[i]+words[i]
	result = temp+' '*space_count[-1]
	return result
# print(swap_words(' dd b  c   a  '))
# print(' dd b  c   a  ')
assert ' b dd  c   a  ' == swap_words(' dd b  c   a  ')












































































