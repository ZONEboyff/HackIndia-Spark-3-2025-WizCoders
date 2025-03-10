from hyperon import *



metta = MeTTa()


class Task:
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = deadline
        self.priority = priority

    def __repr__(self):
        return f"Task(name={self.name}, deadline={self.deadline}, priority={self.priority})"

    def copy(self):
        return Task(self.name, self.deadline, self.priority)


def inititalize_space():
    with open('task.metta', 'r') as f:
        metta.run(f.read())


def update_space():
    result = metta.space().get_atoms()
    with open('task.metta', 'w') as f:
        for atom in result:
            f.write(str(atom) + '\n')


def add_tasks():
    name = input('Enter task name: ')
    deadline = input('Enter deadline: ')
    priority = input('Enter priority(0-10): ')
    current_task = Task(name,deadline,priority)
    atom = metta.parse_single(f"(Task \"{current_task.name}\" \"{current_task.priority}\" \"{current_task.deadline}\")")
    metta.space().add_atom(atom)
    print("Task Added Successfully")


def update_tasks():
    name = input('Enter task name to update: ')
    deadline = input('Enter deadline: ')
    priority = input('Enter priority(0-10): ')
    current_task = Task(name,deadline,priority)
    atom = metta.parse_single(f"(Task \"{current_task.name}\" \"{current_task.priority}\" \"{current_task.deadline}\")")
    previous_atom = get_task(name)
    if previous_atom:
        metta.space().remove_atom(previous_atom)
        metta.space().add_atom(atom)
    else:
        print("Task Not Found")

def get_task(name):
    pattern = metta.parse_single(f'(Task \"{name}\" $x $y)')
    query= metta.space().query(pattern=pattern)
    if query:
        atom = metta.parse_single(f"(Task \"{name}\" {query[0]['x']} {query[0]['y']})")
        return atom
    else:
        return None

def get_all_tasks():
    pattern = metta.parse_single(f'(Task $x $y $z)')

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


def sort_tasks():
    pass


def give_optimal_schedule():
    pass

def delete_dependencies(atom):
    name = atom.get_children()[1]
    pattern1 = metta.parse_single(f"({name} depends $x)")
    query1= metta.space().query(pattern=pattern1)
    if query1:
        for query in query1:
            dep_atom = metta.parse_single(f"({name} depends {query['x']})")
            metta.space().remove_atom(dep_atom)

    pattern2 = metta.parse_single(f"($y depends {name})")
    query2= metta.space().query(pattern=pattern2)
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

def show_network():
    pass


def main():
    inititalize_space()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add a Task")
        print("2. Add a Dependency")
        print("3. Update a Task")
        print("4. View Optimal Schedule")
        print("5. Delete a Task")
        print("6. Show Network")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_tasks()

            case "2":
                add_dep()

            case "3":
                update_tasks()

            case "4":
                give_optimal_schedule()

            case "5":
                delete_tasks()

            case "7":
                update_space()
                break

            case _:
                print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()