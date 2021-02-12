import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/CA2/job-vacancy-by-industry-level3.csv', sep=',')

re2020 = '^2020-Q3'
df = df[df['quarter'].str.contains(re2020)]

df1 = df[df.industry1 == 'services']

print(df1)

df2 = df1[['job_vacancy','industry3']]
df3 = df2.reset_index()
del df3['index']
print(df3)

values = df3['job_vacancy']
labels = df3['industry3']
explode = (0,0,0,0,0,0,0,0,0,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0)

plt.pie(values, labels=values, explode=explode, startangle = 52, counterclock=False, wedgeprops = {'width' : 0.38})

plt.legend(labels,loc ="lower center", bbox_to_anchor =(0.47, 1.05), ncol = 3)

plt.show()
