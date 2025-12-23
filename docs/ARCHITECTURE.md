# Architecture Overview

## High-Level Design

- **src/task_model.py**: Task class (data model)
- **src/storage.py**: Storage and persistence (MeTTa/Hyperon)
- **src/dependency.py**: Dependency management and scheduling
- **src/visualization.py**: Visualization (NetworkX, Matplotlib)
- **src/task_scheduler.py**: Main entry point and CLI

## Key Principles
- SOLID, DRY, Clean Code
- Separation of concerns (logic, config, tests, docs)
- Secure by default (no secrets in code)


│   ├── task_model.py
│   ├── storage.py
│   ├── dependency.py
│   ├── visualization.py
│   └── task_scheduler.py
## Extensibility
- Add new modules to `src/` for features (e.g., REST API, web UI)
- Use config-driven patterns for environment and secrets

## Ownership
- Each module should have a clear owner (see CONTRIBUTING.md)

## Diagram
```
project-root/
├── src/
│   ├── task_scheduler.py
│   └── ...
├── config/
├── tests/
├── docs/
├── scripts/
├── README.md
└── ...
```
