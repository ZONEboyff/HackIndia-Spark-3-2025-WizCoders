# TaskExpert

TaskExpert is a smart task scheduling app designed to streamline your workflow. With all your tasks scheduled in advance, you can focus on getting things done without the stress of deciding what to do next. Tasks are prioritized and scheduled based on deadlines, urgency, and dependencies—ensuring that prerequisite tasks are completed before others.

## Features


## Architecture
- **src/task_model.py**: Task data model
- **src/storage.py**: Persistent storage (MeTTa/Hyperon)
- **src/dependency.py**: Dependency and scheduling logic
- **src/visualization.py**: Dependency graph visualization
- **src/task_scheduler.py**: Main CLI entry point
- **config/**: Configuration, environment, secrets (never committed)
- **tests/**: Unit and integration tests
- **docs/**: Architecture, design, and contribution docs
- **scripts/**: Automation and utility scripts

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.
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


## Future Enhancements
- **Transitive Dependency Resolution**: Automatically detect and manage indirect dependencies.
- **Visualization**: Provide a graph-based UI for task dependencies.
- **Real-Time Updates**: Dynamically update task priorities and schedules.

## Contributing
Feel free to submit issues and pull requests to improve TaskExpert.

