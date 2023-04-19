import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# os.environ["OPENAI_API_KEY"] = "{your-api-key}"

global retriever
def load_embedding():
    embedding = OpenAIEmbeddings()
    global retriever
    vectordb = Chroma(persist_directory='db', embedding_function=embedding)
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})


def prompt(query):
    prompt_template = """请注意：请谨慎评估query与提示的Context信息的相关性，只根据本段输入文字信息的内容进行回答，如果query与提供的材料无关，请回答"我不知道"，另外也不要回答无关答案：
    Context: {context}
    Context: {context}
    Question: {question}
    Answer:"""
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    docs = retriever.get_relevant_documents(query)
    
    # 基于docs来prompt，返回你想要的内容
    chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff", prompt=PROMPT)
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
