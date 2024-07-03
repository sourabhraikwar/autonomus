"""
Tasks
"""
from typing import Any
from crewai import Task, Agent


class CrewTask:
    """
    Custom Task
    """

    def get_task(self, **kwargs: Any) -> Task:
        """
        Get Task instance by passing arguments
        in dictionary type format
        :param agent:
        :param kwargs:
        :return: Task
        """
        task_details = {
            "description": "{task_description}",
            "expected_output": "{task_expected_output}",
        }
        task_details.update(kwargs)
        return Task(**task_details)
