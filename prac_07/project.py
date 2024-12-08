from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def is_completed(self):
        return self.completion_percentage == 100