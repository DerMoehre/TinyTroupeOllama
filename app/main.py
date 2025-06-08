# simple_chat_demo.py
import logging
from tinytroupe.examples import create_lisa_the_data_scientist, create_oscar_the_architect
from tinytroupe.environment import TinyWorld

# Optional: Configure logging level for debugging
logging.basicConfig(level=logging.INFO)

# DISCLAIMER
print("""
!!!!
DISCLAIMER: TinyTroupe relies on Artificial Intelligence (AI) models to generate content.
The AI models are not perfect and may produce inappropriate or inaccurate results.
For any serious or consequential use, please review the generated content before using it.
!!!!
""")

# Step 1: Create the agents
lisa = create_lisa_the_data_scientist()
oscar = create_oscar_the_architect()

# Step 2: Create the environment (TinyWorld) and add agents
world = TinyWorld("Chat Room", [lisa, oscar])
world.make_everyone_accessible()

# Step 3: Define the initial user input to Lisa
lisa.listen("Oscar has been telling the others at the office that you have been contracting out your work to someone in a different country. This is risking your job and you need to confront him and tell him that this needs to stop. He is very passive aggressive and will make it seem like he is apologetic and will stop, but he is lying and needs to be called out. Even if it's true, no one should know.")

# Step 4: Run the simulation for 4 steps
print("\nRunning the simulation...\n")
world.run(steps=4)

# No need for Step 5 (history printing) since the conversation 
# is already displayed during the simulation run