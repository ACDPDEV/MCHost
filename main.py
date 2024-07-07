import threading
import requests
import subprocess
import time
import os


#CONFIGURACIÓN DE INSTALACIÓN
version = "1.21" # Version del servidor
# Software -> solo disponible Spigot
authtoken = "" # token de ngrok, si aún no lo tienes consíguelo en https://dashboard.ngrok.com/get-started/your-authtoken


def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    try:
        for line in iter(process.stdout.readline, ''):
            print(line.strip())
    except KeyboardInterrupt:
        process.terminate()

    rc = process.wait()
    return rc
def secondary_proccess(url):
    while True:
        response = requests.get(url)
        time.sleep(10)

try:
    from pyngrok import ngrok
except:
    run_command("pip install pyngrok")

def run():
    server_path = "/workspaces/MChost/MCserver"
    ngrok.set_auth_token(authtoken)
    if os.path.exists(server_path):
        tunnel = ngrok.connect(addr="25565", proto="tcp")
        print(f"IP de tu servidor: {tunnel.public_url}")
        run_command("cd MCserver && sudo bash run.sh")
    else:
        # sudo mkdir MCserver
        # cd MCserver
        # sudo wget https://download.getbukkit.org/spigot/spigot-{version}.jar
        # sudo mv spigot-{version}.jar server.jar
        # touch run.sh
        # echo 'java -Xmx10G -Xms10G -jar server.jar nogui' > run.sh
        # sudo chmod +x run.sh
        # sudo bash run.sh
        # sed -i 's/eula=false/eula=true/' eula.txt
        # sudo bash run.sh
        run_command(f"sudo mkdir MCserver && cd MCserver && sudo wget https://download.getbukkit.org/spigot/spigot-{version}.jar && sudo mv spigot-{version}.jar server.jar && touch run.sh && echo 'java -Xmx10G -Xms10G -jar server.jar nogui' > run.sh && sudo chmod +x run.sh && sudo bash run.sh && sed -i 's/eula=false/eula=true/' eula.txt")
        tunnel = ngrok.connect(addr="25565", proto="tcp")
        print("")
        print("")
        print("---------------------------------------------")
        print(f"IP de tu servidor: {tunnel.public_url}")
        print("---------------------------------------------")
        print("")
        print("")
        run_command("cd MCserver && sudo bash run.sh")
def main():
    url = "https://jsonplaceholder.typicode.com/users"

    server = threading.Thread(target=run)
    data_thread = threading.Thread(target=secondary_proccess, args=(url,))
    server.start()
    data_thread.start()
    server.join()
    data_thread.join()

if __name__ == "__main__":
    print("by ACDP10")
    main()