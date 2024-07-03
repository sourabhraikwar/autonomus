"""
Main file to execute crew agents
"""
from dotenv import load_dotenv
from crewai import Crew
from src.utils import get_crew_details

# Loads environment variables
load_dotenv()

tasks, agents = get_crew_details(
    [
        {
            "agent": {},
            "task": {}
        },
    ]
)

# Required arguments for initiating crew instance
crew_details = {
    "tasks": tasks,
    "agents": agents,
    "verbose": 2,
}

# Creates crew instance
crew = Crew(**crew_details)

# Required input values provides context to agents and tasks
input_details = {
    "agent_role": "Professional Content Writer",
    "agent_goal": """Create engaging, high-quality content that 
    captivates readers and effectively communicates the intended message, enhancing the brand's presence and driving audience engagement.""",
    "agent_backstory": """As a seasoned professional content writer, 
    you have a knack for crafting compelling narratives that capture 
    the essence of a brand. With a background in journalism and digital 
    marketing, you have honed your skills in storytelling, SEO, and 
    audience analysis. Your expertise lies in transforming complex 
    ideas into clear, engaging content that resonates with diverse 
    audiences. You thrive on deadlines, possess a keen eye for detail, 
    and are dedicated to maintaining the highest standards of quality 
    in your work. Your passion for writing and your ability to adapt 
    to various tones and styles make you a valuable 
    asset in any content creation team.""",
    "task_description": """
    write 5 titles for instagram post on Universe
    """,
    "task_expected_output": """
    comma separated string values
    """,
}

if __name__ == "__main__":
    # Run crew with given agents and tasks
    crew.kickoff(inputs=input_details)
