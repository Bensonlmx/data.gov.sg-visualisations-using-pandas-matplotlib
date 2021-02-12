import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/CA2/resale-transactions-by-flat-type-based-on-registered-cases.csv', sep=',')

df1room = df[df.flat_type == '1 room']
sum_1room = df1room[:]['resale_transactions'].sum()
print(sum_1room)

df2room = df[df.flat_type == '2 room']
sum_2room = df2room[:]['resale_transactions'].sum()
print(sum_2room)

df3room = df[df.flat_type == '3 room']
sum_3room = df3room[:]['resale_transactions'].sum()
print(sum_3room)

df4room = df[df.flat_type == '4 room']
sum_4room = df4room[:]['resale_transactions'].sum()
print(sum_4room)

df5room = df[df.flat_type == '5 room']
sum_5room = df5room[:]['resale_transactions'].sum()
print(sum_5room)

df5room = df[df.flat_type == '5 room']
sum_5room = df5room[:]['resale_transactions'].sum()
print(sum_5room)

dfemg = df[df.flat_type == 'Executive and Multi-generation']
sum_emg = dfemg[:]['resale_transactions'].sum()
print(sum_emg)

dfhudc = df[df.flat_type == 'HUDC']
sum_hudc = dfhudc[:]['resale_transactions'].sum()
print(sum_hudc)

data = [sum_1room, sum_2room, sum_3room, sum_4room, sum_5room, sum_emg, sum_hudc]
labels = ['1 room', '2 room', '3 room', '4 room', '5 room', 'Executive', 'HUDC']
plt.xticks(range(len(data)), labels)
plt.xlabel('Resale Flat Type')
plt.ylabel('Number of Transactions')
plt.title('Resale Transactions by Flat Type based on Registered Cases from 2006 to 2019')

rect1 = plt.bar(range(len(data)), data) 

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%i' % int(height),
        ha='center', va='bottom')
autolabel(rect1)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.show()


