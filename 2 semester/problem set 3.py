# def unique(string: str) -> int:
# 	result = 0
# 	symbols=[]
# 	for chr in string:
# 		if chr not in symbols: symbols.append(chr)
# 	result=len(symbols)
# 	result=len(set(string))
# 	return result
#
# assert unique("aaaaaaaa") == 1
# assert unique("abab") == 2
# assert unique("abcd") == 4


# def is_anagram(word1: str, word2: str) -> bool:
# 	result = False
# 	symword1=[]
# 	dictsym={}
# 	count=0
# 	# for chr in word1:
# 	# 	if chr not in symword1: symword1.append(chr)
# 	# for chrs in word2:
# 	# 	if chrs in symword1: count+=1
# 	# if count==len(word2): result=True
#
# 	if set(word1)==set(word2): result=True
# 	return result
#
# assert is_anagram("abcd", "acdb")
# assert not is_anagram("abcde", "dl")


# def lengthOfLongestSubstring(s: str) -> int:
# 	result = 0
# 	chrset=set()
# 	# dicts={}
# 	# for i in range(len(s)):
# 	# 	dicts.setdefault(s[i],"")
# 	# 	dicts[s[i]]+=str(i)
# 	# print(dicts)
#
# 	return result
# lengthOfLongestSubstring('abcabcbb')


# def is_anagram_for_list(word: str,words: list) -> list:
# 	boollist=[]
# 	for elem in words:
# 		if set(elem).issubset(set(word)): boollist.append("True")
# 		else: boollist.append('False')
# 	return boollist
#
# print(is_anagram_for_list('абвгдеж',['еж','где','абоба']))

def is_scolarship_correct(best_students, active_students, delinquent_studens, lagging_students, all_students,
                          scolarships):
	""" Проверка корректности распределения стипендий по соц.группам студентов.

		Вход:
			best_students: list
				список лучших студентов
			active_students: list
				список социально активных студентов
			delinquent_students: list
				список студентов с дисциплинарками
			lagging_students: list
				список отстающих студентов
			all_students: list
				список всех студентов университета
			scolarships: list
				список студентов, выдвинутых на получение стипендии

		Условия:
			1. Все лучшие студенты обязаны получить стипендию
			2. Среди социально активных студентов, которые не являются при этом лучшими, получить стипендию может не больше половины
			3. Среди студентов с дисциплинарными взысканиями стипендию может получить не больше одного человека
			4. Студенты с плохими оценками не могут получить стипендию
			5. Среди студентов, не включенных в списки лучших, худших или социально активных, получить стипендию могут не более трёх человек

		Выход:
			is_correct: bool
				Отчёт о корректности распределения стипендий.
				True - если правила соблюдены, а иначе False.
	"""
	result = False
	list_res=[]
	count_res=0
	count_best=0
	for stud in best_students:
		if stud in scolarships:
			count_best+=1
	if count_best==len(best_students): count_res+=1
	count_act=0
	for stud in active_students:
		if stud in scolarships and stud not in best_students:
			count_act+=1
	if count_act<=len(active_students)//2+1: count_res+=1
	count_deling=0
	for stud in delinquent_studens:
		if stud in scolarships:
			count_deling+=1
	if count_deling<=1: count_res+=1
	count_lag=0
	for stud in lagging_students:
		if stud in scolarships:
			count_lag+=1
	if count_lag==0: count_res+=1
	usual=0
	for stud in all_lists:
		if stud in scolarships: usual+=1
	if usual<=3: count_res+=1
	if count_res==5: result=True
	return result
all_students = ["Орехов Максим", "Морозова Мия", "Семенов Александр", "Горбунов Виктор", "Владимиров Фёдор",
                "Любимова Виктория", "Иванов Марк", "Кузнецова Дарья", "Кузнецова Екатерина", "Осипов Михаил",
                "Лебедев Александр", "Меркулов Артём", "Беляева Вера", "Дорохов Никита", "Власов Владимир",
                "Семенова Мария", "Михайлов Савва", "Карасев Артём", "Мухин Михаил", "Белякова Юлия",
                "Судаков Фёдор", "Власов Матвей", "Суслова Алина", "Королева Амелия", "Панин Дмитрий"]

all_students2 = ["Орехов Максим", "Морозова Мия", "Семенов Александр",
                "Иванов Марк", "Меркулов Артём", "Беляева Вера", "Дорохов Никита", "Власов Владимир",
                "Семенова Мария", "Михайлов Савва", "Мухин Михаил", "Белякова Юлия",
                "Судаков Фёдор", "Суслова Алина", "Королева Амелия"]

best_students = ["Любимова Виктория", "Карасев Артём", "Власов Матвей", "Панин Дмитрий"]

active_students = ["Любимова Виктория", "Карасев Артём", "Кузнецова Дарья", "Кузнецова Екатерина", "Осипов Михаил",
                   "Лебедев Александр"]

delinquent_studens = ["Мухин Михаил", "Белякова Юлия"]

lagging_students = ["Горбунов Виктор", "Владимиров Фёдор"]

scolarships = ["Любимова Виктория", "Карасев Артём", "Власов Матвей", "Панин Дмитрий", "Кузнецова Екатерина", "Судаков Фёдор"]

all_lists=list(set(all_students)-set(best_students)-set(active_students)-set(lagging_students))
assert is_scolarship_correct(best_students, active_students, delinquent_studens, lagging_students, all_students, scolarships)
# print(is_scolarship_correct(best_students, active_students, delinquent_studens, lagging_students, all_students, scolarships))
































































