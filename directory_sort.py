#!/usr/bin/env python

#Author = Brandon Papp
#Written = 10-Dec-2015
#Modified = 11-Dec-2015

#Takes in a command line argument and if its a directory it will sort every file by size

import sys
import os

if sys.version_info.major != 2:
    print("This program requires Python 2. Please install and run this program with Python 2")

def main():
    #Take command line argument
    directory = os.path.abspath(sys.argv[1])
    paths = []

    #Run if argument passed is a valid directory
    if os.path.isdir(directory):
        #Add all file paths found in given directory tree
        paths = ( os.path.join(basedir, filename) for basedir, dirs, files in os.walk(directory) for filename in files)

        #Sort list of files based on size
        sorted_files = sorted(paths, key = os.path.getsize)

        #Write each entry to stdout
        i = 0
        while i < len(sorted_files):
            sys.stdout.write(sorted_files[i] + '\n')
            i = i + 1

    #Command line argument is not a directory
    else:
        print "Error path not found!"


if __name__ == "__main__":
    main()
