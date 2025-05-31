from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("your groq key"), model_name="meta-llama/llama-4-scout-17b-16e-instruct")


if __name__ == "__main__":
    response = llm.invoke("Famous Cities in the World")
    print(response.content)





