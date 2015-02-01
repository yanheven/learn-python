'''
Created on Dec 14, 2014

@author: hyphen
'''
import argparse
def parseArgs(args=None):
    parser=argparse.ArgumentParser(
                                   description="test cmd argparse")
    
    parser.add_argument('test cmd',
                        action='store',
                        nargs='+',
                        help='desc of the cmd')
    
    parser.add_argument('-h',
                        'help',
                        dest='help',
                        action='store',
                        default=None,
                        help='this help')
    
if __name__=='__mani__':
    parseArgs()
    