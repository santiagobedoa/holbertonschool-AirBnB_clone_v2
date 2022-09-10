#!/usr/bin/python3
""" Cleans deployment"""

from os import listdir, remove
from fabric.api import local, env, run, put
from os.path import exists

env.hosts = ['3.91.84.106', '3.80.230.115']


def do_clean(number=0):
    """ Removes all but given number of archives"""
    num_files = 1 if number == "0" or number == "1" else 2
    try:
        # Remote Files
        dir = "/data/web_static/releases/"
        string = run("for i in %s*; do echo $i; done" % dir)
        files = string.replace("\r", "").split("\n")
        files = sorted(files)[:-1] if num_files == 1 else sorted(files)[:-2]
        for file in files:
            if "web_static_" in file:
                run('rm -rf {}'.format(file))

        # LocalFiles
        Lfiles = listdir("versions")
        Lfiles = sorted(Lfiles)[:-1] if num_files == 1 else sorted(Lfiles)[:-2]
        for file in Lfiles:
            remove("versions/{}".format(file))

    except Exception as e:
        print(e)
