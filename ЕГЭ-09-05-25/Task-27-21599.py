# from math import dist
#
# def centroid(cluster):
#     distance = []
#     for dot in cluster:
#         sum_dist = 0
#         for dot2 in cluster:
#             sum_dist += dist(dot, dot2)
#         distance.append([sum_dist, dot])
#     return min(distance)[1]
#
# with open('27_A_21599.txt') as file:
#     cluster_A1 = []
#     cluster_A2 = []
#     cluster_A3 = []
#     for i in file:
#         x, y = map(float, i.split())
#         if y > x - 10:
#             cluster_A1.append([x, y])
#         elif y < x - 10 and y > -5:
#             cluster_A2.append([x, y])
#         else:
#             cluster_A3.append([x, y])
#
# centers = [centroid(cluster) for cluster in [cluster_A1, cluster_A2, cluster_A3]]
# px = sum(center[0] for center in centers) / len(centers)
# py = sum(center[1] for center in centers) / len(centers)
#
# print(int(px * 10000), int(py * 10000))

from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_B_21599.txt') as file:
    cluster_B1 = []
    cluster_B2 = []
    cluster_B3 = []
    cluster_B4 = []
    cluster_B5 = []
    cluster_B6 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -2 * x - 26 and y > -5:
            cluster_B1.append([x, y])
        elif y > -2 * x - 26 and x < -10:
            cluster_B2.append([x, y])
        elif x > -10 and y > 1.5 * x + 10:
            cluster_B3.append([x, y])
        elif y > 0.625 * x + 0.375 and y < 1.5 * x + 10:
            cluster_B4.append([x, y])
        elif y < 0.625 * x + 0.375 and y > -5:
            cluster_B5.append([x, y])
        else:
            cluster_B6.append([x, y])

centers = [centroid(cluster) for cluster in [cluster_B1, cluster_B2, cluster_B3,cluster_B4, cluster_B5, cluster_B6]]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)
print(int(abs(px * 10000)), int(abs(py * 10000)))