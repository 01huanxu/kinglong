import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')

import unittest
import grpc
import hmi_error_code_pb2
import hmi_grpc_api_pb2_grpc
import hmi_system_control_pb2


channel = grpc.insecure_channel('127.0.0.1:8090')
stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)


class TestReboot(unittest.TestCase):
    def test_reboot(self):
        res = stub.ShutdownSystem(hmi_system_control_pb2.SystemControlRequest(
            type=hmi_system_control_pb2.REBOOT))
        print res
        self.assertTrue(res.code == hmi_error_code_pb2.SYSTEM_CTRL_ERROR)

    def test_shutdown(self):
        res = stub.ShutdownSystem(hmi_system_control_pb2.SystemControlRequest(
            type=hmi_system_control_pb2.SHUTDOWN))
        print res
        self.assertTrue(res.code == hmi_error_code_pb2.SYSTEM_CTRL_ERROR)

    def test_poweroff(self):
        res = stub.ShutdownSystem(hmi_system_control_pb2.SystemControlRequest(
            type=hmi_system_control_pb2.POWEROFF))
        print res
        self.assertTrue(res.code == hmi_error_code_pb2.SYSTEM_CTRL_ERROR)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReboot)
    unittest.TextTestRunner(verbosity=2).run(suite)
