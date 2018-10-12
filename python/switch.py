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
import hmi_car_device_pb2
import random


class SwitchContlMsgTest(unittest.TestCase):
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
#        env_utils.play_record('channel_test.record')

    def tearDown(self):
        time.sleep(2)
        env_utils.stop_hmi_server()
"""
    def test_switch_control_api(self,control_switch):
        request = hmi_car_devive_pb2.DeciveControlRequest()
        request.action.append(control_switch)
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
        return (stub,request)
    
    def test_swith_control(self):
        stub,request= test_switch_control_api(hmi_car_devive_pb2.ON)
        response = stub.SwitchDoor(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

    def test_aircondition_control(self,air_conditon_switch):
        request = hmi_car_devive_pb2.AirConditionRequest(1,2,2,3,1)  
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
        response = stub.NotiAirCondition(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

    def test_alarm_horn(self):
        request = hmi_car_devive_pb2.TriggerRequest(1,2)  
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
        response = stub.TriggerAlarmHorn(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)
"""    

    def test_emergency_stop(self):
        print("Request: " )
        request = hmi_car_device_pb2.TriggerRequest(header=1.0 ,bool_flag=True)  
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
	try:
        	response = stub.TriggerEmergencyStop(request)
	except Exception,e:
    		print ('Error: err,str(Exception)',str(e))
        print("Request: " )
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        print("Request: " )
        self.assertTrue(response.HasField('info'), response)
    
    
        
if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())

