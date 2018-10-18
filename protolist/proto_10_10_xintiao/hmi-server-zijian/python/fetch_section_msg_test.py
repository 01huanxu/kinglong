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
import random


class FetchSectionMsgTest(unittest.TestCase):
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
        env_utils.play_record('channel_test.record')

    def tearDown(self):
        time.sleep(2)
        env_utils.stop_hmi_server()

    def test_fetch_no_ultrasonic(self):
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.ULTRASONIC)
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        response = stub.FetchSectionMsg(request)
        print("Response: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('ultrasonic'), response)

    def test_fetch_device(self):
        env_utils.play_record('chassis.record')
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.DEVICE)
        print("Request: " + str(request))

        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        response = stub.FetchSectionMsg(request)
        print("Response: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        device = response.device
        self.assertTrue(device.HasField('timestamp'), device)
        self.assertTrue(device.HasField('dump_energy'), device)
        self.assertTrue(device.HasField('door'), device)
        self.assertTrue(device.HasField('head_lamp'), device)
        self.assertTrue(device.HasField('front_lamp'), device)
        self.assertTrue(device.HasField('emergency_lamp'), device)
        self.assertTrue(device.HasField('courtesy_lamp'), device)
        self.assertTrue(device.HasField('air_condition'), device)
        self.assertTrue(device.HasField('driving_range'), device)
        self.assertTrue(device.HasField('server_init_timestamp'), device)
        self.assertTrue(device.HasField('vin'), device)
        self.assertTrue(device.HasField('charge_state'), device)
        self.assertTrue(device.HasField('parking_brake'), device)
        self.assertTrue(device.HasField('carid'), device)
        self.assertTrue(device.HasField('gear_location'), device)

    def test_fetch_ultrasonic(self):
        env_utils.play_record('ultrasonic.record')
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.ULTRASONIC)
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

        try:
            response = stub.FetchSectionMsg(request)
        except Exception as e:
            print(str(e))
        print("Response: " + str(response))

        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('ultrasonic'), response)
        self.assertTrue(len(response.ultrasonic.ranges) == 16, response)

    def test_fetch_low_illumination(self):
        env_utils.play_record('perception_obstacles.record')
        # env_utils.play_record('ultrasonic.record')
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.OBSTACLES)
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(15)
        response = stub.FetchSectionMsg(request)
        # print("Response: " + str(response))
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('obstacles'), response)
        word_obstacles = response.obstacles
        self.assertTrue(word_obstacles.HasField('low_illumination'), word_obstacles)
        self.assertTrue(word_obstacles.HasField('timestamp'), word_obstacles)
        print("low_illumination: " + str(word_obstacles.low_illumination))
        obstacles_list = word_obstacles.obstacles
        obstacle = obstacles_list[0]
        self.assertTrue(obstacle.HasField('id'), obstacle)
        self.assertTrue(obstacle.HasField('type'), obstacle)
        self.assertTrue(obstacle.HasField('heading'), obstacle)
        self.assertTrue(obstacle.HasField('position'), obstacle)
        self.assertTrue(obstacle.HasField('length'), obstacle)
        self.assertTrue(obstacle.HasField('width'), obstacle)
        self.assertTrue(obstacle.HasField('height'), obstacle)

    def call_fetch_api(self, fetch_key):
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(fetch_key)
        print("Request: " + str(request))
        host_port = "127.0.0.1:" + self.random_port
        channel = grpc.insecure_channel(host_port)
        stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
        response = stub.FetchSectionMsg(request)
        return response

    def test_fetch_adc(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.ADC_STATUS)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('adc'), response)

    def test_fetch_operation_status(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.OPERATION_STATUS)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('operate'), response)
    
    def test_fetch_routing(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.ROUTING)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('routing'), response)

    def test_fetch_prediction(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.PREDICTION)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('obstacles'), response)
    
    def test_fetch_traffic_light(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.TRAFFIC_LIGHT)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('obstacles'), response)
    
    def test_fetch_monitor(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.MONITOR)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('monitor'), response)

    def test_fetch_hud_info(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.HUD_INFO)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('hud_info'), response)

    def test_fetch_sys_state(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.SYS_STATE)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('sys_state'), response)

    def test_fetch_ota_status(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.OTA_STATUS)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertTrue(response.HasField('ota_status'), response)

    def test_fetch_ultrasonic_info(self):
        response = self.call_fetch_api(hmi_fetch_msg_pb2.ULTRASONIC_INFO)
        self.assertTrue(response.code == hmi_error_code_pb2.OK, response)
        self.assertFalse(response.HasField('ultrasonic_info'), response)

if __name__ == '__main__':
    unittest.main(testRunner=g_ut.GTestStyleRunner())
