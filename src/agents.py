"""
Agents
"""
import os
from typing import Any
from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

# Loads environment variables
load_dotenv()

# Sets required constants from environment
os.environ["OPENAI_API_KEY"] = "NA"
OLLAMA_MODEL_NAME = os.environ.get("OLLAMA_MODEL_NAME")
OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE")
CURRENT_LLM = os.environ.get('CURRENT_LLM')

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_MODEL = os.environ.get('GROQ_MODEL')


class CrewAgent:
    """
    Provides crew agent instance
    """
    # Creates llm instance
    ollama = ChatOpenAI(
        model=OLLAMA_MODEL_NAME,
        base_url=OPENAI_API_BASE,
    )
    groq = ChatGroq(
        api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        stop_sequences=[]
    )

    def get_agent(self, **kwargs: Any) -> Agent:
        """
        Get Agent instance by passing arguments
        in dictionary type format
        :param kwargs:
        :return:
        """
        agent_details = {
            "role": "{agent_role}",
            "goal": "{agent_goal}",
            "backstory": "{agent_backstory}",
            "allow_delegation": False,
            "step_callback": lambda return_values: print(return_values, "\n"),
            "max_iter": 3
        }
        agent_details.update(kwargs)
        llm = self.groq if CURRENT_LLM == 'GROQ' else self.ollama
        agent_details.update({"llm": llm, "function_calling_llm": llm})
        return Agent(**agent_details)
