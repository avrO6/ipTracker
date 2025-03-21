import subprocess
import json
import argparse

VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"

parser = argparse.ArgumentParser(description="Consulta información sobre una dirección IP usando ip.guide")
parser.add_argument("--ip", help="Dirección IP a consultar")
args = parser.parse_args()

def banner():
    print(rf" ###########################################")
    print(rf"# {VERDE}  _____  _____   ____  _      ______      {RESET}#")
    print(rf'# {VERDE} |_   _||  __ \   ____  _      ______     {RESET}#')
    print(rf"# {VERDE}   | |  | |__) |  ____  _      ______     {RESET}#")
    print(rf"# {VERDE}   | |  |  ___/  ____  _      ______      {RESET}#")
    print(rf"# {VERDE}   | |  | |      ____  _      ______      {RESET}#")
    print(rf"# {VERDE}  _| |_ | |      ____  _      ______      {RESET}#")
    print(rf"# {VERDE} |_____||_|      ____  _      ______      {RESET}#")
    print(rf'#                                           #')
    print(rf" ###########################################")
    print(rf"{AMARILLO}      IPTRACKER - Rastrea cualquier IP         {RESET}")
    print(rf"{AMARILLO}      Versión 1.0 - ¡Sigue el rastro!          {RESET}")
    
    

def get_data_from_api(ip):

    try:
        full_url = f"ip.guide/{ip}"
        
        result = subprocess.run(["curl", "-sL", full_url], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    except json.JSONDecodeError:
        return {"error": "Error al decodificar la respuesta JSON"}

if __name__ == "__main__":    
    banner()
    data = get_data_from_api(args.ip)

    if "location" in data:
        location = data["location"]
        print(json.dumps(location, indent=4))
    else:
        print("No se encontraron datos de ubicación.")
