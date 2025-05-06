# def dist(dot1, dot2):
#     return max(abs(dot1[0] - dot2[0]), abs(dot1[1] - dot2[1]))
#
# def centroid(cluster):
#     distance =[]
#     for dot in cluster:
#         sum_dist = 0
#         for dot2 in cluster:
#             sum_dist += dist(dot, dot2)
#         distance.append([sum_dist,dot])
#     return min(distance)[1]
#
# with open('27.3.A_19891.txt') as file:
#     cluster_A1 = []
#     cluster_A2 = []
#     for i in file:
#         x, y = map(float, i.split())
#         if x < 3:
#             cluster_A1.append([x, y])
#         else:
#             cluster_A2.append([x, y])
#
# centers = [centroid(cluster) for cluster in [cluster_A1, cluster_A2]]
# px = sum(center[0] for center in centers) / len(centers)
# py = sum(center[1] for center in centers) / len(centers)
# print(int(px * 10000), int(py * 10000))

def dist(dot1, dot2):
    return max(abs(dot1[0] - dot2[0]), abs(dot1[1] - dot2[1]))

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27.3.B_19891.txt') as file:
    cluster_B1 = []
    cluster_B2 = []
    cluster_B3 = []
    cluster_B4 = []
    for i in file:
        x, y = map(float, i.split())
        if y > 2:
            cluster_B1.append([x, y])
        if -2 < y < 2 and x > 2:
            cluster_B2.append([x, y])
        if -2 < y < 2 and x < 1:
            cluster_B3.append([x, y])
        if y < -2:
            cluster_B4.append([x, y])

centers = [centroid(cluster) for cluster in [cluster_B1, cluster_B2, cluster_B3, cluster_B4]]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)
print(int(px * 10000), int(py * 10000))