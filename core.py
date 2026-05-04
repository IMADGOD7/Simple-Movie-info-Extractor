from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()


from langchain_mistralai import ChatMistralAI
model= ChatMistralAI( model="mistral-small")

class movie_info(BaseModel):
    title: List[str]
    genre: Optional[str]
    main_characters: Optional[List[str]]
    director: Optional[str]
    cast: Optional[List[str]]
    release_year: Optional[int]
    short_summary: List[str]
    themes: Optional[List[str]]

parser= PydanticOutputParser(pydantic_object=movie_info)

# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system",
#     """You are an expert movie analyst.
#
# Your task is to extract key information from a movie description.
#
# Return the output strictly in JSON format with these fields:
# - title
# - genre
# - main_characters
# - director
# - release_year
# - short_summary (2-3 lines)
# - themes
#
# Rules:
# - If a field is missing, return null
# - Do NOT make up information
# - Output only valid JSON, nothing else
# """),
#
#     ("human",
#     """Movie Paragraph:
#{movie_text}""")
# ])

chat_prompt = ChatPromptTemplate.from_messages([
    ("system",""" Extract information from the movie description {format_instruction} """),
    ("human","{paragraph}")
])

movie_description=input("Enter a movie description:")
real_prompt= chat_prompt.invoke({"paragraph": movie_description, "format_instruction": parser.get_format_instructions()})
response=model.invoke(real_prompt)
print(response.content)