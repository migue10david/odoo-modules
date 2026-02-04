{
    "name": "User Task Manager",
    "version": "1.0",
    "category": "Productivity",
    "summary": "User Task Manager efficiently",
    "description": """
        This module allows users to create, manage, and track their tasks effectively
        Feacture include task assignment, deadline, priority, and progress tracking
    """,
    "author": "Miguel Angel",
    "depends": [
        "base"
    ],
    "data": [
        "security/task_security.xml",
        "security/ir.model.access.csv",
        "views/task_view.xml"
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "user_task_manager/static/src/css/task_kanban.css",
        ],
    },
} # type: ignore