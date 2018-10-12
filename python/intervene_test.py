# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Authors: yugao(yugao@baidu.com)
Date:    2018/08/18 19:12:03
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
import global_adc_status_pb2


class InterveneTest(unittest.TestCase):
    """
    User intervene test cases.
    """

    def setUp(self):
        flags = {
            'hmi_server_host': '127.0.0.1'
        }
        env_utils.start_hmi_server(flags)

    def tearDown(self):
        env_utils.stop_hmi_server()
        env_utils.stop_parameter_server()

    def test_intervene(self):
        env_utils.start_parameter_server()

        request = hmi_driving_control_pb2.InterveneRequest(
            params=global_adc_status_pb2.UserCustomMessage(ignore_blocked_obstacle=True))

        channel = grpc.insecure_channel("127.0.0.1:8090")
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        print("Client request: " + str(request))

        response = stub.Intervene(request)
        print("Client received: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK)

        os.system('cyber_param list')

    def test_intervene_error(self):
        request = hmi_driving_control_pb2.InterveneRequest(
            params=global_adc_status_pb2.UserCustomMessage(ignore_blocked_obstacle=True))

        channel = grpc.insecure_channel("127.0.0.1:8090")
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        print("Client request: " + str(request))

        response = stub.Intervene(request)
        print("Client received: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.SET_GLOBAL_PARAM_ERROR)


if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())
