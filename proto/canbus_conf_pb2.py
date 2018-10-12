# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canbus_conf.proto

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
  name='canbus_conf.proto',
  package='baidu.idl_car.canbus',
  syntax='proto2',
  serialized_pb=_b('\n\x11\x63\x61nbus_conf.proto\x12\x14\x62\x61idu.idl_car.canbus\"\x95\x02\n\x0cPbCanbusConf\x12\x39\n\x07\x65ntries\x18\x01 \x03(\x0b\x32(.baidu.idl_car.canbus.PbCanbusConf.Entry\x1a\x96\x01\n\x05\x45ntry\x12\x35\n\x04type\x18\x01 \x02(\x0e\x32\'.baidu.idl_car.canbus.PbCanbusConf.Type\x12\x0b\n\x03key\x18\x02 \x02(\t\x12\x0f\n\x07int_val\x18\x03 \x01(\x03\x12\x12\n\nstring_val\x18\x04 \x01(\t\x12\x10\n\x08\x62ool_val\x18\x05 \x01(\x08\x12\x12\n\ndouble_val\x18\x06 \x01(\x01\"1\n\x04Type\x12\x07\n\x03INT\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04')
)



_PBCANBUSCONF_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='baidu.idl_car.canbus.PbCanbusConf.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=272,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_PBCANBUSCONF_TYPE)


_PBCANBUSCONF_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='baidu.idl_car.canbus.PbCanbusConf.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='baidu.idl_car.canbus.PbCanbusConf.Entry.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='baidu.idl_car.canbus.PbCanbusConf.Entry.key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='baidu.idl_car.canbus.PbCanbusConf.Entry.int_val', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='baidu.idl_car.canbus.PbCanbusConf.Entry.string_val', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_val', full_name='baidu.idl_car.canbus.PbCanbusConf.Entry.bool_val', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='baidu.idl_car.canbus.PbCanbusConf.Entry.double_val', index=5,
      number=6, type=1, cpp_type=5, label=1,
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
  serialized_start=120,
  serialized_end=270,
)

_PBCANBUSCONF = _descriptor.Descriptor(
  name='PbCanbusConf',
  full_name='baidu.idl_car.canbus.PbCanbusConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='baidu.idl_car.canbus.PbCanbusConf.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PBCANBUSCONF_ENTRY, ],
  enum_types=[
    _PBCANBUSCONF_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=321,
)

_PBCANBUSCONF_ENTRY.fields_by_name['type'].enum_type = _PBCANBUSCONF_TYPE
_PBCANBUSCONF_ENTRY.containing_type = _PBCANBUSCONF
_PBCANBUSCONF.fields_by_name['entries'].message_type = _PBCANBUSCONF_ENTRY
_PBCANBUSCONF_TYPE.containing_type = _PBCANBUSCONF
DESCRIPTOR.message_types_by_name['PbCanbusConf'] = _PBCANBUSCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbCanbusConf = _reflection.GeneratedProtocolMessageType('PbCanbusConf', (_message.Message,), dict(

  Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), dict(
    DESCRIPTOR = _PBCANBUSCONF_ENTRY,
    __module__ = 'canbus_conf_pb2'
    # @@protoc_insertion_point(class_scope:baidu.idl_car.canbus.PbCanbusConf.Entry)
    ))
  ,
  DESCRIPTOR = _PBCANBUSCONF,
  __module__ = 'canbus_conf_pb2'
  # @@protoc_insertion_point(class_scope:baidu.idl_car.canbus.PbCanbusConf)
  ))
_sym_db.RegisterMessage(PbCanbusConf)
_sym_db.RegisterMessage(PbCanbusConf.Entry)


# @@protoc_insertion_point(module_scope)
