# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inspector_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import inspector_msg_pb2 as inspector__msg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='inspector_service.proto',
  package='adu.workers.inspector',
  syntax='proto2',
  serialized_pb=_b('\n\x17inspector_service.proto\x12\x15\x61\x64u.workers.inspector\x1a\x13inspector_msg.proto2\xdc\x02\n\x10InspectorService\x12q\n\x14\x43oarseCameraValidity\x12*.adu.workers.inspector.CoarseCameraRequest\x1a+.adu.workers.inspector.CoarseCameraResponse\"\x00\x12\x65\n\x10LidarImuValidity\x12&.adu.workers.inspector.LidarImuRequest\x1a\'.adu.workers.inspector.LidarImuResponse\"\x00\x12n\n\x13LidarCameraValidity\x12).adu.workers.inspector.LidarCameraRequest\x1a*.adu.workers.inspector.LidarCameraResponse\"\x00\x42\x02P\x01')
  ,
  dependencies=[inspector__msg__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)