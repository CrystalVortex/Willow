# Willow

Willow
Willow is a Python build system that can be used to create, compile, delete, and add dependencies to projects. It is a command-line tool that can be used to automate various tasks related to building and managing software projects.

# Usage
To use Willow, you can run the script with various command-line arguments:

# --create
To create a new project, you can use the --create flag followed by the name of the project and the location where it should be created:

python willow.py --create myproject --location /path/to/project
This will create a new project called myproject in the /path/to/project directory.

# --compile
To compile a project, you can use the --compile flag followed by the directory of the project that should be compiled:

python willow.py --compile /path/to/project
This will compile the project located at /path/to/project.

--delete
To delete a project, you can use the --delete flag followed by the directory of the project that should be deleted:

python willow.py --delete /path/to/project
This will delete the project located at /path/to/project.

# --add
To add a dependency to a project, you can use the --add flag followed by the directory of the project, the location of the dependency, and the name of the dependency:

python willow.py --add /path/to/project --location /path/to/dependency --depname mydependency
This will add the mydependency dependency located at /path/to/dependency to the project located at /path/to/project.

# --version
To get the current version of Willow, you can use the --version flag:

python willow.py --version
This will print the current version of Willow to the console.

# API
Willow also provides an API that can be used to perform the same tasks programmatically. The willowapi module provides the following functions:

create(name, location): creates a new project with the specified name at the specified location.
compile(directory): compiles the project located at the specified directory.
delete(directory): deletes the project located at the specified directory.
add_dependency(project_dir, dep_dir, depname): adds the specified dependency to the project located at project_dir.
getversion(): returns the current version of Willow.
Conclusion
Willow is a powerful tool for building and managing software projects in Python. It provides a simple command-line interface as well as a powerful API for performing tasks programmatically. If you're looking for a reliable and flexible build system for your Python projects, Willow is definitely worth checking out.
