import ReAct 
from ReAct import ReAct
import re
import os
from openai import OpenAI
from dotenv import load_dotenv
from tools import use_cmd
import prompt

session = ReAct(model="gpt-4o")

def main(): 
    question = ''
    while question != 'q':
        question = input("Please enter a task to gitBot: ")
        session.run_session(question)
    else:
        print(f"session is over")   

main()