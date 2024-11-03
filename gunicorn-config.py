# gunicorn_config.py

# Number of worker processes. Generally, 2-4 workers per CPU core is a good starting point.
workers = 2

# Number of threads per worker. Adjust based on the app’s performance and the server’s resources.
threads = 4

# Address and port to bind Gunicorn to
bind = "0.0.0.0:8000"

# Set timeout for requests in seconds. This can help prevent timeouts with larger models.
timeout = 120

# Set log level (e.g., 'debug', 'info', 'warning', 'error', 'critical')
loglevel = 'info'

# Optional: Set preload_app=True if you want to load the app before forking workers.
# This can be helpful for apps that load large machine learning models.
preload_app = True
