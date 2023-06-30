#using open ai and serpapi to get  valued answers from the web to the specific user prompt

!pip install langchain==0.0.218
!pip install openai
!pip install streamlit
!pip install PyPDF2
!pip install mistune
!pip install google-search-results


from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools import AIPluginTool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent
from langchain import OpenAI, SerpAPIWrapper
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from PyPDF2 import PdfReader
import html
import mistune
import os



'''import openai
openai.api_key = 'Your OPEN AI API KEY'
def fun():
  for chunk in openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user","content": "what is one + one"}],stream=True,):
      content= chunk["choices"][0].get("delta", {}).get("content")
      yield content
for x in fun():
  print(x)
  print("########")'''
