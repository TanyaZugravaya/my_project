import json
from datetime import datetime

def load_notes(filename):
    with open(filename, "r") as file:
        return json.load(file)

def save_notes(filename, notes):
    with open(filename, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    notes.append({
        "id": len(notes) + 1,
        "title": input("Введите заголовок заметки: "),
        "body": input("Введите текст заметки: "),
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "updated_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })
    print("Заметка успешно добавлена!")

def edit_note():
    note_id = int(input("Введите ID заметки, которую хотите изменить: "))
    note = find_note_by_id(note_id)
    if note:
        note["title"] = input("Введите новый заголовок заметки: ")
        note["body"] = input("Введите новый текст заметки: ")
        note["updated_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print("Заметка успешно изменена!")
    else:
        print("Заметка с таким ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    note = find_note_by_id(note_id)
    if note:
        notes.remove(note)
        print("Заметка успешно удалена!")
    else:
        print("Заметка с таким ID не найдена.")

def find_note_by_id(note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None

def list_notes():
    print("Список заметок:")
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}, Дата изменения: {note['updated_at']}")
    print()

def filter_notes_by_date():
    date = input("Введите дату для фильтрации (в формате dd-mm-yyyy): ")
    filtered_notes = [note for note in notes if note["created_at"].startswith(date) or note["updated_at"].startswith(date)]
    if filtered_notes:
        print("Найденные заметки:")
        for note in filtered_notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}, Дата изменения: {note['updated_at']}")
        print()
    else:
        print("Заметки с указанной датой не найдены.")

def menu():
    while True:
        print("Выберите действие:")
        print("1. Вывести все заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Фильтровать заметки по дате")
        print("0. Выход")
        
        choice = input("Введите номер действия: ")

        if choice == "1":
            list_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            filter_notes_by_date()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
        print()

try:
    notes = load_notes("notes.json")
except FileNotFoundError:
    notes = []

menu()
save_notes("notes.json", notes)