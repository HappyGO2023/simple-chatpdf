import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

# os.environ["OPENAI_API_KEY"] = "{your-api-key}"

# 将文件中的文字拆分成小的文件Embedding并持久化
def persist_embedding(history_file):
    loader = TextLoader(history_file)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap  = 30,
        length_function = len,
    )
    docs = text_splitter.split_documents(documents)

    # 将embedding数据持久化到本地磁盘
    persist_directory = 'db'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)
    vectordb.persist()
    vectordb = None 

if __name__ == "__main__":
    # embdding并且持久化
    persist_embedding("china_history.txt")