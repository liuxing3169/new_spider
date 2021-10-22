"""文件助手
"""
import os

def repos_init():
    path = './logs'
    if not os.path.exists(path):
        os.mkdir(path)
    # if not os.path.exists(path + '/debug'):
    #     os.mkdir(path + '/debug')
    if not os.path.exists(path + '/news'):
        os.mkdir(path + '/news')