import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from Bio import SeqIO
from collections import Counter
import matplotlib.pyplot as plt

# Словарь с аминокислотами
AMINO_ACID_CLASSES = {
	'A': 'Гидрофобная', 'V': 'Гидрофобная', 'L': 'Гидрофобная', 'I': 'Гидрофобная', 'M': 'Гидрофобная',
	'F': 'Гидрофобная', 'W': 'Гидрофобная', 'P': 'Гидрофобная',
	'G': 'Гидрофильная нейтральная', 'S': 'Гидрофильная нейтральная', 'T': 'Гидрофильная нейтральная',
	'C': 'Гидрофильная нейтральная', 'Y': 'Гидрофильная нейтральная', 'N': 'Гидрофильная нейтральная',
	'Q': 'Гидрофильная нейтральная',
	'D': 'Гидрофильная отрицательная', 'E': 'Гидрофильная отрицательная',
	'K': 'Гидрофильная положительная', 'R': 'Гидрофильная положительная', 'H': 'Гидрофильная положительная',
	'B': 'Неопределённая (Asp или Asn)', 'Z': 'Неопределённая (Glu или Gln)', 'X': 'Неизвестная',
	'U': 'Гидрофильная нейтральная'
}


class ProteinAnalyzer:
	def __init__(self, filename):
		self.filename = filename
		self.statistics = Counter()
		self.lock = threading.Lock()

	def process_sequence(self, sequence):
		local_stats = Counter(AMINO_ACID_CLASSES[aa] for aa in sequence if aa in AMINO_ACID_CLASSES)
		return local_stats

	def analyze_single_thread(self):
		self.statistics.clear()
		for record in SeqIO.parse(self.filename, "fasta"):
			self.statistics.update(self.process_sequence(record.seq))
		return self.statistics

	def analyze_multithreading(self, num_threads=4):
		self.statistics.clear()
		with ThreadPoolExecutor(max_workers=num_threads) as executor:
			results = executor.map(self.process_sequence,
			                       (record.seq for record in SeqIO.parse(self.filename, "fasta")))
		for res in results:
			self.statistics.update(res)
		return self.statistics

	def analyze_multiprocessing(self, num_processes=4):
		self.statistics.clear()
		with ProcessPoolExecutor(max_workers=num_processes) as executor:
			results = executor.map(self.process_sequence,
			                       (record.seq for record in SeqIO.parse(self.filename, "fasta")))
		for res in results:
			self.statistics.update(res)
		return self.statistics


def measure_time(analyzer, method, *args):
	start = time.time()
	result = method(*args)
	return time.time() - start, result


if __name__ == "__main__":
	fasta_file = "seq10000.fasta"
	analyzer = ProteinAnalyzer(fasta_file)

	# Измеряем время выполнения
	time_single, _ = measure_time(analyzer, analyzer.analyze_single_thread)
	time_threads, _ = measure_time(analyzer, analyzer.analyze_multithreading, 4)
	time_processes, _ = measure_time(analyzer, analyzer.analyze_multiprocessing, 4)

	print(f"Однопоточное выполнение: {time_single:.4f} сек")
	print(f"Многопоточное выполнение (4 потока): {time_threads:.4f} сек")
	print(f"Многопроцессное выполнение (4 процесса): {time_processes:.4f} сек")

	# График
	plt.bar(["Однопоточный", "Многопоточный (4)", "Многопроцессный (4)"], [time_single, time_threads, time_processes],
	        color=['blue', 'green', 'red'])
	plt.ylabel("Время выполнения (сек)")
	plt.title("Сравнение времени работы")
	plt.show()
