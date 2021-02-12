import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/CA2/median-rent-by-town-and-flat-type.csv', sep=',')

re2020 = '^2020'
df1 = df[df['quarter'].str.contains(re2020)]

dfAngMoKio = df1[(df1.flat_type =='4-RM') & (df1.town == 'ANG MO KIO')]
sum_AngMoKio = dfAngMoKio[:]['median_rent'].median()

dfBedok = df1[(df1.flat_type =='4-RM') & (df1.town == 'BEDOK')]
sum_Bedok = dfBedok[:]['median_rent'].median()

dfBishan = df1[(df1.flat_type =='4-RM') & (df1.town == 'BISHAN')]
sum_Bishan = dfBishan[:]['median_rent'].median()

dfBukitBatok = df1[(df1.flat_type =='4-RM') & (df1.town == 'BUKIT BATOK')]
sum_BukitBatok = dfBukitBatok[:]['median_rent'].median()

dfBukitMerah = df1[(df1.flat_type =='4-RM') & (df1.town == 'BUKIT MERAH')]
sum_BukitMerah = dfBukitMerah[:]['median_rent'].median()

dfBukitPanjang = df1[(df1.flat_type =='4-RM') & (df1.town == 'BUKIT PANJANG')]
sum_BukitPanjang = dfBukitPanjang[:]['median_rent'].median()

dfCentral = df1[(df1.flat_type =='4-RM') & (df1.town == 'CENTRAL')]
sum_Central = dfCentral[:]['median_rent'].median()

dfChoaChuKang = df1[(df1.flat_type =='4-RM') & (df1.town == 'CHOA CHU KANG')]
sum_ChoaChuKang = dfChoaChuKang[:]['median_rent'].median()

dfClementi = df1[(df1.flat_type =='4-RM') & (df1.town == 'CLEMENTI')]
sum_Clementi = dfClementi[:]['median_rent'].median()

dfGeylang = df1[(df1.flat_type =='4-RM') & (df1.town == 'GEYLANG')]
sum_Geylang = dfGeylang[:]['median_rent'].median()

dfHougang = df1[(df1.flat_type =='4-RM') & (df1.town == 'HOUGANG')]
sum_Hougang = dfHougang[:]['median_rent'].median()

dfJurongEast = df1[(df1.flat_type =='4-RM') & (df1.town == 'JURONG EAST')]
sum_JurongEast = dfJurongEast[:]['median_rent'].median()

dfJurongWest = df1[(df1.flat_type =='4-RM') & (df1.town == 'JURONG WEST')]
sum_JurongWest = dfJurongWest[:]['median_rent'].median()

dfKallang_Whampoa = df1[(df1.flat_type =='4-RM') & (df1.town == 'KALLANG/WHAMPOA')]
sum_Kallang_Whampoa = dfKallang_Whampoa[:]['median_rent'].median()

dfMarineParade = df1[(df1.flat_type =='4-RM') & (df1.town == 'MARINE PARADE')]
sum_MarineParade = dfMarineParade[:]['median_rent'].median()
print(sum_MarineParade)

dfPasirRis = df1[(df1.flat_type =='4-RM') & (df1.town == 'PASIR RIS')]
sum_PasirRis = dfPasirRis[:]['median_rent'].median()

dfPunggol = df1[(df1.flat_type =='4-RM') & (df1.town == 'PUNGGOL')]
sum_Punggol = dfPunggol[:]['median_rent'].median()

dfQueenstown = df1[(df1.flat_type =='4-RM') & (df1.town == 'QUEENSTOWN')]
sum_Queenstown = dfQueenstown[:]['median_rent'].median()

dfSembawang = df1[(df1.flat_type =='4-RM') & (df1.town == 'SEMBAWANG')]
sum_Sembawang = dfSembawang[:]['median_rent'].median()

dfSengkang = df1[(df1.flat_type =='4-RM') & (df1.town == 'SENGKANG')]
sum_Sengkang = dfSengkang[:]['median_rent'].median()

dfSerangoon = df1[(df1.flat_type =='4-RM') & (df1.town == 'SERANGOON')]
sum_Serangoon = dfSerangoon[:]['median_rent'].median()

dfTampines = df1[(df1.flat_type =='4-RM') & (df1.town == 'TAMPINES')]
sum_Tampines = dfTampines[:]['median_rent'].median()

dfToaPayoh = df1[(df1.flat_type =='4-RM') & (df1.town == 'TOA PAYOH')]
sum_ToaPayoh = dfToaPayoh[:]['median_rent'].median()

dfWoodlands = df1[(df1.flat_type =='4-RM') & (df1.town == 'WOODLANDS')]
sum_Woodlands = dfWoodlands[:]['median_rent'].median()

dfYishun = df1[(df1.flat_type =='4-RM') & (df1.town == 'YISHUN')]
sum_Yishun = dfYishun[:]['median_rent'].median()

data = [sum_AngMoKio, sum_Bedok, sum_Bishan, sum_BukitBatok, sum_BukitMerah, sum_BukitPanjang, sum_Central, sum_ChoaChuKang, sum_Clementi, sum_Geylang, sum_Hougang, sum_JurongEast, sum_JurongWest, sum_Kallang_Whampoa, sum_MarineParade, sum_PasirRis, sum_Punggol, sum_Queenstown, sum_Sembawang, sum_Sengkang, sum_Serangoon, sum_Tampines, sum_ToaPayoh, sum_Woodlands, sum_Yishun]

labels = ['Ang Mo Kio', 'Bedok', 'Bishan', 'Bukit Batok', 'Bukit Merah', 'Bukit Panjang', 'Central', 'Choa Chu Kang', 'Clement', 'Geylang', 'Hougang', 'Jurong East', 'Jurong West', 'Kallang/Whampoa', 'Marine Parade', 'Pasir Ris', 'Punggol', 'Queenstown', 'Sembawang', 'Sengkang', 'Serangoon', 'Tampines', 'Toa Payoh', 'Woodlands', 'Yishun']
plt.xticks(range(len(data)), labels, rotation=90)
plt.xlabel('Town')
plt.ylabel('Median rent (S$)')
plt.title('Median rent of 4-room HDB flat by town in 2020')
plt.scatter(range(len(data)), data)

plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.show()


