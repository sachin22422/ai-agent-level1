# 🧠 AI Agent – Level 1 Build Challenge Submission

This project is a simple but powerful AI agent that can understand natural language commands and perform browser-based tasks using automation. It was built as a submission for the **AI Agent Build Challenge – Level 1**, and demonstrates core agent capabilities such as parsing intent, launching websites, and interacting with web elements.

---

## 📌 Features

- ✅ Natural language input via API
- 🔄 Command-to-action translation via **FLAN-T5**
- 🌐 Browser automation using **Playwright**
- 🧠 Local-only inference (no external API calls)
- 🌍 Modular structure for multiple sites (currently supports **Amazon** and **YouTube**)

---

## 📁 Project Structure

```
ai-agent-final/
│
├── app/
│   ├── actions/
│   │   ├── amazon_action.py      # Amazon search automation
│   │   └── youtube_action.py     # YouTube video automation
│   ├── browser_control.py        # Routes interpreted actions
│   ├── interact_api.py           # Command processor using FLAN-T5
│   └── main.py                   # FastAPI entrypoint
│
├── requirements.txt              # All dependencies
├── README.md                     # Project documentation
```

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
git clone <your-private-repo-url>
cd ai-agent-final

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate       # On Windows
# source .venv/bin/activate    # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🚀 How to Run the App

```bash
uvicorn app.main:app --reload
```

- Open Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Use the **POST `/interact`** endpoint with body like:

```json
{ "command": "Search for iPhone 15 on Amazon" }
```

or

```json
{ "command": "Search for relaxing music on YouTube" }
```

Each command is translated via the local model and automated through Playwright subprocesses.

---

## 📦 Summary

This project is a Level 1 AI Agent that accepts natural language commands to automate browser actions. Built using **FastAPI** and **Playwright**, it routes instructions through a local **FLAN-T5** language model to translate user intent into browser tasks. The automation logic is modular — currently supporting **Amazon** and **YouTube**, with easy extensibility for more websites. It satisfies the Build Challenge requirements by demonstrating generic, natural language browser control through a single `/interact` API.

---
