# Willow


Willow is a Python build system that can be used to create, compile, delete, scan projects, and add dependencies to projects. It is a command-line tool that can be used to automate various tasks related to building and managing software projects.

# Usage
To use Willow, you can run the script with various command-line arguments:

# --create
To create a new project, you can use the --create flag followed by the name of the project and the location where it should be created:

python willow.py --create myproject --location /path/to/project
This will create a new project called myproject in the /path/to/project directory.

# --compile
To compile a project, you can use the --compile flag followed by the directory of the project that should be compiled:

willow --compile /path/to/project
This will compile the project located at /path/to/project.

# --delete
To delete a project, you can use the --delete flag followed by the directory of the project that should be deleted:

willow --delete /path/to/project
This will delete the project located at /path/to/project.

# --add
To add a dependency to a project, you can use the --add flag followed by the directory of the project, the location of the dependency, and the name of the dependency:

willow --add GITHUB-URL --location /path/to/project --depname mydependency
This will add the mydependency dependency located at /path/to/project

# --version
To get the current version of Willow, you can use the --version flag:

willow --version
This will print the current version of Willow to the console.

# --scan
To scan a project for any dependencies that does not come with python, use the --scan flag:
willow --scan project-name
This will return a list of things and add it to a file located in project-name/willow/build-dependencies/
Files with syntax errors are not included and give an error.

# --run
Creates a "test" folder in willow/ with the executable, use the --run flag:
willow --run project-name

# --fix
Fixes any folders that may have been deleted, use the --fix flag:
willow --fix project-name

# --backup
Back up a project, use the --backup flag:
willow --backup project-name
This will create a folder in the root directory of willow with a backup including the time and date.


# API
Willow also provides an API that can be used to perform the same tasks programmatically. These are some of the Willow-api functions:

create(name, location): creates a new project with the specified name at the specified location. </br>
compile(directory): compiles the project located at the specified directory. </br>
delete(directory): deletes the project located at the specified directory. </br>
add_dependency(project_dir, dep_dir, depname): adds the specified dependency to the project located at project_dir. </br>
version(): returns the current version of Willow. </br>
scan(directory): scans a project and search for dependencies to create a requirements.txt. </br>

Willow is a powerful tool for building and managing software projects in Python. It provides a simple command-line interface as well as a powerful API for performing tasks programmatically. If you're looking for a reliable and flexible build system for your Python projects, Willow is definitely worth checking out.

# Building
### Check the wiki for building willow

# Project
Make sure to star it if you like it ⭐️
