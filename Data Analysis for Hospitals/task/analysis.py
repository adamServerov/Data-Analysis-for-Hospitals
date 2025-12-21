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
df.to_csv(r'C:\Users\AdamSinov\Documents\dof.csv', index=False)
hos_name = df['hospital'].value_counts().idxmax()
gen_hos = df[df['hospital'] == 'general']
stomach_share = (gen_hos['diagnosis'] == 'stomach').mean().round(3)
sports_hos = df[df['hospital'] == 'sports']
injury_share = round((sports_hos['diagnosis'] == 'dislocation').mean(),3)
gen_ages = gen_hos['age'].median()
sports_ages = sports_hos['age'].median()
diff = gen_ages - sports_ages
hos_mos = (df[df['blood_test'] == 't']['hospital'].value_counts().idxmax())
hos_count = (df[df['blood_test'] == 't']['hospital'].value_counts().max())

# Import visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# ===== QUESTION 1: Most common age with histogram =====
# Clean age data
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df_age_clean = df[(df['age'] >= 0) & (df['age'] <= 120)].copy()
df_age_clean = df_age_clean.dropna(subset=['age'])

# Find most common exact age
age_mode = df_age_clean['age'].mode()[0]

# Determine which range it falls into
ranges = [(0, 15), (15, 35), (35, 55), (55, 70), (70, 80)]
age_range_answer = ""
for start, end in ranges:
    if start <= age_mode < end:
        age_range_answer = f"{start}-{end}"
        break

# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(df_age_clean['age'], bins=[0, 15, 35, 55, 70, 80],
         edgecolor='black', alpha=0.7, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.title('Distribution of Patient Ages (All Hospitals)')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# ===== QUESTION 2: Most common diagnosis with pie chart =====
# Clean diagnosis data (replace 0 with NaN)
df['diagnosis'] = df['diagnosis'].replace(0, pd.NA)
df_diag_clean = df.dropna(subset=['diagnosis'])

# Get most common diagnosis
most_common_diagnosis = df_diag_clean['diagnosis'].mode()[0]

# Create pie chart
plt.figure(figsize=(8, 5))
diagnosis_counts = df_diag_clean['diagnosis'].value_counts()
diagnosis_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Diagnoses (All Hospitals)')
plt.ylabel('')  # Hide ylabel
plt.tight_layout()
plt.show()

# ===== QUESTION 3: Height violin plot =====
# Clean height data
df['height'] = pd.to_numeric(df['height'], errors='coerce')
df_height_clean = df.dropna(subset=['height'])

# Create violin plot
plt.figure(figsize=(8, 5))
sns.violinplot(x='hospital', y='height', data=df_height_clean)
plt.title('Height Distribution by Hospital')
plt.xlabel('Hospital')
plt.ylabel('Height')
plt.tight_layout()
plt.show()

# ===== PRINT ANSWERS =====
print(f"\nThe answer to the 1st question: {age_range_answer}")
print(f"The answer to the 2nd question: {most_common_diagnosis}")
print("The answer to the 3rd question: It's because...")
# Note: For question 3, no special answer format is required



