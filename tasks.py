import json
import sys
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text())


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))


def add_task(title):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: [{task['id']}] {title}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "x" if t["done"] else " "
        print(f"[{status}] {t['id']}. {t['title']}")


def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Done: {t['title']}")
            return
    print(f"Task {task_id} not found.")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f"Deleted task {task_id}")


def search_tasks(keyword):
    tasks = load_tasks()
    results = [t for t in tasks if keyword in t["title"]]
    if not results:
        print("No matches found.")
        return
    for t in results:
        print(f"  {t['id']}. {t['title']}")


def main():
    args = sys.argv[1:]
    if not args:
        print("Commands: add | list | done | delete")
        return

    command = args[0]
    if command == "add" and len(args) > 1:
        add_task(" ".join(args[1:]))
    elif command == "list":
        list_tasks()
    elif command == "done" and len(args) > 1:
        complete_task(int(args[1]))
    elif command == "delete" and len(args) > 1:
        delete_task(int(args[1]))
    elif command == "search" and len(args) > 1:
        search_tasks(args[1])
    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()
