from sklearn.decomposition import PCA

file_csv = 'data_csv_small.csv'
df = pd.read_csv(file_csv)

columns = ['pre_pterm', 'pre_fterm',
           'pre_loans_next_pay_summ','pre_loans_outstanding',
           'pre_loans_total_overdue', 'pre_loans_max_overdue_sum',
           'pre_loans_credit_cost_rate', 'is_zero_loans5',
           'is_zero_loans530', 'is_zero_loans3060',
           'is_zero_loans6090', 'is_zero_loans90',
           'pre_util','pre_maxover2limit', 
           'is_zero_util', 'is_zero_over2limit',
           'enc_paym_0', 'enc_paym_1', 'enc_paym_2',
           'enc_paym_3', 'enc_paym_4', 'enc_paym_5',
           'enc_paym_6', 'enc_paym_7', 'enc_paym_8',
           'enc_paym_9', 'enc_paym_10', 'enc_paym_11',
           'enc_paym_12', 'enc_paym_13', 'enc_paym_14',
           'enc_paym_15', 'enc_paym_16', 'enc_paym_17',
           'enc_paym_18', 'enc_paym_19', 'enc_paym_20',
           'enc_paym_21', 'enc_paym_22',
           'enc_paym_23', 'enc_paym_24']

X = df.loc[:, columns].copy()
pca = PCA()   
pca.fit(X)  

100*pca.explained_variance_ratio_.round(3)
