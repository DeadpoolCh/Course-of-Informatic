def copy_fasta_n_times(input_fasta: str, output_fasta: str, n: int):
	"""
	Читает содержимое входного FASTA-файла и копирует его n раз в выходной файл.
	:param input_fasta: путь к исходному FASTA-файлу
	:param output_fasta: путь к выходному FASTA-файлу
	:param n: количество повторений содержимого
	"""
	with open(input_fasta, 'r') as infile:
		fasta_content = infile.read()

	with open(output_fasta, 'w') as outfile:
		for _ in range(n):
			outfile.write(fasta_content)
			outfile.write('\n')  # Разделяет копии пустой строкой


# Пример использования
input_fasta = "allseq.fasta"
output_fasta = "allseq2.fasta"
n = 5  # Количество повторений
copy_fasta_n_times(input_fasta, output_fasta, n)
