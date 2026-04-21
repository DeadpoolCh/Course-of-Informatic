import re
def temp_melt(str):
    a=str.lower().count('a')
    t=str.lower().count('t')
    c=str.lower().count('c')
    g=str.lower().count('g')
    gc,at=c+g,a+t
    return round(69.3+0.41*(gc*100/len(str))-(650/(gc+at)),2),gc*100/len(str)

def max_complementarity(s1, s2):
    comp = str.maketrans('ATGC', 'TACG')
    s2_rc = s2.translate(comp)[::-1]
    max_match = 0
    for shift in range(-len(s1)+1, len(s2)):
        match = 0
        local_max = 0
        for i in range(len(s1)):
            j = i + shift
            if 0 <= j < len(s2_rc):
                if s1[i] == s2_rc[j]:
                    match += 1
                    local_max = max(local_max, match)
                else:
                    match = 0
        max_match = max(max_match, local_max)
    return max_match

def has_3prime_dimer(s1, s2, min_match=3):
    comp = str.maketrans('ATGC', 'TACG')
    s2_rc = s2.translate(comp)[::-1]
    tail = s1[-5:]
    for shift in range(-len(tail)+1, len(s2_rc)):
        match = 0
        for i in range(len(tail)):
            j = i + shift
            if 0 <= j < len(s2_rc):
                if tail[i] == s2_rc[j]:
                    match += 1
                    if match >= min_match:
                        return True
                else:
                    match = 0
    return False

def is_good_primer_pair(p1, p2):
    if max_complementarity(p1, p2) >= 4:
        return False
    if has_3prime_dimer(p1, p2):
        return False
    if abs(temp_melt(p1)[0] - temp_melt(p2)[0])>2:
        return False
    if 40>temp_melt(p1)[1]>60:
        return False
    if 40>temp_melt(p2)[1]>60:
        return False
    return True

v5,v3=[],[]
with open('311.txt') as f:
    for line in f:
        if line.startswith("5'"): v5.append(line[3:len(line)-1])
        elif line.startswith("3'"): v3.append(line[3:len(line)-1])

sv5,sv3='',''
for i in v5:
    sv5+=i
for i in v3:
    sv3+=i
# print(sv5)
# print(sv3)

m = re.search(r"[a,c,t,g]+", sv5)
if m:
    start, end = m.start(), m.end() - 1

forward,reversed=[],[]
for i in range(15,31):
    for j in range(start-100,start):
        str5=sv5[j:j+i]
        tm5=temp_melt(str5)[0]
        if tm5>=55 and tm5<=60 and str5.isupper():
            forward.append([str5,tm5])
    for t in range(end,end+100):
        str3=sv3[t:t + i]
        tm3=temp_melt(str3)[0]
        if tm3 >= 55 and tm3 <= 60 and str3.isupper():
                reversed.append([str3, tm3])
for i in range(len(forward)):
    print(forward[i],reversed[i],is_good_primer_pair(forward[i][0],reversed[i][0]),sep='\n')

