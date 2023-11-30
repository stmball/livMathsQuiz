import argparse
import json
import hashlib

def parse_args():

    parser = argparse.ArgumentParser(description='Question Parser')
    parser.add_argument('filename', help='File to parse into questions format')

    args = parser.parse_args()

    return args.filename

def parse_questions():

    with open(parse_args(), 'r') as f:
        data = f.read()

    questions = data.split('\n')
    questions = [q.split("::") for q in questions]
    return questions

def save_questions(questions):

    questions = [{
        "title": q[0],
        "text": q[1],
        "solution_hash": hashlib.md5(q[2].encode()).hexdigest(),
    } for q in questions]

    with open('questions.js', 'w') as f:
        f.write("const questions = ")
        json.dump(questions, f, indent=4)
    


if __name__ == '__main__':
    parse_args()
    questions =  parse_questions()
    save_questions(questions)