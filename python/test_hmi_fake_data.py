#test rpc
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Authors: yugao(yugao@baidu.com)
Date:    2018/08/13 18:46:29
"""
from __future__ import print_function

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')

import time
import unittest
import fake_cybertron_data
import grpc
import g_ut
import conf_loader
import env_utils


import hmi_common_pb2
import hmi_error_code_pb2
import hmi_grpc_api_pb2_grpc
import random


class FakeMsgTest(unittest.TestCase):
    random_port = ""
    """
    Fetch test cases.
    """

    def setUp(self):
        self.random_port = str(random.randint(8000,9000))
        flags = {
            'hmi_server_host': '127.0.0.1',
            'hmi_server_port': self.random_port,
            'hmi_camera_params_path': os.path.abspath(os.path.dirname(__file__)) + '/params',
        }
        env_utils.start_hmi_server(flags)

    def tearDown(self):
        time.sleep(2)
        env_utils.stop_hmi_server()
   
    def test_fake_data(self):
       fake_cybertron_data.fake_data_test()

if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())
