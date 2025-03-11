from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os 
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")


webagents=Agent(
    name='web_agent',
    description='A web agent that can search the web for information',
    model=OpenAIChat(api_key=openai_api_key, id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    markdown=True,
    instructions="you should also include the source of the information in your response",
    show_tool_calls=True
)

stock_agent=Agent(
    name='stock_agent',
    description='A stock agent that can search the web for information',
    model=OpenAIChat(api_key=openai_api_key, id="gpt-4o-mini"),
    tools=[YFinanceTools()],
    show_tool_calls=True
)

agent_team=Agent(
    team=[webagents,stock_agent],
    model=OpenAIChat(api_key=openai_api_key, id="gpt-4o-mini"),
    markdown=True,
    instructions="you should also include the source of the information in your response and tables to show the information",
    show_tool_calls=True
)

agent_team.print_response("Analyze the company likes apple, google, amazon, microsoft, tesla, and nvidia and give me which should buy long term and which should sell short term", stream=True)
