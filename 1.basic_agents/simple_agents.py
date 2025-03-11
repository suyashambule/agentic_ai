from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os 
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(api_key=groq_api_key, id="qwen-2.5-32b"),
    description="You are a helpful assistant that can answer questions and help with tasks.",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("who won india vs newzealand in champtions trophy 2025", stream=True)





