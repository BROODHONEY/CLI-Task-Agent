from langchain.tools import Tool

def read_file(file_path: str) -> str:
    """Read the contents of a file and return it as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"error: {e}"
    
file_reader_tool = Tool(
    name = "File Reader",
    func=read_file,
    description="Useful for reading the contents of a file. Input should be the file path as a string.")