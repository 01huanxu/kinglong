# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_collect_car_device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_collect_car_device.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x1chmi_collect_car_device.proto\x12\x07\x61\x64u.hmi\"1\n\rCollectDevice\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x11\n\todo_meter\x18\x02 \x01(\x01\x42\x02P\x01')
)




_COLLECTDEVICE = _descriptor.Descriptor(
  name='CollectDevice',
  full_name='adu.hmi.CollectDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='adu.hmi.CollectDevice.speed', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='odo_meter', full_name='adu.hmi.CollectDevice.odo_meter', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['CollectDevice'] = _COLLECTDEVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectDevice = _reflection.GeneratedProtocolMessageType('CollectDevice', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTDEVICE,
  __module__ = 'hmi_collect_car_device_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.CollectDevice)
  ))
_sym_db.RegisterMessage(CollectDevice)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)
