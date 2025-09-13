# Agentic AI Framework

An intelligent multi-agent system built with the Agno framework for creating autonomous AI agents capable of web searching, financial analysis, and collaborative task execution.

## 🚀 Overview

This project demonstrates the power of agentic AI by implementing specialized agents that can:
- Perform web searches and information retrieval
- Analyze financial data and stock market trends
- Work collaboratively in multi-agent teams
- Make autonomous decisions based on available tools

## 🏗️ Project Structure

```
agentic_ai/
│
├── 1.basic_agents/
│   ├── simple_agents.py        # Basic agent implementation with web search
│   ├── multiagents.py          # Multi-agent team for complex analysis
│   └── simpple.ipynb          # Jupyter notebook for experimentation
│
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## 🤖 Agent Types

### 1. Simple Agent (simple_agents.py)
A basic agent that uses:
- **Model**: Groq Qwen-2.5-32B
- **Tools**: DuckDuckGo web search
- **Capability**: Answer questions using real-time web information

### 2. Multi-Agent System (multiagents.py)
A collaborative team of specialized agents:

#### Web Agent
- **Purpose**: Web search and information retrieval
- **Model**: OpenAI GPT-4o-mini
- **Tools**: DuckDuckGo search
- **Features**: Sources citation, markdown formatting

#### Stock Agent
- **Purpose**: Financial data analysis
- **Model**: OpenAI GPT-4o-mini
- **Tools**: Yahoo Finance integration
- **Features**: Real-time stock data, market analysis

#### Agent Team
- **Coordination**: Combines web and stock agents
- **Output**: Structured analysis with tables and sources
- **Use Case**: Complex financial research and recommendations

## 🛠️ Prerequisites

- Python 3.8+
- OpenAI API key
- Groq API key

## 📦 Installation

1. **Clone or download the project**
   ```bash
   cd /Users/suyash/Desktop/agentic_ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🚀 Usage

### Running Simple Agent

```bash
python 1.basic_agents/simple_agents.py
```

This will execute a web search query about cricket match results using the Groq model.

### Running Multi-Agent System

```bash
python 1.basic_agents/multiagents.py
```

This will perform comprehensive stock analysis of major tech companies (Apple, Google, Amazon, Microsoft, Tesla, NVIDIA) and provide investment recommendations.

### Custom Queries

Modify the queries in the Python files:

```python
# For simple agent
agent.print_response("Your question here", stream=True)

# For multi-agent team
agent_team.print_response("Your complex analysis request", stream=True)
```

## 📊 Key Dependencies

- **agno**: Core agentic AI framework
- **openai**: OpenAI API integration
- **groq**: Groq API integration
- **python-dotenv**: Environment variable management
- **duckduckgo-search**: Web search functionality
- **yfinance**: Financial data retrieval
- **streamlit**: Web interface (for future UI development)
- **pandas**: Data manipulation and analysis
- **lancedb**: Vector database for embeddings
- **pypdf**: PDF document processing

## 🔧 Configuration

### Model Configuration

**Groq Models:**
```python
model=Groq(api_key=groq_api_key, id="qwen-2.5-32b")
```

**OpenAI Models:**
```python
model=OpenAIChat(api_key=openai_api_key, id="gpt-4o-mini")
```

### Agent Customization

```python
agent = Agent(
    name='custom_agent',
    description='Agent description',
    model=your_model,
    tools=[YourTools()],
    markdown=True,
    instructions="Custom instructions",
    show_tool_calls=True
)
```

## 💡 Example Use Cases

### Information Retrieval
```python
agent.print_response("What are the latest developments in AI?", stream=True)
```

### Financial Analysis
```python
agent_team.print_response(
    "Compare the financial performance of Tesla vs traditional automakers",
    stream=True
)
```

### Research Tasks
```python
agent_team.print_response(
    "Research and analyze the impact of renewable energy on oil companies",
    stream=True
)
```

## 🎯 Features

- **🧠 Multiple LLM Support**: OpenAI GPT-4, Groq Qwen models
- **🔍 Web Search**: Real-time information via DuckDuckGo
- **📈 Financial Data**: Yahoo Finance integration for stock analysis
- **🤝 Multi-Agent Collaboration**: Specialized agents working together
- **📝 Markdown Output**: Formatted, readable responses
- **🔗 Source Attribution**: Automatic citation of information sources
- **📊 Data Visualization**: Tables and structured data presentation
- **🎛️ Tool Integration**: Extensible tool system for custom functionality

## 🔮 Future Enhancements

- [ ] Streamlit web interface for interactive agent chat
- [ ] PDF document analysis capabilities
- [ ] Vector database integration for knowledge management
- [ ] Custom tool development framework
- [ ] Agent performance monitoring and analytics
- [ ] Voice interface integration
- [ ] Real-time data streaming capabilities

## 🛠️ Development

### Adding New Agents

1. Define agent purpose and capabilities
2. Select appropriate model and tools
3. Configure instructions and behavior
4. Test with sample queries

### Creating Custom Tools

```python
from agno.tools.base import Tool

class CustomTool(Tool):
    def search(self, query: str):
        # Your custom tool logic
        pass
```

## 🐛 Troubleshooting

### Common Issues

**API Key Errors:**
- Verify API keys in `.env` file
- Check API key permissions and quotas

**Import Errors:**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version compatibility

**Model Access Issues:**
- Verify model IDs are correct
- Check API provider availability

## 📚 Resources

- [Agno Framework Documentation](https://github.com/agnoframework/agno)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Groq API Documentation](https://console.groq.com/docs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

For questions, issues, or contributions, please reach out or create an issue in the repository.

---

*Empowering AI agents to work autonomously and collaboratively! 🤖✨*
