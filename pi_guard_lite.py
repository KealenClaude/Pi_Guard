import subprocess
import os
import time
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>PiGuard Lite - Network Monitor</title></head>
<body>
<h1>PiGuard Lite - Connection Logs</h1>
<pre>{{ logs }}</pre>
</body>
</html>
'''

def get_connections():
    result = subprocess.run("ss -tunap", shell=True, capture_output=True, text=True)
    return result.stdout

@app.route('/')
def index():
    logs = get_connections()
    return render_template_string(HTML, logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
