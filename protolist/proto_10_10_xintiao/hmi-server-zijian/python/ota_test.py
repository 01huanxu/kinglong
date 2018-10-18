#!/usr/bin/env python
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
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
import random
import hmi_ota_pb2


class OtaTest(unittest.TestCase):
    random_port = ""
    """
    Fetch test cases.
    """

    def setUp(self):
        self.random_port = str(random.randint(8000,9000))
        flags = {
            'hmi_server_host': '.0.0.1',
            'hmi_server_port': self.random_port,
            'hmi_camera_params_path': os.path.abspath(os.path.dirname(__file__)) + '/params',
        }
        try:
            env_utils.start_hmi_server(flags)
        except Exception as e:
            print(str(e))            
        # env_utils.play_record('channel_test.record')

    def tearDown(self):
        time.sleep(2)
        # env_utils.stop_hmi_server()
        
    def send_ota_msg(self, msg):
        request = hmi_ota_pb2.OtaRequest()
        try:
            request.action = msg
        except Exception as e:
            print(str(e))
        channel = grpc.insecure_channel("127.0.0.1:" + self.random_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        response = stub.NotiOTAClient(request)
        return response

    def test_start_upgrade(self):
        msg = hmi_ota_pb2.START_UPGRADE
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OTA_ERROR, response)
        print("Response: " + str(response))

    def test_has_oper_upgrade(self):
        msg = hmi_ota_pb2.HAS_OPER_UPGRADE
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OTA_ERROR, response)
        print("Response: " + str(response))

    def test_get_upgrade_result(self):
        msg = hmi_ota_pb2.GET_UPGRADE_RESULT
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OTA_ERROR, response)
        print("Response: " + str(response))

    def test_has_upgrade_description(self):
        msg = hmi_ota_pb2.HAS_UPGRADE_DESCRIPTION
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OTA_ERROR, response)
        print("Response: " + str(response))

    def test_has_oper_upgrade(self):
        msg = hmi_ota_pb2.HAS_OPER_UPGRADE
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OTA_ERROR, response)
        print("Response: " + str(response))


    def test_oper_upgrade_install(self):
        msg = hmi_ota_pb2.OPER_UPGRADE_INSTALL
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OTA_ERROR, response)
        print("Response: " + str(response))

    def test_oper_upgrade_ignore(self):
        msg = hmi_ota_pb2.OPER_UPGRADE_IGNORE
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OTA_ERROR, response)
        print("Response: " + str(response))

if __name__ == '__main__':
    try:
        unittest.main(testRunner=g_ut.GTestStyleRunner())
    except Exception as e:
        print(str(e))
