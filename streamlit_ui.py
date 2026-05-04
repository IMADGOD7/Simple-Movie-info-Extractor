import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

# ----------------- Setup -----------------
load_dotenv()
model = ChatMistralAI(model="mistral-small")

class movie_info(BaseModel):
    title: List[str]
    genre: Optional[str]
    main_characters: Optional[List[str]]
    director: Optional[str]
    cast: Optional[List[str]]
    release_year: Optional[int]
    short_summary: List[str]
    themes: Optional[List[str]]

parser = PydanticOutputParser(pydantic_object=movie_info)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract information from the movie description. {format_instruction}"),
    ("human", "{paragraph}")
])

# ----------------- UI Config -----------------
st.set_page_config(page_title="Movie Extractor", page_icon="🎬", layout="centered")

# Custom CSS (clean card UI)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .box {
        padding: 20px;
        border-radius: 12px;
        background-color: #161b22;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.markdown("<h1 style='text-align: center;'>🎬 Movie Info Extractor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Paste a movie description and get structured insights</p>", unsafe_allow_html=True)

# ----------------- Input Box -----------------
st.markdown("<div class='box'>", unsafe_allow_html=True)
movie_description = st.text_area("Movie Description", height=180, placeholder="Enter movie plot here...")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Button -----------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    run = st.button("✨ Extract Info", use_container_width=True)

# ----------------- Output -----------------
if run:
    if movie_description.strip() == "":
        st.warning("Please enter a movie description.")
    else:
        with st.spinner("Analyzing movie..."):
            real_prompt = chat_prompt.invoke({
                "paragraph": movie_description,
                "format_instruction": parser.get_format_instructions()
            })

            response = model.invoke(real_prompt)

            try:
                parsed = parser.parse(response.content)

                st.markdown("<div class='box'>", unsafe_allow_html=True)
                st.subheader("📊 Extracted Information")
                st.json(parsed.dict())
                st.markdown("</div>", unsafe_allow_html=True)

            except:
                st.error("Failed to parse response. Try again.")