import pandas as pd
import os
import pyarrow.parquet as pq

path = "train_data"                             
for i,file in enumerate(os.listdir(path)):
    print('train_data_' + str(i) + '.pq')
    file = 'train_data_' + str(i) + '.pq'
    dataset = pq.ParquetDataset(os.path.join(path,file))
    df = dataset.read(use_threads=True).to_pandas()
    df_gr = df.groupby('id').agg('mean')
    file_csv = file.replace('.pq', '.csv')
    df_gr.to_csv(os.path.join('train_data_csv_all',file_csv))
os.listdir(path)

path = 'train_data_csv_all'  
frames = []
for i,file_csv in enumerate(os.listdir(path)):
    file_csv = 'train_data_' + str(i) + '.csv'
    df = pd.read_csv(os.path.join('train_data_csv_all',file_csv) )
    frames.append(df)

result = pd.concat(frames)
file_csv_all = '1_data_csv_all.csv'
result.to_csv(file_csv_all)
df_all = pd.read_csv(file_csv_all)