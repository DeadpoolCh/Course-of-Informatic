# Глобальное выравнивание: все оптимальные варианты
seq1 = "CTTGGGGA"
seq2 = "TGGGTGA"

# scoring
match = 0
mismatch = -4
gap = -1

# создаём матрицу
n = len(seq1)
m = len(seq2)
score_matrix = [[0]*(n+1) for _ in range(m+1)]
trace_matrix = [[[] for _ in range(n+1)] for _ in range(m+1)]

# заполняем рамку
for i in range(1, m+1):
    score_matrix[i][0] = score_matrix[i-1][0] + gap
    trace_matrix[i][0].append('U')  # Up
for j in range(1, n+1):
    score_matrix[0][j] = score_matrix[0][j-1] + gap
    trace_matrix[0][j].append('L')  # Left



# заполнение основной матрицы
for i in range(1, m+1):
    for j in range(1, n+1):
        diag = score_matrix[i-1][j-1] + (match if seq1[j-1]==seq2[i-1] else mismatch)
        up = score_matrix[i-1][j] + gap
        left = score_matrix[i][j-1] + gap
        max_score = max(diag, up, left)
        score_matrix[i][j] = max_score
        if diag == max_score:
            trace_matrix[i][j].append('D')
        if up == max_score:
            trace_matrix[i][j].append('U')
        if left == max_score:
            trace_matrix[i][j].append('L')
for _ in score_matrix:
    print(*_)
# traceback: собираем все оптимальные выравнивания
def traceback(i, j, align1="", align2=""):
    if i == 0 and j == 0:
        yield (align1[::-1], align2[::-1])
        return
    for move in trace_matrix[i][j]:
        if move == 'D':
            yield from traceback(i-1, j-1, align1+seq1[j-1], align2+seq2[i-1])
        elif move == 'U':
            yield from traceback(i-1, j, align1+'-', align2+seq2[i-1])
        elif move == 'L':
            yield from traceback(i, j-1, align1+seq1[j-1], align2+'-')

# собираем все варианты
all_alignments = list(traceback(m, n))

# вывод
print(f"Score: {score_matrix[m][n]}")
print(f"Number of optimal alignments: {len(all_alignments)}\n")
for a1, a2 in all_alignments:
    print(a1)
    print(a2)
    print()