"""Receive and reply to emails."""
from robocorp.tasks import task
from robocorp import workitems
import json

@task
def minimal_task():
    print("Starting.")

    # Loop through input work items, there should be only emails in them.
    # There most likely should be only one item and one email, 
    # but we'll handle multiple just in case.
    for item in workitems.inputs:

        print("Processing work item:", item)

        try:
            email = item.email()

            print("Email sent by:", email.from_.address)
            print("Email subject:", email.subject)
            print("Email body:", email.text)
        except Exception as e:
            print(f"Error: {e}")

