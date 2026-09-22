from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

#load API keys from .env file
load_dotenv()

# create gemini model object
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# send a message to gemini
response = llm.invoke(
    "Explain software architecture in one sentence."
)

#print the response
print(response.content)