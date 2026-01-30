from langchain.agents import AgentType, initialize_agent
from langchain.llms import HuggingFacePipeline

from tools.calculator import calculator_tool
from tools.file_reader import file_reader_tool
from tools.summarizer import summarizer_tool

def create_agent(llm):
    tools =[
        calculator_tool,
        file_reader_tool,
        summarizer_tool
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    return agent