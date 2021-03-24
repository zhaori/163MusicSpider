"""
调用了Windows系统下的DOS命令

"""

import os


def sys_move(old_folder, new_folder):
    # 移动文件
    os.system(r'move /y {} {} '.format(old_folder, new_folder))


def sys_copy(old_file, new_file):
    # 复制文件
    os.system(r'copy {} {}'.format(old_file, new_file))


def copy_folder(old_folder, new_folder):
    # 复制文件夹
    os.system(r'xcopy {} {} /S /H /E /Y'.format(old_folder, new_folder))


def del_file(file):
    # 删除文件
    os.system("del {} /s /f /q".format(file))


def del_folder(folder):
    # 删除文件夹
    os.system("rd /s/q {}".format(folder))


def kill_pid(pid):
    # 根据进程号杀死进程
    os.system(f"taskkill/pid {pid} -f")


SYSTEM_TEMP = str(os.popen("echo %temp%").readline()).strip('\n')
