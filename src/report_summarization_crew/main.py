#!/usr/bin/env python

# Import the crew class we defined
from report_summarization_crew.crew import ReportSummarizationCrew


def run():
    """
    This function starts the crew execution.
    """

    # Inputs that will replace {field} in YAML files
    inputs = {
        'field': 'Education'
    }

    # Create crew object
    my_crew = ReportSummarizationCrew().crew()

    # Start execution
    result = my_crew.kickoff(inputs=inputs)

    # If something fails during execution, catch it
    try:
        result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# Standard Python entry point
if __name__ == "__main__":
    run()