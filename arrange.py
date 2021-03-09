#!/usr/bin/env python3

from os import listdir
from os.path import isdir, abspath
from argparse import ArgumentParser

from classes.DIR import DIR
from classes.File import File

add_dir_help = '''set up a directory to add files to.
When this is used, --ext option has to be used, to specify
the extensions that goes in the new directory'''

ext_help = '''A space separated  of extensions that go into the new directory
specified using the add_dir option.
NOTE, this is not to be used alone. it has to be used with the --add-dir option.'''

parser = ArgumentParser(description='Arrange the given dir')
parser.add_argument('--dir', help='specify a directory to clean (default: Downloads)')
parser.add_argument('--all', help='clean all directories in home/user', action='store_true')
parser.add_argument('--add_dir', help=add_dir_help)
parser.add_argument('--ext', help=ext_help)
args = parser.parse_args()

username = abspath(__name__)[2]


def clean_dir(target_dir):
	dir_contents = listdir(target_dir)
	for file_ in dir_contents:
		file = File(f'{target_dir}/{file_}')
		file.operate()


# User commands
if args.dir:
	clean_dir(args.dir)
elif args.add_dir:
	if args.ext:
		ext = (args.ext.split())
		new_dir = DIR(args.add_dir, ext)
		new_dir.dir_setup()
	else:
		print("Please use --ext option to specify the new directory's extensions")
elif args.ext and not args.add_dir:
	print('Cannot use --ext alone! Refer to help for more')
elif args.all:
	for directory in listdir(f'/home/{username}'):
		if isdir(directory):
			clean_dir(directory)
else:
	clean_dir('Downloads')