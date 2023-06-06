#!/usr/bin/env python3
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
import subprocess
BASE_ARGV=['pandoc', '--self-contained', '--from=gfm', '--to=html']
def convert_file(inputname, outputname):
    subprocess.check_call(BASE_ARGV+['-o', outputname, '--']+[inputname])
def main():
    convert_file('index.md','index.html')

if __name__ == '__main__':
    main()
