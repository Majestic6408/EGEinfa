from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_A_17916.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    for i in file:
        x, y = map(float, i.split())
        if y > 8:
            cluster_A1.append([x, y])
        else:
            cluster_A2.append([x, y])

center1 = centroid(cluster_A1)
center2 = centroid(cluster_A2)

px = (center1[0] + center2[0]) / 2
py = (center1[1] + center2[1]) / 2

print(int(px * 10000), int(py * 10000))