import pandas as pd
import os

f = 1
file_list = list()
df_list = list()

for root, dirs, files in os.walk(r"C:\Users\matrp\Desktop\csv_ivium_new_data"):
    for file in files:
        if file.endswith('.csv'):
            file_list.append(os.path.join(root, file))

df_list = []

for file in file_list:
    df = pd.read_csv(file, index_col=[0])
    if f == 1:
        names = list(df[df.columns[0]])
        names += ['milk/antibiotic', 'conc']
        f = 0

    current = list(df['Current, A'])
    conc = float(file.split(os.sep)[-1].split('_')[-2])
    antibiotic = file.split(os.sep)[-1].split('_')[0]
    values = current.copy()
    values.append(antibiotic)
    values.append(conc)
    df_list.append(values)
    #len(values) = 1042
print('Hello')
main_df = pd.DataFrame(data = df_list, columns = names)
main_df.to_csv('milc.csv')
