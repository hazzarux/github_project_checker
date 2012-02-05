#!/usr/bin/python2.7
# -*- coding: utf-8 -*-



"""
-- github_project_checker.py --
Created on Mon Sep 26 22:17:12 2011

@licence: GNU GPL v3+
@author: Yigit Ozkan < yigitozkan2804@gmail.com >
"""

import os
import commands

def get_home_path(): #gets the home path of the user
    home_dir = os.getenv("HOME")
    #print "home path is: "+home_dir
    return home_dir

def get_all_subdirs(directory): #adds full path to dir and then returns list of subdirectories
    list_of_subdirs = os.walk(directory).next()[1]
    subdirs=[]
    for subdir in list_of_subdirs:
        subdir2=os.path.join(directory,subdir)
        subdirs.append(subdir2)
    #print subdirs
    return subdirs
    
def get_subdirs(directory): #simply gets dirs :)
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]

def main():
    #os.system('clear')
    home = get_home_path()
    #print "home path ready to be analyzed: "+home
    subdirs = get_all_subdirs(home)
    #print "all subdirs ready to be analyzed."
    github_dirs=[]
    #print "github repos found:"
    for subdir in subdirs:
        if ".git" in get_subdirs(subdir):
            #print subdir
            if "project_checker" not in subdir:
                github_dirs.append(subdir)
    for project in github_dirs:
        #print "            "+project
        output = commands.getoutput('cd '+ project + '; git status')
        #print output
        if 'clean' not in output:
            print 'problem with '+project
    print "ALL SET, CAPTAIN!"
    
if __name__ == '__main__':
    main()
