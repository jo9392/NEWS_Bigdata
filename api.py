import requests
import json
import time
import pandas as pd
#time out 있는 응답 함수
def web_request(method_name, url, dict_data, is_urlencoded=True, timeout_seconds=3):
    """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
    method_name = method_name.upper()  # 메소드이름을 대문자로 바꾼다
    if method_name not in ('GET', 'POST'):
        raise Exception('method_name is GET or POST plz...')

    if method_name == 'GET':  # GET방식인 경우
        response = requests.get(url=url, params=dict_data, timeout=timeout_seconds)
    elif method_name == 'POST':  # POST방식인 경우
        if is_urlencoded is True:
            response = requests.post(url=url, data=dict_data, \
                                     timeout=timeout_seconds,
                                     headers={'Content-Type': 'application/x-www-form-urlencoded'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), \
                                     timeout=timeout_seconds, headers={'Content-Type': 'application/json'})

    dict_meta = {'status_code': response.status_code, 'ok': response.ok, 'encoding': response.encoding,
                 'Content-Type': response.headers['Content-Type']}
    if 'json' in str(response.headers['Content-Type']):  # JSON 형태인 경우
        return {**dict_meta, **response.json()}
    else:  # 문자열 형태인 경우
        return {**dict_meta, **{'text': response.text}}

#timeout이 발생하면 두번 더 시도하는 함수
def web_request_retry(num_retry=3, sleep_seconds=1, **kwargs):
    """timeout발생 시 sleep_seconds쉬고 num_retyrp번 재시도 한다"""
    for n in range(num_retry):
        try:
            return web_request(**kwargs)
        except requests.exceptions.Timeout:
            print(str(n+1) + ' Timeout')
            time.sleep(sleep_seconds)
            continue
    return None

#json 형식의 input 데이터
datas = {
    "access_key": "16ca0e32-df44-4e27-84db-45f6604fad18",
    "argument": {
        "query": "서비스 AND 출시",
        "published_at": {
            "from": "2019-01-01",
            "until": "2019-03-31"
        },
        "provider": [
            "경향신문",
        ],
        "category": [
            "정치>정치일반",
            "IT_과학"
        ],
        "category_incident": [
            "범죄",
            "교통사고",
            "재해>자연재해"
        ],
        "byline": "",
        "provider_subject": [
            "경제", "부동산"
        ],
        "subject_info": [
            ""
        ],
        "subject_info1": [
            ""
        ],
        "subject_info2": [
            ""
        ],
        "subject_info3": [
            ""
        ],
        "subject_info4": [
            ""
        ],
        "sort": {"date": "desc"},
        "hilight": 200,
        "return_from": 0,
        "return_size": 5,
        "fields": [
            "byline",
            "category",
            "category_incident",
            "provider_news_id"
        ]
    }
}

#요청 URL
url = "http://tools.kinds.or.kr:8888/search/news"

#응답 받아오기
response = requests.post(url, data = json.dumps(datas)) #타임아웃 없는 버전
#response = web_request_retry(method_name='POST', url=url, dict_data=datas, is_urlencoded=True, num_retry=2) #타임아웃 있는 버전

#status code 확인
if response.status_code == 200:
    print("된다")
    #print(json.loads(response.test))
elif response.status_code == 400:
    print("액세스키 만료")
elif response.status_code == 408:
    print("timeout")
else:
    print("뭔가 이상하다")

#객체 가져오기
output = response.json()
print(output)

#json -> dataframe 형태로 변경
df = pd.json_normalize(output['documents'])

#dataframe -> csv 파일로 변경 후 로컬 폴더에 저장
df.to_csv('sample.csv')
