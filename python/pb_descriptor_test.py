import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')
from google.protobuf import descriptor
from google.protobuf import symbol_database
import hmi_car_device_pb2

Data_all=symbol_database.Default()
print(Data_all)
    
#def get_all_messges(data):
#    symbol_database.


def test_func():
    print('test-database-begin')
    print(Data_all.GetSymbol('DeciveControlRequest'))
   # print(Data_all._symbols_by_file)

test_func()
    
