from google.adk.agents import Agent
from .tools import categorize_ingredients, estimate_budget

root_agent = Agent(
    name="recipe_agent",
    model="gemini-2.5-flash",
    description="AI Recipe Agent",
    instruction="""
    You are an intelligent recipe agent.

    The user will provide ingredients.

    Your tasks:
    1. Understand the ingredients.
    2. Use categorize_ingredients to understand food groups.
    3. Decide the most suitable recipe using Gemini reasoning.
    4. Use estimate_budget to estimate the cost.
    5. Explain why the recipe was chosen.
    6. Provide step-by-step cooking instructions.

    Do not use a predefined recipe database.
    Use your own reasoning to create or suggest recipes.
    Keep the answer simple and practical.
    """,
    tools=[
        categorize_ingredients,
        estimate_budget
    ]
)