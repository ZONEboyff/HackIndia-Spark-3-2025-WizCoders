# TaskExpert

TaskExpert is a smart task scheduling app designed to streamline your workflow. With all your tasks scheduled in advance, you can focus on getting things done without the stress of deciding what to do next. Tasks are prioritized and scheduled based on deadlines, urgency, and dependencies—ensuring that prerequisite tasks are completed before others.

## Features
- **Automated Task Scheduling**: Tasks are automatically scheduled based on priority and dependencies.
- **Dependency Management**: Ensures prerequisite tasks are completed before dependent tasks.
- **Deadline-Based Prioritization**: Urgent tasks are prioritized to meet deadlines.
- **Graph-Based Representation**: Uses MeTTa language and AtomSpace for efficient task organization.

## Technologies Used
- **MeTTa**: A declarative and functional programming language for knowledge graphs.
- **AtomSpace**: A knowledge graph representation for managing tasks and dependencies.
- **Python Integration**: For interacting with MeTTa and dynamic task handling.

## Getting Started
### Prerequisites
- Python 3.x
- Hyperon MeTTa

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ZONEboyff/HackIndia-Spark-3-2025-WizCoders.git
   cd HackIndia-Spark-3-2025-WizCoders
   ```
2. Install dependencies:
   ```bash
   pip install hyperonpy
   pip install hyperon
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Add tasks dynamically with dependencies:
   ```python
   add_task("TaskA", "2025-03-10", "High")
   add_task("TaskB", "2025-03-12", "Medium", ["TaskA"])
   ```
2. Query task dependencies:
   ```python
   query_dependencies("TaskB")
   ```

## Future Enhancements
- **Transitive Dependency Resolution**: Automatically detect and manage indirect dependencies.
- **Visualization**: Provide a graph-based UI for task dependencies.
- **Real-Time Updates**: Dynamically update task priorities and schedules.

## Contributing
Feel free to submit issues and pull requests to improve TaskExpert.

