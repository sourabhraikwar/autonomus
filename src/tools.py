"""
Tools
"""
from typing import Any
from crewai_tools import BaseTool


class CustomTool(BaseTool):
    """
    CustomTool
    """
    name: str = "CustomTool"
    description: str = "some custom description, to perform custom operation"

    def _run(self, **kwargs: Any) -> None:
        """
        abstract method override
        :param kwargs:
        :return:
        """
        pass