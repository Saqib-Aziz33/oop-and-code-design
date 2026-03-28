# Software entities (classes, modules, functions) should be:

# Open for extension
# Closed for modification

# 👉 You should be able to add new behavior without changing existing code.


# ===================================== BAD Example
"""
Every time you add a new customer type:

1. You must modify this class
2. Risk breaking existing logic
3. Violates OCP
"""


from abc import ABC, abstractmethod


class DiscountCalculator:
    def calculate(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.9
        elif customer_type == "premium":
            return amount * 0.8
        elif customer_type == "vip":
            return amount * 0.7


# ===================================== GOOD Example
"""
We use polymorphism + abstraction.
🎉 Now:
Add new discount → create new class
❌ No modification to existing code
✅ Fully extensible
🔍 Real-World Analogy

Think of a mobile charger system:

Wall socket (fixed, stable)
You plug in different chargers (USB-C, Lightning, etc.)

👉 You extend behavior by plugging in, not by changing the wall.

🎯 Purpose of OCP
Prevent breaking existing code
Enable scalability
Make systems flexible for future features
🧩 Where You Use It

You apply OCP when:

Business rules change often
You expect new variations (types, behaviors)
You want plug-and-play architecture

"""


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass


class RegularDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.9


class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.8


class VIPDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.7


class DiscountCalculator:
    def calculate(self, strategy: DiscountStrategy, amount):
        return strategy.apply_discount(amount)


def main():
    calculator = DiscountCalculator()

    result = calculator.calculate(VIPDiscount(), 100)
    print(result)  # 70


if __name__ == "__main__":
    main()
