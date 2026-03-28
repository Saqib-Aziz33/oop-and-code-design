# A class should have only one reason to change.
# 1 class = 1 Job


# ===================================== BAD Example
"""
This class has 3 responsibilities:

1. Generate report
2. Save to file
3. Send email
"""


class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.generate())

    def send_email(self, email):
        print(f"Sending email to {email} with report")


# ===================================== GOOD Example
"""
✔️ Now:
Report → only generates data
FileSaver → only handles file I/O
EmailSender → only handles email sending
🔍 Real-World Analogy

Think of a restaurant kitchen:

👨‍🍳 Chef → cooks food
🧾 Cashier → handles billing
🚚 Delivery person → delivers food

If the chef also had to deliver food and manage billing → chaos.
"""


class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report: {self.data}"


class FileSaver:
    def save(self, content, filename):
        with open(filename, "w") as f:
            f.write(content)


class EmailSender:
    def send(self, content, email):
        print(f"Sending email to {email} with content:\n{content}")
