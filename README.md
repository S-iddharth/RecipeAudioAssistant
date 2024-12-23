
# Recipe Audio Assistant

## Overview
The Recipe Audio Assistant is a user-friendly web application designed to guide users through the cooking process step by step. It generates natural language explanations for each step of the recipe and suggests ingredient substitutions when needed, ensuring a seamless cooking experience.

---

## Features

- **Step-by-step Cooking Guidance**
  - Provides clear instructions for each step in the recipe.

- **Ingredient Substitution Suggestions**
  - Offers alternative ingredients in case the required ones are unavailable.

- **Interactive User Interface**
  - Streamlit-based interface for ease of use and accessibility.

- **Natural Language Explanations**
  - Powered by GPT-2, the system generates human-like explanations for cooking steps.

---

## Tech Stack

### Frontend:
- **Streamlit**: For building the interactive web-based UI.

### Backend:
- **TensorFlow GPT-2**: For generating instructions and explanations.
- **ChromaDB**: A vector database used for storing and retrieving recipe data efficiently.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/recipe-audio-assistant.git
   cd recipe-audio-assistant
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Select a Recipe**:
   - Use the sidebar to choose from available recipes.

2. **Follow Step-by-Step Instructions**:
   - View and interact with each step.

3. **Request Explanations**:
   - Click the "Explain" button to get detailed guidance for any step.

4. **Get Substitution Suggestions**:
   - Use the "Ingredient Substitutions" button for alternative ingredients.

---

## Deployment

The application can be deployed on Azure using Azure App Service. Ensure the following:
- All required dependencies are included in your environment.
- Audio playback is supported if needed for future enhancements.

---

## Evaluation

### Key Metrics:
- **Instruction Clarity**: Rate how well the steps are explained.
- **Substitution Relevance**: Evaluate the accuracy and relevance of ingredient alternatives.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---

## Contact
For any inquiries or feedback, please reach out to [your-email@example.com].
