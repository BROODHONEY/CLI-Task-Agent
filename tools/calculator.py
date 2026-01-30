from langchain.tools import Tool

def calculate(expression: str) -> str:
    """Evaluate a mathematical expression and return the result as a string."""
    try:
        # Safely evaluate the expression
        return str(eval(expression))
    except Exception as e:
        return f"error: {e}"
    
calculator_tool = Tool(
    name = "Calculator",
    func=calculate,
    description="Useful for when you need to perform mathematical calculations. Input should be a valid mathematical expression.")
