# LinkedIn Post Generator 

## Overview
The **Lyzr LinkedIn Post Generator** is a Streamlit-based application designed to automate the creation and publishing of LinkedIn posts. Powered by **Lyzr Agent API**, this tool uses AI-driven strategies to generate professional, engaging, and impactful LinkedIn posts. The app streamlines the process by leveraging advanced features such as contextual analysis, keyword optimization, and tool calling for direct publishing.

---

## Features
- **AI-Powered LinkedIn Post Creation**:
  - Generate engaging headlines and structured content.
  - Enhance visibility through trending keyword research.
  - Create professional LinkedIn posts with user-provided text and image URLs.

- **Streamlined Publishing**:
  - Automatically publish LinkedIn posts using the integrated `post_image_and_text_linkedin` tool.
  - Ensure posts are grammatically correct and visually appealing.

- **User-Friendly Interface**:
  - Simple text input field for post content and image URLs.
  - Easy-to-use "Generate" button for quick results.

---

## Installation

### Prerequisites
- **Python**: Ensure Python 3.8 or higher is installed.
- **Dependencies**: Install required packages via `requirements.txt`.
- **API Keys**: Obtain the following keys:
  - **Lyzr API Key**
  - **OpenAI API Key**

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lyzr-linkedin-generator.git
   cd lyzr-linkedin-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API Keys:
   - Create a `.env` file in the project directory.
   - Add your API keys:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     LYZR_API_KEY=your_lyzr_api_key
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## Usage

1. **Input Post Content**:
   - Provide the textual content and relevant image URL for your LinkedIn post in the text area.
2. **Generate Post**:
   - Click the "Generate" button to create and publish your post.
3. **Review Results**:
   - The generated LinkedIn post will be displayed in the app interface.

---

## File Structure
```
lyzr-linkedin-generator/
│
├── app.py                  # Main application file
├── LyzrAgent.py            # Custom class for Lyzr Agent integration
├── requirements.txt        # Python dependencies
├── .env                    # Environment file for storing API keys
├── logo/                   # Directory for logo assets
│   ├── lyzr-logo.png
│   ├── lyzr-logo-cut.png
```

---

## Key Functionalities

### 1. **Agent Creation**
- Initializes a Lyzr environment and agent for LinkedIn post generation and publishing.

### 2. **AI-Driven Content Generation**
- Leverages OpenAI GPT models for crafting LinkedIn posts based on user input.

### 3. **Automated Publishing**
- Directly publishes the generated LinkedIn posts using Lyzr tools.

---

## Dependencies
- **Streamlit**: Interactive UI framework.
- **dotenv**: For managing environment variables.
- **Lyzr Agent API**: Integration for creating and managing agents.
- **Python (>=3.8)**

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments
- Built using the **Lyzr Agent API**.
- Designed for professionals seeking to streamline LinkedIn post creation and publishing.

---
