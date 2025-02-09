# import requests
# import gzip
# import shutil
#
# url = 'https://rest.uniprot.org/uniprotkb/stream?compressed=true&format=fasta&query=%28Insulin%29'
# with requests.get(url, stream=True) as request:
#     request.raise_for_status()
#     with open('insulin.fasta.gz', 'wb') as f_out_gz:
#         f_out_gz.write(request.content)
# with gzip.open('insulin.fasta.gz', 'rb') as f_in:
#     with open('insulin.fasta', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)
#
# from Bio import SeqIO
#
# with open('seq100.fasta','w') as f100,open('seq1000.fasta','w') as f1000, open('seq10000.fasta','w') as f10000, open('allseq.fasta','w') as alls:
#     count_100,count_1000,count_10000 = 0,0,0
#     for seq_record in SeqIO.parse("insulin.fasta", "fasta"):
#         if count_100 < 100:
#             f100.write(f">{seq_record.seq}\n".strip('>'))
#             count_100 += 1
#         if count_1000 < 1000:
#             f1000.write(f">{seq_record.seq}\n".strip('>'))
#             count_1000 += 1
#         if count_10000 < 10000:
#             f10000.write(f">{seq_record.seq}\n".strip('>'))
#             count_10000 += 1
#         alls.write(f">{seq_record.seq}\n".strip('>'))

import time
time_start = time.time()
amino_acid = {
    'A': 'Гидрофобная',   # Аланин (Ala)
    'V': 'Гидрофобная',   # Валин (Val)
    'L': 'Гидрофобная',   # Лейцин (Leu)
    'I': 'Гидрофобная',   # Изолейцин (Ile)
    'M': 'Гидрофобная',   # Метионин (Met)
    'F': 'Гидрофобная',   # Фенилаланин (Phe)
    'W': 'Гидрофобная',   # Триптофан (Trp)
    'P': 'Гидрофобная',   # Пролин (Pro)

    'G': 'Гидрофильная нейтральная',  # Глицин (Gly)
    'S': 'Гидрофильная нейтральная',  # Серин (Ser)
    'T': 'Гидрофильная нейтральная',  # Треонин (Thr)
    'C': 'Гидрофильная нейтральная',  # Цистеин (Cys)
    'U': 'Гидрофильная нейтральная',  # Селеноцистеин (Sec)
    'Y': 'Гидрофильная нейтральная',  # Тирозин (Tyr)
    'N': 'Гидрофильная нейтральная',  # Аспарагин (Asn)
    'Q': 'Гидрофильная нейтральная',  # Глутамин (Gln)

    'D': 'Гидрофильная отрицательная',  # Аспарагиновая кислота (Asp)
    'E': 'Гидрофильная отрицательная',  # Глутаминовая кислота (Glu)

    'K': 'Гидрофильная положительная',  # Лизин (Lys)
    'R': 'Гидрофильная положительная',  # Аргинин (Arg)
    'H': 'Гидрофильная положительная',  # Гистидин (His)

    'B': 'Неопределённая (Asp или Asn)',  # B = Asx (Aspartate или Asparagine)
    'Z': 'Неопределённая (Glu или Gln)',  # Z = Glx (Glutamate или Glutamine)
    'X': 'Неизвестная'  # X = Любая аминокислота
}
statistic = {category: 0 for category in set(amino_acid.values())}
with open('allseq.fasta','r') as seq10000:
    for seq in seq10000:
        set_acid=set(seq.strip())
        for acid in set_acid:
            statistic[amino_acid[acid]]+=seq.count(acid)
print(statistic)
print(time.time()-time_start)