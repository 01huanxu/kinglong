#!/usr/bin/env python
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Authors: yugao(yugao@baidu.com)
Date:    2018/10/03 07:29:31
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
import hmi_collect_data_pb2
import random


class WorkModeTest(unittest.TestCase):
    random_port = ""
    """
    Fetch test cases.
    """

    def setUp(self):
        self.random_port = str(random.randint(8000,9000))
        self.flags = {
            'hmi_server_host': '127.0.0.1',
            'hmi_server_port': self.random_port,
            'hmi_camera_params_path': os.path.abspath(os.path.dirname(__file__)) + '/params',
        }
        env_utils.start_hmi_server(self.flags)
        env_utils.start_parameter_server()

    def tearDown(self):
        time.sleep(2)
        env_utils.stop_hmi_server()
        env_utils.stop_parameter_server()

    def test_fetch_work_state(self):
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.WORK_STATE)
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        response = stub.FetchSectionMsg(request)
        print("Response: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('work_state_result'), response)
        self.assertTrue(response.work_state_result.car_work_mode == hmi_collect_data_pb2.OPER_MODE, response)

    def test_change_work_state(self):
        request = hmi_collect_data_pb2.WorkStateRequest()
        request.car_work_mode = hmi_collect_data_pb2.AID_MODE
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        response = stub.NotiWorkingState(request)
        print("Response: " + str(response))

        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.WORK_STATE)
        print("Request: " + str(request))
        response = stub.FetchSectionMsg(request)
        print("Response: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('work_state_result'), response)
        self.assertTrue(response.work_state_result.car_work_mode == hmi_collect_data_pb2.AID_MODE, response)

    def test_restore_work_state(self):
        request = hmi_collect_data_pb2.WorkStateRequest()
        request.car_work_mode = hmi_collect_data_pb2.AID_MODE
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        response = stub.NotiWorkingState(request)
        print("Response: " + str(response))

        env_utils.stop_hmi_server()
        env_utils.start_hmi_server(self.flags)

        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.WORK_STATE)
        print("Request: " + str(request))
        response = stub.FetchSectionMsg(request)
        print("Response: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('work_state_result'), response)
        self.assertTrue(response.work_state_result.car_work_mode == hmi_collect_data_pb2.AID_MODE, response)

if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())
