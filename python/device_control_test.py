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

    def hmi_assert_true(self,response):
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

    def switch_control_api(self,control_switch):
        request = hmi_car_device_pb2.DeciveControlRequest(action=control_switch)
        #request.action.append(control_switch)
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        self.stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(1)
        return request

    def multi_enmu_type_test(self,func):
        test_enum_datas=[hmi_car_device_pb2.ON,hmi_car_device_pb2.OFF]
        for test_enum_data in test_enum_datas:
            print("Request: " + str(test_enum_data))
            request=self.switch_control_api(test_enum_data)
            response = func(request)
            self.hmi_assert_true(response)

    def test_swith_door_control(self):
        self.multi_enmu_type_test(self.stub.SwitchDoor)
                    
'''
    def test_swith_headlights_control(self):
        test_enum_datas=[hmi_car_device_pb2.ON,hmi_car_device_pb2.OFF]
        for test_enum_data in test_enum_datas:
            print("Request: " + str(test_enum_data))
            stub,request=self.switch_control_api(test_enum_data)
            response = stub.SwitchHeadLights(request)
            self.hmi_assert_true(response)
       

    def test_swith_frontlamp_control(self):
        try:
            stub,request=self.switch_control_api(hmi_car_device_pb2.ON)
        except Exception,e:
            print ("Error: err,str(Exception)"+str(e))
        
        response = stub.SwitchFrontLamp(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

        try:
            stub,request=self.switch_control_api(hmi_car_device_pb2.OFF)
        except Exception,e:
            print ("Error: err,str(Exception)"+str(e))
        
        response = stub.SwitchFrontLamp(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

    def test_swith_emergencylamp_control(self):
        try:
            stub,request=self.switch_control_api(hmi_car_device_pb2.ON)
        except Exception,e:
            print ("Error: err,str(Exception)"+str(e))
        
        response = stub.SwitchEmergencyLamp(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

        try:
            stub,request=self.switch_control_api(hmi_car_device_pb2.ON)
        except Exception,e:
            print ("Error: err,str(Exception)"+str(e))
        
        response = stub.SwitchEmergencyLamp(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OFF, response)
        self.assertTrue(response.HasField('info'), response)


    def test_swith_courtesylamp_control(self):
        try:
            stub,request=self.switch_control_api(hmi_car_device_pb2.ON)
        except Exception,e:
            print ("Error: err,str(Exception)"+str(e))
        
        response = stub.SwitchCourtesyLamp(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

        try:
            stub,request=self.switch_control_api(hmi_car_device_pb2.OFF)
        except Exception,e:
            print ("Error: err,str(Exception)"+str(e))
        
        response = stub.SwitchCourtesyLamp(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)


    def test_aircondition_control(self):       
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
        request = hmi_car_device_pb2.AirConditionRequest(header=1,temperature=25,mode=hmi_car_device_pb2.ECO, fan=3,open=True)  
        print("Request: " + str(request))
        response = stub.NotiAirCondition(request)                
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

        time.sleep(1)
        request = hmi_car_device_pb2.AirConditionRequest(header=1,temperature=25,mode=hmi_car_device_pb2.COLD, fan=3,open=True)  
        response = stub.NotiAirCondition(request)                
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

        time.sleep(1)       
        request = hmi_car_device_pb2.AirConditionRequest(header=1,temperature=25,mode=hmi_car_device_pb2.WARM, fan=3,open=True)  
        response = stub.NotiAirCondition(request)                
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

        time.sleep(1)
        request = hmi_car_device_pb2.AirConditionRequest(header=1,temperature=25,mode=hmi_car_device_pb2.FAN, fan=3,open=True)  
        response = stub.NotiAirCondition(request)                
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)  

        time.sleep(1)
        request = hmi_car_device_pb2.AirConditionRequest(header=1,temperature=25,mode=hmi_car_device_pb2.AUTO_MODE, fan=3,open=True)
        response = stub.NotiAirCondition(request)                
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)  


    def test_alarm_horn(self):
        request = hmi_car_device_pb2.TriggerRequest(header=1,bool_flag=True)  
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
        response = stub.TriggerAlarmHorn(request)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)

    def test_emergency_stop(self):
        print("Request: " )    
        try:
            request = hmi_car_device_pb2.TriggerRequest(header=1.0 ,bool_flag=True)  
        except Exception,e:
            print ('Error: err,str(Exception)',str(e))
        
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(2)

        try:
            response = stub.TriggerEmergencyStop(request)
        except Exception,e:
            print ('Error: err,str(Exception)',str(e))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('info'), response)
 '''   
        
if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())

