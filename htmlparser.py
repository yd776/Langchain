#HTML CONVERSION USING HARDCODING

pip install langchain
pip install openai
pip install streamlit
pip install PyPDF2
pip install mistune
pip install google-search-results
pip install google-search-results
pip install google-api-wrapper
pip install flask-codemirror

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
from langchain.callbacks import StreamingStdOutCallbackHandler
import os
from langchain.utilities import GoogleSearchAPIWrapper
from typing import Any





#import your serpapi and openai keys in enviornment

def pdf_to_text(file):#pdf_to_text function uses Pdfreader library and gets the text component from pdf and stores it as a string
  a= PdfReader(file).pages[0].extract_text()
  return a

def text_to_html(text):#text_to_html function uses openai to convert text to html
  from langchain.prompts import PromptTemplate
  from langchain.chains import LLMChain
  from langchain.chains import LLMChain

  prompt = PromptTemplate.from_template("convert the following  {text}? in html5 format ")

  chain = LLMChain(llm=llm, prompt=prompt)
  return chain.run(text)

def dummy(input=""):#dummy function
  return 45

def google_serp(text):
  from langchain.agents import load_tools
  from langchain.agents import initialize_agent
  from langchain.agents import AgentType
  from langchain.llms import OpenAI

  llm = OpenAI(temperature=0,openai_api_key="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")
  tools = load_tools(["serpapi", "llm-math"], llm=llm)
  agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
  agent.run(text)



def name_func(query):
  print("aaaaaaa", query)
  return "this is the result"+query

tool6=Tool(
    name="python name function",
    func=name_func,
    description="a python function which takes the query and respond with a message string"
)

tool1=Tool(
    name="pdf_to_text_tool",
    func=pdf_to_text,
    description="Converts the pdf to a fstring format input should be pdf"
)
tool2=Tool(
    name="dummy",
    func=dummy,
    description = "returns a constant value"
)
tool3 = Tool(
    name='convert_to_html',
    func=text_to_html,
    description="Useful for when you need to convert the answer from a string to a html format "
)
tool4=Tool(
    name='google_search',
    func=google_serp,
    description="Searches google and gives the output"
)
tools=[tool1,tool2,tool3,tool4]




sir_prompt='''i want you to read text from a pdf and convert it into html format with all the tags and syntax  :


Use the following format:

Question: You have to take the pdf , extract the text from it and convert it into html format
Thought: you should always think on what tool should you be using and using your own methods as well
Action: the action to take place should only be one of [tool1,tool2,tool3,tool4]
Action Input: the input to the action and how to you convert it in html
Observation: the result of the action may or may not be in html format but the final answer should be in html format
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought:  the final answer should be of the format html if not convert html
Final Answer:  the final answer to the original input question should be in html do nont summarize the text you are not allowed to understand it

Question: {input}
Thought:{agent_scratchpad}'''

"""# SETTING UP THE MEMORY AND CHAIN"""

llm = OpenAI(model_name='text-davinci-003',temperature=0,openai_api_key='your API KEY',streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
tools = load_tools(["serpapi", "llm-math"], llm=llm)
zero_agent = initialize_agent(
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    #verbose=True,
    intermediate_steps=True,
    prompt=sir_prompt,
    max_iterations=5,
)
text=input()
a=zero_agent(text)
b=(a["output"])
print(b)
text_to_html(b)
