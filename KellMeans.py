from operator import itemgetter
import random
import math
import numpy as np


def getMinMax(data):
    return [min(data, key=itemgetter(0))[0], max(data, key=itemgetter(0))[0],
            min(data, key=itemgetter(1))[1], max(data, key=itemgetter(1))[1]]


# Get Euclidean distance between two points
def getDistance(loc1, loc2):
    diff = [loc1[0] - loc2[0], loc1[1] - loc2[1]]
    return math.sqrt((diff[0] ** 2) + (diff[1] ** 2))


def createCentroid(min_maxes):
    return [random.randint(min_maxes[0], min_maxes[1]), random.randint(min_maxes[2], min_maxes[3]), []]


def getLocs(centroids):
    ret = []
    for centroid in centroids:
        ret.append([centroid[0], centroid[1]])
    return ret


class KellMeans:
    centroids = []
    data = []
    labels = []

    def fitData(self, data):
        self.centroids = []
        self.data = data
        # Get data boundaries
        min_maxes = getMinMax(self.data)
        # Generate random centroids inside data boundaries
        self.centroids.append(createCentroid(min_maxes))
        self.centroids.append(createCentroid(min_maxes))
        full_flag = False
        while not full_flag:
            flag = False
            while not flag:
                flag = self.k_means()
            full_flag = self.kellMeans()


    def k_means(self):
        locs1 = getLocs(self.centroids)
        self.parentData()
        self.moveCentroids()
        locs2 = getLocs(self.centroids)
        dists = []
        for i in range(0, len(locs1)):
            dists.append(getDistance(locs1[i], locs2[i]))
        if max(dists) < 0.0001:
            return True
        return False

    def parentData(self):
        self.labels = []
        for point in self.data:
            centroid = []
            distance = math.inf
            for cur_centroid in self.centroids:
                cur_dist = getDistance(point, cur_centroid)
                if cur_dist < distance:
                    distance = cur_dist
                    centroid = cur_centroid
            centroid[2].append(point)
            self.labels.append(self.centroids.index(centroid))

    def moveCentroids(self):
        for centroid in self.centroids:
            x = []
            y = []
            for point in centroid[2]:
                x.append(point[0])
                y.append(point[1])
            centroid[0] = np.mean(x)
            centroid[1] = np.mean(y)

    def kellMeans(self):
        print("SPLIT")
        # Split based on standard deviation and mean etc
        return True
