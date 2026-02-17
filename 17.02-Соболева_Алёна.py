import json
import os

#имя файла для хранения данных
name_file = "data.json"

#статусы проектов
statuses = ["Планирование", "В работе", "Готов"]


def load_data():
    #загружает данные из JSON файла. Если файла нет, создает пустую структуру
    if not os.path.exists(name_file):
        return {"projects": []}

    try:
        with open(name_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Ошибка чтения файла данных. Создается новый файл.")
        return {"projects": []}


def save_data(data):
    #сохраняет данные в JSON файл
    with open(name_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_project_by_id(projects, project_id):
     #ищет проект по ID
    for project in projects:
        if project["id"] == project_id:
            return project
    return None


#функции меню
def show_projects():
    #1. Показать проекты
    data = load_data()
    projects = data.get("projects", [])

    print("\nСписок проектов")
    if not projects:
        print("Проектов пока нет.")
    else:
        print(f"{'ID':<5} | {'Название':<20} | {'Статус':<15} | {'Задач':<5}")
        print("-" * 55)
        for p in projects:
            task_count = len(p.get("tasks", []))
            print(f"{p['id']:<5} | {p['name']:<20} | {p['status']:<15} | {task_count:<5}")
    print("-" * 55)


def create_project():
    #2. Создать проект
    name = input("Введите название нового проекта: ").strip()
    if not name:
        print("Название не может быть пустым.")
        return

    data = load_data()

    #генерируем новый ID
    new_id = 1
    if data["projects"]:
        new_id = max(p["id"] for p in data["projects"]) + 1

    new_project = {
        "id": new_id,
        "name": name,
        "status": "Планирование",  #статус по умолчанию
        "tasks": []
    }

    data["projects"].append(new_project)
    save_data(data)
    print(f"Проект '{name}' успешно создан с ID: {new_id}")


def add_task():
    #3. Добавить задачу
    show_projects()
    try:
        project_id = int(input("Введите ID проекта для добавления задачи: "))
    except ValueError:
        print("ID должен быть числом.")
        return

    data = load_data()
    project = get_project_by_id(data["projects"], project_id)
    if project:
        task_name = input("Введите название задачи: ").strip()
        if task_name:
            #генерируем ID задачи внутри проекта
            new_task_id = 1
            if project["tasks"]:
                new_task_id = max(t["id"] for t in project["tasks"]) + 1

            project["tasks"].append({
                "id": new_task_id,
                "title": task_name,
                "done": False
            })
            save_data(data)
            print(f"Задача '{task_name}' добавлена в проект '{project['name']}'")
        else:
            print("Название задачи не может быть пустым.")
    else:
        print("Проект с таким ID не найден.")


def show_tasks_in_project():
    #4. Показать задачи в проекте
    show_projects()
    try:
        project_id = int(input("Введите ID проекта для просмотра задач: "))
    except ValueError:
        print("ID должен быть числом.")
        return

    data = load_data()
    project = get_project_by_id(data["projects"], project_id)

    if project:
        print(f"\nЗадачи проекта: {project['name']}")
        if not project["tasks"]:
            print("В этом проекте задач нет.")
        else:
            print(f"{'ID':<5} | {'Статус':<6} | {'Название задачи'}")
            print("-" * 40)
            for task in project["tasks"]:
                status = "[x]" if task["done"] else "[ ]"
                print(f"{task['id']:<5} | {status:<6} | {task['title']}")
        print("-" * 40)
    else:
        print("Проект с таким ID не найден.")


def change_project_status():
    #5. Изменение статуса проекта
    show_projects()
    try:
        project_id = int(input("Введите ID проекта для изменения статуса: "))
    except ValueError:
        print("ID должен быть числом.")
        return

    data = load_data()
    project = get_project_by_id(data["projects"], project_id)

    if project:
        print(f"\nТекущий статус проекта '{project['name']}': {project['status']}")
        print("Доступные статусы:")
        for i, status in enumerate(statuses, 1):
            print(f"{i}. {status}")

        try:
            choice = int(input("Выберите новый статус (номер): "))
            if 1 <= choice <= len(statuses):
                project["status"] = statuses[choice - 1]
                save_data(data)
                print(f"Статус проекта изменен на: {project['status']}")
            else:
                print("Неверный выбор.")
        except ValueError:
            print("Введите число.")
    else:
        print("Проект с таким ID не найден.")


#главное меню
def main():
    while True:
        print("\nМЕНЕДЖЕР ПРОЕКТОВ")
        print("1. Показать проекты")
        print("2. Создать проект")
        print("3. Добавить задачу")
        print("4. Показать задачи в проекте")
        print("5. Изменить статус проекта")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_projects()
        elif choice == "2":
            create_project()
        elif choice == "3":
            add_task()
        elif choice == "4":
            show_tasks_in_project()
        elif choice == "5":
            change_project_status()
        elif choice == "0":
            print("Выход из приложения.")
            break
        else:
            print("Неверная команда, попробуйте снова.")


if __name__ == "__main__":
    main()