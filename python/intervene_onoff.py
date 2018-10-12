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


request = hmi_driving_control_pb2.InterveneRequest(
    params=global_adc_status_pb2.UserCustomMessage(ignore_blocked_obstacle=bool(int(sys.argv[1]))))

channel = grpc.insecure_channel("127.0.0.1:8090")
stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

print("Client request: " + str(request))

response = stub.Intervene(request)
print("Client received: " + str(response))
