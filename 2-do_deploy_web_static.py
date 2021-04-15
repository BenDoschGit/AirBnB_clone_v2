#!/usr/bin/python3
"""Module with function that distributes an archive to your web servers,
using the function do_deploy"""
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os

env.user = 'ubuntu'
env.hosts = ['35.196.75.2', '52.91.170.7']


def do_deploy(archive_path):
    """Function that distributes an archive to your web servers,
    using the function do_deploy"""
    if not os.path.exists(archive_path):
        return False
    temp = archive_path.split("/")
    archive_file = temp[1]
    temp = archive_file.split(".")
    no_extenshion = temp[0]
    new_dir = "/data/web_static/releases/" + no_extenshion + "/"

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(new_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, new_dir))
        run("rm /tmp/{}".format(archive_file))
        run("mv {}web_static/* {}".format(new_dir, new_dir))
        run("rm -rf {}web_static".format(new_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_dir))
        print("New version deployed!")
        return(True)
    except:
        print("Failed")
        return False
