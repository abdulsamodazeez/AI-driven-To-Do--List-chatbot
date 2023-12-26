import re

class ToDoChatbot:
    def __init__(self):
        self.name = "ToDoBot"
        self.lists = {}  # Dictionary to store lists (name: tasks)

    def create_list(self, list_name):
        if list_name not in self.lists:
            self.lists[list_name] = []
            return f"Created a new to-do list named '{list_name}'."
        else:
            return f"A list named '{list_name}' already exists."

    def add_task(self, list_name, task):
        if list_name in self.lists:
            self.lists[list_name].append(task)
            return f"Added '{task}' to your '{list_name}' list."
        else:
            return f"No list named '{list_name}' found. Please create it first."

    def remove_task(self, list_name, task):
        if list_name in self.lists and task in self.lists[list_name]:
            self.lists[list_name].remove(task)
            return f"Removed '{task}' from your '{list_name}' list."
        else:
            return f"'{task}' is not in your '{list_name}' list or the list does not exist."

    def display_list(self, list_name):
        if list_name in self.lists:
            return "\n".join(self.lists[list_name]) or "The list is currently empty."
        else:
            return f"No list named '{list_name}' found."

    def respond(self, user_input):
        create_match = re.match(r"create a (new )?list name it ['\"]?(.*?)['\"]?$", user_input, re.IGNORECASE)
        if create_match:
            list_name = create_match.group(2)
            return self.create_list(list_name)

        add_match = re.match(r"add ['\"]?(.*?)['\"]? to ['\"]?(.*?)['\"]?$", user_input, re.IGNORECASE)
        if add_match:
            task, list_name = add_match.groups()
            return self.add_task(list_name, task)

        remove_match = re.match(r"remove ['\"]?(.*?)['\"]? from ['\"]?(.*?)['\"]?$", user_input, re.IGNORECASE)
        if remove_match:
            task, list_name = remove_match.groups()
            return self.remove_task(list_name, task)

        display_match = re.match(r"show ['\"]?(.*?)['\"]?$", user_input, re.IGNORECASE)
        if display_match:
            list_name = display_match.group(1)
            return self.display_list(list_name)

        return "I'm sorry, I didn't understand. Please use commands like 'create a list named', 'add', 'remove', or 'display'."

# Create an instance of the chatbot
chatbot = ToDoChatbot()

while True:
    user_input = input(f"User Input: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"{chatbot.name}: {response}")
