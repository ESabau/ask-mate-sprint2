import datetime
import connection
import os

def get_item_by_id(items,id):
    for item in items:
        if item["id"] == id:
            return item

    return None


def send_question_to_display_by_id(question_id):
    all_questions = connection.read_csv("question.csv")
    question = get_item_by_id(all_questions, question_id)
    return question


def get_answers_for_question(answers,question_id):
    all_answers = []
    for answer in answers:
        if answer["question_id"] == question_id:
            all_answers.append(answer)

    return all_answers


def send_answer_to_display_by_id(question_id):
    all_answers = connection.read_csv("answer.csv")
    answers = get_answers_for_question(all_answers, question_id)
    return answers


def delete_item_from_items(items, item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return items


def delete_one_answer(question_id, answer_id):
     all_answers = connection.read_csv("answer.csv")
     for answer in all_answers:
        if answer["question_id"] == question_id and answer["id"] == answer_id:
                if answer.get("image") != None:
                    if os.path.exists(answer["image"]):
                        os.remove(answer["image"])
                all_answers.remove(answer)
                return all_answers


def delete_all_answers_for_question(question_id):
    all_answers = connection.read_csv("answer.csv")
    updated_answers = []
    for answer in all_answers:
        if answer["question_id"] == question_id:
            if answer.get("image") != None:
                if os.path.exists(answer["image"]):
                    os.remove(answer["image"])
        else:
            updated_answers.append(answer)

    return updated_answers


def add_like(items,item_id):
    for item in items:
        if item["id"] == item_id:
            item["vote_number"] = int(item.get("vote_number", 0))+1
            return items



def remove_like(items,item_id):
    for item in items:
        if item["id"] == item_id:
            item["vote_number"] = int(item.get("vote_number", 0)) - 1
            return items


def get_new_id(questions):
    new_id = 0
    for question in questions:
        if int(question['id']) > new_id:
            new_id = int(question['id'])
    return new_id + 1


def update_question(edited_question):
    questions = connection.read_csv("question.csv")
    for question in questions:
        if question["id"] == edited_question["id"]:
            question["title"] = edited_question["title"]
            question["message"] = edited_question["message"]
            question["image"] = edited_question["image"]
    return questions


def get_current_timestamp():
    now = datetime.datetime.now()
    return int(datetime.datetime.timestamp(now))


def convert_date(timestamp):
    date_time = datetime.datetime.fromtimestamp(int(timestamp))
    time_formatted = date_time.strftime('%d-%b-%Y (%H:%M:%S)')
    return time_formatted



def update_votes(items,item_id,post_result):
    for item in items:
        if item["id"] == item_id:
            if post_result["vote_answer"] == "dislike":
                item["vote_number"] = int(item.get("vote_number", 0)) - 1
            elif post_result["vote_answer"] == "like":
                item["vote_number"] = int(item.get("vote_number", 0)) +1
            return items



def delete_image(item_id):
    item = send_question_to_display_by_id(item_id)
    path = item.get('image')
    if os.path.exists(path):
        os.remove(path)

