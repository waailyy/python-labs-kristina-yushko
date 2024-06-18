from datetime import date, timedelta
import json

class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes="", duration=0, recurrence=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence

    def is_due_today(self):
        return self.due_date == date.today()

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
            'status': self.status,
            'priority': self.priority,
            'notes': self.notes,
            'duration': self.duration,
            'recurrence': self.recurrence
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data['title'],
            description=data['description'],
            due_date=date.fromisoformat(data['due_date']),
            status=data.get('status', 'Pending'),
            priority=data.get('priority', 'Medium'),
            notes=data.get('notes', ''),
            duration=data.get('duration', 0),
            recurrence=data.get('recurrence')
        )

    def __repr__(self):
        return (f"Task(title={self.title!r}, description={self.description!r}, due_date={self.due_date}, "
                f"status={self.status!r}, priority={self.priority!r}, notes={self.notes!r}, duration={self.duration}, recurrence={self.recurrence!r})")

class Schedule:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(('added', task))

    def remove_task(self, task_title):
        task = self.get_task(task_title)
        if task:
            self.tasks.remove(task)
            self.history.append(('removed', task))

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.due_date < date.today() and task.status != 'Completed']

    def list_tasks_due_today(self):
        return [task for task in self.tasks if task.is_due_today() and task.status != 'Completed']

    def sort_tasks_by_due_date(self):
        return sorted(self.tasks, key=lambda task: task.due_date)

    def update_task(self, task_title, **kwargs):
        task = self.get_task(task_title)
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            self.history.append(('updated', task))

    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
            self.history.append(('completed', task))

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status == 'Completed']

    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]

    def check_deadlines(self):
        tomorrow = date.today() + timedelta(days=1)
        return [task for task in self.tasks if task.due_date == tomorrow]

    def list_all_tasks(self):
        return self.tasks

    def list_tasks_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self):
        return self.history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != 'Completed']

    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self):
        total_tasks = len(self.tasks)
        completed_tasks = len(self.list_completed_tasks())
        return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0.0

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            self.tasks = [Task.from_dict(data) for data in tasks_data]
            self.history.append(('loaded', filename))

# Example usage
if __name__ == "__main__":
    task1 = Task(
        title="Buy groceries",
        description="Milk, Bread, Eggs",
        due_date=date.today() - timedelta(days=1)
    )
    task2 = Task(
        title="Prepare breakfast",
        description="Use groceries to prepare breakfast",
        due_date=date.today() + timedelta(days=2)
    )
    schedule = Schedule()
    schedule.add_task(task1)
    schedule.add_task(task2)
    