▶️ YouTube Demo: [Watch Here](https://www.youtube.com/watch?v=B3IQRdgbdDM&list=PLe-YIIlt-fbNajMvdZoBUdjZNbmLOMJSU&index=2&ab_channel=Jatin)  
---
# 📄 AI Report Generator using LangGraph + Llama3

**AI Report Generator** is an intelligent, structured, and automated report builder powered by **LangGraph**, **LangChain**, and **GROQ's Llama3**. This tool dynamically plans, drafts, and synthesizes professional-quality reports on any topic you choose — within seconds.

This project is designed to show the power of **agentic workflows**, **structured output planning**, and **parallel generation**, all visualized as a dynamic LangGraph pipeline.

---

## 🚀 What It Does

Give it a topic like:

```text
"Create a report on Agentic AI RAGs"
````

And it will:

1. 🧠 **Plan** your report using structured outputs (with section titles + summaries)
2. ✍️ **Assign AI writers** (agents) to draft each section **in parallel**
3. 🧩 **Merge and polish** everything into a final, markdown-formatted report

---

## 🧱 Built With

| Tool                | Purpose                                  |
| ------------------- | ---------------------------------------- |
| **LangGraph**       | Graph-based agent workflow orchestration |
| **LangChain**       | LLM interfaces, prompt control           |
| **GROQ Llama3**     | Fast and accurate open-weight LLM        |
| **Pydantic**        | Schema validation and structured output  |
| **Streamlit**       | Web UI for easy report generation        |
| **Python + Dotenv** | Clean environment management             |

---

## 🖼️ App Preview

```text
📌 Topic: Evolution of LLMs in Enterprise Search

# Output Structure:
- Introduction
- Historical Progression of LLMs
- Modern Use in RAG Pipelines
- Case Studies
- Future Outlook
```

Each section is neatly generated with markdown formatting and no unnecessary preamble.

---

## 🧠 How It Works (Graph View)

```
[Start] 
   ↓
[Orchestrator] → assigns → [llm_call (xN)] 
   ↓
[Synthesizer]
   ↓
[Final Report]
```

✅ Orchestrator: Plans sections
✅ llm\_call: Agents write each section
✅ Synthesizer: Combines into final report

This is all dynamically controlled via LangGraph’s `StateGraph`.

---

## 📂 Project Structure

```
📄 ai-report-generator/
├── app.py                     # Streamlit web app
├── report_graph.ipynb         # Dev notebook for testing the workflow
├── .env                       # Secure API keys
├── README.md
└── requirements.txt
```

---

## 📦 Requirements

```txt
langchain
langgraph
langchain-core
langchain-community
langchain-groq
langchain-together
streamlit
python-dotenv
ipykernel
Ipython
arxiv
wikipedia
```

---

## 🔧 Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/jatinydav557/Report-generator-agent
cd Report-generator-agent
```

### 2. Create `.env` file

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_key
TAVILY_API_KEY=your_tavily_key
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🧠 Why This Project Matters

While most people are stuck writing prompts manually, this project proves that:

* LLMs can be **coordinated like teams** (graph-driven task flow)
* Reports can be **planned structurally**, not just generated as a blob
* You can **scale writing** by assigning tasks to AI agents working in parallel

It's a real-world application of **Agentic AI**, built for **speed**, **structure**, and **clarity**.

---

## 🛠️ Future Features

* [ ] Export reports as PDF or DOCX
* [ ] Add interactive feedback to revise individual sections
* [ ] Use memory to build multi-report pipelines

---

## 🤝 Credits

* [LangGraph](https://www.langgraph.dev/)
* [LangChain](https://www.langchain.com/)
* [GROQ](https://groq.com/)
* [Streamlit](https://streamlit.io/)

---
## 🙋‍♂️ Let's Connect

* **💼 LinkedIn:** [www.linkedin.com/in/jatin557](https://www.linkedin.com/in/jatin557)
* **📦 GitHub:** [https://github.com/jatinydav557](https://github.com/jatinydav557)
* **📬 Email:** [jatinydav557@gmail.com](mailto:jatinydav557@gmail.com)
* **📱 Contact:** [`+91-7340386035`](tel:+917340386035)
* **🎥 YouTube:** [Checkout my other working projects](https://www.youtube.com/@jatinML/playlists)
---
By - Me

