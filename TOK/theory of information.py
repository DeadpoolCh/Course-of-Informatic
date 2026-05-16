import pandas as pd
import math as m
import heapq
from itertools import count

strs='ИССЛЕДОВАНИЯ ТРЕБУЮТ ТОЧНОСТИ И ЛОГИКИ'
letter=[*set(strs)]

freq_dict={i:strs.count(i) for i in letter}
prob_dict={l:strs.count(l)/len(strs) for l in letter}
prod_dict=sorted(prob_dict.items(),key=lambda x:x[1],reverse=True)
freq_dict=sorted(freq_dict.items(),key=lambda x:x[1],reverse=True)

ascii_inf=len(strs)*8
print(f'Информация по ASCII = {len(strs)*8} бит')

df=pd.DataFrame(prod_dict, columns=['Символы','Вероятность'])
df['Частота']=[x[1] for x in freq_dict]

h=-1*sum([i*m.log(i,2) for i in df['Вероятность']])
print(f'Энтропия сообщения = {h:.2f} бит')
mean_len=h/m.log(2,2)
print(f'Среднее число символов кода на 1 букву (при двоичном кодировании) >= {mean_len:.2f}\n')

heap = []
counter = count()

for _, row in df.iterrows():
    heapq.heappush(
        heap,
        (row['Вероятность'], next(counter), row['Символы'])
    )

while len(heap) > 1:
    p1, _, left = heapq.heappop(heap)
    p2, _, right = heapq.heappop(heap)
    merged = (left, right)
    heapq.heappush(
        heap,
        (p1 + p2, next(counter), merged)
    )
tree = heap[0][2]

def build_codes(node, code='', codes=None):
    if codes is None:
        codes = {}
    if isinstance(node, str):
        codes[node] = code
        return codes
    left, right = node
    build_codes(left, code + '0', codes)
    build_codes(right, code + '1', codes)
    return codes

codes = build_codes(tree)

df['Кодир. Хаффмана'] = df['Символы'].map(codes)

mean_len_haf=(df['Вероятность']*df['Кодир. Хаффмана'].str.len()).sum()
print(f'Средняя длина при кодировке по Хаффману = {mean_len_haf:.2f}')
print(f'Изменение информации при кодировке по Шеннону-Фано = {ascii_inf-mean_len_haf*len(strs):.2f} бит или на {(ascii_inf-mean_len_haf*len(strs))/ascii_inf*100:.2f}%\n')


codes = {}

def shannon_fano(symbols, prefix=''):
    if len(symbols) == 1:
        symbol = symbols[0][0]
        codes[symbol] = prefix or '0'
        return
    total = sum(p for _, p in symbols)
    accum = 0
    split_idx = 0
    for i, (_, p) in enumerate(symbols):
        accum += p
        if accum >= total / 2:
            split_idx = i
            break

    left = symbols[:split_idx + 1]
    right = symbols[split_idx + 1:]

    shannon_fano(left, prefix + '0')
    if right:
        shannon_fano(right, prefix + '1')

shannon_fano(prod_dict)

df['Код Шеннона-Фано'] = df['Символы'].map(codes)

mean_len_shen = (df['Вероятность']*df['Код Шеннона-Фано'].str.len()).sum()
print(f'Средняя длина при кодировке по Шеннону-Фано = {mean_len_shen:.2f}')
print(f'Изменение информации при кодировке по Шеннону-Фано = {ascii_inf-mean_len_shen*len(strs):.2f} бит или на {(ascii_inf-mean_len_shen*len(strs))/ascii_inf*100:.2f}%')

print(df)
