import streamlit as st
import re

# input data
st.title("Flash Cards")
text = st.text_area("Insert flash cards here:", height=400)
st.button("submit")

# seperate questions from answers

qa = {}

question_start = 0
question_end = 0
answer_start = 0
answer_end = 0

for index, letter in enumerate(text):
    if letter == "?":
        question_end = index
        answer_start = question_end+1
        print("Question")
        print(question_start, question_end)

        question = text[question_start:question_end+1]
 
        question = re.sub('\s+', ' ', question).strip('#')

        print(question)

    if letter == "#":
        answer_end = index
        question_start = answer_end
        print("Answer")
        print(answer_start, answer_end)

        answer = text[answer_start:answer_end+1]

        answer = re.sub('\s+', ' ', answer).strip('#').replace("•", "\n •").replace(".", ". \n")

        print(answer)

        qa[question] = answer

print(qa)

# display questions

for question in qa:
    expander = st.expander(question)
    expander.text(qa[question])
