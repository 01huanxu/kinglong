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


    def Make_certain_request(self):
        self.request_list=[
            ota_pb2.OtaResponse(status=ota_pb2.CONNECT)
        ]
        for request in self.request_list:
            print(str(request))
            yield request 
            self.semaphore.acquire()
            print("-----------")
             
        
    def read_data(self):
        while True:
            time.sleep(0.5)
            for response in self.response_list:
                self.request_list.append(ota_pb2.OtaResponse(status=ota_pb2.OK))
                self.semaphore.release() 
                print(str(response))

    def Stream_hmi_to_ota(self):
        t1 = threading.Thread(target=self.read_data)
        t2 = threading.Thread(target=self.app_test)
        self.response_list = self.__class__.stub.StreamHmiToOta(self.Make_certain_request())
        t1.start()
        t2.start()
        t1.join()
        t2.join()

            
    def Make_ota_request(self):
        request_list=[ota_pb2.OtaRequest(action=ota_pb2.OTA2HMI_HAS_UPGRADE),
                    ota_pb2.OtaRequest(action=ota_pb2.OTA2HMI_HAS_EMERGENCY_UPGRADE),
        ]
        for request in request_list:
            print(str(request))
            yield request

    def Stream_ota_to_hmi(self):   
        response_list = self.__class__.stub.StreamOtaToHmi(self.Make_ota_request())
        for response in response_list:
            print (str(response))
    
    def send_ota_msg(self, msg):
        request = hmi_ota_pb2.OtaRequest()
        try:
            request.action = msg
        except Exception as e:
            print(str(e))
        
        response = self.__class__.stub.NotiOTAClient(request)
        return response

    def test_has_upgrade_description(self):
        msg = hmi_ota_pb2.HAS_UPGRADE_DESCRIPTION
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        print("Response: " + str(response))

    def test_has_oper_upgrade(self):
        msg = hmi_ota_pb2.HAS_OPER_UPGRADE
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        print("Response: " + str(response))


    def test_oper_upgrade_install(self):
        msg = hmi_ota_pb2.OPER_UPGRADE_INSTALL
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        print("Response: " + str(response))

    def test_oper_upgrade_ignore(self):
        msg = hmi_ota_pb2.OPER_UPGRADE_IGNORE
        try:
            response = self.send_ota_msg(msg)
        except Exception as e:
            print(str(e))
        print("Response: " + str(response))

    def app_test(self):
        time.sleep(20)
        ota_stream.test_has_oper_upgrade()
        ota_stream.test_has_upgrade_description()
        ota_stream.test_oper_upgrade_ignore()
        ota_stream.test_oper_upgrade_install()

if __name__ == '__main__':
    ota_stream=simulate_trigger()
    ota_stream.Stream_ota_to_hmi()
    ota_stream.Stream_hmi_to_ota()
    
    