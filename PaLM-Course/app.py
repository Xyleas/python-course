import project_charter
import risk_management
import project_plan
import os

api_key = os.environ.get('PATH_TO_API_KEY')

# Capture user input
product_idea = input('What would you like to build?:')

# Generate project charter
project_charter_text = project_charter.generate(api_key, product_idea)
#testing print(project_charter_text)
project_plan = project_plan.generate(api_key, project_charter_text)

risk_management_text = risk_management.generate(api_key, project_charter_text)

print(risk_management_text)