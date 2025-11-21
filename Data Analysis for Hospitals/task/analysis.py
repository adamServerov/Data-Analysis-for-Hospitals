# write your code here
import pandas as pd

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')
names = general.columns

prenatal.columns = names
sports.columns = names
df = pd.concat([general,prenatal, sports], axis = 0, ignore_index = True)
df.drop("Unnamed: 0", axis =1, inplace= True)
pd.set_option('display.max_columns', 8)
df.dropna(axis = 0, how = 'all', inplace = True)

df.loc[(df['hospital'] == 'prenatal') & (df['gender'] == 'm'), 'gender'] = 'f'
col_fill = ['bmi','diagnosis','blood_test', 'ecg','ultrasound','mri','xray','children','months']
df[col_fill] = df[col_fill].fillna(0)
print(df.shape)
print(df.sample(n=20, random_state=30))


