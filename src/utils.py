"""
Utils
"""
from .agents import CrewAgent
from .tasks import CrewTask


def get_crew_details(details: list) -> [list, list]:
    """

    :param details: list
    :return:
    """
    agents, tasks = [], []
    for detail in details:
        # Agents
        agent = CrewAgent().get_agent(**detail['agent'])
        # Tasks
        task_details = {
            "agent": agent
        }
        task_details.update(detail['task'])
        task = CrewTask().get_task(**task_details)
        agents.append(agent)
        tasks.append(task)

    return tasks, agents

