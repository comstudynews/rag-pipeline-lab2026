from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# TODO: text-embedding-3-small 모델을 생성하세요.
embeddings = None

text = "도서는 최대 5권까지 대출할 수 있다."

if embeddings is None:
    raise SystemExit("TODO: OpenAIEmbeddings를 생성하세요.")

vector = embeddings.embed_query(text)

print("벡터 길이:", len(vector))
print("앞부분 10개 값:")
print(vector[:10])
