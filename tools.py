
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from app.db_handler import setup_dummy_database

def get_tools(llm):
    conn = setup_dummy_database()
    db = SQLDatabase(conn)
    sql_chain = SQLDatabaseChain(llm=llm, database=db)

    tools = [
        Tool(name="SQLQuery", func=sql_chain.run, description="Query structured data"),
    ]
    return tools
