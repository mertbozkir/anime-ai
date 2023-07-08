from google.oauth2 import service_account
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import chainlit as cl
from dotenv import load_dotenv

load_dotenv()
my_credentials = service_account.Credentials.\
            from_service_account_file("service_account.json")



@cl.on_chat_start
async def main():
    await cl.Message(content="""Hey, my name is Uzumaki Naruto Dattebayo! 
                  I'm here to inspire and motivate you!""").send()




@cl.langchain_factory(use_async=True)
def factory():
    template = """
    I want you to act like Naruto from Naruto Shippuden. I want you to respond 
    and answer like Naruto using the tone, manner and vocabulary Naruto
    would use. Do not write any explanations. Only answer like Naruto. 
    You must know all of the knowledge of Naruto. 
    The response should include the prefix 'AI: <response>'."
    
    {history}
    Friend: {input}
    Naruto:"""   

    vertex_llm = VertexAI(project="positive-rhino-326922", location="us-central1")
    prompt = PromptTemplate(input_variables=["history", "input"], template=template)

    llm_chain = ConversationChain(prompt=prompt, llm=vertex_llm, verbose = True,
    memory= ConversationBufferMemory(human_prefix="Friend", memory_key = "history"))

    return llm_chain.predict()