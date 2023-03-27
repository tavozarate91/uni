import pandas
import numpy

# Anmerkung: Man kann die Datei auch in Excel/Libreoffice öffnen.
cars = pandas.read_csv('cars.csv')

# Wir geben die Namen der Spalten/Merkmale aus.
columns = cars.columns
for i,col in enumerate(columns):
    print('%.2d : %s' %(i,col))
    
# Wir konvertieren die Daten in ein Numpy-Array.
data = cars.values.astype('float')

print(cars.dollar_price.mean())
print(cars.dollar_price.median())
#Durschnitt > Median in diesem Fall

prices = cars.dollar_price
# display histogram of prices
import matplotlib.pyplot as plt
plt.hist(prices, bins=1000)
plt.show()
