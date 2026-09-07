
# 🔎 Deep Research AI Agent

An AI-powered deep research system that autonomously plans searches, gathers information from the web, generates a detailed research report, and delivers the final report through email.

## 🚀 Live Demo

**Try the application:**  
https://deep-research-41zf.onrender.com/

## ✨ Features

- 🤖 **Multi-Agent Architecture**
  - Planner Agent
  - Search Agent
  - Writer Agent
  - Email Agent

- 🔎 **Intelligent Web Research**
  - Generates multiple search queries
  - Performs concurrent searches
  - Uses Tavily for web search

- 🧠 **LLM-Powered Reasoning**
  - Gemini for planning
  - OpenRouter models for research and report generation

- 📝 **Structured Research Reports**
  - Comprehensive Markdown reports
  - Executive summary
  - Follow-up research questions

- 📧 **Automatic Email Delivery**
  - Sends the generated research report through SMTP

- ⚡ **Asynchronous Execution**
  - Concurrent search execution using Python `asyncio`
  - Streaming research status updates

## 🏗️ Architecture

```text
                    User Query
                        │
                        ▼
                ┌───────────────┐
                │ Planner Agent │
                └───────┬───────┘
                        │
                 Search Plan
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
     Search Agent  Search Agent  Search Agent
          │             │             │
       Tavily         Tavily        Tavily
          │             │             │
          └─────────────┼─────────────┘
                        │
                  Search Results
                        │
                        ▼
                ┌───────────────┐
                │  Writer Agent │
                └───────┬───────┘
                        │
                  Research Report
                        │
                        ▼
                ┌───────────────┐
                │  Email Agent  │
                └───────┬───────┘
                        │
                        ▼
                    Email Sent
````

## 🛠️ Tech Stack

| Technology        | Purpose              |
| ----------------- | -------------------- |
| Python            | Core application     |
| OpenAI Agents SDK | Agent orchestration  |
| Gradio            | Web interface        |
| Gemini            | Research planning    |
| OpenRouter        | LLM inference        |
| Tavily            | Web search           |
| Pydantic          | Structured output    |
| SMTP              | Email delivery       |
| asyncio           | Concurrent execution |
| Render            | Deployment           |

## 📁 Project Structure

```text
Deep-Research/
│
├── deep_research/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── search_agent.py
│   │   ├── writer_agent.py
│   │   └── email_agent.py
│   │
│   ├── services/
│   │   └── messenger.py
│   │
│   ├── app.py
│   ├── config.py
│   ├── research_manager.py
│   ├── simple.py
│   └── styles.py
│
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── README.md
```

## ⚙️ How It Works

1. The user enters a research question.
2. The **Planner Agent** converts the question into multiple search queries.
3. The **Search Agent** performs the searches concurrently using Tavily.
4. The collected information is passed to the **Writer Agent**.
5. The Writer Agent generates a structured research report.
6. The **Email Agent** sends the completed report through SMTP.
7. The final report is displayed in the Gradio interface.

## 🔐 Environment Variables

Create a `.env` file locally with your API credentials:

```env
OPENROUTER_API_KEY=your_openrouter_key
GEMINI_API_KEY=your_gemini_key
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key

EMAIL_SMTP_SERVER=your_smtp_server
EMAIL_SMTP_PORT=your_smtp_port
EMAIL_ADDRESS=your_email
EMAIL_APP_PASSWORD=your_email_app_password
```

**Never commit `.env` or API keys to GitHub.**

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/codedbyshashi/Deep-Research.git
cd Deep-Research
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your `.env` file and add the required credentials.

Run the application:

```bash
python deep_research/app.py
```

Then open the local Gradio URL shown in the terminal.

## ☁️ Deployment

The application is deployed using **Render**.

Every push to the `main` branch can trigger an automatic deployment:

```text
git push origin main
        ↓
      GitHub
        ↓
      Render
        ↓
   Build & Deploy
        ↓
  Live Application
```

## 📌 Future Improvements

* Persistent research history
* Citation management
* Search-result ranking
* More LLM providers
* PDF report generation
* User authentication
* Research session management

## 👨‍💻 Author

**Kota Shashidhar Reddy**

Computer Science & Engineering

---

⭐ If you find this project interesting, consider giving the repository a star.
