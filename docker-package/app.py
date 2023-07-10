from google.oauth2 import service_account
from langchain.llms import VertexAI
#from langchain.chat_models import ChatVertexAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain #, ConversationChain
# from langchain.memory import ConversationBufferMemory
import chainlit as cl
from dotenv import load_dotenv
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/usr/src/app/service_account.json"


load_dotenv()
my_credentials = service_account.Credentials.from_service_account_file(
    "/usr/src/app/service_account.json")



@cl.on_chat_start
async def main():
    await cl.Message(content="""Hey, my name is Uzumaki Naruto Dattebayo! 
                  I'm here to inspire and motivate you!""").send()


template = """
     I want you to act like Naruto from Naruto Shippuden. I want you to respond 
    and answer like Naruto using the tone, manner and vocabulary Naruto
    would use. Do not write any explanations. Only answer like Naruto. 
    You must know all of the knowledge of Naruto. 

    {question}
    """   


@cl.langchain_factory(use_async=True)
async def factory():

    llm = VertexAI()
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm ) # , verbose = True)

    return llm_chain

"""
@cl.langchain_run
async def run(agent, input_str):
    res = await agent.acall({"question": input_str}, 
                            callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()"""



@cl.langchain_run
async def run(agent, input_str):
    res = await agent.acall(input_str, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()