# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_joy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor_joy.proto',
  package='adu.common.sensor',
  syntax='proto2',
  serialized_pb=_b('\n\x10sensor_joy.proto\x12\x11\x61\x64u.common.sensor\x1a\x0cheader.proto\"e\n\x03Joy\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.adu.common.header.Header\x12\x10\n\x04\x61xes\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x13\n\x07\x62uttons\x18\x03 \x03(\rB\x02\x10\x01\x12\x0c\n\x04mode\x18\x04 \x02(\x05')
  ,
  dependencies=[header__pb2.DESCRIPTOR,])




_JOY = _descriptor.Descriptor(
  name='Joy',
  full_name='adu.common.sensor.Joy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='adu.common.sensor.Joy.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='axes', full_name='adu.common.sensor.Joy.axes', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='buttons', full_name='adu.common.sensor.Joy.buttons', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='mode', full_name='adu.common.sensor.Joy.mode', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=53,
  serialized_end=154,
)

_JOY.fields_by_name['header'].message_type = header__pb2._HEADER
DESCRIPTOR.message_types_by_name['Joy'] = _JOY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Joy = _reflection.GeneratedProtocolMessageType('Joy', (_message.Message,), dict(
  DESCRIPTOR = _JOY,
  __module__ = 'sensor_joy_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.sensor.Joy)
  ))
_sym_db.RegisterMessage(Joy)


_JOY.fields_by_name['axes'].has_options = True
_JOY.fields_by_name['axes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_JOY.fields_by_name['buttons'].has_options = True
_JOY.fields_by_name['buttons']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
