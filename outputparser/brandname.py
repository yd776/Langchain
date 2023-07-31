!pip -q install langchain openai tiktoken cohere
import os

os.environ["OPENAI_API_KEY"] = "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"
!pip show langchain
from langchain.chat_models import ChatOpenAI

chat_llm = ChatOpenAI(temperature=0.0)
template_string = """You are a master branding consulatant who specializes in naming brands. \
You come up with catchy and memorable brand names.

Take the brand description below delimited by triple backticks and use it to create the name for a brand.

brand description: ```{brand_description}```

then based on the description and you hot new brand name give the brand a score 1-10 for how likely it is to succeed.
"""
from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(template_string)
