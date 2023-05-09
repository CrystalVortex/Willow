# Imports

from termcolor import colored

from colorama import init

import datetime

from pathlib import Path

import os

import shutil

import random

import time

import requests

import ast

#########################


dt = datetime.datetime.now()


###### Log4py (lpy)

# Important lines:
# Line 202 (Version changing)

init(strip=False)

version = "WLOW [1.0.0] LPY [0.1]"

def LOG_FILE_ENABLED(mode, log_file_name):
    global enabled
    enabled = False
    if mode == True:
        global file
        enabled = True
        file = open(f"{log_file_name}.log", "a")


def INFO(log):
    print(f"[LOG] [INFO] {dt} : {log}")
    if enabled == True:
        file.write(f"[LOG] [INFO] {dt} : {log}\n")


def WARNING(log):
    print(colored(f'[LOG] [WARNING] {dt}: {log}', 'yellow'))
    if enabled == True:
        file.write(f"[LOG] [WARNING] {dt} : {log}\n")

def ERROR(log):
    print(colored(f'[LOG] [ERROR] {dt}: {log}', 'red'))
    if enabled == True:
        file.write(f"[LOG] [ERROR] {dt} : {log}\n")

def DEBUG(log):
    print(colored(f'[LOG] [DEBUG] {dt}: {log}', 'magenta'))
    if enabled == True:
        file.write(f"[LOG] [DEBUG] {dt} : {log}\n")

def SUCCESS(log):
    print(colored(f'[LOG] [SUCCESS] {dt}: {log}', 'green'))
    if enabled == True:
        file.write(f"[LOG] [SUCCESS] {dt} : {log}\n")

LOG_FILE_ENABLED(False, "")



###### API 



def create(name, location):
    INFO(f"Creating project '{name}' in location '{location}'.")

    os.chdir(location)

    Path(name).mkdir(exist_ok=True,parents=True)

    os.chdir(name)

    Path("willow/builds").mkdir(exist_ok=True,parents=True)

    Path("willow/config").mkdir(exist_ok=True,parents=True)

    Path("willow/build-docs").mkdir(exist_ok=True,parents=True)

    Path("source/branches/main/dependencies").mkdir(exist_ok=True,parents=True)

    Path("willow/build-requirements/").mkdir(exist_ok=True,parents=True)

    with open(f"source/branches/main/main.py", mode="w") as f:
        f.write("# Welcome! You can start writing some code here! To add dependencies run 'willow --dependency https://github.com/example/example! --location project-path'. For further documentation please read the wiki on github!")
        f.close()
    return SUCCESS(f"Project is done creating! go to {name}/source/branches/main/main.py to start editing.")


def checkif_willowproject(location):
    import os
    if os.path.isdir(location):
        return True
    else:
        return False

def compile(location):
    if checkif_willowproject(location) == True:

        INFO("Starting...")

        BUILD = random.randint(1,10000)

        os.mkdir(f"{location}/willow/builds/{BUILD}")

        if os.path.exists(f"{location}/source/branches/main/main.py"):

            SUCCESS("Found main.py, building main branch...")

            os.system("pip3 install pyinstaller")

            os.system(f"pyinstaller --onefile --distpath {location}/willow/builds/{BUILD} {location}/source/branches/main/main.py")

            if os.path.isdir("build"):
                INFO("Removing temporary folders...")

                shutil.rmtree("build")
            else:
                ERROR("Failed to delete extra folders. You may have to delete 'build' manuelly.")
            SUCCESS("Done!")
        else:
            ERROR(f"Invalid or corrupt {location}/source/branches/main/main.py")
    else:
        ERROR("invalid location! check your path and try again.")

def delete(location):
    WARNING("Project will be deleted in 10 seconds!!! press control + c on your keyboard to cancel or else your project will be deleted!")

    time.sleep(10)

    WARNING("Deleting...")

    time.sleep(3)

    if checkif_willowproject(location) == True:
        shutil.rmtree(location)

        SUCCESS("Project has been deleted.")
    else:
        ERROR("invalid project. Try checking if its a valid project and try again. Make sure to check the location.")

def add_dependency(url, location, depname):
    if checkif_willowproject(location) == True:

        SUCCESS("Project found. Checking url...")

        response = requests.get(url)

        if response.status_code == 200:
            SUCCESS(f"Download starting...")

            depadd = requests.get(url, allow_redirects=True)

            open(f"{depname}.zip", "wb").write(depadd.content)

            SUCCESS("Download complete...")

            INFO("Unpacking...")

            shutil.unpack_archive(f"{depname}.zip",f"{location}/source/branches/main/dependencies")

            SUCCESS("Unpacking complete...")

            INFO(f"Installing dependencies of {depname}")
            dir_list = os.listdir(f"{location}/source/branches/main/dependencies/")
            for directory in dir_list:
                if directory.startswith(f"{depname}-"):
                    os.system(f"pip3 install -r {location}/source/branches/main/dependencies/{directory}/requirements.txt")
                    
                    os.system(f"pip3 install {location}/source/branches/main/dependencies/{directory}")

                    SUCCESS("Done... Removing temporary files...")

                    os.remove(f"{depname}.zip")

                    SUCCESS("Installed...")

        else:
            ERROR("Invalid URL. Check that its correct or if the website is currently online.")    
        

    else:
        ERROR("Invaid/corrupt project. Try checking the location again.")

def getversion():
    version = "Version: 1.1.0"
    return version

def scan(location):
    root_dir = location+"/source/branches/main/"

    required_modules = set()

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r") as f:
                    try:
                        module_ast = ast.parse(f.read())
                        for node in module_ast.body:
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    SUCCESS(f"Added: {alias.name}")
                                    required_modules.add(alias.name)
                            elif isinstance(node, ast.ImportFrom):
                                required_modules.add(node.module)
                    except SyntaxError:
                        ERROR(f"Syntax Errors in file: {filename}, skipping")

                        pass

    with open(f"{location}/willow/build-requirements/requirements.txt", "w") as f:
        
        f.write("\n".join(sorted(module for module in required_modules if module is not None)))

        SUCCESS("Scan finished. go to /willow/build-requirements/")

