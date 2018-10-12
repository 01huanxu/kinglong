# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_collect_disk_info.proto

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
  name='hmi_collect_disk_info.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x1bhmi_collect_disk_info.proto\x12\x07\x61\x64u.hmi\"\"\n\x0f\x44iskInfoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x9b\x02\n\x10\x44iskInfoResponse\x12\x32\n\x07\x65rrcode\x18\x01 \x01(\x0e\x32!.adu.hmi.DiskInfoResponse.ErrCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\tdisk_info\x18\x03 \x03(\x0b\x32\".adu.hmi.DiskInfoResponse.DiskInfo\x12\x19\n\x11has_external_disk\x18\x04 \x01(\x08\x1aM\n\x08\x44iskInfo\x12\x13\n\x0bmount_point\x18\x01 \x01(\t\x12\x10\n\x08\x65xternal\x18\x02 \x01(\x08\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0c\n\x04used\x18\x04 \x01(\x04\"!\n\x07\x45rrCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01')
)



_DISKINFORESPONSE_ERRCODE = _descriptor.EnumDescriptor(
  name='ErrCode',
  full_name='adu.hmi.DiskInfoResponse.ErrCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=327,
  serialized_end=360,
)
_sym_db.RegisterEnumDescriptor(_DISKINFORESPONSE_ERRCODE)


_DISKINFOREQUEST = _descriptor.Descriptor(
  name='DiskInfoRequest',
  full_name='adu.hmi.DiskInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='adu.hmi.DiskInfoRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=40,
  serialized_end=74,
)


_DISKINFORESPONSE_DISKINFO = _descriptor.Descriptor(
  name='DiskInfo',
  full_name='adu.hmi.DiskInfoResponse.DiskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount_point', full_name='adu.hmi.DiskInfoResponse.DiskInfo.mount_point', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external', full_name='adu.hmi.DiskInfoResponse.DiskInfo.external', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='adu.hmi.DiskInfoResponse.DiskInfo.size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used', full_name='adu.hmi.DiskInfoResponse.DiskInfo.used', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=248,
  serialized_end=325,
)

_DISKINFORESPONSE = _descriptor.Descriptor(
  name='DiskInfoResponse',
  full_name='adu.hmi.DiskInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errcode', full_name='adu.hmi.DiskInfoResponse.errcode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='adu.hmi.DiskInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_info', full_name='adu.hmi.DiskInfoResponse.disk_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_external_disk', full_name='adu.hmi.DiskInfoResponse.has_external_disk', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DISKINFORESPONSE_DISKINFO, ],
  enum_types=[
    _DISKINFORESPONSE_ERRCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=360,
)

_DISKINFORESPONSE_DISKINFO.containing_type = _DISKINFORESPONSE
_DISKINFORESPONSE.fields_by_name['errcode'].enum_type = _DISKINFORESPONSE_ERRCODE
_DISKINFORESPONSE.fields_by_name['disk_info'].message_type = _DISKINFORESPONSE_DISKINFO
_DISKINFORESPONSE_ERRCODE.containing_type = _DISKINFORESPONSE
DESCRIPTOR.message_types_by_name['DiskInfoRequest'] = _DISKINFOREQUEST
DESCRIPTOR.message_types_by_name['DiskInfoResponse'] = _DISKINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiskInfoRequest = _reflection.GeneratedProtocolMessageType('DiskInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISKINFOREQUEST,
  __module__ = 'hmi_collect_disk_info_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.DiskInfoRequest)
  ))
_sym_db.RegisterMessage(DiskInfoRequest)

DiskInfoResponse = _reflection.GeneratedProtocolMessageType('DiskInfoResponse', (_message.Message,), dict(

  DiskInfo = _reflection.GeneratedProtocolMessageType('DiskInfo', (_message.Message,), dict(
    DESCRIPTOR = _DISKINFORESPONSE_DISKINFO,
    __module__ = 'hmi_collect_disk_info_pb2'
    # @@protoc_insertion_point(class_scope:adu.hmi.DiskInfoResponse.DiskInfo)
    ))
  ,
  DESCRIPTOR = _DISKINFORESPONSE,
  __module__ = 'hmi_collect_disk_info_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.DiskInfoResponse)
  ))
_sym_db.RegisterMessage(DiskInfoResponse)
_sym_db.RegisterMessage(DiskInfoResponse.DiskInfo)


# @@protoc_insertion_point(module_scope)