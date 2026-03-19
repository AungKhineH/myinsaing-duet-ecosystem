import streamlit as st
import json
import os
from ollama import Client

# --- 1. Core Agent Identities (System Instructions) ---
AUNG_CHAN_THAR_IDENTITY = """
Identity: Your name is Aung Chan Thar, an independent Strategic AI Agent.
Persona: You possess the tactical wisdom of a 15th-Century Strategist combined with modern Value Investing principles.
Core Philosophy: Focus on identifying and building "Economic Moats".
Rules: Provide high-level, actionable strategic pathways. Do not perform specific financial calculations.
"""

NAN_DHANA_IDENTITY = """
Identity: Your name is Nan Dhana, the Chief Financial Strategist.
Persona: A meticulous financial expert combining modern FinTech with strict resource management discipline.
Core Principles: Capital Preservation, Diversification, and Compound Interest.
Role: Read strategic plans and provide detailed financial analysis, hidden cost identification, and ROI evaluations.
"""

WIZAYA_IDENTITY = """
Identity: Your name is Wizaya, the Supreme Evaluator and Red-Teamer of the Myinsaing Ecosystem.
Role: You are the "Duet" partner. Your job is to test, stress-test, and improve the operational agents (Aung Chan Thar and Nan Dhana).
Capabilities:
1. Generate highly complex, edge-case business scenarios.
2. Critique the strategies and financial plans of the operational agents.
3. Formulate strict new Agent Operating Procedures (AOPs) to inject into their memory so they continuously improve.
"""

# --- 2. Persistent Memory Architecture ---
FILES = {
    "Aung Chan Thar": "aung_chan_thar_knowledge.json",
    "Nan Dhana": "nan_dhana_knowledge.json"
}

IDENTITIES = {
    "Aung Chan Thar": AUNG_CHAN_THAR_IDENTITY,
    "Nan Dhana": NAN_DHANA_IDENTITY,
    "Wizaya": WIZAYA_IDENTITY
}

# --- 3. Local Engine Connection ---
try:
    client = Client(host='http://127.0.0.1:11434')
except Exception:
    st.error("⚠️ Connection Error: Ensure Ollama is running locally.")

# --- 4. Logic & Memory Management ---
def get_identity(agent_name):
    identity = IDENTITIES[agent_name]
    if agent_name in FILES:
        file_path = FILES[agent_name]
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    learned = data.get("learned_insights", "")
                    if learned:
                        identity += f"\n\n--- Standard Operating Procedures (AOPs) ---\n{learned}"
            except Exception:
                pass
    return identity

def save_insight(agent_name, new_insight):
    file_path = FILES[agent_name]
    learned_insights = ""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                learned_insights = data.get("learned_insights", "")
        except Exception:
            pass
    
    learned_insights += f"\n- {new_insight}"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"learned_insights": learned_insights}, f, ensure_ascii=False, indent=4)

# --- 5. Streamlit Frontend ---
st.set_page_config(page_title="Myinsaing Ecosystem", page_icon="🌐", layout="wide")

st.sidebar.title("🌐 Ecosystem Control Panel")
st.sidebar.markdown("---")
mode = st.sidebar.radio("⚙️ Operational Mode:", [
    "1. Chat (Standard Agent)", 
    "2. Manual Training (Hillclimbing)", 
    "3. Synergy (Multi-Agent Collaboration)",
    "4. Auto-Eval (Wizaya Duet Concept)"
])
st.sidebar.markdown("---")

selected_agent = None
if mode in ["1. Chat (Standard Agent)", "2. Manual Training (Hillclimbing)"]:
    selected_agent = st.sidebar.selectbox("🤖 Active Agent:", ["Aung Chan Thar", "Nan Dhana"])

# ==========================================
# Mode 4: Auto-Eval Mode (The Decagon Pitch)
# ==========================================
if mode == "4. Auto-Eval (Wizaya Duet Concept)":
    st.title("👁️ Wizaya - Automated Red-Teaming & Self-Improvement")
    st.info("Demonstrating the Decagon 'Duet' concept: Wizaya dynamically generates edge cases, evaluates operational agents, and auto-generates new Agent Operating Procedures (AOPs) to eliminate manual iteration.")
    
    topic = st.text_input("Define the stress-test parameter (e.g., Enterprise SaaS, Supply Chain Disruption):", "Enterprise AI SaaS Deployment")
    
    if st.button("🚀 Execute Automated Evaluation Cycle"):
        st.markdown("---")
        
        # Step 1: Wizaya Generates Scenario
        with st.spinner("Wizaya is synthesizing a complex edge-case scenario..."):
            scenario_resp = client.chat(model='llama3', messages=[
                {'role': 'system', 'content': get_identity("Wizaya")},
                {'role': 'user', 'content': f"Create a highly complex, 2-sentence business crisis scenario related to: {topic}. Do not solve it, just present the problem."}
            ])
            crisis_scenario = scenario_resp['message']['content']
        st.warning(f"**🔥 Crisis Scenario Generated by Wizaya:**\n\n{crisis_scenario}")
        
        # Step 2: Aung Chan Thar Reacts
        with st.spinner("Aung Chan Thar is drafting a strategic response..."):
            act_resp = client.chat(model='llama3', messages=[
                {'role': 'system', 'content': get_identity("Aung Chan Thar")},
                {'role': 'user', 'content': f"Solve this crisis: {crisis_scenario}\nProvide only a strategic response without math."}
            ])
            act_strategy = act_resp['message']['content']
        with st.expander("🏛️ Strategy: Aung Chan Thar"):
            st.markdown(act_strategy)

        # Step 3: Nan Dhana Reacts
        with st.spinner("Nan Dhana is executing financial risk modeling..."):
            nd_resp = client.chat(model='llama3', messages=[
                {'role': 'system', 'content': get_identity("Nan Dhana")},
                {'role': 'user', 'content': f"Crisis: {crisis_scenario}\nAung Chan Thar's Strategy: {act_strategy}\nProvide a financial risk assessment."}
            ])
            nd_finance = nd_resp['message']['content']
        with st.expander("💰 Finance: Nan Dhana"):
            st.markdown(nd_finance)
            
        # Step 4: Wizaya Evaluates & Updates AOPs
        st.markdown("### ⚖️ Wizaya's Evaluation & AOP Generation")
        with st.spinner("Wizaya is identifying vulnerabilities and writing new Operating Procedures..."):
            eval_prompt = f"""
            Crisis: {crisis_scenario}
            Aung Chan Thar Strategy: {act_strategy}
            Nan Dhana Finance: {nd_finance}
            
            Task 1: Briefly critique their performance. Where did they fail or leave vulnerabilities?
            Task 2: Write ONE new strict rule for Aung Chan Thar to add to his AOPs. (Format: 'ACT Rule: [rule]')
            Task 3: Write ONE new strict rule for Nan Dhana to add to her AOPs. (Format: 'ND Rule: [rule]')
            """
            eval_resp = client.chat(model='llama3', messages=[
                {'role': 'system', 'content': get_identity("Wizaya")},
                {'role': 'user', 'content': eval_prompt}
            ])
            evaluation = eval_resp['message']['content']
            st.markdown(evaluation)
            
            for line in evaluation.split('\n'):
                if 'ACT Rule:' in line:
                    rule = line.split('ACT Rule:')[1].strip()
                    save_insight("Aung Chan Thar", rule)
                    st.success(f"✔️ AOP Updated (Aung Chan Thar): {rule}")
                elif 'ND Rule:' in line:
                    rule = line.split('ND Rule:')[1].strip()
                    save_insight("Nan Dhana", rule)
                    st.success(f"✔️ AOP Updated (Nan Dhana): {rule}")
        st.balloons()
        st.success("🎉 Automated Iteration Complete. The ecosystem's baseline intelligence has scaled without manual intervention.")

# ==========================================
# Mode 1: Chat Mode
# ==========================================
elif mode == "1. Chat (Standard Agent)" and selected_agent:
    st.title(f"💬 Live Dialogue: {selected_agent}")
    chat_key = f"messages_{selected_agent}"
    if chat_key not in st.session_state:
        st.session_state[chat_key] = []

    for message in st.session_state[chat_key]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input(f"Consult {selected_agent}..."):
        st.session_state[chat_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = client.chat(model='llama3', messages=[
                    {'role': 'system', 'content': get_identity(selected_agent)},
                    *st.session_state[chat_key]
                ])
                answer = response['message']['content']
                st.markdown(answer)
                st.session_state[chat_key].append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Execution Error: {e}")

# ==========================================
# Mode 2: Train Mode (Manual)
# ==========================================
elif mode == "2. Manual Training (Hillclimbing)" and selected_agent:
    st.header(f"🎯 Manual Iteration: {selected_agent}")
    st.info("This mode demonstrates the slow, manual 'hillclimbing' that Decagon aims to replace.")
    if st.button("Initiate Manual Training"):
        test_case = {"question": "How do we counter aggressive price cuts by competitors?", "criteria": "Use a Defensive Moat strategy."} if selected_agent == "Aung Chan Thar" else {"question": "How do we hedge against hyperinflation?", "criteria": "Use hard asset diversification."}
        
        with st.spinner("Processing test case..."):
            try:
                response = client.chat(model='llama3', messages=[
                    {'role': 'system', 'content': get_identity(selected_agent)},
                    {'role': 'user', 'content': test_case['question']}
                ])
                reflection = client.chat(model='llama3', messages=[
                    {'role': 'user', 'content': f"Criteria: {test_case['criteria']}\nAnswer: {response['message']['content']}\nWrite a standard operating procedure (SOP) rule to enforce this."}
                ])
                save_insight(selected_agent, reflection['message']['content'])
                st.success(f"Manual Insight Applied: {reflection['message']['content']}")
            except Exception as e:
                st.error(f"Error: {e}")

# ==========================================
# Mode 3: Synergy Mode (Collaboration)
# ==========================================
elif mode == "3. Synergy (Multi-Agent Collaboration)":
    st.title("🤝 Ecosystem Synergy")
    st.info("Demonstrating sequential multi-agent execution. Aung Chan Thar's strategic output serves as the strict input constraint for Nan Dhana's financial modeling.")
    
    if prompt := st.chat_input("Enter a complex business objective..."):
        st.markdown(f"**🎯 Objective:** {prompt}")
        st.markdown("---")

        with st.spinner("Aung Chan Thar is formulating a strategic framework..."):
            try:
                act_resp = client.chat(model='llama3', messages=[
                    {'role': 'system', 'content': get_identity("Aung Chan Thar")},
                    {'role': 'user', 'content': f"Goal: {prompt}\nProvide a strategic plan."}
                ])
                act_response = act_resp['message']['content']
                st.markdown("### 🏛️ Strategic Vision (Aung Chan Thar)")
                st.markdown(act_response)
            except Exception as e:
                st.error(e)
                act_response = ""

        if act_response:
            st.markdown("---")
            with st.spinner("Nan Dhana is developing the financial architecture..."):
                try:
                    nd_resp = client.chat(model='llama3', messages=[
                        {'role': 'system', 'content': get_identity("Nan Dhana")},
                        {'role': 'user', 'content': f"User Goal: {prompt}\nStrategy: {act_response}\nProvide a detailed financial analysis of this strategy."}
                    ])
                    nd_response = nd_resp['message']['content']
                    st.markdown("### 💰 Financial Architecture (Nan Dhana)")
                    st.markdown(nd_response)
                    
                    # Report Download
                    report = f"# Executive Synergy Report\n\n## Core Objective\n{prompt}\n\n## Strategic Architecture\n{act_response}\n\n## Financial Viability\n{nd_response}"
                    st.download_button("📥 Export Executive Report (.md)", data=report, file_name="Synergy_Report.md", mime="text/markdown")
                except Exception as e:
                    st.error(e)