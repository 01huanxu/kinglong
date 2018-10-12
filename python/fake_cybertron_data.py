#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2018 v_xuhuan01@Baidu.com, Inc. All Rights Reserved
#
#########################################################
"""
    Filename: fake_cybertron_data.py
"""
import pdb
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')
import time
import json
import car_status_pb2
import decision_pb2
import global_adc_status_pb2
import odometry_pb2
# from ota.client.proto import ota_upgrade_info_pb2
import cybertron
import conf_loader

class fake_node_data(object):
    
    def __init__(self,node,filename,ymal_filename,message_descriptor,seconds_inval):
        if type(message_descriptor)==str :
            str_list=message_descriptor.split('.')
            message_descriptor=eval(message_descriptor)
        
        self.second=seconds_inval
        self.msgs=[]  
        self.messge_desriptor=message_descriptor
        params=str_list[1]
        self.cyber_node_create(node,filename)
        self.load_conf_parm(ymal_filename,params)

    @classmethod
    def class_init(cls):
        cybertron.init.init()

    def cyber_node_create(self,node_name,filename):
        node = cybertron.node.Node(node_name)
        #r = node.create_reader("/fake/hmi_to_fake_res", global_adc_status_pb2.Chassis, callback_f)
        self.w = node.create_writer('/'+node_name+'/'+filename, self.messge_desriptor)
    
    def load_conf_parm(self,ymal_filename,params):
        cf=conf_loader.ConfLoader(ymal_filename)
        #if not cf None:
        parms_list=cf.prms[params]
        #print(parms_list)
        for each_parm in parms_list:
            #print (each_parm)
            self.msgs.append(self.messge_desriptor(**each_parm))
       

    def send_msg(self):
        for msg in self.msgs:
            time.sleep(self.second) 
            self.w.write(msg)
            print ("sendmsg:",msg)
        #node.spin_once()
"""
    "carstatus":['pnc','carstatus','fake_data_conf.yaml','car_status_pb2.Status'] 
      
    "PerceptionObstacles ":['perception','obstacles','fake_data_conf.yaml','car_status_pb2.Status'],
    "ADCTrajectory":['pnc','planning','fake_data_conf.yaml','car_status_pb2.Status'],
    "PredictionObstacles":['pnc','prediction','fake_data_conf.yaml','car_status_pb2.Status'],
    "TrafficLightDetection":['perception','traffic_light_status','fake_data_conf.yaml','car_status_pb2.Status'],
    "PatrolStatus":['patrol','status','fake_data_conf.yaml','car_status_pb2.Status'],
    "ImpendingCollisionEdges":['perception','carultrasonic_objects','fake_data_conf.yaml','car_status_pb2.Status'],
    "PadMessage":['pnc','pad_proxy','fake_data_conf.yaml','car_status_pb2.Status'],
    "Chassis":['planning','proxy/DuDriveChassis ','fake_data_conf.yaml','car_status_pb2.Status'],
    "Ultrasonic":['sensor','ultrasonic/Ultrasonic','fake_data_conf.yaml','car_status_pb2.Status'],
"""
fake_dict={
        #"Chassis":['planning','proxy/DuDriveChassis','fake_chassis_conf.yaml','global_adc_status_pb2.Chassis',1.0] ,
        #"Pose":['pnc','carstatus','fake_pose_conf.yaml','odometry_pb2.Pose',1.0],
        "DecisionResult":['pnc','decision','DecisionResult.yaml','decision_pb2.DecisionResult',0.5]
}

def fake_data_test():
    times=5
    fack_node_object=[]
    fake_node_data.class_init()
    for key,value in fake_dict.items():
        print('send %s data to file node /%s/%s,data_conf is %s,pb is from %s'%(key,value[0],value[1],value[2],value[3]))
        test_fake_node=fake_node_data(value[0],value[1],value[2],value[3],value[4])
        fack_node_object.append(test_fake_node)

    while True:
        times-=1
        if times==0 :
            return 
        for each_test_fake_node in fack_node_object:
            each_test_fake_node.send_msg()
            print("-----------send over---------------")
        
if __name__ == "__main__":
    fake_data_test()
