#!/usr/bin/python3
""" Write a Fabric py script that generates a .tgz archive
 from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function to generate a .tgz archive """
    local('mkdir -p versions')
    tar_dir = local("tar -czvf versions/web_static_{}.tgz web_static/".format((
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))), capture=True)

    if tar_dir.succeeded:
        return tar_dir
    return None
