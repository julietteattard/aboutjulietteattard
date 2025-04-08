#!/usr/bin/env python3
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
import subprocess
BASE_ARGV=['pandoc', '--embed-resources', '--standalone','--from=gfm']
TO_HTML=['--to=html']
TO_PDF= ['--to=pdf', '--pdf-engine=weasyprint']

def convert_file(inputname, outputname, outformat, extras=None):
    if not extras:
        extras=[]
    subprocess.check_call(BASE_ARGV+['-o', outputname]+ outformat + extras + ['--', inputname])
def main():
    convert_file('index.md','index.html', TO_HTML)
    convert_file('resume.md','resume.html', TO_HTML, extras=['--css=resume.css'])
    convert_file('resume.md','resume.pdf', TO_PDF, extras=['--css=resume.css'])

if __name__ == '__main__':
    main()
