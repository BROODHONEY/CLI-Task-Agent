from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from agent import create_agent

def main():
    hf_pipeline = pipeline(
        "text-generation",
        model="gpt2",
        max_new_tokens=512
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    agent = create_agent(llm)

    while True:
        task = input("Enter a task for the agent (or 'exit' to quit): ")
        if task.lower() == 'exit':
            break

        result = agent.run(task)
        print(f"Agent's response: {result}\n")

if __name__ == "__main__":
    main()