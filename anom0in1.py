df_y = pd.read_csv('train_target.csv')
y  = df_y.flag.values[:1000000].copy()
y_ = df_y.flag.values[:1000000].copy()

counter_norm, counter_anom = 0, 0
ind_norm, ind_anom = [], []
for i,x_pay in enumerate(np.array(X_pay)):
    if y_[i]==0 and min(x_pay)>0:
        counter_anom +=1
        ind_anom.append(i)
        y_[i]=1
    else:
        counter_norm +=1
        ind_norm.append(i)
