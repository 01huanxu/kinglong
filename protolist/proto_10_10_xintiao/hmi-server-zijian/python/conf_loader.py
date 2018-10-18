# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Authors: ligaifan(ligaifan@baidu.com)
Date:    2018/06/10 16:16:49
""" 
import os
import sys
import yaml
import textwrap
import sys


class ConfLoader(object):
    """
    Convert yaml file to dict variables, and write the variables back to the yaml file
    """
    def __init__(self, filename):
        self.filename = filename

    def abs_filepath(self, filename):
        """
        Get a standard absolute file path
        The default directory should be under the 'utils/../'
        """
        # If it's a relative path, then convert it to absolutely path
        # Else, directly pass the 'filename' argument
        if filename and filename[0] != '/':
            relative_path = os.path.dirname(os.path.realpath(__file__))
            # the filename should be under the main dir : util/../filename
            filename = relative_path + '/' + filename 

        return filename

    def read_conf(self, filename):
        """
        Read the params from the 'filename' file.
        return: {} or list values
        """
        if not filename:
            return {}
        parms = {}
        try:
            f = open(self.abs_filepath(filename))
            parms = yaml.load(f)
            # all upper
            parms.update({k:v for k, v in parms.items()})
            f.close()
        except Exception as e:
            print e
        return parms

    @property
    def prms(self):
        """
        get a dict variable from the yaml file
        """
        return self.read_conf(self.filename)


if __name__ == '__main__':
    """
    only for debug
    """
    st = ConfLoader('../conf/testinfo.yaml')
    print "params: ", st.prms
