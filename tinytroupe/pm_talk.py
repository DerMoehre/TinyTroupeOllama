import logging
from tinytroupe.examples import create_petra_the_product_manager, create_leo_the_customer
from tinytroupe.environment import TinyWorld


# DISCLAIMER
print("""
!!!!
DISCLAIMER: TinyTroupe relies on Artificial Intelligence (AI) models to generate content.
The AI models are not perfect and may produce inappropriate or inaccurate results.
For any serious or consequential use, please review the generated content before using it.
!!!!
""")
# Step 1: Create the agents
petra = create_petra_the_product_manager()
leo = create_leo_the_customer()

# Step 2: Create the environment (TinyWorld) and add agents
world = TinyWorld("Meeting Room", [petra, leo])
world.make_everyone_accessible()

# Step 3: Define the initial user input to Lisa
petra.listen("""You are in a meeting with Leo, a potential customer. 
             Your task is to find out, what problems he needs to solve in his daily life 
             and how your product could help him to do so. 
             You want to understand the daily struggles he has and what work needs to be done.""")

# Step 4: Run the simulation for 4 steps
print("\nRunning the simulation...\n")
world.run(steps=4)