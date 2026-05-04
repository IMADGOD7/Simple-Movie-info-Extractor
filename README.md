# Movie Information Extractor

A Generative AI-powered application that extracts structured information from movie descriptions using Mistral AI and LangChain.

## Features

- **AI-Powered Extraction**: Analyzes movie descriptions to extract key details like title, genre, characters, director, release year, summary, and themes.
- **Structured Output**: Returns information in JSON format using Pydantic models.
- **Web UI**: Clean Streamlit interface for easy interaction.
- **Command-Line Support**: Direct Python script execution.

## Tech Stack

- **Language**: Python
- **AI Model**: Mistral AI (via LangChain)
- **Frameworks**: LangChain, Streamlit, Pydantic
- **Dependencies**: See `requirements.txt`

## Setup

1. **Clone or Download** the project.

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set API Key**:
   - Create a `.env` file in the root directory.
   - Add your Mistral AI API key:
     ```
     MISTRAL_API_KEY=your_api_key_here
     ```

4. **Run the Application**:
   - **Web UI** (recommended):
     ```bash
     streamlit run streamlit_ui.py
     ```
   - **Command-Line**:
     ```bash
     python Cinesage/core.py
     ```
     Then enter a movie description when prompted.

## Usage

1. Enter a detailed movie description in the text area (web UI) or input prompt (CLI).
2. Click "Extract Information" (web UI) or press Enter (CLI).
3. View the extracted JSON data with fields like title, genre, main_characters, etc.


## Notes

- Ensure your Mistral AI API key is valid and has sufficient credits.
- The AI model (`mistral-small`) is used for extraction; adjust in `core.py` if needed.
- Output fields may be `null` if information is missing from the description.

## License

[Add license if applicable]
