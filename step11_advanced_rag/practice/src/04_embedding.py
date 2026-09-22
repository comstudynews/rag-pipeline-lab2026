from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# 문장을 의미 벡터로 변환할 Embedding 모델입니다.
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

text = "도서는 최대 5권까지 대출할 수 있다."
vector = embeddings.embed_query(text)

print("벡터 길이:", len(vector))
print("앞부분 10개 값:")
print(vector[:10])
