from operator import itemgetter
import random
import math


def getMinMax(data):
    return [min(data, key=itemgetter(0))[0], max(data, key=itemgetter(0))[0],
            min(data, key=itemgetter(1))[1], max(data, key=itemgetter(1))[1]]


# Get Euclidean distance between two points
def getDistance(loc1, loc2):
    diff = [loc1[0] - loc2[0], loc1[1] - loc2[1]]
    return math.sqrt((diff[0] ** 2) + (diff[1] ** 2))


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
        self.centroids.append([random.randint(min_maxes[0], min_maxes[1]), random.randint(min_maxes[2], min_maxes[3]), []])
        self.centroids.append([random.randint(min_maxes[0], min_maxes[1]), random.randint(min_maxes[2], min_maxes[3]), []])
        self.k_means()

    def k_means(self):
        self.parentData()
        self.moveCentroids()

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
            new_pos = []
            x = []
            y = []
            for point in centroid[2]:
                x.append(point[0])
                y.append(point[1])
            new_pos.append(sum(x)/len(centroid[2]))
            new_pos.append(sum(y)/len(centroid[2]))
            centroid[0] = new_pos[0]
            centroid[1] = new_pos[1]
