from app import app
from flask import render_template, request, render_template, redirect, url_for
import re
from openai import OpenAI

client = OpenAI()
def get_functions(text):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "what functions should a (an)" + text + " device have?"}
    ]
    )   
    # print(completion.choices[0].message.content)
    ans = completion.choices[0].message.content
    print(ans)
    # ans = [a for a in ans if a]

    # print("function:", ans)
    return ans

def get_designs(text):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "what kind of design can afford" + text}
    ]
    )   
    print(completion.choices[0].message.content)
    ans = completion.choices[0].message.content
    return ans

def get_structures(text):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "what design structures can achieve" + text}
    ]
    )   
    # 打印生成内容和打印5选择的功能关键词
    print(completion.choices[0].message.content)
    ans = completion.choices[0].message.content
    return ans

selected_function = ""
# functions = ""
# designs = ""
# structures = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_text', methods=['POST'])
def submit_text():
    # 获取输入关键词
    text_value = request.form.get('keyword')

    # 获取GPT输出
    functions = get_functions(text_value)

    return render_template('index.html', functions = functions)

@app.route('/submit_function', methods=['POST'])
def submit_function():
    # selected_function = request.form.get('function')
    global selected_function
    # 获取输入关键词
    selected_function = request.form.get('function')

    # 获取GPT输出
    designs = get_designs(selected_function)

    return render_template('index.html', designs = designs)

@app.route('/submit_design', methods=['POST'])
def submit_design():
    selected_design = request.form.get('design')

    # 获取GPT输出
    structures = get_structures(selected_design)

    return render_template('index.html', structures = structures)

@app.route('/submit_structure', methods=['POST'])
def submit_structure():
    selected_structure = request.form.get('structure')
    # (function1, structure2)
    print(selected_function, selected_structure)
    return render_template('index.html', selected_function = selected_function, selected_structure = selected_structure)

