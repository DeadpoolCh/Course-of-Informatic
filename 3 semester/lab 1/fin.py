import gzip
import shutil
import requests
from tqdm import tqdm
import time
import threading
import multiprocessing
from Bio import SeqIO
from collections import Counter,defaultdict
from queue import Queue
import matplotlib.pyplot as plt

amino_acid = {
	'A': 'hydrophobic', 'V': 'hydrophobic', 'L': 'hydrophobic', 'I': 'hydrophobic', 'M': 'hydrophobic',
	'F': 'hydrophobic', 'W': 'hydrophobic', 'P': 'hydrophobic',
	'G': 'hydrophilic neutral', 'S': 'hydrophilic neutral', 'T': 'hydrophilic neutral',
	'C': 'hydrophilic neutral', 'Y': 'hydrophilic neutral', 'N': 'hydrophilic neutral',
	'Q': 'hydrophilic neutral',
	'D': 'hydrophilic negative', 'E': 'hydrophilic negative',
	'K': 'hydrophilic positive', 'R': 'hydrophilic positive', 'H': 'hydrophilic positive',
	'B': 'special', 'Z': 'special', 'X': 'unkown',
	'U': 'hydrophilic neutral'
}


class FileDownloader:
    def __init__(self, url, output_file, block_size=1024):
        self.url = url
        self.output_file = output_file
        self.block_size = block_size
        self.total_size = 0
    def get_file_size(self):
        response = requests.head(self.url)
        self.total_size = int(response.headers.get('content-length', 0))
        return self.total_size
    def download(self):
        response = requests.get(self.url, stream=True)
        self.total_size = int(response.headers.get('content-length', 0))

        with open(self.output_file, 'wb') as file, tqdm(
                total=self.total_size, unit='B', unit_scale=True, desc=self.output_file
        ) as progress_bar:
            for data in response.iter_content(self.block_size):
                file.write(data)
                progress_bar.update(len(data))
    def unpack(self):
        with gzip.open(self.output_file, 'rb') as f_in:
            with open('insulin.fasta', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    def cut(self):
        with open('seq100.txt','w') as f100,open('seq1000.txt','w') as f1000, open('seq10000.txt','w') as f10000, open('allseq.txt','w') as alls:
            count_100,count_1000,count_10000 = 0,0,0
            for seq_record in SeqIO.parse("insulin.fasta", "fasta"):
                if count_100 < 100:
                    f100.write(f">{seq_record.seq}\n".strip('>'))
                    count_100 += 1
                if count_1000 < 1000:
                    f1000.write(f">{seq_record.seq}\n".strip('>'))
                    count_1000 += 1
                if count_10000 < 10000:
                    f10000.write(f">{seq_record.seq}\n".strip('>'))
                    count_10000 += 1
                alls.write(f">{seq_record.seq}\n".strip('>'))
    def masscopy(self,input_txt,output_txt, n):
        with open(input_txt, 'r') as infile:
            txt_content = infile.read()
        with open(output_txt, 'w') as outfile:
            for _ in range(n):
                outfile.write(txt_content)

class ProteinAnalyser:
    def __init__(self, file):
        self.file=file
        self.statistics = Counter()
    def process_sequence(self, sequence):
        return Counter(amino_acid[aa] for aa in sequence.strip() if aa in amino_acid)
    def analyse_single_thread(self):
        self.statistics.clear()
        results = defaultdict(Counter)
        with open(self.file, 'r') as file:
            for i, seq in enumerate(file):
                counts = self.process_sequence(seq)
                self.statistics+=counts
                results[i+1] = counts
        self.save_results(results,'single.txt')
    def save_results(self, results, filename):
        with open(filename, "w") as file:
            for i, counts in results.items():
                file.write(f"Sequence {i}: {dict(counts)}\n")

    def measure_time(self, func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        result=end_time - start_time
        # print(f"Execution time for {func.__name__}: {result:.4f} seconds")
        return result

    def analyse_multi_thread(self, num_threads=4):
        self.statistics.clear()
        queue = Queue()
        results = defaultdict(Counter)
        def worker():
            while True:
                item = queue.get()
                if item is None:
                    break
                i, seq = item
                counts = self.process_sequence(seq)
                self.statistics += counts
                results[i + 1] = counts
                queue.task_done()
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)
        with open(self.file, 'r') as file:
            for i, seq in enumerate(file):
                queue.put((i, seq))
        queue.join()
        for _ in threads:
            queue.put(None)
        for thread in threads:
            thread.join()
        self.save_results(results,'multitheads.txt')

    def analyse_multi_process(self, num_processes=4):
        self.statistics.clear()
        manager = multiprocessing.Manager()
        queue = manager.Queue()
        results = manager.dict()
        processes = []
        for _ in range(num_processes):
            process = multiprocessing.Process(target=ProteinAnalyser.worker, args=(queue, results))
            process.start()
            processes.append(process)
        with open(self.file, 'r') as file:
            for i, seq in enumerate(file):
                queue.put((i, seq))
        queue.join()
        for _ in processes:
            queue.put(None)
        for process in processes:
            process.join()
        self.statistics = sum(results.values(), Counter())
        self.save_results(results,'multiprocecces.txt')
    @staticmethod
    def worker(queue, results):
        while True:
            item = queue.get()
            if item is None:
                break
            i, seq = item
            counts = Counter(amino_acid[aa] for aa in seq.strip() if aa in amino_acid)
            results[i + 1] = counts
            queue.task_done()




url = 'https://rest.uniprot.org/uniprotkb/stream?compressed=true&format=txt&query=%28Insulin%29'
downloader = FileDownloader(url, 'insulin.fasta.gz')
# downloader.download()
# downloader.unpack()
# downloader.cut()
downloader.masscopy('allseq.txt', 'massallseq.txt',50)

# if __name__ == '__main__':
#     for file in ['seq100.txt','seq1000.txt','allseq.txt','massallseq.txt']:
#         analyser=ProteinAnalyser(file)
#         analyser.measure_time(analyser.analyse_single_thread)
#         analyser.measure_time(analyser.analyse_multi_thread)
#         analyser.measure_time(analyser.analyse_multi_process)


def test_files():
    file_sizes = ['seq100.txt', 'seq1000.txt', 'massallseq.txt']
    times_single = []
    times_multi_thread = []
    times_multi_process = []

    for file in file_sizes:
        analyser = ProteinAnalyser(file)
        times_single.append(analyser.measure_time(analyser.analyse_single_thread))
        times_multi_thread.append(analyser.measure_time(analyser.analyse_multi_thread))
        times_multi_process.append(analyser.measure_time(analyser.analyse_multi_process))

    plt.figure(figsize=(10, 6))
    plt.plot(file_sizes, times_single, label='Single-thread', marker='o')
    plt.plot(file_sizes, times_multi_thread, label='Multi-thread', marker='o')
    plt.plot(file_sizes, times_multi_process, label='Multi-process', marker='o')
    plt.xlabel('File')
    plt.ylabel('Time (seconds)')
    plt.title('Time vs File Size for Different Modes')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_threads_processes():
    file = 'allseq.txt'  # Фиксированный большой файл
    num_threads_processes = [1, 2, 4, 8, 16]  # Число потоков/процессов для тестирования
    times_multi_thread = []
    times_multi_process = []

    for num in num_threads_processes:
        analyser = ProteinAnalyser(file)
        times_multi_thread.append(analyser.measure_time(analyser.analyse_multi_thread, num_threads=num))
        times_multi_process.append(analyser.measure_time(analyser.analyse_multi_process, num_processes=num))

    plt.figure(figsize=(10, 6))
    plt.plot(num_threads_processes, times_multi_thread, label='Multi-thread', marker='o')
    plt.plot(num_threads_processes, times_multi_process, label='Multi-process', marker='o')
    plt.xlabel('Number of Threads/Processes')
    plt.ylabel('Time (seconds)')
    plt.title('Time vs Number of Threads/Processes')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    test_files()
    test_threads_processes()
