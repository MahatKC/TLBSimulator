from inspect import trace
import numpy as np
import pandas as pd
pd.set_option("display.precision", 8)
TEMPO_ACESSO_TLB = 10
TEMPO_ACESSO_MEM = 100

def read_trace(n, arq):
    tlb = []
    arquivo = open("Trace/"+arq, "r")
    hit = 0
    miss = 0
    for linha in arquivo:
        #número da página tem 20 bits
        endereco = linha[:5]
        if endereco in tlb:
            hit += 1
        elif len(tlb) < n:
            miss += 1
            tlb.append(endereco)
        else:
            miss += 1
            #política de substituição aleatória
            indice = np.random.randint(0, n)
            tlb[indice] = endereco
    arquivo.close()
    #média da taxa de acerto
    return hit/(hit + miss)

trace_files = ["bigone.trace", "bzip.trace", "gcc.trace", "sixpack.trace", "swim.trace"]
for i in range(1, 13):
    for trace_file in trace_files:
        taxa = read_trace(2**i, trace_file)
        #cálculo do tempo médio de acesso usando a taxa recebida em read_trace
        tma = taxa*(TEMPO_ACESSO_TLB + TEMPO_ACESSO_MEM) + (1 - taxa)*(TEMPO_ACESSO_TLB + 2*TEMPO_ACESSO_MEM)
        #criação do dataframe com os resultados obtidos (taxa e tempo médio de acesso) 
        # conforme o tamanho da TLB e o arquivo selecionado
        results = pd.DataFrame({
            'Tamanho': [2**i],
            'Arquivo': [trace_file],
            'Taxa': [taxa],
            'Tempo médio de acesso': [tma]
        })
        if i == 1 and trace_file == trace_files[0]:
            results.to_csv("Resultados.csv",index=False)
        else:
            file_df = pd.read_csv("Resultados.csv")
            file_df = pd.concat([file_df,results], ignore_index=True)
            file_df.to_csv("Resultados.csv",index=False)