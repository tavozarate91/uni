# ZELLE 2 (Python-Code)

# FIXME: Führen Sie den Python-Code aus
# 1. Klicken Sie auf die Zelle
# 2. Ändern Sie den Code unten (geben Sie z.B. 20x statt 10x HelloWorld aus,
#    und ersetzen Sie in weird_point_cloud() 8 durch 15).
# 3. Führen Sie mit STRG+ENTER den Code aus.
# 4. Sie sollten unter der Zelle die Ausgabe sehen (etwas Text und einen Plot).

# diese Zeile bewirkt, dass der Plot direkt im Notebook erscheint.
#matplotlib inline 

# Import von Python-Paketen
import numpy as np
import matplotlib.pyplot as plt

# "Hello World" 10x ausgeben
for i in range(15):
    print("Hello World %d!" %i)

# eine Funktion, die eine 2D-Punktwolke generiert
# (eine Liste von x-Koordinaten und eine von y-Koordinaten)
def weird_point_cloud():
    # Zahlen von 0 bis 8 im Abstand von 0.01
    x = np.arange(0, 15, 0.01)
    # y-Werte = sin(x) + Zufallszahlen
    y = np.sin(x) + np.random.random(len(x))
    return x, y

# Plotte die Punktwolke
x,y = weird_point_cloud()
plt.scatter(x,y, color="red", s=2)
plt.show()
