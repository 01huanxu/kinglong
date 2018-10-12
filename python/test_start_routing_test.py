import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')

import unittest
import grpc
import hmi_error_code_pb2
import hmi_grpc_api_pb2_grpc
import hmi_system_control_pb2
import hmi_routing_pb2
import hmi_common_pb2
import common_geometry_pb2
import conf_loader



channel = grpc.insecure_channel('127.0.0.1:8090')
stub = hmi_grpc_api_pb2_grpc.HMIGrpcServiceStub(channel)

cf = conf_loader.ConfLoader("testinfo.yaml")
prms = cf.prms['RoutingRequest_dasha']
print(str(prms))

req = hmi_routing_pb2.RoutingRequest(\
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

class TestRouting(unittest.TestCase):
    def test_routing(self):
        print("test_routing")
        res = stub.StartRouting(req)
        print res
        self.assertTrue(res.code == hmi_error_code_pb2.OK)

    # def test_pre_routing(self):
    #     print("test_pre_routing")
    #     res = stub.PreRouting(req)
    #     print res
    #     self.assertTrue(res.code == hmi_error_code_pb2.OK)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRouting)
    unittest.TextTestRunner(verbosity=2).run(suite)
