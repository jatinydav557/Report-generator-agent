import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import Annotated, List
import operator
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.constants import Send
from langgraph.graph import StateGraph, START, END

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)

# Define schemas
class Section(BaseModel):
    name: str = Field(description="Name for this section of the report")
    description: str = Field(description="Brief overview of the section")

class Sections(BaseModel):
    sections: List[Section] = Field(description="Sections of the report")

planner = llm.with_structured_output(Sections)

# Graph state types
class State(TypedDict):
    topic: str
    sections: list[Section]
    completed_sections: Annotated[list, operator.add]
    final_report: str

class WorkerState(TypedDict):
    section: Section
    completed_sections: Annotated[list, operator.add]

# Graph node functions
def orchestrator(state: State):
    report_sections = planner.invoke(
        [
            SystemMessage(content="Generate a plan for the report."),
            HumanMessage(content=f"Here is the report topic: {state['topic']}"),
        ]
    )
    return {"sections": report_sections.sections}

def llm_call(state: WorkerState):
    section = llm.invoke(
        [
            SystemMessage(
                content="Write a report section following the provided name and description. Include no preamble. Use markdown."
            ),
            HumanMessage(
                content=f"Section name: {state['section'].name}\nDescription: {state['section'].description}"
            ),
        ]
    )
    return {"completed_sections": [section.content]}

def assign_workers(state: State):
    return [Send("llm_call", {"section": s}) for s in state["sections"]]

def synthesizer(state: State):
    return {"final_report": "\n\n---\n\n".join(state["completed_sections"])}

# Build LangGraph workflow
builder = StateGraph(State)
builder.add_node("orchestrator", orchestrator)
builder.add_node("llm_call", llm_call)
builder.add_node("synthesizer", synthesizer)
builder.add_edge(START, "orchestrator")
builder.add_conditional_edges("orchestrator", assign_workers, ["llm_call"])
builder.add_edge("llm_call", "synthesizer")
builder.add_edge("synthesizer", END)
workflow = builder.compile()

# ==== Streamlit UI ====
st.set_page_config(page_title="📄 AI Report Generator", layout="centered")
st.title("📄 LangGraph Report Generator ")

topic = st.text_input("Enter your report topic", placeholder="aaj kis topic pe aapko report chahiye?")

if st.button("Generate Report"):
    with st.spinner("Generating report..."):
        state = workflow.invoke({"topic": topic})
        st.markdown(state["final_report"])
