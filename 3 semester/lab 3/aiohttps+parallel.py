import pandas as pd
import aiohttp
import time
import matplotlib.pyplot as plt
import seaborn as sns
import asyncio

async def download_fasta(input_ID:list,output_f):
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
times={}
for ID in ID:
    start_time = time.time()
    count_v,count_e = asyncio.run(download_fasta(ID,output))
    times[len(ID)]=[time.time()- start_time,count_v,count_e]

# print(*times.values(),sep='\n')

plt.figure(figsize=[8,6])
plt.plot(times.keys(),[v[0] for v in times.values()],marker="o",color="r",label="График времени от кол-ва запросов")
plt.xlabel('Кол-во запросов')
plt.ylabel('Время, сек')
plt.legend()
plt.grid()
plt.savefig('output5.png')
plt.show()

df = pd.DataFrame.from_dict(times,columns=["Time",'Valid','Error'],orient='index')
df.index.name="Len"
df.reset_index(inplace=True)
dfm=df.melt(id_vars=['Len'],value_vars=['Valid','Error'],var_name='Type', value_name='Count')
plt.figure(figsize=[8,6])
sns.barplot(x='Len',y='Count',hue='Type',data=dfm)
plt.xlabel("Количество запросов")
plt.ylabel('Количество')
plt.title('Распределение успешных и ошибочных запросов')
plt.grid()
plt.savefig('output6.png')
plt.show()


