import os,subprocess,sys,threading
def main():
    def start_server():
        script_dir = os.path.abspath(sys.path[0])
        http_server_command = f"python -m http.server 8000 --directory {script_dir}"
        subprocess.Popen(http_server_command, shell=True)
        url = "http://localhost:8000"
        if sys.platform == "win32":
            os.system(f"start {url}")
        elif sys.platform == "darwin":
            os.system(f"open {url}")
        else:
            os.system(f"xdg-open {url}")
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    print('Press enter to hide the logs.')