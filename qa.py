import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# os.environ["OPENAI_API_KEY"] = "{your-api-key}"

global retriever
def load_embedding():
    embedding = OpenAIEmbeddings()
    global retriever
    vectordb = Chroma(persist_directory='db', embedding_function=embedding)
    retriever = vectordb.as_retriever(search_type="mmr")

# 参考https://python.langchain.com/en/latest/modules/chains/index_examples/question_answering.html?highlight=context
# langchain的DOC写的是真乱...
def prompt(query):
    prompt_template = """参考context，有且仅回答关联的相信，如果没有结果请回答我不知道；用中文回答，
    Context: {context}
    Question: {question}
    Answer:"""
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    docs = retriever.get_relevant_documents(query)
    # 基于docs来prompt，返回你想要的内容，so easy吧！
    chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff", prompt=PROMPT)
    result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
    return result['output_text']

if __name__ == "__main__":
    # load embedding
    load_embedding()
    # 循环输入查询，直到输入 "exit"
    while True:
        query = input("Enter query (or 'exit' to quit): ")
        if query == 'exit':
            print('exit')
            break
        print("Query:" + query + '\nAnswer:' + prompt(query) + '\n')