!pip install llama-index
!pip install openai
!pip install ib_insync
!pip install pandas
!pip install jinja2
!pip install streamlit

import os
os.environ["OPENAI_API_KEY"] = 'YOUR OPEN API KEY'

from llama_index import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

OPENAI_API_KEY = "YOUR OPEN API KEY"
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
documents = SimpleDirectoryReader('/content/story.txt').load_data()
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist('a.json')


from llama_index import StorageContext, load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir="/content/a.json")
index = load_index_from_storage(storage_context)



from pathlib import Path
from llama_index import download_loader

PDFReader = download_loader("PDFReader")
loader = PDFReader()
documents = Path("/filename.pdf")

content = loader.load_data(documents)
a=((content[0]))
text = a.text
print(text)

#print(content["text"][int("0")])
#output
'''1/I S ELL MY DREAMS
Short stories
INTRODUCTION
A short story is a prose narrative of limited length.
It organises the action and thoughts of its
characters into the pattern of a plot. The plot
form may be comic, tragic, romantic or satiric.
The central incident is selected to manifest, as
much as possible, the protagonist’s life and
character , and the details contribute to the
development of the plot.
The term ‘short story’ covers a great diversity of
prose fiction, right from the really short ‘short
story’ of about five hundred words to longer and
more complex works. The longer ones, with their
status of middle length, fall between the tautness
of the short narrative and the expansiveness of
the novel.
There can be thematic variation too. The stories
deal with fantasy, reality, alienation and the
problem of choice in personal life. There are three
short stories and two long ones in this section
representing writers from five cultures.
Rationalised 2023-24'''
