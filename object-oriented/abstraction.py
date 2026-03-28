# Detailed Reference
# https://www.geeksforgeeks.org/data-abstraction-in-python/

# Abstraction hides the internal implementation details while exposing only the necessary functionality.
# It helps focus on “what to do” rather than “how to do it.”

# Types of Abstraction:
# Partial Abstraction: Abstract class contains both abstract and concrete methods.
# Full Abstraction: Abstract class contains only abstract methods(like interfaces).

from abc import ABC, abstractmethod


class Browser(ABC):  # Abstract Class
    def __init__(self, version):
        self.version = version

    @abstractmethod
    def js_engine(self):  # Abstract Method
        pass

    def about(self):  # Concrete Method
        print(f"Browser's version: {self.version}")


class Chrome(Browser):  # Partial Abstraction
    def js_engine(self):
        self.engine = "v8"


class Firefox(Browser):  # Partial Abstraction
    def js_engine(self):
        self.engine = "spider-monkey"


browsers = [Chrome("123.45.1"), Firefox("44.23.4")]

for browser in browsers:
    browser.about()

chrome = Chrome("0.0.2")
print(chrome)
