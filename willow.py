import argparse

from api import willowapi


parser = argparse.ArgumentParser(description='Willow. The Python build system')

parser.add_argument('--create', metavar='create', type=str,
                    help='Name of the project to create')

parser.add_argument('--location', metavar='location', type=str,
                    help='Location where the project should be created')

parser.add_argument('--compile', metavar='compile', type=str,
                    help='directory of the project that should be compiled')

parser.add_argument('--delete', metavar='delete', type=str,
                    help='directory of the project that should be deleted')

parser.add_argument('--add', metavar='adddep', type=str,
                    help='directory of the project that a dependency should be added to')

parser.add_argument('--depname', metavar='depname', type=str,
                    help='name of the dependency to be added to a project')

parser.add_argument('--scan', metavar='scan', type=str,
                    help='Name of the project to scan')

parser.add_argument('--run', metavar='scan', type=str,
                    help='Name of the project to run')

parser.add_argument('--version', nargs="?", const=True,
                    help='Willow Version')

parser.add_argument('--fix', metavar='scan', type=str,
                    help='Name of the project to fix')

parser.add_argument('--backup', metavar='scan', type=str,
                    help='Name of the project to backup')


args = parser.parse_args()

if args.create and args.location:
    import os
    if args.location == "?CURRENT": # Or you can just use '.'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        willowapi.create(args.create, dir_path)
    else:
        willowapi.create(args.create, args.location)

if args.compile:
    willowapi.compile(args.compile)

if args.delete:
    willowapi.delete(args.delete)

if args.add and args.location and args.depname:
    willowapi.add_dependency(args.add, args.location, args.depname)

if args.version:
    print(willowapi.version())

if args.scan:
    willowapi.scan(args.scan)

if args.run:
    willowapi.run(args.run)

if args.fix:
    willowapi.fix(args.fix)

if args.backup:
    willowapi.backup(args.backup)
