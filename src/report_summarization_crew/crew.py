# Import core CrewAI components
from crewai import Agent, Crew, Process, Task, TaskOutput

# These decorators help auto-build agents, tasks and the crew
from crewai.project import CrewBase, agent, crew, task

# BaseAgent is used for typing (not required but good practice)
from crewai.agents.agent_builder.base_agent import BaseAgent

# Used for type hints
from typing import List, Any


# CrewBase decorator automatically:
# - Loads agents.yaml
# - Loads tasks.yaml
# - Connects agents and tasks using decorators
@CrewBase
class ReportSummarizationCrew():
    """This class defines the entire multi-agent workflow."""

    # These lists will automatically store all agents and tasks
    agents: List[BaseAgent]
    tasks: List[Task]

    # Path to YAML configuration files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    # -----------------------------
    # Guardrail Function
    # -----------------------------
    # This function checks if summary exceeds word limit.
    # It runs AFTER the summarization task completes.
    # If it fails, CrewAI retries the task.
    def validate_word_count_for_summary(self, result: TaskOutput) -> tuple[bool, Any]:
        try:
            word_limit = 300  # maximum allowed words

            # result.raw contains the actual text output from the agent
            result_text: str = result.raw.strip()

            # Count words by splitting on spaces
            word_count: int = len(result_text.split(" "))

            # If word count exceeds limit → return False
            if word_count > word_limit:
                return (
                    False,
                    "Summary exceeds 300 words. Please reduce the length."
                )

            # If everything is fine → return True
            return (True, result_text)

        except Exception as e:
            return (False, f"Unexpected error occurred: {str(e)}")


    # -----------------------------
    # Agent 1: Report Generator
    # -----------------------------
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            # Loads configuration from agents.yaml
            config=self.agents_config['report_generator'],  # type: ignore[index]
            verbose=True  # shows reasoning in terminal
        )


    # -----------------------------
    # Agent 2: Report Summarizer
    # -----------------------------
    @agent
    def report_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['report_summarizer'],  # type: ignore[index]
            verbose=True
        )


    # -----------------------------
    # Task 1: Generate Full Report
    # -----------------------------
    @task
    def report_generation_task(self) -> Task:
        return Task(
            # Loads task details from tasks.yaml
            config=self.tasks_config['report_generation_task'],  # type: ignore[index]

            # Save output file automatically
            output_file='reports/report_new.md'
        )


    # -----------------------------
    # Task 2: Summarize Report
    # -----------------------------
    @task
    def report_summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_summarization_task'],  # type: ignore[index],

            # Save summary
            output_file='reports/report_summary_new.md',

            # Attach guardrail function
            guardrail=self.validate_word_count_for_summary,

            # Retry max 3 times if guardrail fails
            guardrail_max_retries=3
        )


    # -----------------------------
    # Create the Crew
    # -----------------------------
    @crew
    def crew(self) -> Crew:
        """
        This method assembles:
        - Agents
        - Tasks
        - Execution process
        """

        return Crew(
            agents=self.agents,  # Auto-collected by @agent
            tasks=self.tasks,    # Auto-collected by @task

            # Sequential means:
            # Task 1 runs → then Task 2 runs
            process=Process.sequential,

            verbose=True
        )