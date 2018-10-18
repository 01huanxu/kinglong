# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_overlap.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='map_overlap.proto',
  package='adu.common.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n\x11map_overlap.proto\x12\x10\x61\x64u.common.hdmap\x1a\x0cmap_id.proto\"[\n\x0fLaneOverlapInfo\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05\x65nd_s\x18\x02 \x01(\x01\x12\x10\n\x08is_merge\x18\x03 \x01(\x08\x12\x16\n\x0ehas_precedence\x18\x04 \x01(\x08\"\x13\n\x11SignalOverlapInfo\"\x15\n\x13StopSignOverlapInfo\"\x16\n\x14\x43rosswalkOverlapInfo\"\x15\n\x13JunctionOverlapInfo\"\x12\n\x10YieldOverlapInfo\"\x16\n\x14\x43learAreaOverlapInfo\"\x16\n\x14SpeedBumpOverlapInfo\"\x19\n\x17ParkingSpaceOverlapInfo\"\xd2\x05\n\x11ObjectOverlapInfo\x12 \n\x02id\x18\x01 \x01(\x0b\x32\x14.adu.common.hdmap.Id\x12>\n\x11lane_overlap_info\x18\x03 \x01(\x0b\x32!.adu.common.hdmap.LaneOverlapInfoH\x00\x12\x42\n\x13signal_overlap_info\x18\x04 \x01(\x0b\x32#.adu.common.hdmap.SignalOverlapInfoH\x00\x12G\n\x16stop_sign_overlap_info\x18\x05 \x01(\x0b\x32%.adu.common.hdmap.StopSignOverlapInfoH\x00\x12H\n\x16\x63rosswalk_overlap_info\x18\x06 \x01(\x0b\x32&.adu.common.hdmap.CrosswalkOverlapInfoH\x00\x12\x46\n\x15junction_overlap_info\x18\x07 \x01(\x0b\x32%.adu.common.hdmap.JunctionOverlapInfoH\x00\x12\x45\n\x17yield_sign_overlap_info\x18\x08 \x01(\x0b\x32\".adu.common.hdmap.YieldOverlapInfoH\x00\x12I\n\x17\x63lear_area_overlap_info\x18\t \x01(\x0b\x32&.adu.common.hdmap.ClearAreaOverlapInfoH\x00\x12I\n\x17speed_bump_overlap_info\x18\n \x01(\x0b\x32&.adu.common.hdmap.SpeedBumpOverlapInfoH\x00\x12O\n\x1aparking_space_overlap_info\x18\x0b \x01(\x0b\x32).adu.common.hdmap.ParkingSpaceOverlapInfoH\x00\x42\x0e\n\x0coverlap_info\"`\n\x07Overlap\x12 \n\x02id\x18\x01 \x01(\x0b\x32\x14.adu.common.hdmap.Id\x12\x33\n\x06object\x18\x02 \x03(\x0b\x32#.adu.common.hdmap.ObjectOverlapInfo')
  ,
  dependencies=[map__id__pb2.DESCRIPTOR,])




_LANEOVERLAPINFO = _descriptor.Descriptor(
  name='LaneOverlapInfo',
  full_name='adu.common.hdmap.LaneOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_s', full_name='adu.common.hdmap.LaneOverlapInfo.start_s', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_s', full_name='adu.common.hdmap.LaneOverlapInfo.end_s', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_merge', full_name='adu.common.hdmap.LaneOverlapInfo.is_merge', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_precedence', full_name='adu.common.hdmap.LaneOverlapInfo.has_precedence', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_end=144,
)


_SIGNALOVERLAPINFO = _descriptor.Descriptor(
  name='SignalOverlapInfo',
  full_name='adu.common.hdmap.SignalOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=146,
  serialized_end=165,
)


_STOPSIGNOVERLAPINFO = _descriptor.Descriptor(
  name='StopSignOverlapInfo',
  full_name='adu.common.hdmap.StopSignOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=167,
  serialized_end=188,
)


_CROSSWALKOVERLAPINFO = _descriptor.Descriptor(
  name='CrosswalkOverlapInfo',
  full_name='adu.common.hdmap.CrosswalkOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=190,
  serialized_end=212,
)


_JUNCTIONOVERLAPINFO = _descriptor.Descriptor(
  name='JunctionOverlapInfo',
  full_name='adu.common.hdmap.JunctionOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=214,
  serialized_end=235,
)


_YIELDOVERLAPINFO = _descriptor.Descriptor(
  name='YieldOverlapInfo',
  full_name='adu.common.hdmap.YieldOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=237,
  serialized_end=255,
)


_CLEARAREAOVERLAPINFO = _descriptor.Descriptor(
  name='ClearAreaOverlapInfo',
  full_name='adu.common.hdmap.ClearAreaOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=257,
  serialized_end=279,
)


_SPEEDBUMPOVERLAPINFO = _descriptor.Descriptor(
  name='SpeedBumpOverlapInfo',
  full_name='adu.common.hdmap.SpeedBumpOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=281,
  serialized_end=303,
)


_PARKINGSPACEOVERLAPINFO = _descriptor.Descriptor(
  name='ParkingSpaceOverlapInfo',
  full_name='adu.common.hdmap.ParkingSpaceOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=305,
  serialized_end=330,
)


_OBJECTOVERLAPINFO = _descriptor.Descriptor(
  name='ObjectOverlapInfo',
  full_name='adu.common.hdmap.ObjectOverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='adu.common.hdmap.ObjectOverlapInfo.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lane_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.lane_overlap_info', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.signal_overlap_info', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_sign_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.stop_sign_overlap_info', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crosswalk_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.crosswalk_overlap_info', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='junction_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.junction_overlap_info', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yield_sign_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.yield_sign_overlap_info', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clear_area_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.clear_area_overlap_info', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_bump_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.speed_bump_overlap_info', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parking_space_overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.parking_space_overlap_info', index=9,
      number=11, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='overlap_info', full_name='adu.common.hdmap.ObjectOverlapInfo.overlap_info',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=333,
  serialized_end=1055,
)


_OVERLAP = _descriptor.Descriptor(
  name='Overlap',
  full_name='adu.common.hdmap.Overlap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='adu.common.hdmap.Overlap.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object', full_name='adu.common.hdmap.Overlap.object', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1057,
  serialized_end=1153,
)

_OBJECTOVERLAPINFO.fields_by_name['id'].message_type = map__id__pb2._ID
_OBJECTOVERLAPINFO.fields_by_name['lane_overlap_info'].message_type = _LANEOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['signal_overlap_info'].message_type = _SIGNALOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['stop_sign_overlap_info'].message_type = _STOPSIGNOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['crosswalk_overlap_info'].message_type = _CROSSWALKOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['junction_overlap_info'].message_type = _JUNCTIONOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['yield_sign_overlap_info'].message_type = _YIELDOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['clear_area_overlap_info'].message_type = _CLEARAREAOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['speed_bump_overlap_info'].message_type = _SPEEDBUMPOVERLAPINFO
_OBJECTOVERLAPINFO.fields_by_name['parking_space_overlap_info'].message_type = _PARKINGSPACEOVERLAPINFO
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['lane_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['lane_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['signal_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['signal_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['stop_sign_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['stop_sign_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['crosswalk_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['crosswalk_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['junction_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['junction_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['yield_sign_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['yield_sign_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['clear_area_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['clear_area_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['speed_bump_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['speed_bump_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OBJECTOVERLAPINFO.oneofs_by_name['overlap_info'].fields.append(
  _OBJECTOVERLAPINFO.fields_by_name['parking_space_overlap_info'])
_OBJECTOVERLAPINFO.fields_by_name['parking_space_overlap_info'].containing_oneof = _OBJECTOVERLAPINFO.oneofs_by_name['overlap_info']
_OVERLAP.fields_by_name['id'].message_type = map__id__pb2._ID
_OVERLAP.fields_by_name['object'].message_type = _OBJECTOVERLAPINFO
DESCRIPTOR.message_types_by_name['LaneOverlapInfo'] = _LANEOVERLAPINFO
DESCRIPTOR.message_types_by_name['SignalOverlapInfo'] = _SIGNALOVERLAPINFO
DESCRIPTOR.message_types_by_name['StopSignOverlapInfo'] = _STOPSIGNOVERLAPINFO
DESCRIPTOR.message_types_by_name['CrosswalkOverlapInfo'] = _CROSSWALKOVERLAPINFO
DESCRIPTOR.message_types_by_name['JunctionOverlapInfo'] = _JUNCTIONOVERLAPINFO
DESCRIPTOR.message_types_by_name['YieldOverlapInfo'] = _YIELDOVERLAPINFO
DESCRIPTOR.message_types_by_name['ClearAreaOverlapInfo'] = _CLEARAREAOVERLAPINFO
DESCRIPTOR.message_types_by_name['SpeedBumpOverlapInfo'] = _SPEEDBUMPOVERLAPINFO
DESCRIPTOR.message_types_by_name['ParkingSpaceOverlapInfo'] = _PARKINGSPACEOVERLAPINFO
DESCRIPTOR.message_types_by_name['ObjectOverlapInfo'] = _OBJECTOVERLAPINFO
DESCRIPTOR.message_types_by_name['Overlap'] = _OVERLAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LaneOverlapInfo = _reflection.GeneratedProtocolMessageType('LaneOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _LANEOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.LaneOverlapInfo)
  ))
_sym_db.RegisterMessage(LaneOverlapInfo)

SignalOverlapInfo = _reflection.GeneratedProtocolMessageType('SignalOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _SIGNALOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.SignalOverlapInfo)
  ))
_sym_db.RegisterMessage(SignalOverlapInfo)

StopSignOverlapInfo = _reflection.GeneratedProtocolMessageType('StopSignOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _STOPSIGNOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.StopSignOverlapInfo)
  ))
_sym_db.RegisterMessage(StopSignOverlapInfo)

CrosswalkOverlapInfo = _reflection.GeneratedProtocolMessageType('CrosswalkOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _CROSSWALKOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.CrosswalkOverlapInfo)
  ))
_sym_db.RegisterMessage(CrosswalkOverlapInfo)

JunctionOverlapInfo = _reflection.GeneratedProtocolMessageType('JunctionOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _JUNCTIONOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.JunctionOverlapInfo)
  ))
_sym_db.RegisterMessage(JunctionOverlapInfo)

YieldOverlapInfo = _reflection.GeneratedProtocolMessageType('YieldOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _YIELDOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.YieldOverlapInfo)
  ))
_sym_db.RegisterMessage(YieldOverlapInfo)

ClearAreaOverlapInfo = _reflection.GeneratedProtocolMessageType('ClearAreaOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _CLEARAREAOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.ClearAreaOverlapInfo)
  ))
_sym_db.RegisterMessage(ClearAreaOverlapInfo)

SpeedBumpOverlapInfo = _reflection.GeneratedProtocolMessageType('SpeedBumpOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDBUMPOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.SpeedBumpOverlapInfo)
  ))
_sym_db.RegisterMessage(SpeedBumpOverlapInfo)

ParkingSpaceOverlapInfo = _reflection.GeneratedProtocolMessageType('ParkingSpaceOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _PARKINGSPACEOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.ParkingSpaceOverlapInfo)
  ))
_sym_db.RegisterMessage(ParkingSpaceOverlapInfo)

ObjectOverlapInfo = _reflection.GeneratedProtocolMessageType('ObjectOverlapInfo', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTOVERLAPINFO,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.ObjectOverlapInfo)
  ))
_sym_db.RegisterMessage(ObjectOverlapInfo)

Overlap = _reflection.GeneratedProtocolMessageType('Overlap', (_message.Message,), dict(
  DESCRIPTOR = _OVERLAP,
  __module__ = 'map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.hdmap.Overlap)
  ))
_sym_db.RegisterMessage(Overlap)


# @@protoc_insertion_point(module_scope)