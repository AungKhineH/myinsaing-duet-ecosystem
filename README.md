# Myinsaing Ecosystem: Self-Improving Multi-Agent Architecture

An advanced, locally-hosted AI agent ecosystem demonstrating automated red-teaming and self-improvement without manual human iteration.

Built with **Python**, **Streamlit**, and **Ollama (Llama 3)**, this project serves as a functional prototype of the "Duet" evaluation concept—where a dedicated supervisor agent automatically stress-tests operational agents and writes new Agent Operating Procedures (AOPs) to their persistent memory.

## 🚀 The Core Problem Solved

Currently, enterprise AI teams spend days on "manual hillclimbing"—reading transcripts, identifying edge-case failures, and manually tweaking agent prompts.

The **Myinsaing Ecosystem** automates this lifecycle. It features a dedicated evaluator agent that continuously generates complex crisis scenarios, critiques the operational agents' responses, and automatically injects new, strict rules into their local knowledge bases (`.json`), scaling the system's baseline intelligence exponentially.

## 🤖 Ecosystem Architecture

The ecosystem relies on strict domain isolation and sequential multi-agent collaboration, featuring three specialized agents:

1. **Aung Chan Thar (Strategic Vision):** Focuses entirely on high-level business strategy, competitive advantage ("Economic Moats"), and market positioning.
2. **Nan Dhana (Financial Architecture):** A specialized FinTech agent that reads strategic output and calculates financial viability, risk, capital allocation, and ROI.
3. **Wizaya (The "Duet" Evaluator):** The supreme red-teamer. Wizaya does not solve problems; it breaks the other agents by generating difficult edge cases, evaluates their failures, and writes new AOPs.

## ⚙️ Key Features & Operational Modes

* **Auto-Eval Mode (Automated Red-Teaming):** Wizaya dynamically creates a crisis scenario, forces the operational agents to react, evaluates their performance, and permanently saves new operating rules to their memory files.
* **Synergy Mode (Multi-Agent Collaboration):** Sequential execution where Aung Chan Thar's strategic output serves as the strict input constraint for Nan Dhana's financial modeling. Includes one-click Markdown Executive Report exports.
* **Manual Training (Hillclimbing):** A baseline mode to demonstrate the legacy method of manually feeding test cases to agents to generate SOPs.
* **Live Chat:** Standard dialogue mode with individual agents, enhanced by their dynamically updated persistent memory.

## 🛠️ Installation & Setup

This ecosystem is designed to run completely locally, ensuring data sovereignty and zero API costs during the high-volume self-improvement loops.

### Prerequisites

* **Python 3.11** (Recommended for dependency stability)
* **Ollama** installed and running locally ([Download Ollama](https://ollama.com/download))

### 1. Pull the Local LLM

Ensure the Llama 3 model is downloaded to your local Ollama engine:

```bash
ollama pull llama3
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Ecosystem

Start the Master Orchestrator UI:

```bash
python -m streamlit run myinsaing_ecosystem.py
```

## 📂 Project Structure

* `myinsaing_ecosystem.py`: The master orchestrator and Streamlit frontend.
* `aung_chan_thar_knowledge.json`: Auto-generated persistent memory file (created dynamically).
* `nan_dhana_knowledge.json`: Auto-generated persistent memory file (created dynamically).

## 🎯 The Vision

As agents move from simple chatbots to autonomous enterprise operators, iteration speed is everything. By utilizing an automated evaluator to manage the agent lifecycle from the first deployment to the hundredth improvement, the Myinsaing architecture proves that self-improving ecosystems are the future of scalable AI deployment.
