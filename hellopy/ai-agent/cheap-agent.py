import os
import json
from openai import OpenAI

# 1. Initialize the client (Using Groq for blazing fast, free/cheap tokens)
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="gsk_..."  # Replace with your actual Groq API key
)

# 2. Define our "Tools" (Just standard Python functions)
def calculate(expression: str) -> str:
    """Evaluates a mathematical expression safely."""
    try:
        # Note: eval is used here purely for a simple demo; do not use on untrusted inputs
        print("---------------- evaluating: --------------------")
        print( expression)
        return str(eval(expression))
    except Exception as e:
        return f"Error evaluating expression: {e}"

# Map tool names to actual functions
AVAILABLE_TOOLS = {
    "calculate": calculate
}

# 3. Create the System Prompt (The rules of the agentic loop)
SYSTEM_PROMPT = """
You are a helpful AI Agent operating in a loop: Thought, Action, PAUSE, Observation.

You have access to the following tools:
- calculate: Takes a math string expression and evaluates it. E.g., calculate: 2+2

Process:
1. You receive a user prompt.
2. Formulate a Thought about what to do.
3. If you need a tool, output 'Action: tool_name: argument' and then PAUSE on a new line. Do not write anything else.
4. If you have the final answer, output 'Answer: [your final answer]'.

Example Session:
User: What is 45 * 12?
Thought: I need to multiply 45 by 12. I will use the calculate tool.
Action: calculate: 45 * 12
PAUSE

Observation: 540

Thought: I now have the result.
Answer: 45 multiplied by 12 is 540.
"""

def run_agent_loop(user_prompt: str):
    # Initialize the conversation history with the system rules
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    print(f"🚀 Starting Agent for prompt: '{user_prompt}'\n")

    # Run the loop up to 5 times to prevent infinite loops if the LLM gets confused
    for turn in range(5):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", # Changed from 'mixtral-8x7b-32768' to 'llama3-8b-8192'
            messages=messages,
            temperature=0.0
        )

        ai_response = response.choices[0].message.content
        print(f"+++ Turn {turn + 1} +++")
        print(ai_response)

        # Append the AI's thoughts/actions to history
        messages.append({"role": "assistant", "content": ai_response})

        # breakpoint()
        # Check if the agent wants to give the final answer
        if turn > 0 and "Answer:" in ai_response:
            # breakpoint()
            print("\n✅ Task completed successfully!")
            break

        # breakpoint()

        # Check if the agent is trying to call a tool
        if "Action:" in ai_response:
            # breakpoint()
            # Parse out the action details
            # Expected format: "Action: calculate: 45 * 12"
            try:
                # breakpoint()
                line = [l for l in ai_response.split('\n') if "Action:" in l][0]
                parts = line.replace("Action:", "").strip().split(":")
                # breakpoint()
                tool_name = parts[0].strip()
                tool_arg = parts[1].strip()

                print('++++++++++ +++++++', line, parts, tool_name, tool_arg)

                if tool_name in AVAILABLE_TOOLS:
                    print(f"\n⚙️  Executing tool '{tool_name}' with argument '{tool_arg}'...")
                    # Run the Python tool
                    observation = AVAILABLE_TOOLS[tool_name](tool_arg)
                    print(f"📊 Observation: {observation}\n")

                    # Feed the result back to the LLM
                    messages.append({"role": "user", "content": f"Observation: {observation}"})
                else:
                    messages.append({"role": "user", "content": f"Observation: Error - Tool '{tool_name}' doesn't exist."})
            except Exception as e:
                messages.append({"role": "user", "content": f"Observation: Error parsing your action format."})

# 4. Run the Agent
if __name__ == "__main__":
    prompt = "Take the number of days in a leap year, multiply it by 15, and then add 100."
    run_agent_loop(prompt)