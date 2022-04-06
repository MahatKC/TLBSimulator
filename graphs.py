import matplotlib.pyplot as plt
import pandas as pd
pd.set_option("display.precision", 8)

sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
#sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

csv_file = pd.read_csv("Resultados.csv") 

bigone_mask =  csv_file['Arquivo'] == 'bigone.trace'
bigone_data = csv_file[bigone_mask]
resultados_bigone = bigone_data['Taxa'].tolist()

bzip_mask = csv_file['Arquivo'] == 'bzip.trace'
bzip_data = csv_file[bzip_mask]
resultados_bzip = bzip_data['Taxa'].tolist()

gcc_mask = csv_file['Arquivo'] == 'gcc.trace'
gcc_data = csv_file[gcc_mask]
resultados_gcc = gcc_data['Taxa'].tolist()

sixpack_mask = csv_file['Arquivo'] == 'sixpack.trace'
sixpack_data = csv_file[sixpack_mask]
resultados_sixpack = sixpack_data['Taxa'].tolist()

swim_mask = csv_file['Arquivo'] == 'swim.trace'
swim_data = csv_file[swim_mask]
resultados_swim = swim_data['Taxa'].tolist()

df = pd.DataFrame({
    'tam': sizes,
    'te_bigone': resultados_bigone,
    'te_bzip': resultados_bzip,
    'te_gcc': resultados_gcc,
    'te_sixpack': resultados_sixpack,
    'te_swim': resultados_swim
    })

plt.figure()
plt.title("Aleatório")
plt.xlabel("Tamanho da TLB")
plt.ylabel("Taxa de acerto")
plt.plot(df['tam'], df['te_bigone'], color='g', label='bigone')
plt.plot(df['tam'], df['te_bzip'], color='r', label='bzip')
plt.plot(df['tam'], df['te_gcc'], color='b', label='gcc')
plt.plot(df['tam'], df['te_sixpack'], color='y', label='sixpack')
plt.plot(df['tam'], df['te_swim'], color='m', label='swim')
plt.legend()
plt.xscale("log", basex=2)
plt.show()


