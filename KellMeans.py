from operator import itemgetter
import random
import math
import numpy as np

import matplotlib.pyplot as plt


def getMinMax(data):
    return [min(data, key=itemgetter(0))[0], max(data, key=itemgetter(0))[0],
            min(data, key=itemgetter(1))[1], max(data, key=itemgetter(1))[1]]


# Get Euclidean distance between two points
def getDistance(loc1, loc2):
    diff = [loc1[0] - loc2[0], loc1[1] - loc2[1]]
    return math.sqrt((diff[0] ** 2) + (diff[1] ** 2))


def createCentroid(min_maxes):
    return [random.uniform(min_maxes[0], min_maxes[1]), random.uniform(min_maxes[2], min_maxes[3]), []]


def getLocs(centroids):
    ret = []
    for centroid in centroids:
        ret.append([centroid[0], centroid[1]])
    return ret


def toSplit(centroid):
    x = []
    y = []
    for point in centroid[2]:
        x.append(point[0])
        y.append(point[1])
    # Check distribution of each axis
    if toSplitSingleAxis(x):
        return True
    if toSplitSingleAxis(y):
        return True
    return False


def toSplitSingleAxis(data):
    # Calculate bin width for distribution
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25
    width = iqr / pow(len(data), (1 / 3))
    # Make a list that is the same length as the amount of bins
    dist = [0] * math.ceil((np.max(data) - np.min(data)) / width)
    # Put data in bins
    for entry in data:
        pos = int(math.floor((entry - np.min(data)) / width))
        dist[pos] += 1
    norm_dist = []
    for i in range(1, len(dist) - 1):
        norm_dist.append((dist[i - 1] + dist[i] + dist[i + 1]) / 3)
    trim_dist = []
    for i in range(0, len(norm_dist) - 1):
        if norm_dist[i] > norm_dist[i + 1]:
            for j in range(i, len(norm_dist)):
                trim_dist.append(norm_dist[j])
            break
    grad = np.gradient(trim_dist)
    maxBin = np.max(trim_dist)
    for n in grad:
        if n > 0.2*maxBin:
            return True
    return False


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
        full_flag = False
        while not full_flag:
            flag = False
            while not flag:
                flag = self.kMeans()
            full_flag = self.kellMeans()

    def kMeans(self):
        locs1 = getLocs(self.centroids)
        self.parentData()
        self.moveCentroids()
        locs2 = getLocs(self.centroids)
        dists = []
        for i in range(0, len(locs1)):
            dists.append(getDistance(locs1[i], locs2[i]))
        if max(dists) < 0.00001:
            return True
        return False

    def parentData(self):
        self.labels = []
        # Empty centroids of data
        for centroid in self.centroids:
            centroid[2] = []
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
            if len(x) >= 1 and len(y) >= 1:
                centroid[0] = np.mean(x)
                centroid[1] = np.mean(y)

    def kellMeans(self):
        # Split based on standard deviation and mean etc
        for centroid in self.centroids:
            if toSplit(centroid):
                self.centroids.append([centroid[0] + 1, centroid[1] + 1, []])
                return False
        return True

    def display(self):
        print("\nCENTROIDS COUNT - " + str(len(self.centroids)))
        for centroid in self.centroids:
            print("CENTROID - [" + str(centroid[0]) + ", " + str(centroid[1]) + "]")
        print("\nLABELS")
        print(self.labels)
