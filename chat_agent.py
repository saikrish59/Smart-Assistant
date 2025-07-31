
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from app.tools import get_tools

def chat_with_agent(query, docs):
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    retriever = db.as_retriever()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm = ChatOpenAI(temperature=0)

    tools = get_tools(llm)
    agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", memory=memory, verbose=True)
    result = agent.run(query)
    reasoning = "Used LangChain tools: vector search and/or SQL based on query intent."
    return result, reasoning
