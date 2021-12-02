# KNU 한국어 감성사전
# 작성자 : 온병원, 박상민, 나철원
# 소속 : 군산대학교 소프트웨어융합공학과 Data Intelligence Lab
# 홈페이지 : dilab.kunsan.ac.kr
# 작성일 : 2018.05.14
# 뜻풀이 데이터 출처 : https://github.com/mrchypark/stdkor
# 신조어 데이터 출처 : https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%ED%84%B0%EB%84%B7_%EC%8B%A0%EC%A1%B0%EC%96%B4_%EB%AA%A9%EB%A1%9D
# 이모티콘 데이터 출처: https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98
# SentiWordNet_3.0.0_20130122 데이터 출처 : http://sentiwordnet.isti.cnr.it/
# SenticNet-5.0 데이터 출처 : http://sentic.net/
# 감정단어사전0603 데이터 출처 : http://datascience.khu.ac.kr/board/bbs/board.php?bo_table=05_01&wr_id=91 
# 김은영, “국어 감정동사 연구”, 2004.02, 학위논문(박사) - 전남대학교 국어국문학과 대학원


#-*-coding:utf-8-*-

import json
import csv
import pandas as pd
import numpy as np
import pickle
pd.set_option('mode.chained_assignment',  None)

class KnuSL():

	def data_list(wordname, count):
		with open('C:\python\hackerton\emotion\SentiWord_info.json', encoding='utf-8-sig', mode='r') as f:
			data = json.load(f)
		result = ['None','None']
		for i in range(0, len(data)):
			if data[i]['word'] == wordname:
				result.pop()
				result.pop()
				result.append(data[i]['word_root'])
				result.append(data[i]['polarity'])

		r_word = result[0]
		s_word = result[1]
		# 옆에 포인트 추가 : s_word
		df_pop['point'][count] = s_word
		#print('어근 : ' + r_word)
		#print('극성 : ' + s_word)
		#print(s_word)
		return r_word, s_word

#pickle -> list -> df
for i in range(1,20):
	usmeat = 'Mun\\title_cut\Mun_' + str(i) + '.pkl'
	with open(usmeat, 'rb') as f:
	  mydict = pickle.load(f)
	df_pop = pd.DataFrame(mydict)
	print(df_pop)
######################################

#csv -> df
#df_pop = pd.read_csv('jojungdong.csv', encoding='cp949')

#df 한줄로 만들기
	columns = len(df_pop.columns)
	rows = len(df_pop.index) #단어 개수
	total = columns * rows
	cur_col = 0
	cur_row = 0
	count = 0
	df_pop_2 = pd.DataFrame(index=range(0,total), columns=['hilight', 'point'])

	for cur_col in range(0,columns):
		cur_row = 0
		for cur_row in range(0, rows):
			count = cur_col*rows + cur_row
			df_pop_2['hilight'][count] = df_pop[cur_col][cur_row]
			cur_row = cur_row +1
		cur_col = cur_col+1
		print(i,"번째 파일을 한줄로 합치는 중, ",count)

#한 줄로 만든 것을 적절한 형식의 df로 전처리
	df_pop_2['hilight'].isnull().sum()
	df_pop = df_pop_2['hilight'].dropna()
	df_pop.isnull().sum()
	df_pop = df_pop.to_frame()
	type(df_pop)
	df_pop["point"] = np.nan
	df_pop.columns
#바른 단어 제거
	barun = df_pop[df_pop['hilight'] == "바른"].index
	df_pop = df_pop.drop(barun)
	df_pop.reset_index()

	total = len(df_pop.index)
	count = 0

	if __name__ == "__main__":
		ksl = KnuSL
		cnt = 0

		while(cnt < total):

			wordname = df_pop['hilight'][df_pop.index[cnt]]
			#print(wordname)
			#wordname = wordname.strip(" ")

			#if wordname != "#":
			ksl.data_list(wordname, df_pop.index[cnt])
			#print("\n")
			cnt = cnt + 1
			print(i, "번째 단어 분석중, ",cnt)

	#집계 되지 않은 단어의 컬럼은 제거
	point_NaN = df_pop[df_pop['point'] == 'None'].index
	df_pop2 = df_pop.drop(point_NaN)
	df_pop2 = df_pop2.dropna(axis=0)

	#df -> csv로 저장
	usmeat_e = 'Mun\\title_emotion\Mun_' + str(i) + '.csv'
	df_pop2.to_csv(usmeat_e)

#점수 합계 내기
hong_list = []
for i in range(1,20):
	Hong_e = 'Hong\\title_emotion\Hong_' + str(i) + '.csv'
	df_sum1 = pd.read_csv(Hong_e)
	l_url = 'Hong\\title_cut\Hong_' + str(i) + '.pkl'
	with open(l_url, 'rb') as f:
		mydict = pickle.load(f)
	df_pop = pd.DataFrame(mydict)
	l = len(df_pop)
	print('Hong의 ', i, '번째 길이는 ', l, )
	hong_list.append(int(df_sum1['point'].sum()*10000/l))
print(hong_list)


Mun_list = []
for i in range(1,20):
	Mun_e = 'Mun\\title_emotion\Mun_' + str(i) + '.csv'
	df_sum1 = pd.read_csv(Mun_e)
	l_url = 'Mun\\title_cut\Mun_' + str(i) + '.pkl'
	with open(l_url, 'rb') as f:
		mydict = pickle.load(f)
	df_pop = pd.DataFrame(mydict)
	l = len(df_pop)
	print('Mun의 ',i,'번째 길이는 ',l,)
	if l ==0:
		print(i,'번째는 0..')
	else:
		Mun_list.append(int(df_sum1['point'].sum()*10000/l))
print(Mun_list)


Usmeat_list = []
for i in range(1,20):
	Usmeat_e = 'USmeat\emotion\\USmeat_' + str(i) + '.csv'
	try:
		df_sum1 = pd.read_csv(Usmeat_e, encoding='cp949')
	except UnicodeDecodeError as e1 :
		try :
			df_sum1 = pd.read_csv(Usmeat_e, encoding='euc-kr')
		except UnicodeDecodeError as e1 :
			df_sum1 = pd.read_csv(Usmeat_e)
		else:
			print(i)
	else:
		print(i)
	l = len(df_sum1.index)
	Usmeat_list.append(int(df_sum1['point'].sum()*10000/l))
	print(i)

print(hong_list)
print(Mun_list)
print(Usmeat_list)

#point 합계를 파일로 저장
hong_fin = 'Hong\\title_emotion\Hong_fin3.csv'
hong_fin_df = pd.DataFrame(hong_list)
hong_fin_df.to_csv(hong_fin)

Mun_fin = 'Mun\\title_emotion\Mun_fin3.csv'
Mun_fin_df = pd.DataFrame(Mun_list)
Mun_fin_df.to_csv(Mun_fin)

USmeat_fin = 'USmeat\emotion\\USmeat_fin.csv'
USmeat_fin_df = pd.DataFrame(Usmeat_list)
USmeat_fin_df.to_csv(USmeat_fin)
