import time

class StudyBuddy:
    def __init__(self, user_name):
        self.user_name = user_name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"[+] Task '{task}' added for {self.user_name}.")

    def show_tasks(self):
        print(f"\n--- Task List for {self.user_name} ---")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def generate_study_summary(self, topic):
        print(f"\n[AI] Generating study summary for: {topic}...")
        time.sleep(1)
        return f"Summary for {topic}: Focus on key concepts and practice regularly."

if __name__ == "__main__":
    buddy = StudyBuddy("Student")
    buddy.add_task("Review Python Basics")
    buddy.add_task("Prepare for Hackathon")
    buddy.show_tasks()
    
    summary = buddy.generate_study_summary("Machine Learning Basics")
    print(summary)
