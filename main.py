import matplotlib.pyplot as plt
from KellMeans import KellMeans

x = []
y = []

# Read data
file = open("clustering_data.csv", "r")
lines = file.readlines()
file.close()
for line in lines:
    if line.__contains__("."):
        x.append(float(line.split(",")[0]))
        y.append(float(line.split(",")[1]))
data = list(zip(x, y))


km = KellMeans()
km.fitData(data)

km.display()
plt.scatter(x, y, c=km.labels)
plt.show()
