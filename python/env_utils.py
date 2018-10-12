#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Control of test environment.

Authors: yugao(yugao@baidu.com)
Date:    2018/08/06 11:06:55
"""
import os
import time
import thread
import logging


cybertron_path = os.environ['CYBERTRON_PATH']


def start_hmi_server(flags):
    cmd = cybertron_path + '/bin/hmi_server --flagfile=' \
        + cybertron_path + '/conf/hmi_server.conf'
    for k, v in flags.iteritems():
        cmd += ' --%s=%s' % (k, v)
    cmd += ' > /dev/null 2>&1'
    logging.info('[%s]', cmd)
    print '[%s]' % cmd
    thread.start_new_thread(os.system, (cmd,))
    time.sleep(10)


def stop_hmi_server():
    time.sleep(2)
    os.system('pkill -9 hmi_server')


def start_data_status_service():
    cmd = 'bash ' + cybertron_path + '/bin/data_manager/bin/data_status_service_start.sh'
    print '[%s]' % cmd
    thread.start_new_thread(os.system, (cmd,))
    time.sleep(5)


def stop_data_status_service():
    cmd = 'ps -ef | grep collector_data_status_server.py | \
        grep -v grep | awk \'{print $2}\' | xargs -i kill -INT {}'
    os.system(cmd)
    time.sleep(1)


def start_cybertron(launch_file):
    pass


def stop_cybertron(launch_file):
    pass


def start_parameter_server():
    cmd = cybertron_path + '/bin/parameter_server_node'
    cmd += ' > /dev/null 2>&1'
    thread.start_new_thread(os.system, (cmd,))
    time.sleep(5)


def stop_parameter_server():
    os.system('pkill -9 parameter_serve')


def play_record(record_file):
    cmd = 'cyber_recorder play ' + cybertron_path + \
        '/test/kinglong/unit_test/hmi-server/python/data/' + record_file
    print '[%s]' % cmd
    thread.start_new_thread(os.system, (cmd,))
    time.sleep(10)