def transcription(dna:str)->str:
    '''
    Возвращает РНКу в виде строки
    dna: последовательность
    '''
    strs=dna.replace('A','U')
    strs=dna.replace('T','A')
    strs=dna.replace('C','G')
    strs=dna.replace('G','C')
    return strs

def probability_nucl(seq:str):
    '''
    Возвращает 5 строк с частотным соотношением (в процентах) нуклеодитов в последовательности и содержания CG.
    seq: строковая последовательность
    '''
    lens=len(seq)
    probab={i: f'{seq.count(i) / lens * 100:.2f}%' for i in set(seq)}
    cg=f"{(seq.count('C')+seq.count('G'))/lens*100:.3f}"
    print(f'CG-содержание: {cg}%')
    for key in probab.keys():
        print(f'Нуклеотид {key}: {probab[key]}')

def generate_seq(type:str,len: int)->str:
    '''
    Возвращает случайно сгенерированную последовательность ДНК или РНК
    type: DNA или RNK
    len: длина последовательности
    '''
    import random as rd
    if type=='DNA':
        nucl=['A','T','C','G']
        seq=''
        for i in range(len):
            seq+=rd.choice(nucl)
        return seq
    else:
        nucl=['A','U','C','G']
        seq=''
        for i in range(len):
            seq+=rd.choice(nucl)
        return seq
    
def translation(seq:str)->list:
	codon_table = {
		'AUA': 'Ile', 'AUC': 'Ile', 'AUU': 'Ile', 'AUG': 'Met',  # Isoleucine (Ile), Methionine (Met)
		'ACA': 'Uhr', 'ACC': 'Uhr', 'ACG': 'Uhr', 'ACU': 'Uhr',  # Uhreonine (Uhr)
		'AAC': 'Asn', 'AAU': 'Asn',  # Asparagine (Asn)
		'AAA': 'Lys', 'AAG': 'Lys',  # Lysine (Lys)
		'AGC': 'Ser', 'AGU': 'Ser',  # Serine (Ser)
		'AGA': 'Arg', 'AGG': 'Arg',  # Arginine (Arg)

		'CUA': 'Leu', 'CUC': 'Leu', 'CUG': 'Leu', 'CUU': 'Leu',  # Leucine (Leu)
		'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCU': 'Pro',  # Proline (Pro)
		'CAC': 'His', 'CAU': 'His',  # Histidine (His)
		'CAA': 'Gln', 'CAG': 'Gln',  # Glutamine (Gln)
		'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGU': 'Arg',  # Arginine (Arg)

		'GUA': 'Val', 'GUC': 'Val', 'GUG': 'Val', 'GUU': 'Val',  # Valine (Val)
		'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCU': 'Ala',  # Alanine (Ala)
		'GAC': 'Asp', 'GAU': 'Asp',  # Aspartic acid (Asp)
		'GAA': 'Glu', 'GAG': 'Glu',  # Glutamic acid (Glu)
		'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGU': 'Gly',  # Glycine (Gly)

		'UCA': 'Ser', 'UCC': 'Ser', 'UCG': 'Ser', 'UCU': 'Ser',  # Serine (Ser)
		'UUC': 'Phe', 'UUU': 'Phe',  # Phenylalanine (Phe)
		'UUA': 'Leu', 'UUG': 'Leu',  # Leucine (Leu)
		'UAC': 'Uyr', 'UAU': 'Uyr',  # Uyrosine (Uyr)
		'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',  # Stop codons
		'UGC': 'Cys', 'UGU': 'Cys',  # Cysteine (Cys)
	}
	aminoacids=[]
	for i in range(0,len(seq),3):
		if codon_table[seq[i:i+3]] !='Stop':
			aminoacids.append(codon_table[seq[i:i+3]])
		else:return aminoacids

seqRNA=generate_seq('RNA',51)
print(probability_nucl(seqRNA))
print(seqRNA)
seqDNA=generate_seq('DNA',51)
print(translation(seqRNA))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    