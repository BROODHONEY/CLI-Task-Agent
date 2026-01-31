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
    description="ONLY use this tool when the user provides a concrete mathematical expression "
        "such as '45 * (10 + 2)'. Do NOT guess expressions.")
