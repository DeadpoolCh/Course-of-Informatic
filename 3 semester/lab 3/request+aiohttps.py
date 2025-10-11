import pandas as pd
import requests
import aiohttp
import asyncio
import time
import matplotlib.pyplot as plt


def download_fasta(input_ID:list,output_f):
    count_validated=0
    count_errors=0
    with open(output_f,'w',encoding='utf-8') as f:
        for ID in input_ID:
            query_link = f"https://rest.uniprot.org/uniprotkb/search?query={ID}&format=fasta"
            try:
                response = requests.get(query_link, timeout=1)
                if response.status_code == requests.codes['ok']:
                    f.write(response.text)
                    count_validated+=1
                else:
                    response.raise_for_status()
            except requests.exceptions.RequestException:
                count_errors+=1
    return count_validated,count_errors

async def download_fasta_aio(input_ID:list,output_f):
    count_validated=0
    count_errors=0
    async with aiohttp.ClientSession() as session:
        tasks=[]
        for ID in input_ID:
            query_link = f"https://rest.uniprot.org/uniprotkb/search?query={ID}&format=fasta"
            tasks.append(session.get(query_link))
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        with open(output_f, 'w', encoding='utf-8') as f:
            for response, ID in zip(responses, input_ID):
                if isinstance(response, Exception):
                    count_errors += 1
                    continue
                if response.status == 200:
                    data = await response.text()
                    f.write(data)
                    count_validated += 1
                else: count_errors += 1
    return count_validated,count_errors


input_pd=pd.read_excel('uniprot.xlsx',engine="openpyxl")
IDlist=input_pd['Entry'].tolist()
ID=[IDlist[:i] for i in range(10,len(IDlist)+10,10)]
output='download_fasta_aio.fasta'
output2='download_fasta_request.fasta'
times={}
times2={}
for ID in ID:
    start_time = time.time()
    count_v,count_e = asyncio.run(download_fasta_aio(ID,output))
    times[len(ID)]=[time.time()- start_time,count_v,count_e]
    count_v2,count_e2 = download_fasta(ID,output2)
    times2[len(ID)]=[time.time()- start_time,count_v2,count_e2]

plt.figure(figsize=[8,6])
plt.plot(times.keys(),[v[0] for v in times.values()],marker="o",color="r",label='aio')
plt.plot(times2.keys(),[v[0] for v in times2.values()],marker="o",color="g",label='request')
plt.title('Зависимость времени от кол-ва запросов')
plt.xlabel('Кол-во запросов')
plt.ylabel('Время, сек')
plt.legend()
plt.grid()
plt.savefig('outputall.png')
plt.show()



