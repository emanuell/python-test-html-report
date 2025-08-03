class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def validate_email(email):
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    return len(parts[0]) > 0 and len(parts[1]) > 0


def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def process_list(items):
    if not items:
        return []
    return [item.upper() if isinstance(item, str) else item for item in items]