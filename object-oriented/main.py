# The 4 pillars of object-oriented programming (OOP) in Python (and generally in programming) are:
# Encapsulation: Bundling data (attributes) and methods (functions) that operate on the data into a single unit (class).
# Abstraction: Hiding complex implementation details and providing a simplified interface.
# Inheritance: Allowing a class to inherit attributes and methods from another class, promoting code reuse.
# Polymorphism: Using a single interface to represent different data types or objects.


class Browser:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.history = []

    def about(self):
        print(f"Name: {self.name} \nVersion: {self.version} \n.........")

    def deleteHistory(self):
        print("Deleting history☠️☠️\n.........")
        self.history = []

    def showHistory(self):
        print("Latest Visits:")
        for i in range(len(self.history)):
            print(self.history[i])
        print(".........")

    def goto(self, url):
        self.history.append(url)
        print(f"visiting {url}\n.........")


chrome = Browser("Google Chrome", "121.214.366")
chrome.about()
chrome.goto("https://google.com")
chrome.goto("https://youtube.com")
chrome.showHistory()

chrome.deleteHistory()
chrome.showHistory()
