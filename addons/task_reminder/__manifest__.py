{
    'name': 'Task Reminder',
    'version': '1.0',
    'summary': 'Simple practice module to manage tasks with reminders',
    'author': 'Your Name',
    'website': 'https://www.example.com',  # optional
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'views/task_views.xml',
        'views/personal_task_views.xml',
        'templates/task_qweb.xml',
        'data/reminder_cron.xml',
        'security/ir.model.access.csv'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,   # 👈 this makes it show as a standalone app
    'auto_install': False,
    'license': 'LGPL-3',
}
