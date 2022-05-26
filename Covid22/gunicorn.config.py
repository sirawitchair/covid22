bind = '0.0.0.0:8001'
raw_env = [
   'DJANGO_SETTINGS_MODULE=Covid22.settings'
]
user = 'adminswc'
group = 'adminswc'
backlog = 2048
workers = 2
accesslog = '/home/adminswc/COVID22/logs/gunicorn.log'
errorlog = '/home/adminswc/COVID22/logs/gunicorn.error.log'
capture_output = True