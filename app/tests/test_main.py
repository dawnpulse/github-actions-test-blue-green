import subprocess
import time
import urllib.request
import os


def test_hello():
    # Start the server
    proc = subprocess.Popen(["python", "main.py"], cwd=os.path.dirname(__file__))
    time.sleep(1)  # Give the server a moment to start up

    try:
        with urllib.request.urlopen("http://localhost:8080") as response:
            body = response.read().decode()
            assert response.status == 200
            assert "Hello, World!" in body
    finally:
        proc.terminate()
        proc.wait()
