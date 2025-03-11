import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
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
  system_instruction="Act as a senior game developers and designer.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Create an idea for a {{game_genre}} game about {{topic}} that can be developed in {{time_to_develop}}.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, let's brainstorm a game idea!  I'm putting on my senior dev and design hats. To give you the best concept, I'll need a bit more information. \n\nFirst, please fill in the following:\n\n*   **{{game_genre}}:** (e.g., RPG, Strategy, Platformer, Puzzle, Simulation, etc.)\n*   **{{topic}}:** (e.g., space exploration, ancient civilizations, cooking, managing a zoo, etc.)\n*   **{{time_to_develop}}:** (e.g., 6 months, 1 year, a weekend, etc.) - *Be realistic about the timeframe*\n\nOnce I have that, I can create a detailed idea, outlining core mechanics, a target audience, a compelling hook, and considerations for the development timeline you've given. I will make sure to consider your constraints.\n\n**In the meantime, here are some example ideas to show you the kind of detail you can expect:**\n\n**Example 1 (Short Dev Time):**\n\n*   **{{game_genre}}:**  Simple Arcade Puzzle\n*   **{{topic}}:**  Sorting Vintage Vinyl Records\n*   **{{time_to_develop}}:** A Weekend (approx. 48 hours)\n\n    *   **Concept:** A fast-paced puzzle game where the player sorts virtual vinyl records into different categories (e.g., genre, era, artist) as they scroll down a conveyor belt.\n    *   **Core Mechanics:** Tap/click or drag and drop to sort. Timer-based challenge. Increasing speed and complexity.\n    *   **Target Audience:** Casual players, puzzle fans, music enthusiasts.\n    *   **Hook:** Simple, addictive gameplay with a vintage aesthetic, and a \"just one more try\" feeling.\n    *   **Development Notes:** Focus on a single core mechanic, simple art style, and sound effects. Minimal UI/UX needed. Possible high-score functionality.\n\n**Example 2 (Medium Dev Time):**\n\n*   **{{game_genre}}:**  Light Strategy/Management Simulation\n*   **{{topic}}:**  Running a Fantasy Bakery\n*   **{{time_to_develop}}:** 6 Months\n\n    *   **Concept:** A charming management game where the player builds and runs a bakery in a fantasy world, crafting magical treats for unique clientele.\n    *   **Core Mechanics:** Resource management, recipe crafting using whimsical ingredients, hiring and managing staff, fulfilling orders, expanding the bakery, research and new recipe discovery, light story elements.\n    *   **Target Audience:**  Players who enjoy casual strategy, management games, and charming aesthetics.\n    *   **Hook:** The satisfying loop of crafting and selling magical baked goods, combined with a lighthearted fantasy setting.\n    *   **Development Notes:** Would need well designed UI and a progression system. Requires attention to both the art style and sound. Should have a clear progression, but it doesn't need to be infinitely scalable. \n\n**Example 3 (Long Dev Time):**\n\n*   **{{game_genre}}:**  Action-Adventure RPG\n*   **{{topic}}:**  Exploring a City Built Inside a Giant Clockwork Mechanism\n*   **{{time_to_develop}}:** 1 Year+\n\n    *   **Concept:** An action RPG where the player explores a vast city built inside a giant clockwork mechanism. The player is trying to stop the mechanism from failing.\n    *   **Core Mechanics:** Combat using unique clockwork-inspired weapons, puzzles based on manipulating gears and cogs, exploration of vertical levels, character customization and progression, a branching storyline with multiple endings.\n    *   **Target Audience:** RPG fans, players who enjoy exploration and engaging combat, and those who like mystery and complex stories.\n    *   **Hook:** Unique setting, engaging combat, compelling storyline, character customization.\n    *   **Development Notes:** Requires a larger team, in-depth level design, well-developed combat system, a complex storyline, voice acting, and well-developed AI. Will need strong project management.\n\nOkay, I'm ready for your input! Let me know your desired genre, topic, and development time, and let's design your game.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)