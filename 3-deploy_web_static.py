#!/usr/bin/python3
""" Write a Fabric script that distributes an archive
to my web servers
"""
from fabric.api import local, env, run, put
from datetime import datetime
from os.path import exists

env.hosts = ['52.87.251.222', '54.89.194.182']


def do_pack():
    """Function to generate a .tgz archive]"""
    local('mkdir -p versions')
    tar_dir = local("tar -czvf versions/web_static_{}.tgz web_static/".format((
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))), capture=True)

    if tar_dir.succeeded:
        return tar_dir
    return None


def do_deploy(archive_path):
    """Function to deploy an archive to my web servers"""
    if exists(archive_path):

        file_path = archive_path.split("/")[1]

        serv_path = "/data/web_static/releases/{}".format(
            file_path.replace(".tgz", ""))
        put('{}'.format(archive_path), '/tmp/')
        # ???
        run('mkdir -p {}'.format(serv_path))
 
        run('tar -xzf /tmp/{} -C {}/'.format(
            file_path,
            serv_path))

        run('rm /tmp/{}'.format(file_path))

        run('mv -f {}/web_static/* {}/'.format(serv_path, serv_path))

        run('rm -rf {}/web_static'.format(
            serv_path))

        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(
            serv_path))

        return True
    else:
        return False
    

def deploy():
    """Deploy archive to my two servers"""
    archive = do_pack()
    if archive is None:
        return False
    else:
        value = archive.__dict__["command"].split(" ")[-2]
        print(value)
        return do_deploy(value)
