#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
this script is used to push my notes to github
'''

import os
import argparse
import time

HOME_DIR = os.environ['HOME']
DOCS_DIR = os.path.join(HOME_DIR, 'Documents')
Notes_DIR_NAME = 'Notes'

class GPush(object):

    def __init__(self):
        self.docs_dir = DOCS_DIR
        self.notes_dir_list = []

    def _load_notes_dir(self):
        main_dirs = filter(os.path.isdir, os.listdir(self.docs_dir))
        for d in main_dirs:
            if os.path.exists(os.path.join(d, Notes_DIR_NAME)):
                self.notes_dir_list.append(os.path.join(d, Notes_DIR_NAME))

        return len(self.notes_dir_list)

    def convert_path(self, input_path):
        p = os.path.abspath(input_path)
        if os.path.exists(p):
            return p
        else:
            print(f"The path <{input_path}> is invalid!")
            return False

    def push(self, target_dir, comment):
        target_dir = self.convert_path(target_dir)
        try:
            print(f'Directory----> {target_dir}')
            os.chdir(target_dir)

            print(f'git adding...')
            os.system('git add -A')

            print(f'git commiting <{comment}>')
            os.system(f'git commit -m {comment}')

            print(f'git pushing...')
            os.system('git push origin master')

            return True

        except Exception as e:
            print(e)

    def push_all(self, target_dir_list, comment):
        for target_dir in target_dir_list:
            self.push(target_dir, comment)
        return len(target_dir_list)


def main():
    current_time = time.strftime("%Y-%m-%d %H:%M:$S", time.localtime())
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help='Push all notes to github', action='store_true')
    parser.add_argument('-d', '--dir', help='The target Dir you want to push', action='store_const', const='.', type=str)
    parser.add_argument('comment', help='The git commit comments', type=str, default=f'commit at{current_time}')
    args = parser.parse_args()

    print(f" -a is {args.all} \n  -d is {args.dir} \n  -comment is {args.comment}")

if __name__ == '__main__':
    main()
