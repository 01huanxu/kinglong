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
import hmi_car_device_pb2
import hmi_fetch_msg_pb2
import ota_pb2
import random
import thread
import threading
import env_utils
import hmi_ota_pb2

Local_test=True
class simulate_trigger(object):
    
    is_class_init=False
    stub=None
    def __init__(self):
        if self.__class__.is_class_init==False:
            if Local_test is True:
                self.server_init()
            self.class_init()
            self.__class__.is_class_init=True

    def server_init(self):
        flags = {
            'hmi_server_host': '127.0.0.1',
            'hmi_server_port': 9898,
            'hmi_camera_params_path': os.path.abspath(os.path.dirname(__file__)) + '/params',
        }
        env_utils.start_hmi_server(flags)

    def class_init(self):
        print('class init')
        if Local_test is True:
            host_port = "127.0.0.1:9898"
        else :  
            host_port = "192.168.10.6:8090"
        channel = grpc.insecure_channel(host_port)
        self.request_list=[]
        self.response_list=[]
        self.semaphore = threading.Semaphore(0)
        self.t_list=[]
        self.__class__.stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)
        time.sleep(5)
    
    def trigger_fetch(self):
        request = hmi_fetch_msg_pb2.FetchKeys()
        request.keys.append(hmi_fetch_msg_pb2.ALL)
        response = self.__class__.stub.FetchSectionMsg(request)
        print(response)

    def trigger(self):
        request = hmi_car_device_pb2.TriggerRequest(header=1.0 ,bool_flag=True)
        try:
            response = self.__class__.stub.TriggerEmergencyStop(request)
        except Exception,e:
            print ('Error: err,str(Exception)',str(e))

    def multi_trigger(self):
         for i in range(2000):
             self.trigger_fetch()

    def multi_threads(self):
        thread_list=[]
        for i in range(2000):
            t1 = threading.Thread(target=self.multi_trigger)
            t1.start()
            print("threas id is %d :"%i)    
        for thread in thread_list:
            thread.join()

if __name__ == '__main__':
    ota_stream=simulate_trigger()
    ota_stream.multi_threads()
   
    
    