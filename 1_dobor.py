import requests
import random


def main():
    categories = requests.get('https://jservice.io/api/categories?count=100', verify=False).json()  # даем на выбор категории
    print('Доступные категории')
    for num, category in enumerate(categories, 1):
        print(f'{num}. {category.get("title")}')
    category_num = int(input('Введите номер категории: ')) - 1
    questions_num = int(categories[category_num].get('clues_count'))
    category_id = int(categories[category_num].get('id'))
    user_questions_num = int(input(f'введите необходимое количество вопросов (максимальное кол-во. {questions_num}): '))
    questions = requests.get(f'https://jservice.io/api/category?id={category_id}', verify=False).json().get('clues')
    random.choice(questions)
    for question_num, question in enumerate(questions[:user_questions_num], 1):
        with open(f'вопрос {question_num}.txt', 'w', encoding='utf8') as file:
            file.write(question.get('question'))


if __name__ == '__main__':
    main()
