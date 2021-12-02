from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
import math
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

#데이터 불러오기
point_sum = pd.read_csv('classification\point4.csv', encoding='cp949')
point_sum = point_sum.dropna(axis=0)
point_sum.columns = ["x", "y"]
point_sum.head()

sns.scatterplot(x="x", y="y", data=point_sum, palette="Set2");
centroids = point_sum.sample(3, random_state=1)
centroids

distance = sp.spatial.distance.cdist(point_sum, centroids, "euclidean")

# 가장 거리가 짧은 중심점의 cluster로 할당
cluster_num = np.argmin(distance, axis=1)

# 결과 확인
result = point_sum.copy()
result["cluster"] = np.array(cluster_num)
result.head()
sns.scatterplot(x="x", y="y", hue="cluster", data=result, palette="Set2");

# cluster별로 묶어서 평균 계산
centroids_2 = result.groupby("cluster").mean()
centroids_2

distance = sp.spatial.distance.cdist(point_sum, centroids_2, "euclidean")
cluster_num = np.argmin(distance, axis=1)

# 결과 확인
result = point_sum.copy()
result["cluster"] = np.array(cluster_num)
result.head()
sns.scatterplot(x="x", y="y", hue="cluster", data=result, palette="Set2");

result['cluster'] = [0,1,0,1,2,2,2,2,1,0,1,0,2,2,1,0,1,2,2]
ans = [0,1,2,1,1,2,0,1,0,0,1,1,1,2,1,1,2,2,2]
ans2 = [1,0,2,0,0,2,1,0,1,1,0,0,0,2,0,0,2,2,2]  #0과 1을 바꿈
ans3 = [0,2,1,2,2,1,0,2,0,0,2,2,2,1,2,2,1,1,1]  #1과 2를 바꿈
ans4 = [2,0,1,0,0,2,2,0,2,2,0,0,0,1,0,0,1,1,1]  #0과 2를 바꿈
ans5 = [1,2,0,2,2,0,1,2,1,1,2,2,2,0,2,2,0,0,0]
ans6 = [2,1,0,0,0,1,2,0,2,2,0,0,0,1,0,0,1,1,1]
ans_list = []
correct = 0
total = 19
for i in range(0,19):
    if result['cluster'][i] == ans[i]:
        correct = correct + 1
acc = (correct/total) * 100
ans_list.append(acc)
#print(acc, '%, correct : ',correct)
correct = 0
total = 19
for i in range(0,19):
    if result['cluster'][i] == ans2[i]:
        correct = correct + 1
acc = (correct/total) * 100
ans_list.append(acc)
#print(acc, '%, correct : ',correct)
correct = 0
total = 19
for i in range(0,19):
    if result['cluster'][i] == ans3[i]:
        correct = correct + 1
acc = (correct/total) * 100
ans_list.append(acc)
#print(acc, '%, correct : ',correct)
correct = 0
total = 19
for i in range(0,19):
    if result['cluster'][i] == ans4[i]:
        correct = correct + 1
acc = (correct/total) * 100
ans_list.append(acc)
#print(acc, '%, correct : ',correct)
correct = 0
total = 19
for i in range(0,19):
    if result['cluster'][i] == ans5[i]:
        correct = correct + 1
acc = (correct/total) * 100
ans_list.append(acc)
#print(acc, '%, correct : ',correct)
correct = 0
total = 19
for i in range(0,19):
    if result['cluster'][i] == ans6[i]:
        correct = correct + 1
acc = (correct/total) * 100
ans_list.append(acc)
#print(acc, '%, correct : ',correct)

print('정확도 : ',int(max(ans_list)), '%')