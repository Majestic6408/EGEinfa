from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_A_21720 (1).txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    for i in file:
        x, y = map(float, i.split())
        if y > -2:
            cluster_A1.append([x, y])
        else:
            cluster_A2.append([x, y])

clusters = [cluster_A1, cluster_A2]
centers = [centroid(cluster) for cluster in clusters]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print(abs(int(px * 10000)), abs(int(py * 10000)))

with open('27_B_21720.txt') as file:
    cluster_B1 = []
    cluster_B2 = []
    cluster_B3 = []
    for i in file:
        x, y = map(float, i.split())
        if x > -6 and y > 0:
            cluster_B1.append([x, y])
        if y < 0:
            cluster_B2.append([x, y])
        if y > 0 and x < -6:
            cluster_B3.append([x, y])

clusters = [cluster_B1, cluster_B2, cluster_B3]
centers = [centroid(cluster) for cluster in clusters]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print(abs(int(px * 10000)), abs(int(py * 10000)))