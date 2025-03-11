import google.generativeai as genai
from Markdown2docx import Markdown2docx

# Capture user input
#reorganized product_idea = input('What would you like to build?:')

def generate(api_key, product_idea):

  # Create the model
  genai.configure(api_key= api_key)

  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }



  model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
  )

  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          "Act as a senior project manager with vast experience in software development. Write a brief Project Charter document for our product idea. The Project Charter should include the following sections:\n\nProject Title and Description\n\nProject Purpose or Justification\n\nObjectives and Constraints\n\nScope Description\n\nProject Deliverables\n\nProject Budget\n\nStakeholder Identification\n\nHigh-Level Risks and Assumptions\n\nOur product idea is: {{product idea}}\n\nNow please write the Project Charter with the 8 sections mentioned above:",
        ],
      },
      {
        "role": "model",
        "parts": [
          "Okay, I understand. Let's get this Project Charter drafted. Based on the product idea you provide, I will fill in the specifics. Here's the template, followed by an example, and then I will be ready for you to tell me what your product idea is so we can fill it in:\n\n**Project Charter Template**\n\n**1. Project Title and Description**\n\n*   **Project Title:**  [Project Name - Concise and clear]\n*   **Project Description:** [A brief overview of what the project is about, its core functionality, and what it aims to achieve.]\n\n**2. Project Purpose or Justification**\n\n*   **Purpose:** [The reason for undertaking the project. What problem does it solve, or what opportunity does it address?]\n*   **Justification:** [Why is this project important?  How does it align with the company's strategy and goals? What are the potential benefits?]\n\n**3. Objectives and Constraints**\n\n*   **Objectives (SMART):** [Specific, Measurable, Achievable, Relevant, Time-bound goals for the project.]\n*   **Constraints:** [Limitations on the project, such as budget, time, resources, technical limitations, or legal restrictions.]\n\n**4. Scope Description**\n\n*   **In Scope:** [What features and functionalities will be included in this project.]\n*   **Out of Scope:** [What features and functionalities will *not* be included in this project.]\n\n**5. Project Deliverables**\n\n*   [A list of specific, tangible outputs of the project. This includes software, documentation, test cases, reports etc.]\n\n**6. Project Budget**\n\n*   **Estimated Budget:** [A preliminary budget range for the entire project. This may include personnel, software licenses, infrastructure, and other costs.]\n\n**7. Stakeholder Identification**\n\n*   **Key Stakeholders:** [List of key individuals and groups that have an interest or influence in the project, including project team members, end users, business owners, and sponsors.]\n\n**8. High-Level Risks and Assumptions**\n\n*   **High-Level Risks:** [Potential risks that could negatively impact the project's success, including technical challenges, budget overruns, resource constraints, and market changes.]\n*   **Assumptions:** [Assumptions being made about the project environment, for example: technology compatibility, availability of third-party services, market trends, or customer adoption rates.]\n\n**Example (using a hypothetical idea: a mobile task management app):**\n\n**1. Project Title and Description**\n\n*   **Project Title:** Mobile Task Management Application Development\n*   **Project Description:** This project aims to develop a mobile application for iOS and Android platforms to enable users to efficiently manage their tasks, set reminders, categorize activities, and collaborate with others on shared task lists.\n\n**2. Project Purpose or Justification**\n\n*   **Purpose:** To provide a user-friendly mobile solution for personal and team task management, improving productivity and collaboration.\n*   **Justification:**  There is a growing need for effective task management solutions that are easily accessible on mobile devices. This app will fill a gap in the market, enhance user experience, and potentially generate revenue through subscriptions or premium features.\n\n**3. Objectives and Constraints**\n\n*   **Objectives:**\n    *   Develop a functioning mobile app for iOS and Android platforms within 6 months.\n    *   Achieve a user satisfaction rating of 4 out of 5 stars within the first 3 months after launch.\n    *   Secure 1000 active users within the first month of launch.\n*   **Constraints:**\n    *   Budget limit of $150,000\n    *   Development team of 5 developers and 2 QA engineers.\n    *   Limited access to certain third-party APIs.\n\n**4. Scope Description**\n\n*   **In Scope:**\n    *   User authentication and profile management.\n    *   Task creation, editing, and deletion.\n    *   Task prioritization and due date setting.\n    *   Task categorization using tags or categories.\n    *   Push notification reminders.\n    *   Basic task sharing and collaboration features.\n    *   iOS and Android app compatibility.\n*   **Out of Scope:**\n    *   Integration with complex project management software.\n    *   Advanced reporting and analytics.\n    *   Cross-platform desktop application.\n\n**5. Project Deliverables**\n\n*   iOS and Android mobile application.\n*   User documentation.\n*   Test cases and results.\n*   Deployment and release plan.\n\n**6. Project Budget**\n\n*   **Estimated Budget:** $140,000 - $150,000\n\n**7. Stakeholder Identification**\n\n*   **Key Stakeholders:**\n    *   Project Sponsor (Executive Management)\n    *   Project Manager\n    *   Development Team\n    *   QA Engineers\n    *   Potential End Users\n    *   Marketing Team\n\n**8. High-Level Risks and Assumptions**\n\n*   **High-Level Risks:**\n    *   Technical challenges with integrating third-party services.\n    *   Potential delays in development due to resource constraints.\n    *   Competitor market entry.\n*   **Assumptions:**\n    *   The availability of necessary iOS and Android development tools.\n    *   Adequate user interest and adoption rate.\n    *   Stable internet connectivity for app functionality.\n\n---\n\n**Now, tell me your product idea so we can fill this out for *your* specific project! I'm ready when you are.**\n",
        ],
      },
    ]
  )

  response = chat_session.send_message("INSERT_INPUT_HERE")

  print(response.text)

  # Save response as Word Document
  #testing print(repsonse.result)
  my_file = open('project_charter.md', 'w')
  my_file.write(response.result)
  my_file.close()

  word_file = Markdown2docx('project_charter')
  word_file.eat_soup()
  word_file.save()

  return response.result