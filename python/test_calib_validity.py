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

import grpc
import time

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')

import hmi_grpc_api_pb2_grpc
import hmi_world_pb2
import conf_loader


def run():
    cf = conf_loader.ConfLoader("testinfo.yaml")
    prms = cf.prms['CalibrationValidityRequest']
    print("CalibrationValidityRequest: " + str(prms))

    request = hmi_world_pb2.CalibrationValidityRequest(type=prms['type'])

    channel = grpc.insecure_channel("172.20.72.16:8090")
    stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

    print("Client request: " + str(request))

    response = stub.CheckCalibrationValidity(request)
    print("Greeter client received: " + str(response))

    time.sleep(2)


if __name__ == '__main__':
    run()
