#!/usr/bin/python2.7
# -*- coding: utf-8 -*-



"""
-- github_project_checker.py --
Created on Mon Sep 26 22:17:12 2011

@licence: GNU GPL v3+
@author: Yigit Ozkan < yigitozkan2804@gmail.com >
"""

import os

def get_home_path():
    home_dir = os.getenv("HOME")
    #print "home path is: "+home_dir
    return home_dir

def get_all_subdirs(directory):
    list_of_subdirs = os.walk(directory).next()[1]
    subdirs=[]
    for subdir in list_of_subdirs:
        subdir2=os.path.join(directory,subdir)
        subdirs.append(subdir2)
    #print subdirs
    return subdirs
    
def get_all_github_dirs(subdirs):
    for subdir in subdirs:
        if ".git" in get_all_subdirs(subdir):
            print "github repo found: "+subdir
    
    
def main():
    home = get_home_path()
    print "home path is: "+home
    subdirs = get_all_subdirs(home)
    print "all subdirs have been analyzed."
    get_all_github_dirs(subdirs)
    print "all github directories have been analyzed."

if __name__ == '__main__':
    main()
