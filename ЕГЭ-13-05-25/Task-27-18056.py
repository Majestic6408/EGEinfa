from math import dist
import turtle as t

# def centroid(cluster):
#     distance = []
#     for dot in cluster:
#         sum_dist = 0
#         for dot2 in cluster:
#             sum_dist += dist(dot, dot2)
#         distance.append([sum_dist, dot])
#     return min(distance)[1]
#
# with open('27A_18056.txt') as file:
#     data = [list(map(float, i.split())) for i in file]
#
# eps = 1.5
# clusters = []
# while data:
#     cluster = [data.pop()]
#     for dot in cluster:
#         for dot2 in data.copy():
#             if dist(dot, dot2) < eps:
#                 data.remove(dot2)
#                 cluster.append(dot2)
#     if len(cluster) > 10:
#         clusters.append(cluster)
# print([len(cluster) for cluster in clusters])
# t.tracer(0)
# m = 40
# t.up()
# colors = ['red', 'blue']
# for cluster, color in zip(clusters, colors):
#     for dot in cluster:
#         t.goto(dot[0] * m, dot[1] * m)
#         t.dot(3, color)
# t.done()
# t.update()
# centers = [centroid(cluster) for cluster in clusters]
# px = sum(center[0] for center in centers) / len(centers)
# py = sum(center[1] for center in centers) / len(centers)
# print(abs(int(px * 100000)), abs(int(py * 100000)))

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27B_18056.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.5
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                data.remove(dot2)
                cluster.append(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)
print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)
print(abs(int(px * 100000)), abs(int(py * 100000)))