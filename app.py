import psutil
import time
from flask import Flask, jsonify, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    uptime_secs = int(time.time() - psutil.boot_time())
    hours=uptime_secs//3600
    minutes=(uptime_secs%3600)//60
    return jsonify({
        "cpu": psutil.cpu_percent(interval=.5),
        "memory":float( psutil.virtual_memory().percent),
        "disk": psutil.disk_usage('/').percent,
        "uptime": f"{hours}:{minutes}\ntotal: {uptime_secs}",
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
