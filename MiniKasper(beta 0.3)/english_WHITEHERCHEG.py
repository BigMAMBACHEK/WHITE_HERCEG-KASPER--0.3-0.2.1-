#register/obg.net/github/build_0.3(fixed 0.2.1)/updates/13.03.2024/
#deleted{scanning_host}{install_downloads_animations}{upgrade__list__virus__files}
#install_future/build_vers_0.4/def==separ*****

import os
import subprocess
import sys
import psutil
import socket



processes=[]

commands={
    "[1]help_command":"Shows the available commands",
    "[2]pc_information":"Shows information about the computer",
    "[3]scanning_for_suspicious_processes":"Scans your computer for suspicious processes",
    "[4]checking_disks_for_errors":"Scans disks for errors",
    "[5]":"What's new in the program"
}

def show_info():
    print("Available Commands:")
    for cmd, desc in commands.items():
        print(f"  {cmd}: {desc}")

known_miners_and_viruses=["xmrig","minered","ccmier","trojan"]

def scanning_pc():
    suspicious_processes = []
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'].lower() in known_miners_and_viruses:
            suspicious_processes.append((process.info['name'], process.info['pid']))
    if suspicious_processes:
        message = "Suspicious processes detected:\n"
        for name, pid in suspicious_processes:
            message += f"{name} (PID: {pid})\n"
        print(message)
    else:
        print("No suspicious processes were detected. Your system is clean!")

def pc_info():
    cpu_count = psutil.cpu_count(logical=True) 
    cpu_freq = psutil.cpu_freq()  
    print(f"CPU {cpu_count} logical cores")
    print(f"Processor frequency: {cpu_freq.current:.2f} MHz")


    virtual_mem = psutil.virtual_memory()
    print(f"RAM {virtual_mem.total / (1024 ** 3):.2f} GB")
    print(f"Free memory: {virtual_mem.available / (1024 ** 3):.2f} GB")


    print("\nDisc:")
    for partition in psutil.disk_partitions():
        print(f"Disc: {partition.device}")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  Total: {usage.total / (1024 ** 3):.2f} GB")
        print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
        print(f"  Freely: {usage.free / (1024 ** 3):.2f} GB")


    if psutil.sensors_battery():
        battery = psutil.sensors_battery()
        print("\nBattery")
        print(f"  Charge level: {battery.percent}%")
        print(f"  Battery life: {battery.secsleft // 60} min")
    else:
        print("\nNo battery detected")

def list_drives():
    partitions = psutil.disk_partitions()
    drives = [partition.device for partition in partitions]
    return drives

def check_disk_for_errors():
    try:
        drives = list_drives()
        if not drives:
            print("The disks were not found.")
            return

        print("Available disks:")
        for i, drive in enumerate(drives):
            print(f"{i + 1}: {drive}")

        choice = int(input("Select the disk number to check: "))
        if choice < 1 or choice > len(drives):
            print("Wrong choice.")
            return

        drive = drives[choice - 1]
        command = f'chkdsk {drive}'
        result = os.system(command)

        if result == 0:
            print(f"Disc{drive} checked, no errors found.")
        else:
            print(f"On disk {drive} an error has been detected.")
    except Exception as e:
        print(f"An error occurred while checking the disk: {e}")

known_suspicious_processes = [
    "xmrig", "minered", "ccminer", "trojan", "keylogger", "malware-inject"
]

def check_pc_on_process():
    suspicious_processes = []

    # Проверяем запущенные процессы
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            if process_name in known_suspicious_processes:
                suspicious_processes.append((process.info['name'], process.info['pid']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Игнорируем ошибки доступа к процессу или если процесс завершился
            continue

    # Вывод результата
    if suspicious_processes:
        print("Suspicious processes found:")
        for name, pid in suspicious_processes:
            print(f"  {name} (PID: {pid})")

        # Возможность завершить процессы
        choice = input("Do you want to complete these processes? (Y/n): ").strip().lower()
        if choice == "Y":
            for name, pid in suspicious_processes:
                try:
                    process = psutil.Process(pid)
                    process.terminate()  # Завершение процесса
                    print(f"Process {name} (PID: {pid}) completed.")
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(f"Failed to complete {name} (PID: {pid}): {e}")
        else:
            print("The completion of the processes has been canceled.")
    else:
        print("No suspicious processes were detected.")

def information():
    print("""The program has cut out the scan open ports command on your computer. 
          It is being processed and is undergoing testing. Bugs and other issues will also be searched for later. 
          To contact us, beep in the telegram: @dark_herceg_exe""")

def main():
    print(""" 
///////////////////////////////////////////////////////////////////////////    
 __        ___   _ ___ _____ _____    _   _ _____ ____   ____ _____ ____ 
 \ \      / / | | |_ _|_   _| ____|  | | | | ____|  _ \ / ___| ____/ ___|
  \ \ /\ / /| |_| || |  | | |  _|    | |_| |  _| | |_) | |   |  _|| |  _ 
   \ V  V / |  _  || |  | | | |___   |  _  | |___|  _ <| |___| |__| |_| |
    \_/\_/  |_| |_|___| |_| |_____|  |_| |_|_____|_| \_\\____|_____\____|

///////////////////////////////////////////////////////////////////////////
    """)
    show_info()

    while True:
        user_input = input("\n> ").strip().split()
        if not user_input:
            continue

        command = user_input[0]
        args = user_input[1:]

        if command=="1":
            show_info()
        elif command=="2":
            scanning_pc()
        elif command=="3":
            pc_info()
        elif command=="4":
            check_disk_for_errors()
        elif command=="5":
            information()
        elif command=="6":
            print("Exit programm...")
            break
        else:
            print("Unknown team. Enter the help_command command")



if __name__ == "__main__":
    main()
