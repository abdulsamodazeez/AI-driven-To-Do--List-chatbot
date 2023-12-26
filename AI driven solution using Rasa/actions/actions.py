from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionCreateList(Action):
    def name(self) -> Text:
        return "action_create_list"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Create a new list for the user
        return [SlotSet("user_list", [])]

class ActionAddItem(Action):
    def name(self) -> Text:
        return "action_add_item"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the task from user input
        task = tracker.latest_message.get("text")

        if task:
            # Extract the task name
            #task_name = task.split(" ")[]  # Example extraction method

            # Retrieve the user's list
            user_list = tracker.get_slot("user_list") or []

            # Add the task name to the list
            #user_list.append(task_name)

            dispatcher.utter_message(f"Added '{task}' to your list.")
        else:
            dispatcher.utter_message("Please specify a task to add.")

        return [SlotSet("user_list", user_list)]  # Set the updated slot value

class ActionRemoveItem(Action):
    def name(self) -> Text:
        return "action_remove_item"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the task from user input
        task = tracker.latest_message.get("text")

        if task:
            # Retrieve the user's list
            user_list = tracker.get_slot("user_list") or []

            # Remove the task from the list
            if task in user_list:
                user_list.remove(task)
                dispatcher.utter_message(f"Removed '{task}' from your list.")
            else:
                dispatcher.utter_message(f"'{task}' is not in your list.")
        else:
            dispatcher.utter_message("Please specify a task to remove.")

        return [SlotSet("user_list", user_list)]  # Set the updated slot value


class ActionShowList(Action):
    def name(self) -> Text:
        return "action_show_list"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve the user's list
        user_list = tracker.get_slot("user_list") or []

        if user_list:
            task_list_str = "\n".join(user_list)
            dispatcher.utter_message(f"Your to-do list:\n{task_list_str}")
        else:
            dispatcher.utter_message("Your list is empty.")

        return []

class ActionMarkDone(Action):
    def name(self) -> Text:
        return "action_mark_done"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the task from user input
        task = tracker.latest_message.get("text")

        if task:
            # Retrieve the user's list
            user_list = tracker.get_slot("user_list") or []

            # Mark the task as done (you can implement additional logic here)
            dispatcher.utter_message(f"'{task}' marked as done.")
        else:
            dispatcher.utter_message("Please specify a task to mark as done.")

        return []
