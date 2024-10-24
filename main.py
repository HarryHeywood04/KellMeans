import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from KellMeans import KellMeans


def printKMInfo(km_model):
    print("\nCENTROIDS")
    for centroid in km_model.centroids:
        print(centroid)
    print("\nDATA")
    print(data)
    print("\nLABELS")
    print(km_model.labels)


# Create data
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x, y))

km = KellMeans()
km.fitData(data)
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

printKMInfo(km)
plt.scatter(x, y, c=km.labels)
plt.show()
