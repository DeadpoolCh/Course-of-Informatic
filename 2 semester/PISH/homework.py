# from typing import Union
from parso.python.tree import Class

# def merge_and_process(data: list[Union[int, str, float]]) -> tuple[list[int], list[str], float]:
# 	data_int=list(map(lambda x: x+1, sorted((filter(lambda x: isinstance(x, int), data)))))
# 	data_str=list(sorted(map(lambda x: x.strip('0123456789'), (filter(lambda x: isinstance(x, str), data)))))
# 	data_float=list(filter(lambda x: isinstance(x, float), data))
# 	if len(data_float)==0: data_float=0.0
# 	else: data_float=sum(data_float)/len(data_float)
# 	return data_int, data_str, data_float
#
# print(merge_and_process([3, "abc123", 2.5, "hello", 42, 1.1, "42world", 5]))

def analyze_genome(data: list[int], mutation_mask: int) -> list[int]:
	checked = []
	odd_bits_mask = 0x55555555
	for i in range(len(data)):
		if (data[i] & mutation_mask) == 0:
			if (data[i] & odd_bits_mask) != 0:
				checked.append(i)
	return checked

print(analyze_genome([0b101010, 0b110011, 0b000111, 0b010101],0x55555555))
print(analyze_genome([0b11110000, 0b00001111, 0b10101010],0x55555555))

# def analyze_samples(samples: list[dict], threshold: float) -> dict:
#     result={}
#     for sample in samples:
#         for subs in sample:
#             result.setdefault(subs,[]).append(sample[subs])
#     for subs in result:
#         result[subs]=list(filter(lambda x: x>threshold,result[subs]))
#     return result
#
#
# samples = [
#     {"glucose": 5.5, "oxygen": 7.8},
#     {"glucose": 6.1, "oxygen": 4.3, "sodium": 3.9},
#     {"glucose": 7.0, "sodium": 4.2}
# ]
# threshold = 5.0
# samples = [
#     {"potassium": 2.3, "calcium": 1.1},
#     {"potassium": 3.5, "calcium": 4.4},
# ]
# threshold = 3.0
# result = analyze_samples(samples, threshold)
# print(result)

# def validate_data(func):
#     def wrapper(*args):
#         if len(args) == 1 and isinstance(args[0], list):
#             if all(isinstance(item, (int, float)) for item in args[0]):
#                 return func(*args)
#             else:
#                 raise ValueError("All elements must be numbers")
#         else:
#             raise ValueError("Input must be a list")
#     return wrapper
#
#
# @validate_data
# def calculate_mean(data: list) -> float:
# 	return sum(data) / len(data)
#
# print(calculate_mean([1, 2, 3, 4, 5]))  # 3.0
# print(calculate_mean("12345"))          # ValueError: Input must be a list
# print(calculate_mean([1, "two", 3]))    # ValueError: All elements must be numbers


# class TextAnalyzer():
# 	def __init__(self, text):
# 		self.text = text.strip().lower()
# 	def count_words(self)->int:
# 		return len(self.text.split())
# 	def unique_words(self)->set:
# 		return set(self.text.split())
# 	def find_longest_word(self)->str:
# 		return max(self.text.split(),key=len)
# 	def find_word_frequency(self,word:str)->int:
# 		return self.text.count(word)
# 	def replace_word(self,old:str,new:str)-> None:
# 		self.text=self.text.replace(old, new)
# 	def get_summary(self,max_words: int)->str:
# 		string=self.text.strip().split(' ')[:max_words]
# 		words=''
# 		for word in string:
# 			words+=word+' '
# 		return words
# 	def __str__(self)-> str:
# 		return str(self.text)
# 	def __len__(self)-> int:
# 		return len(self.text.strip())
#
# text = "  DNA sequencing is the process of determining the nucleic acid sequence.    DNA DNA sequencing   "
# analyzer = TextAnalyzer(text)
#
# # Методы анализа текста
# print(analyzer.count_words())               # 10
# print(analyzer.unique_words())             # {'dna', 'sequencing', 'is', 'the', 'process', 'of', 'determining', 'nucleic', 'acid', 'sequence'}
# print(analyzer.find_longest_word())        # 'sequencing'
# print(analyzer.find_word_frequency('dna')) # 3
#
# # Методы обработки текста
# analyzer.replace_word('dna', 'RNA')
# print(str(analyzer))                       # "rna sequencing is the process of determining the nucleic acid sequence. rna rna sequencing"
# print(analyzer.get_summary(5))             # "rna sequencing is the process"
#
# # Специальные методы
# print(len(analyzer))












































































