# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openapi_server_mobile_grpc.proto

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
  name='openapi_server_mobile_grpc.proto',
  package='adu.workers.openapi',
  syntax='proto2',
  serialized_pb=_b('\n openapi_server_mobile_grpc.proto\x12\x13\x61\x64u.workers.openapi\"@\n\x0e\x43onnectRequest\x12.\n\x04type\x18\x01 \x02(\x0e\x32 .adu.workers.openapi.ConnectType\"L\n\x10NotiControlReply\x12\x38\n\nreply_type\x18\x01 \x02(\x0e\x32$.adu.workers.openapi.NotiControlType*?\n\x0b\x43onnectType\x12\x17\n\x13HUD_CONNECT_CONTROL\x10\x00\x12\x17\n\x13\x41PP_CONNECT_CONTROL\x10\x01*N\n\x0fNotiControlType\x12\x16\n\x12NOTI_STOP_STRAIGHT\x10\x00\x12\x13\n\x0fNOTI_STOP_ASIDE\x10\x01\x12\x0e\n\nNOTI_GO_ON\x10\x02\x32~\n\x17OpenApiServiceForMoblie\x12\x63\n\x11NotiMobileControl\x12#.adu.workers.openapi.ConnectRequest\x1a%.adu.workers.openapi.NotiControlReply\"\x00\x30\x01')
)

_CONNECTTYPE = _descriptor.EnumDescriptor(
  name='ConnectType',
  full_name='adu.workers.openapi.ConnectType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HUD_CONNECT_CONTROL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_CONNECT_CONTROL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=201,
  serialized_end=264,
)
_sym_db.RegisterEnumDescriptor(_CONNECTTYPE)

ConnectType = enum_type_wrapper.EnumTypeWrapper(_CONNECTTYPE)
_NOTICONTROLTYPE = _descriptor.EnumDescriptor(
  name='NotiControlType',
  full_name='adu.workers.openapi.NotiControlType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTI_STOP_STRAIGHT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTI_STOP_ASIDE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTI_GO_ON', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=266,
  serialized_end=344,
)
_sym_db.RegisterEnumDescriptor(_NOTICONTROLTYPE)

NotiControlType = enum_type_wrapper.EnumTypeWrapper(_NOTICONTROLTYPE)
HUD_CONNECT_CONTROL = 0
APP_CONNECT_CONTROL = 1
NOTI_STOP_STRAIGHT = 0
NOTI_STOP_ASIDE = 1
NOTI_GO_ON = 2



_CONNECTREQUEST = _descriptor.Descriptor(
  name='ConnectRequest',
  full_name='adu.workers.openapi.ConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='adu.workers.openapi.ConnectRequest.type', index=0,
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
  serialized_start=57,
  serialized_end=121,
)


_NOTICONTROLREPLY = _descriptor.Descriptor(
  name='NotiControlReply',
  full_name='adu.workers.openapi.NotiControlReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_type', full_name='adu.workers.openapi.NotiControlReply.reply_type', index=0,
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
  serialized_start=123,
  serialized_end=199,
)

_CONNECTREQUEST.fields_by_name['type'].enum_type = _CONNECTTYPE
_NOTICONTROLREPLY.fields_by_name['reply_type'].enum_type = _NOTICONTROLTYPE
DESCRIPTOR.message_types_by_name['ConnectRequest'] = _CONNECTREQUEST
DESCRIPTOR.message_types_by_name['NotiControlReply'] = _NOTICONTROLREPLY
DESCRIPTOR.enum_types_by_name['ConnectType'] = _CONNECTTYPE
DESCRIPTOR.enum_types_by_name['NotiControlType'] = _NOTICONTROLTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREQUEST,
  __module__ = 'openapi_server_mobile_grpc_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.openapi.ConnectRequest)
  ))
_sym_db.RegisterMessage(ConnectRequest)

NotiControlReply = _reflection.GeneratedProtocolMessageType('NotiControlReply', (_message.Message,), dict(
  DESCRIPTOR = _NOTICONTROLREPLY,
  __module__ = 'openapi_server_mobile_grpc_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.openapi.NotiControlReply)
  ))
_sym_db.RegisterMessage(NotiControlReply)


# @@protoc_insertion_point(module_scope)
