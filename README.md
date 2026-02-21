# Report Summarization Crew

An AI-powered multi-agent system that reads long reports and produces clear, structured summaries automatically.

This project uses a crew of specialized agents to break down documents, extract key points, and generate concise summaries suitable for quick reading, presentations, or further analysis.

## Features

* Multi-agent workflow for summarization
* Handles long reports and documents
* Structured summary output
* Configurable agents and tasks
* Built with CrewAI and LLMs
* Easy to extend for other document workflows

## How It Works

The system uses a crew of agents where each agent has a role:

* Research agent: reads and understands the report
* Analysis agent: extracts key insights
* Writer agent: produces final summary

The crew collaborates step-by-step to generate a clean final summary.

## Project Structure

```
report_summarization_crew/
│
├── src/
│   └── report_summarization_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│       └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/report_summarization_crew.git
cd report_summarization_crew
```

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

Install dependencies:

```
pip install -r requirements.txt
```

Add your API key in `.env`:

```
OPENAI_API_KEY=your_key_here
```

## Usage

Run the project:

```
python main.py
```

The crew will process the report and generate a summarized output.

## Configuration

You can modify:

* `agents.yaml` → define agent roles
* `tasks.yaml` → define workflow
* `crew.py` → logic for execution

## Future Improvements

* PDF upload support
* Web UI with Streamlit
* Multiple summary styles
* Export to DOCX/PDF
* RAG integration

## Tech Stack

* Python
* CrewAI
* LangChain
* OpenAI API

## Author

Dwinayan

## License

MIT License
