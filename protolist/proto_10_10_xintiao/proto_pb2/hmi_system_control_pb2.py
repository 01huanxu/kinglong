# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_system_control.proto

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


import hmi_common_pb2 as hmi__common__pb2
import hmi_error_code_pb2 as hmi__error__code__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_system_control.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x18hmi_system_control.proto\x12\x07\x61\x64u.hmi\x1a\x10hmi_common.proto\x1a\x14hmi_error_code.proto\"@\n\x14SystemControlRequest\x12(\n\x04type\x18\x01 \x02(\x0e\x32\x1a.adu.hmi.SystemControlType\"9\n\x15SystemControlResponse\x12 \n\x04\x63ode\x18\x01 \x02(\x0e\x32\x12.adu.hmi.ErrorCode\"F\n\x16TransferControlRequest\x12,\n\x05owner\x18\x01 \x02(\x0e\x32\x1d.adu.hmi.TransferControlOwner\";\n\x17TransferControlResponse\x12 \n\x04\x63ode\x18\x01 \x02(\x0e\x32\x12.adu.hmi.ErrorCode*H\n\x11SystemControlType\x12\n\n\x06REBOOT\x10\x01\x12\x0c\n\x08SHUTDOWN\x10\x02\x12\x0c\n\x08POWEROFF\x10\x03\x12\x0b\n\x07MOVELOG\x10\x04*+\n\x14TransferControlOwner\x12\x07\n\x03PNC\x10\x01\x12\n\n\x06PATROL\x10\x02\x42\x02P\x01')
  ,
  dependencies=[hmi__common__pb2.DESCRIPTOR,hmi__error__code__pb2.DESCRIPTOR,])

_SYSTEMCONTROLTYPE = _descriptor.EnumDescriptor(
  name='SystemControlType',
  full_name='adu.hmi.SystemControlType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REBOOT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWEROFF', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVELOG', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=335,
  serialized_end=407,
)
_sym_db.RegisterEnumDescriptor(_SYSTEMCONTROLTYPE)

SystemControlType = enum_type_wrapper.EnumTypeWrapper(_SYSTEMCONTROLTYPE)
_TRANSFERCONTROLOWNER = _descriptor.EnumDescriptor(
  name='TransferControlOwner',
  full_name='adu.hmi.TransferControlOwner',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PNC', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PATROL', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=409,
  serialized_end=452,
)
_sym_db.RegisterEnumDescriptor(_TRANSFERCONTROLOWNER)

TransferControlOwner = enum_type_wrapper.EnumTypeWrapper(_TRANSFERCONTROLOWNER)
REBOOT = 1
SHUTDOWN = 2
POWEROFF = 3
MOVELOG = 4
PNC = 1
PATROL = 2



_SYSTEMCONTROLREQUEST = _descriptor.Descriptor(
  name='SystemControlRequest',
  full_name='adu.hmi.SystemControlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='adu.hmi.SystemControlRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=77,
  serialized_end=141,
)


_SYSTEMCONTROLRESPONSE = _descriptor.Descriptor(
  name='SystemControlResponse',
  full_name='adu.hmi.SystemControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.hmi.SystemControlResponse.code', index=0,
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
  serialized_start=143,
  serialized_end=200,
)


_TRANSFERCONTROLREQUEST = _descriptor.Descriptor(
  name='TransferControlRequest',
  full_name='adu.hmi.TransferControlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='adu.hmi.TransferControlRequest.owner', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=202,
  serialized_end=272,
)


_TRANSFERCONTROLRESPONSE = _descriptor.Descriptor(
  name='TransferControlResponse',
  full_name='adu.hmi.TransferControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.hmi.TransferControlResponse.code', index=0,
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
  serialized_start=274,
  serialized_end=333,
)

_SYSTEMCONTROLREQUEST.fields_by_name['type'].enum_type = _SYSTEMCONTROLTYPE
_SYSTEMCONTROLRESPONSE.fields_by_name['code'].enum_type = hmi__error__code__pb2._ERRORCODE
_TRANSFERCONTROLREQUEST.fields_by_name['owner'].enum_type = _TRANSFERCONTROLOWNER
_TRANSFERCONTROLRESPONSE.fields_by_name['code'].enum_type = hmi__error__code__pb2._ERRORCODE
DESCRIPTOR.message_types_by_name['SystemControlRequest'] = _SYSTEMCONTROLREQUEST
DESCRIPTOR.message_types_by_name['SystemControlResponse'] = _SYSTEMCONTROLRESPONSE
DESCRIPTOR.message_types_by_name['TransferControlRequest'] = _TRANSFERCONTROLREQUEST
DESCRIPTOR.message_types_by_name['TransferControlResponse'] = _TRANSFERCONTROLRESPONSE
DESCRIPTOR.enum_types_by_name['SystemControlType'] = _SYSTEMCONTROLTYPE
DESCRIPTOR.enum_types_by_name['TransferControlOwner'] = _TRANSFERCONTROLOWNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemControlRequest = _reflection.GeneratedProtocolMessageType('SystemControlRequest', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMCONTROLREQUEST,
  __module__ = 'hmi_system_control_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.SystemControlRequest)
  ))
_sym_db.RegisterMessage(SystemControlRequest)

SystemControlResponse = _reflection.GeneratedProtocolMessageType('SystemControlResponse', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMCONTROLRESPONSE,
  __module__ = 'hmi_system_control_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.SystemControlResponse)
  ))
_sym_db.RegisterMessage(SystemControlResponse)

TransferControlRequest = _reflection.GeneratedProtocolMessageType('TransferControlRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERCONTROLREQUEST,
  __module__ = 'hmi_system_control_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.TransferControlRequest)
  ))
_sym_db.RegisterMessage(TransferControlRequest)

TransferControlResponse = _reflection.GeneratedProtocolMessageType('TransferControlResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERCONTROLRESPONSE,
  __module__ = 'hmi_system_control_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.TransferControlResponse)
  ))
_sym_db.RegisterMessage(TransferControlResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)