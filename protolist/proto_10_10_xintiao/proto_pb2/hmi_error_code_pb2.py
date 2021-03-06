# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_error_code.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_error_code.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x14hmi_error_code.proto\x12\x07\x61\x64u.hmi*\xc9\t\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x1f\n\x1bROUTING_INVALID_START_POINT\x10\x01\x12\x1d\n\x19ROUTING_INVALID_END_POINT\x10\x02\x12\x1e\n\x1aROUTING_INVALID_WAY_POINTS\x10\x03\x12\"\n\x1eROUTING_CANNOT_CONNECT_SERVICE\x10\x04\x12\x1b\n\x17ROUTING_INVALID_REQUEST\x10\x05\x12\x12\n\x0eROUTING_FAILED\x10\x06\x12\x12\n\x0eROUTING_FORBID\x10\x07\x12&\n\"DEVICE_CTRL_CANNOT_CONNECT_SERVICE\x10\x08\x12\x1d\n\x19\x44\x45VICE_CTRL_ERROR_REQUEST\x10\t\x12\x1f\n\x1b\x44\x45VICE_CTRL_RESPONSE_FAILED\x10\n\x12\x15\n\x11SAFECHECK_INVALID\x10\x0b\x12\x15\n\x11SAFECHECK_WAITING\x10\x1a\x12!\n\x1dLAUNCH_CANNOT_CONNECT_SERVICE\x10\x0c\x12\x15\n\x11LAUNCH_NOT_MANUAL\x10\x1b\x12\r\n\tOTA_ERROR\x10\r\x12\x0f\n\x0bOTA_TIMEOUT\x10\x0e\x12\x0f\n\x0bOTA_UNKNOWN\x10\x0f\x12$\n DISENGAGE_CANNOT_CONNECT_SERVICE\x10\x10\x12%\n!DATA_CHECK_CANNOT_CONNECT_SERVICE\x10\x11\x12 \n\x1c\x43\x41LIBRATION_PARAMS_FILE_LACK\x10\x12\x12\x1b\n\x17\x43\x41LIBRATION_CHECK_ERROR\x10\x13\x12\"\n\x1e\x43\x41LIBRATION_POINTCLOUD_NO_DATA\x10\x14\x12\x1a\n\x16\x43\x41NNOT_CONNECT_SERVICE\x10\x15\x12\x1b\n\x17PREPROC_RESPONSE_FAILED\x10\x16\x12\x15\n\x11SYSTEM_CTRL_ERROR\x10\x17\x12\x1a\n\x16\x45QUAL_WORK_MODE_IGNORE\x10\x18\x12\x1a\n\x16INVALID_REQUEST_PARAMS\x10\x19\x12%\n!DISENGAGE_FEEDBACK_RESPONSE_ERROR\x10\x1d\x12\x18\n\x14INVALID_BASE_MAP_BIN\x10\x1e\x12\x1a\n\x16INVALID_BACKGROUND_PNG\x10\x1f\x12\x14\n\x10INVALID_MAP_JSON\x10 \x12\x1d\n\x19INIT_LOCAL_REQ_NULL_ERROR\x10!\x12 \n\x1cINIT_LOCAL_NOTI_CHNNEL_ERROR\x10\"\x12\x1f\n\x1bINVALID_PARKING_SPACE_POINT\x10\x1c\x12\x1a\n\x16NO_PARKING_SPACE_FOUND\x10#\x12\x12\n\x0eMOVE_LOG_ERROR\x10$\x12\x1a\n\x16SET_GLOBAL_PARAM_ERROR\x10%\x12\x14\n\x10WORKER_NOT_FOUND\x10\x64\x12\x1a\n\x16WORKER_IS_INITIALIZING\x10\x65\x12\x16\n\x12\x43OMMAND_EXEC_ERROR\x10\x66\x12\x11\n\rREQUEST_ERROR\x10g\x12\x17\n\x12LAUNCHER_EXCEPTION\x10\xc7\x01\x12\x1b\n\x16TEMP_RECORD_PLAY_ERROR\x10\xc8\x01\x42\x02P\x01')
)

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='adu.hmi.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_INVALID_START_POINT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_INVALID_END_POINT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_INVALID_WAY_POINTS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_CANNOT_CONNECT_SERVICE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_INVALID_REQUEST', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_FAILED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_FORBID', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_CTRL_CANNOT_CONNECT_SERVICE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_CTRL_ERROR_REQUEST', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_CTRL_RESPONSE_FAILED', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAFECHECK_INVALID', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAFECHECK_WAITING', index=12, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAUNCH_CANNOT_CONNECT_SERVICE', index=13, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAUNCH_NOT_MANUAL', index=14, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTA_ERROR', index=15, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTA_TIMEOUT', index=16, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTA_UNKNOWN', index=17, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISENGAGE_CANNOT_CONNECT_SERVICE', index=18, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_CHECK_CANNOT_CONNECT_SERVICE', index=19, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATION_PARAMS_FILE_LACK', index=20, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATION_CHECK_ERROR', index=21, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATION_POINTCLOUD_NO_DATA', index=22, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CONNECT_SERVICE', index=23, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREPROC_RESPONSE_FAILED', index=24, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM_CTRL_ERROR', index=25, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQUAL_WORK_MODE_IGNORE', index=26, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST_PARAMS', index=27, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISENGAGE_FEEDBACK_RESPONSE_ERROR', index=28, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_BASE_MAP_BIN', index=29, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_BACKGROUND_PNG', index=30, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MAP_JSON', index=31, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT_LOCAL_REQ_NULL_ERROR', index=32, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT_LOCAL_NOTI_CHNNEL_ERROR', index=33, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARKING_SPACE_POINT', index=34, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_PARKING_SPACE_FOUND', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_LOG_ERROR', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_GLOBAL_PARAM_ERROR', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKER_NOT_FOUND', index=38, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKER_IS_INITIALIZING', index=39, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_EXEC_ERROR', index=40, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_ERROR', index=41, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAUNCHER_EXCEPTION', index=42, number=199,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMP_RECORD_PLAY_ERROR', index=43, number=200,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=34,
  serialized_end=1259,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
OK = 0
ROUTING_INVALID_START_POINT = 1
ROUTING_INVALID_END_POINT = 2
ROUTING_INVALID_WAY_POINTS = 3
ROUTING_CANNOT_CONNECT_SERVICE = 4
ROUTING_INVALID_REQUEST = 5
ROUTING_FAILED = 6
ROUTING_FORBID = 7
DEVICE_CTRL_CANNOT_CONNECT_SERVICE = 8
DEVICE_CTRL_ERROR_REQUEST = 9
DEVICE_CTRL_RESPONSE_FAILED = 10
SAFECHECK_INVALID = 11
SAFECHECK_WAITING = 26
LAUNCH_CANNOT_CONNECT_SERVICE = 12
LAUNCH_NOT_MANUAL = 27
OTA_ERROR = 13
OTA_TIMEOUT = 14
OTA_UNKNOWN = 15
DISENGAGE_CANNOT_CONNECT_SERVICE = 16
DATA_CHECK_CANNOT_CONNECT_SERVICE = 17
CALIBRATION_PARAMS_FILE_LACK = 18
CALIBRATION_CHECK_ERROR = 19
CALIBRATION_POINTCLOUD_NO_DATA = 20
CANNOT_CONNECT_SERVICE = 21
PREPROC_RESPONSE_FAILED = 22
SYSTEM_CTRL_ERROR = 23
EQUAL_WORK_MODE_IGNORE = 24
INVALID_REQUEST_PARAMS = 25
DISENGAGE_FEEDBACK_RESPONSE_ERROR = 29
INVALID_BASE_MAP_BIN = 30
INVALID_BACKGROUND_PNG = 31
INVALID_MAP_JSON = 32
INIT_LOCAL_REQ_NULL_ERROR = 33
INIT_LOCAL_NOTI_CHNNEL_ERROR = 34
INVALID_PARKING_SPACE_POINT = 28
NO_PARKING_SPACE_FOUND = 35
MOVE_LOG_ERROR = 36
SET_GLOBAL_PARAM_ERROR = 37
WORKER_NOT_FOUND = 100
WORKER_IS_INITIALIZING = 101
COMMAND_EXEC_ERROR = 102
REQUEST_ERROR = 103
LAUNCHER_EXCEPTION = 199
TEMP_RECORD_PLAY_ERROR = 200


DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)
