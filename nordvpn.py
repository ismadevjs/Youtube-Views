import subprocess
import time

def wait_for_nordvpn_connection():
    check_or_connect = '-g'
    while True:
        try:
            result = subprocess.run(['C:\\Program Files\\NordVPN\\NordVPN.exe', check_or_connect], capture_output=True, text=True)
            print(result)
            output = result.stdout.strip()
            if 'Status: Connected' in output:
                print("NordVPN is connected.")
                break
            else:
                print("NordVPN is not connected. Retrying in 10 seconds...")
                time.sleep(10)
                check_or_connect = '-c'
                print('checking connection ...')
                time.sleep(15)
                result = subprocess.run(['C:\\Program Files\\NordVPN\\NordVPN.exe', "-g"], capture_output=True, text=True)
                output = result.stdout.strip()
                print(result)
                if 'Status: Connected' in output:
                    print("NordVPN is connected.")
                    break
        except subprocess.CalledProcessError:
            print("Error occurred while checking NordVPN status. Retrying in 10 seconds...")
            time.sleep(10)

wait_for_nordvpn_connection()
