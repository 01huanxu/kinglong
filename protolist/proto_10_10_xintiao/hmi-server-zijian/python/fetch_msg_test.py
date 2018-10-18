from __future__ import print_function

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')

import time
import grpc
import hmi_common_pb2
import hmi_error_code_pb2
import hmi_grpc_api_pb2_grpc
import hmi_fetch_msg_pb2
import random

def start():
    host_port = "127.0.0.1:8090"
    channel = grpc.insecure_channel(host_port)
    stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
    time.sleep(5)
    return stub

def fetch_msg_test(stub):
    request = hmi_fetch_msg_pb2.FetchKeys()  
    request.keys.append(hmi_fetch_msg_pb2.OPERATION_STATUS)        
    response = stub.FetchSectionMsg(request)
    print (str(response))

def main():
    stub=start()
    while True :
        time.sleep(1)
        fetch_msg_test(stub)


if __name__ == '__main__':
    main()
   
