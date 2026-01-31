# src/dependency.py
from datetime import datetime

def sort_tasks(tasks):
    tasks = [(task.get_children()[0].get_object().content, task.get_children()[1].get_object().content,
              task.get_children()[2].get_object().content) for task in tasks]
    tasks = [(task[0], datetime.strptime(task[1], '%Y-%m-%d'), int(task[2])) for task in tasks]
    sorted_tasks = sorted(tasks, key=lambda x: (x[2], x[1]))
    return sorted_tasks

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
