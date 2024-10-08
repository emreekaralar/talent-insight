import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl
import seaborn as sns

file_path = 'linkedininsight-automation.xlsx'
xls = pd.ExcelFile(file_path)

df = pd.read_excel(xls, sheet_name='Companies')

data = df.iloc[:4, [df.columns.get_loc('Company'), df.columns.get_loc('Professionals')]]

plt.figure(figsize=(10, 4))
sns.set(style="whitegrid")
ax = sns.barplot(x='Professionals', y='Company', data=data, color=(204/255, 228/255, 222/255), height=0.5)

for index, value in enumerate(data['Professionals']):
    ax.text(value - 300, index, f'{value}', color='black', ha="center", va="center", fontweight = "bold")

plt.xlabel('# of Professionals')
plt.tight_layout()

#plt.savefig('Top Companies employing the most talents in the Poland')

plt.show()
