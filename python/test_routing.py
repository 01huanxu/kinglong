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
import hmi_routing_pb2
import hmi_common_pb2
import common_geometry_pb2
import conf_loader


def run():
    cf = conf_loader.ConfLoader("testinfo.yaml")
    prms = cf.prms['RoutingRequest_xiongan']
    print(str(prms))

    request = hmi_routing_pb2.RoutingRequest(\
        start=hmi_common_pb2.PolygonPoint(\
            x=prms['start']['x'], y=prms['start']['y'], z=prms['start']['z']),
        end=hmi_common_pb2.PolygonPoint(\
            x=prms['end']['x'], y=prms['end']['y'], z=prms['end']['z']),
        start_quaternion=common_geometry_pb2.Quaternion(\
            qx=prms['start_quaternion']['qx'], qy=prms['start_quaternion']['qy'],\
            qz=prms['start_quaternion']['qz'], qw=prms['start_quaternion']['qw']),
        end_quaternion=common_geometry_pb2.Quaternion(\
            qx=prms['end_quaternion']['qx'], qy=prms['end_quaternion']['qy'],\
            qz=prms['end_quaternion']['qz'], qw=prms['end_quaternion']['qw'])
        )

    channel = grpc.insecure_channel("172.20.72.16:8090")
    stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

    print("Client request: " + str(request))

    response = stub.StartRouting(request)
    print("Greeter client received: " + str(response))

    time.sleep(2)


if __name__ == '__main__':
    run()
