from flask import Flask, request, jsonify
import json
import uuid
import os


app=Flask(__name__)

TASKS_FILE="tasks.json"

mood_keywords={"Angry": ["angry", "mad", "furious", "irritated", "annoyed"],
               "Sad": ["sad", "depressed", "unhappy", "crying", "sorrow", "down", "heartbreak" ],
               "Happy": ["happy", "cheerful", "smiling", "grateful", "joyful", "glad", "excited"]
               }

def load_file():
    if not os.path.exists(TASKS_FILE):
        return {}
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_file(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def mood_finder(sentence):
    sentence=sentence.lower()
    for mood, keywords in mood_keywords.items():
        for word in keywords:
            if word in sentence:
                return mood
    return "unknown"


@app.route("/")
def hello():
    return "Hello User"

@app.route("/task", methods=["POST"])
def user_task():
    data=request.get_json()
    sentence=data.get("sentence", "")

    mood=mood_finder(sentence)
    task_id=str(uuid.uuid4())[:6].upper()

    tasks=load_file()
    tasks[task_id]={"sentence": sentence,
                    "mood": mood
                    }
    save_file(tasks)

    return jsonify({"id": task_id, "mood": mood, "sentence": sentence}), 200

@app.route("/task", methods=["GET"])
def user_data():
    task_id = request.args.get("id")
    tasks=load_file()
    task=tasks.get(task_id)

    if task:
        return jsonify({"id": task_id, **task}), 200
    return jsonify({"error": "Task not found."}), 404


if __name__=="__main__":
    app.run(debug=True)

