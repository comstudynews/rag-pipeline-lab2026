from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def build_retriever(file_path: str = "data/sample.txt", k: int = 3):
    # 1) 문서를 읽습니다.
    docs = TextLoader(file_path, encoding="utf-8").load()

    # 2) 이후 Step에서도 같은 Chunk 기준을 사용합니다.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=120,
        chunk_overlap=20,
    )
    chunks = splitter.split_documents(docs)

    # 3) Chunk를 Embedding하여 FAISS 검색 인덱스를 만듭니다.
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 4) RAG Pipeline에서 사용할 Retriever를 반환합니다.
    return vectorstore.as_retriever(search_kwargs={"k": k})


def format_docs(docs) -> str:
    # Document 목록을 LLM이 읽기 좋은 Context 문자열로 변환합니다.
    return "\n\n".join(
        f"[문서 {i}]\n{doc.page_content}"
        for i, doc in enumerate(docs, start=1)
    )
