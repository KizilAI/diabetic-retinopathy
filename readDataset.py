import pandas as pd

# Dataseti okuma
dataset = pd.read_csv("./data/test.csv")
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1:2].values

# İçerideki tüm değerleri 100. değere kadar yazdırma
for i in range(len(X)):
    print("Name: ", X[i], "Value: ", y[i])
    if i == 100:
        break

