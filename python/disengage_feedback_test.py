#!/usr/bin/env python
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Authors: wutong14(wutong14@baidu.com)
Date:    2018/06/10 16:16:49
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
import hmi_driving_control_pb2


class DisengageFeedbackTest(unittest.TestCase):
    """
    Disengage feedback test cases.
    """

    def setUp(self):
        flags = {
            'hmi_server_host': '127.0.0.1'
        }
        env_utils.start_hmi_server(flags)
        env_utils.start_data_status_service()

    def tearDown(self):
        env_utils.stop_hmi_server()
        env_utils.stop_data_status_service()

    def test_disengage_feedback(self):
        """
        """
        cf = conf_loader.ConfLoader("testinfo.yaml")
        prms = cf.prms['DisengageTypeContent']
        print(str(prms))

        request = hmi_driving_control_pb2.DisengageTypeContent(
            timestamp=prms['timestamp'], type=prms['type'])

        channel = grpc.insecure_channel("127.0.0.1:8090")
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        print("Client request: " + str(request))

        response = stub.DisengageTypeFeedback(request)
        print("Greeter client received: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK)
        self.assertTrue(response.info == 'disengage update!')

        time.sleep(2)


if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())
