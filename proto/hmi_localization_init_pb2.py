# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_localization_init.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hmi_error_code_pb2 as hmi__error__code__pb2
import hmi_common_pb2 as hmi__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_localization_init.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x1bhmi_localization_init.proto\x12\x07\x61\x64u.hmi\x1a\x14hmi_error_code.proto\x1a\x10hmi_common.proto\"a\n\x12PositionAndHeading\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\'\n\x08position\x18\x02 \x02(\x0b\x32\x15.adu.hmi.PolygonPoint\x12\x0f\n\x07heading\x18\x03 \x02(\x01\"0\n\x0cLocalInitRes\x12 \n\x04\x63ode\x18\x01 \x02(\x0e\x32\x12.adu.hmi.ErrorCodeB\x02P\x01')
  ,
  dependencies=[hmi__error__code__pb2.DESCRIPTOR,hmi__common__pb2.DESCRIPTOR,])




_POSITIONANDHEADING = _descriptor.Descriptor(
  name='PositionAndHeading',
  full_name='adu.hmi.PositionAndHeading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='adu.hmi.PositionAndHeading.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='adu.hmi.PositionAndHeading.position', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='adu.hmi.PositionAndHeading.heading', index=2,
      number=3, type=1, cpp_type=5, label=2,
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
  serialized_start=80,
  serialized_end=177,
)


_LOCALINITRES = _descriptor.Descriptor(
  name='LocalInitRes',
  full_name='adu.hmi.LocalInitRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.hmi.LocalInitRes.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
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
  serialized_start=179,
  serialized_end=227,
)

_POSITIONANDHEADING.fields_by_name['position'].message_type = hmi__common__pb2._POLYGONPOINT
_LOCALINITRES.fields_by_name['code'].enum_type = hmi__error__code__pb2._ERRORCODE
DESCRIPTOR.message_types_by_name['PositionAndHeading'] = _POSITIONANDHEADING
DESCRIPTOR.message_types_by_name['LocalInitRes'] = _LOCALINITRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PositionAndHeading = _reflection.GeneratedProtocolMessageType('PositionAndHeading', (_message.Message,), dict(
  DESCRIPTOR = _POSITIONANDHEADING,
  __module__ = 'hmi_localization_init_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.PositionAndHeading)
  ))
_sym_db.RegisterMessage(PositionAndHeading)

LocalInitRes = _reflection.GeneratedProtocolMessageType('LocalInitRes', (_message.Message,), dict(
  DESCRIPTOR = _LOCALINITRES,
  __module__ = 'hmi_localization_init_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.LocalInitRes)
  ))
_sym_db.RegisterMessage(LocalInitRes)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)