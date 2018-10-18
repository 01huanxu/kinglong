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

import grpc
import g_ut
import conf_loader
import env_utils

import hmi_common_pb2
import hmi_error_code_pb2
import hmi_grpc_api_pb2_grpc
import hmi_fetch_msg_pb2


class FetchSectionMsgErrorTest(unittest.TestCase):
    """
    Fetch test cases.
    """

    def setUp(self):
        flags = {
            'hmi_server_host': '127.0.0.1',
            'hmi_ultrasonic_idx_list_file': 'aaa.yaml',
        }
        env_utils.start_hmi_server(flags)

    def tearDown(self):
        time.sleep(2)
        env_utils.stop_hmi_server()

    def test_fetch_ultrasonic(self):
        env_utils.play_record('ultrasonic.record')
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.ULTRASONIC)
        print("Request: " + str(request))

        channel = grpc.insecure_channel("127.0.0.1:8090")
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        response = stub.FetchSectionMsg(request)
        print("Response: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('ultrasonic'), response)


if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())
