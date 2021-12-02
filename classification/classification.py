import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat
from matplotlib import font_manager as fm

#폰트 설정
mat.rcParams['axes.unicode_minus'] = False
font_path = r"C:\Windows\Fonts\NanumGothic.otf"
fontprop = fm.FontProperties(fname=font_path, size=18)
print(mat.rcParams['font.family'])
mat.rcParams['font.family'] = 'NanumGothic'
plt.rc('xtick', labelsize=8)  # x축 눈금 폰트 크기
ticklabel=['보수 편향','진보 편향']


# figure, 즉 그래프를 표현할 액자를 먼저 만든다.
plt.figure()

#데이터 삽입
point_sum = pd.read_csv('classification\point.csv', encoding='cp949')
point_sum = point_sum.dropna(axis=0)

# figure 를 출력한다.
plt.xlabel('신문사')
plt.ylabel('2017 대선 기준 신문사 보수 편향 정도')
plt.show()
plt.bar(point_sum['provider'], point_sum['point9'])

plt.show()

