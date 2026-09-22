import math

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def cosine_similarity(a, b):
    # TODO: dot product와 두 벡터의 norm을 이용해 Cosine Similarity를 반환하세요.
    raise NotImplementedError("TODO: cosine_similarity를 완성하세요.")


sentences = [
    "도서는 최대 5권까지 대출할 수 있다.",
    "한 사람이 빌릴 수 있는 책은 최대 다섯 권이다.",
    "토요일 운영시간은 오전 10시부터 오후 5시까지이다.",
]

vectors = embeddings.embed_documents(sentences)
print(cosine_similarity(vectors[0], vectors[1]))
