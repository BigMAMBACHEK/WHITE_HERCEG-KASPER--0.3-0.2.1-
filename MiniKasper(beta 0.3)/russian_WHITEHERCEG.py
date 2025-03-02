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
    "[1]help_command":"Отображает доступные команды",
    "[2]pc_information":"Отображает информацию о компьютере",
    "[3]scanning_for_suspicious_processes":"Проверяет ваш компьютер на наличие подозрительных процессов",
    "[4]checking_disks_for_errors":"Проверяет диски на наличие ошибок",
    "[5]":"Что нового в программе",
    "[6]exit":"Выход из программы"
}

def show_info():
    print("Доступные команды:")
    for cmd, desc in commands.items():
        print(f"  {cmd}: {desc}")

known_miners_and_viruses=["xmrig","minered","ccmier","trojan"]

def scanning_pc():
    suspicious_processes = []
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'].lower() in known_miners_and_viruses:
            suspicious_processes.append((process.info['name'], process.info['pid']))
    if suspicious_processes:
        message = "Обнаружены подозрительные процессы:\n"
        for name, pid in suspicious_processes:
            message += f"{name} (PID: {pid})\n"
        print(message)
    else:
        print("Подозрительных процессов обнаружено не было. Ваша система чиста!")

def pc_info():
    cpu_count = psutil.cpu_count(logical=True) 
    cpu_freq = psutil.cpu_freq()  
    print(f"Процессор {cpu_count} логические ядра")
    print(f"Частота процессора: {cpu_freq.current:.2f} МГц")


    virtual_mem = psutil.virtual_memory()
    print(f"Оперативная память: {virtual_mem.total / (1024 ** 3):.2f} GB")
    print(f"Доступно: {virtual_mem.available / (1024 ** 3):.2f} GB")


    print("\nДиск:")
    for partition in psutil.disk_partitions():
        print(f"Диск: {partition.device}")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  Всего: {usage.total / (1024 ** 3):.2f} GB")
        print(f"  ИСпользовано: {usage.used / (1024 ** 3):.2f} GB")
        print(f"  ДОступно: {usage.free / (1024 ** 3):.2f} GB")


    if psutil.sensors_battery():
        battery = psutil.sensors_battery()
        print("\nБатарея")
        print(f" Уровень заряда: {battery.percent}%")
        print(f"  Время автономной работы: {battery.secsleft // 60} min")
    else:
        print("\nБатарея не обнаружена")

def list_drives():
    partitions = psutil.disk_partitions()
    drives = [partition.device for partition in partitions]
    return drives

def check_disk_for_errors():
    try:
        drives = list_drives()
        if not drives:
            print("Диски были не найдены")
            return

        print("Доступные диски:")
        for i, drive in enumerate(drives):
            print(f"{i + 1}: {drive}")

        choice = int(input("Выберите номер диска для проверки: "))
        if choice < 1 or choice > len(drives):
            print("Неправильный выбор.")
            return

        drive = drives[choice - 1]
        command = f'chkdsk {drive}'
        result = os.system(command)

        if result == 0:
            print(f"Диск{drive} проверен, ошибок не обнаружено.")
        else:
            print(f"На диске {drive} была обнаружена ошибка.")
    except Exception as e:
        print(f"При проверке диска произошла ошибка: {e}")

known_suspicious_processes = [
    "xmrig", "minered", "ccminer", "trojan", "keylogger", "malware-inject"
]

def check_pc_on_process():
    suspicious_processes = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            if process_name in known_suspicious_processes:
                suspicious_processes.append((process.info['name'], process.info['pid']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if suspicious_processes:
        print("Обнаружены подозрительные процессы:")
        for name, pid in suspicious_processes:
            print(f"  {name} (PID: {pid})")

        choice = input("Вы хотите завершить эти процессы? (Y/n): ").strip().lower()
        if choice == "Y":
            for name, pid in suspicious_processes:
                try:
                    process = psutil.Process(pid)
                    process.terminate()  # Завершение процесса
                    print(f"Процесс {name} (PID: {pid}) был остановлен!")
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(f"Не удалось завершить процесс {name} (PID: {pid}): {e}")
        else:
            print("Завершение процесса было отменено.")
    else:
        print("Никаких подозрительных процессов обнаружено не было.")

def information():
    print("""Программа отключила команду сканировать открытые порты на вашем компьютере. 
             Она переделывается и проходит тестирование. Поиск ошибок и других проблем также будет проведен позже. 
             Чтобы связаться со мной в плане находок ошибок или еще чего-то, напишите в telegram: @dark_herceg_exe""")

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
            print("Выход из программы...")
            break
        else:
            print("Неизвестная команда. Введите команду help_command")



if __name__ == "__main__":
    main()
