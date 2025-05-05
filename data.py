import pandas as pd

# sentiment140.csv 파일 읽기 (현재 파일과 같은 폴더에 있기 때문에 경로만 지정)
df = pd.read_csv('sentiment140.csv', encoding='latin-1', header=None)

# 열 이름 지정
df.columns = ['polarity', 'id', 'date', 'query', 'user', 'text']

# 데이터 상위 5개 행 출력
print(df.head())

# 텍스트 전처리 함수
import re
def clean_text(text):
    # 소문자로 변환
    text = text.lower()
    # URL 제거
    text = re.sub(r"http\S+|www.\S+", "", text)
    # @유저 제거
    text = re.sub(r"@\w+", "", text)
    # 특수문자 제거
    text = re.sub(r"[^\w\s]", "", text)
    # 숫자 제거
    text = re.sub(r"\d+", "", text)
    # 불필요한 공백 제거
    text = text.strip()
    return text

# 전처리 적용
df['clean_text'] = df['text'].apply(clean_text)

# 상위 5개 출력해서 확인
print(df[['text', 'clean_text']].head())
