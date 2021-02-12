import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/CA2/rate-of-re-entry-into-employment-by-educational-attainment-quarterly.csv', sep=',')

df1 = df[df['quarter'] > '2019']

fig, ax = plt.subplots()

df2 = df1.groupby(['education1']).plot(x='quarter', y='reentry_rate', ax=ax, legend=False)
plt.legend(["Below Secondary", "Degree", "Diploma & Professional Qualification", "Post-Secondary (Non-Tertiary)", "Secondary"], loc ="best", bbox_to_anchor =(0.33, 1.0), ncol = 1) 
plt.ylabel('Re-entry rate (%)', rotation=90)

print(df2)

plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)



