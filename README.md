# CareConnectAI
Multi-Agent Elderly Care System using LLM Reasoning and SQLite Shared Memory
# CareConnectAI – Multi-Agent Elderly Care System 👵🧠

(This project shows just the demo of the problem solution briefed , this will be implmented upto the mark soon )
CareConnectAI is a simulation-based multi-agent system designed to assist elderly individuals using AI-driven agents that provide health tracking, fall detection, reminders, emergency alerts, and social companionship. Each agent leverages local reasoning with shared memory using SQLite and interacts with others in a coordinated ecosystem.

---

## 🚀 Project Highlights

- 🤖 LLM-based Reasoning (Ollama-ready)
- 🧠 Multi-Agent Collaboration (6 agents)
- 💾 Shared Memory with SQLite
- 📋 Task Logs & Alerts Stored Centrally
- 🗨️ Conversational Agent for Companionship
- 🔔 Real-time Alert & Reminder Simulation
- 💡 Modular Design for Scalability

---

## 🧩 Agents Used

| Agent Name           | Functionality |
|----------------------|----------------|
| HealthMonitorAgent     | Monitors elderly health status and flags risks |
| FallDetectionAgent     | Simulates fall detection and initiates emergency protocols |
| ReminderAgent          | Schedules and delivers medicine & appointment reminders |
| EmergencyAlertAgent    | Sends alerts to caregivers and logs emergencies |
| ConversationAgent      | Provides companionship through small talk |
| AdviceAgent            | Gives health or safety advice based on emotional trend |

---

## 🛠️ Tech Stack

| Component      | Stack Used |
|----------------|------------|
| Language       | Python |
| LLM Engine     | Ollama (local/offline LLMs like LLaMA2, Mistral) |
| Database       | SQLite (in-memory for agent communication) |
| Execution      | Jupyter Notebook / Python script |
| Visualization  | Console output, markdown tables |
| Frontend (Optional) | PPT + screen recording demo |

---

## 📁 Project Structure

CareConnectAI/
├── agents/
│   ├── health_monitor_agent.py
│   ├── fall_detection_agent.py
│   ├── reminder_agent.py
│   ├── emergency_alert_agent.py
│   ├── conversation_agent.py
│   └── advice_agent.py
├── main_simulation.py
├── database/
│   └── agent_logs.db
├── requirements.txt
├── README.md
└── demo_assets/
    ├── careconnect_ppt.pptx
    ├── careconnect_demo.mp4

---

## 🧪 How It Works

1. Each agent is initialized and connected to a common SQLite database.
2. Agents simulate real-time behavior such as heart rate tracking and fall detection.
3. Emotional state scores are logged and evaluated over multiple rounds.
4. Final logs are formatted into a markdown table with timestamps.
5. Optional LLM integration via Ollama enables intelligent dialogue and reasoning.

---

## 📊 Output Example

[HealthMonitorAgent] Ravi's heart rate = 137 bpm  
[FallDetectionAgent] Inactivity duration = 11 min  
[ReminderAgent] 📲 Mobile Notification Sent: Hydrate well today 💧  
[AlertAgent] 🚨 Critical! Immediate caregiver intervention advised.  
[ConversationAgent] Let's do a small breathing exercise together!  
[AdviceAgent] 🔔 Recommend a caregiver visit today.

---

## 📂 Dataset

No external dataset used.  
Sensor values (heart rate, inactivity) are generated using Python’s `random` module to simulate real-time readings from wearables.

---

