#!/usr/bin/python3
"""Module that holds a fucntion for making a tgz archive of web_static"""
import datetime
from fabric.api import local


def do_pack():
    """Function that makes a tgz archive of web_static"""
    local('if [ ! -d "versions" ]; then sudo mkdir "versions"; fi')
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(time)
    result = local("tar -czvf {} web_static".
                   format(file))
    if result.failed:
        return None
    return (file)
