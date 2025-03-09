import pandas as pd
import requests
import time
import matplotlib.pyplot as plt
import seaborn as sns


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



input_pd=pd.read_excel('uniprot.xlsx',engine="openpyxl")
IDlist=input_pd['Entry'].tolist()
ID=[IDlist[:i] for i in range(10,len(IDlist)+10,10)]
output='download_fasta_request.fasta'
times={}
for ID in ID:
    start_time = time.time()
    count_v,count_e = download_fasta(ID,output)
    times[len(ID)]=[time.time()- start_time,count_v,count_e]

plt.figure(figsize=[8,6])
plt.plot(times.keys(),[v[0] for v in times.values()],marker="o",color="r",label="График времени от кол-ва запросов")
plt.xlabel('Кол-во запросов')
plt.ylabel('Время, сек')
plt.legend()
plt.grid()
plt.savefig('output1.png')
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
plt.savefig('output2.png')
plt.show()

