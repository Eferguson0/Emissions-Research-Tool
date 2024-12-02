# Gunicorn configuration
bind = "0.0.0.0:10000"
workers = 1
threads = 4
timeout = 180
max_requests = 1
worker_class = 'sync'
worker_tmp_dir = '/dev/shm'

# Log configuration
accesslog = '-'
errorlog = '-'
loglevel = 'info'
