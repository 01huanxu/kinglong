# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_clear_area.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import map_id_pb2 as map__id__pb2
import map_geometry_pb2 as map__geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='map_clear_area.proto',
  package='adu.common.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n\x14map_clear_area.proto\x12\x10\x61\x64u.common.hdmap\x1a\x0cmap_id.proto\x1a\x12map_geometry.proto\"\x83\x01\n\tClearArea\x12 \n\x02id\x18\x01 \x01(\x0b\x32\x14.adu.common.hdmap.Id\x12(\n\noverlap_id\x18\x02 \x03(\x0b\x32\x14.adu.common.hdmap.Id\x12*\n\x07polygon\x18\x03 \x01(\x0b\x32\x19.adu.common.hdmap.Polygon')
  ,
  dependencies=[map__id__pb2.DESCRIPTOR,map__geometry__pb2.DESCRIPTOR,])




_CLEARAREA = _descriptor.Descriptor(
  name='ClearArea',
  full_name='adu.common.hdmap.ClearArea',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='adu.common.hdmap.ClearArea.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='adu.common.hdmap.ClearArea.overlap_id', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polygon', full_name='adu.common.hdmap.ClearArea.polygon', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=208,
)

_CLEARAREA.fields_by_name['id'].message_type = map__id__pb2._ID
_CLEARAREA.fields_by_name['overlap_id'].message_type = map__id__pb2._ID
_CLEARAREA.fields_by_name['polygon'].message_type = map__geometry__pb2._POLYGON
DESCRIPTOR.message_types_by_name['ClearArea'] = _CLEARAREA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClearArea = _reflection.GeneratedProtocolMessageType('ClearArea', (_message.Message,), dict(
  DESCRIPTOR = _CLEARAREA,
  __module__ = 'map_clear_area_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.ClearArea)
  ))
_sym_db.RegisterMessage(ClearArea)


# @@protoc_insertion_point(module_scope)