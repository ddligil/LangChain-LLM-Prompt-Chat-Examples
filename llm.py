from dotenv import load_dotenv

load_dotenv()

from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "give a {gender} name in {language}."
)

prompt_template.format(
    gender = "girl",
    language = "Turkish",
)
print(prompt_template.format(gender="girl", language="Turkish"))

#give a girl name in Turkish.


from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
response = llm.invoke("what is the capital of Spain")
print(response.content)

#The capital of Spain is Madrid.


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_template(
    "Give a {gender} name in {language}."
)

model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

output=chain.invoke({
    "gender":"girl",
    "language":"Turkish"
})
print(output)
#Elif

prompt = ChatPromptTemplate.from_messages(
    [("system", "You are an English-Turkish translator that\
 return whatever the user says in Turkish."),
    ("user","{input}")]
)

chain = prompt | model | output_parser

ans=chain.invoke(
    {"input":"To be or not to be!"}
)
print(ans)
#Olmak ya da olmamak, işte bütün mesele bu.






