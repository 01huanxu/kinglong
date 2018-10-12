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
    host_port = "192.168.10.6:8090"
    channel = grpc.insecure_channel(host_port)
    stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
    time.sleep(5)
    return stub

def fetch_msg_test():
#	print(hmi_fetch_msg_pb2.DESCRIPTOR.services_by_name)
	print(hmi_fetch_msg_pb2.DESCRIPTOR.message_types_by_name)
	keys=hmi_fetch_msg_pb2.DESCRIPTOR.message_types_by_name
	for key in keys.items() :
	    print(key.fileds_by_name[])		
#	keys=hmi_fetch_msg_pb2.DESCRIPTOR.message_types_by_name.keys();
#	print(hmi_grpc_api_pb2_grpc.DESCRIPTOR.services_by_name)
    #request = hmi_fetch_msg_pb2.FetchKeys()  
#    request.keys.append(hmi_fetch_msg_pb2.OPERATION_STATUS)        
 #   response = stub.FetchSectionMsg(request)
  #  print (response.timestamp,response.distance,response.remain_distance,response.reach_station)

def main():
#    stub=start()
  #  while True :
        time.sleep(1)
        fetch_msg_test()


if __name__ == '__main__':
    main()
   
