import random

# List of fun facts
fun_facts = [
    "Honey never spoils.",
    "Bananas are berries, but strawberries aren't.",
    "A day on Venus is longer than a year on Venus.",
    "Octopuses have three hearts.",
    "Humans share 50% of their DNA with bananas.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "A single cloud can weigh more than a million pounds.",
    "A group of flamingos is called a 'flamboyance.'",
    "There's enough DNA in the human body to stretch from the sun to Pluto and back—17 times.",
    "Sharks have been around longer than trees."
]

# Select a random fun fact
selected_fact = random.choice(fun_facts)

# Read the current README.md file
with open("README.md", "r") as file:
    readme_content = file.read()

# Define the section markers
start_marker = "<!-- FUN_FACT_SECTION -->"
end_marker = "<!-- END_FUN_FACT_SECTION -->"

# Replace the placeholder with the new fun fact
new_readme_content = readme_content.split(start_marker)[0] + start_marker + "\n\n" + selected_fact + "\n\n" + end_marker + readme_content.split(end_marker)[1]

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.write(new_readme_content)
