
from src.task_model import Task
from src.storage import TaskStorage
from src.dependency import sort_tasks, topological_sort
from src.visualization import visualize_dependencies

storage = TaskStorage()
metta = storage.get_metta()

def inititalize_space():
    storage.load()

def update_space():
    storage.save()

def add_tasks():
    name = input('Enter task name: ')
    deadline = input('Enter deadline: ')
    priority = input('Enter priority(0-10): ')
    current_task = Task(name, deadline, priority)
    atom = metta.parse_single(f"(Task \"{current_task.name}\" \"{current_task.deadline}\" \"{current_task.priority}\")")
    metta.space().add_atom(atom)
    print("Task Added Successfully")

def update_tasks():
    name = input('Enter task name to update: ')
    deadline = input('Enter deadline: ')
    priority = input('Enter priority(0-10): ')
    current_task = Task(name, deadline, priority)
    atom = metta.parse_single(f"(Task \"{current_task.name}\" \"{current_task.deadline}\" \"{current_task.priority}\")")
    previous_atom = get_task(name)
    if previous_atom:
        metta.space().remove_atom(previous_atom)
        metta.space().add_atom(atom)
    else:
        print("Task Not Found")

def get_task(name):
    pattern = metta.parse_single(f'(Task \"{name}\" $x $y)')
    query = metta.space().query(pattern=pattern)
    result = metta.run(f'! (match &self (Task \"{name}\" $x $y) ($x $y))')
    if result[0] != []:
        result = result[0][0].get_children()
        atom = metta.parse_single(f"(Task \"{name}\" {result[0]} {result[1]})")
        return atom
    else:
        return None

def add_dep():
    dep = input("Enter the dependent task name: ")
    next = input("Enter the task name on which {} is dependent on: ".format(dep))
    dep_atom = get_task(dep)
    next_atom = get_task(next)
    if next_atom and dep_atom:
        dependency_atom = metta.parse_single(f"({dep_atom.get_children()[1]} depends {next_atom.get_children()[1]})")
        metta.space().add_atom(dependency_atom)
    else:
        print("Tasks Not Found")

def list_tasks():
    result = metta.run(f'! (match &self (Task $x $y $z) ($x $y $z))')
    return result[0]

def sort_tasks():
    # Use dependency.sort_tasks instead
    return sort_tasks(list_tasks())

def get_dependencies(task):
    result = metta.run(f'! (match &self (\"{task}\" depends $x) ($x))')
    if result[0] == []:
        return ({task: []})
    result = [task.get_children()[0].get_object().content for task in result[0]]
    return {task: result}

def get_dependency_dict():
    tasks = list_tasks()
    tasks = [task.get_children()[0].get_object().content for task in tasks]
    dependencies = {}
    for task in tasks:
        dependencies.update(get_dependencies(task))
    return dependencies

def Next_Task():
    optimal_schedule = give_optimal_schedule()
    return optimal_schedule[0]

def show_optimal_schedule():
    optimal_schedule = give_optimal_schedule()
    dependencies = get_dependency_dict()
    print("\nOPTIMAL TASK SCHEDULE:")
    for i, task in enumerate(optimal_schedule, 1):
        deps = dependencies.get(task, [])
        if deps:
            print(f"{i}. {task} (depends on: {', '.join(deps)})")
        else:
            print(f"{i}. {task} (no dependencies)")

def give_optimal_schedule():
    sorted_tasks = sort_tasks(list_tasks())
    sorted_tasks = [task[0] for task in sorted_tasks]
    dependencies = get_dependency_dict()
    optimal_schedule = topological_sort(dependencies, sorted_tasks)
    return optimal_schedule

def topological_sort(dependencies, priority_list):
    graph = {}
    for task, deps in dependencies.items():
        graph[task] = set(deps)
        for dep in deps:
            if dep not in graph:
                graph[dep] = set()
    priority_dict = {task: idx for idx, task in enumerate(priority_list)}
    visited = set()
    temp_visited = set()
    result = []
    def dfs(task):
        if task in visited:
            return True
        if task in temp_visited:
            print(f"Error: Cyclic dependency detected involving task '{task}'")
            return False
        temp_visited.add(task)
        if task in graph:
            deps_sorted = sorted(graph[task], key=lambda x: priority_dict.get(x, float('inf')))
            for dep in deps_sorted:
                if not dfs(dep):
                    return False
        temp_visited.remove(task)
        visited.add(task)
        result.append(task)
        return True
    for task in priority_list:
        if task not in visited:
            if not dfs(task):
                return result
    return result

def visualize_dependencies():
    dependencies = get_dependency_dict()
    visualize_dependencies(dependencies)

def delete_dependencies(atom):
    name = atom.get_children()[1]
    pattern1 = metta.parse_single(f"({name} depends $x)")
    query1 = metta.space().query(pattern=pattern1)
    if query1:
        for query in query1:
            dep_atom = metta.parse_single(f"({name} depends {query['x']})")
            metta.space().remove_atom(dep_atom)
    pattern2 = metta.parse_single(f"($y depends {name})")
    query2 = metta.space().query(pattern=pattern2)
    if query2:
        for query in query2:
            dep_atom = metta.parse_single(f"({query['y']} depends {name})")
            metta.space().remove_atom(dep_atom)

def delete_tasks():
    name = input('Enter task name to delete: ')
    atom = get_task(name)
    if atom:
        metta.space().remove_atom(atom)
        delete_dependencies(atom)
    else:
        print("Task Not Found")

def main():
    inititalize_space()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add a Task")
        print("2. Add a Dependency")
        print("3. Update a Task")
        print("4. View Optimal Schedule")
        print("5. Delete a Task")
        print("6. Visualize dependencies")
        print("7. Next Task")
        print("8. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_tasks()
            case "2":
                add_dep()
            case "3":
                update_tasks()
            case "4":
                show_optimal_schedule()
            case "5":
                delete_tasks()
            case "6":
                visualize_dependencies()
            case "7":
                print("\nNext Task: ", Next_Task())
            case "8":
                update_space()
                break
            case _:
                print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
