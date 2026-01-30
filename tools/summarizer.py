from langchain.tools import Tool
from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    """Summarize the given text and return the summary as a string."""
    try:
        summary = summarizer_pipeline(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"error: {e}"
    
summarizer_tool = Tool(
    name = "Text Summarizer",
    func=summarize_text,
    description="Useful for summarizing long pieces of text.")