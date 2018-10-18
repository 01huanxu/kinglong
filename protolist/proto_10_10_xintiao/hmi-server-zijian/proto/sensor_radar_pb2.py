# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_radar.proto

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


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor_radar.proto',
  package='adu.common.sensor',
  syntax='proto2',
  serialized_pb=_b('\n\x12sensor_radar.proto\x12\x11\x61\x64u.common.sensor\x1a\x0cheader.proto\"\x99\x03\n\x0e\x44\x65lphiRadarObs\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.adu.common.header.Header\x12\x13\n\x0bobstacle_id\x18\x02 \x01(\x05\x12\r\n\x05range\x18\x03 \x02(\x01\x12\r\n\x05theta\x18\x04 \x02(\x01\x12\x17\n\x0fradial_velocity\x18\x05 \x02(\x01\x12\x0b\n\x03rcs\x18\x06 \x01(\x01\x12\x1b\n\x13tangential_velocity\x18\x07 \x01(\x01\x12\x1b\n\x13radial_acceleration\x18\x08 \x01(\x01\x12\r\n\x05width\x18\t \x01(\x01\x12\x1b\n\x13track_group_changed\x18\n \x01(\x08\x12\x1c\n\x14track_med_range_mode\x18\x0b \x01(\x05\x12\x14\n\x0ctrack_status\x18\x0c \x01(\x05\x12\x1b\n\x13track_bridge_object\x18\r \x01(\x08\x12\x14\n\x0ctrack_moving\x18\x0e \x01(\x08\x12\x1a\n\x12track_movable_fast\x18\x0f \x01(\x08\x12\x1a\n\x12track_movable_slow\x18\x10 \x01(\x08\"\xc5\x04\n\rContiRadarObs\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.adu.common.header.Header\x12\x16\n\x0e\x63lusterortrack\x18\x02 \x01(\x08\x12\x13\n\x0bobstacle_id\x18\x03 \x01(\x05\x12\x16\n\x0elongitude_dist\x18\x04 \x02(\x01\x12\x14\n\x0clateral_dist\x18\x05 \x02(\x01\x12\x15\n\rlongitude_vel\x18\x06 \x02(\x01\x12\x13\n\x0blateral_vel\x18\x07 \x02(\x01\x12\x0b\n\x03rcs\x18\x08 \x01(\x01\x12\x0f\n\x07\x64ynprop\x18\t \x01(\x05\x12\x1a\n\x12longitude_dist_rms\x18\n \x01(\x01\x12\x18\n\x10lateral_dist_rms\x18\x0b \x01(\x01\x12\x19\n\x11longitude_vel_rms\x18\x0c \x01(\x01\x12\x17\n\x0flateral_vel_rms\x18\r \x01(\x01\x12\x11\n\tprobexist\x18\x0e \x01(\x01\x12\x12\n\nmeas_state\x18\x0f \x01(\x05\x12\x17\n\x0flongitude_accel\x18\x10 \x01(\x01\x12\x15\n\rlateral_accel\x18\x11 \x01(\x01\x12\x17\n\x0foritation_angle\x18\x12 \x01(\x01\x12\x1b\n\x13longitude_accel_rms\x18\x13 \x01(\x01\x12\x19\n\x11lateral_accel_rms\x18\x14 \x01(\x01\x12\x1b\n\x13oritation_angle_rms\x18\x15 \x01(\x01\x12\x0e\n\x06length\x18\x16 \x01(\x01\x12\r\n\x05width\x18\x17 \x01(\x01\x12\x16\n\x0eobstacle_class\x18\x18 \x01(\x05\"\xfc\x01\n\rRadarObsArray\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.adu.common.header.Header\x12<\n\x04type\x18\x02 \x01(\x0e\x32\x1c.adu.common.sensor.RadarType:\x10\x44\x45LPHI_ESR_92121\x12\x34\n\tdelphiobs\x18\x03 \x03(\x0b\x32!.adu.common.sensor.DelphiRadarObs\x12\x32\n\x08\x63ontiobs\x18\x04 \x03(\x0b\x32 .adu.common.sensor.ContiRadarObs\x12\x18\n\x10measurement_time\x18\x05 \x01(\x01*<\n\tRadarType\x12\x14\n\x10\x44\x45LPHI_ESR_92121\x10\x00\x12\x19\n\x15\x43ONTINENTAL_ARS_40821\x10\x01')
  ,
  dependencies=[header__pb2.DESCRIPTOR,])

_RADARTYPE = _descriptor.EnumDescriptor(
  name='RadarType',
  full_name='adu.common.sensor.RadarType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DELPHI_ESR_92121', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINENTAL_ARS_40821', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1306,
  serialized_end=1366,
)
_sym_db.RegisterEnumDescriptor(_RADARTYPE)

RadarType = enum_type_wrapper.EnumTypeWrapper(_RADARTYPE)
DELPHI_ESR_92121 = 0
CONTINENTAL_ARS_40821 = 1



_DELPHIRADAROBS = _descriptor.Descriptor(
  name='DelphiRadarObs',
  full_name='adu.common.sensor.DelphiRadarObs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='adu.common.sensor.DelphiRadarObs.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obstacle_id', full_name='adu.common.sensor.DelphiRadarObs.obstacle_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='adu.common.sensor.DelphiRadarObs.range', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theta', full_name='adu.common.sensor.DelphiRadarObs.theta', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='radial_velocity', full_name='adu.common.sensor.DelphiRadarObs.radial_velocity', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rcs', full_name='adu.common.sensor.DelphiRadarObs.rcs', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tangential_velocity', full_name='adu.common.sensor.DelphiRadarObs.tangential_velocity', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='radial_acceleration', full_name='adu.common.sensor.DelphiRadarObs.radial_acceleration', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='adu.common.sensor.DelphiRadarObs.width', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_group_changed', full_name='adu.common.sensor.DelphiRadarObs.track_group_changed', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_med_range_mode', full_name='adu.common.sensor.DelphiRadarObs.track_med_range_mode', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_status', full_name='adu.common.sensor.DelphiRadarObs.track_status', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_bridge_object', full_name='adu.common.sensor.DelphiRadarObs.track_bridge_object', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_moving', full_name='adu.common.sensor.DelphiRadarObs.track_moving', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_movable_fast', full_name='adu.common.sensor.DelphiRadarObs.track_movable_fast', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_movable_slow', full_name='adu.common.sensor.DelphiRadarObs.track_movable_slow', index=15,
      number=16, type=8, cpp_type=7, label=1,
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
  serialized_start=56,
  serialized_end=465,
)


_CONTIRADAROBS = _descriptor.Descriptor(
  name='ContiRadarObs',
  full_name='adu.common.sensor.ContiRadarObs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='adu.common.sensor.ContiRadarObs.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clusterortrack', full_name='adu.common.sensor.ContiRadarObs.clusterortrack', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obstacle_id', full_name='adu.common.sensor.ContiRadarObs.obstacle_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_dist', full_name='adu.common.sensor.ContiRadarObs.longitude_dist', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_dist', full_name='adu.common.sensor.ContiRadarObs.lateral_dist', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_vel', full_name='adu.common.sensor.ContiRadarObs.longitude_vel', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_vel', full_name='adu.common.sensor.ContiRadarObs.lateral_vel', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rcs', full_name='adu.common.sensor.ContiRadarObs.rcs', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dynprop', full_name='adu.common.sensor.ContiRadarObs.dynprop', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_dist_rms', full_name='adu.common.sensor.ContiRadarObs.longitude_dist_rms', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_dist_rms', full_name='adu.common.sensor.ContiRadarObs.lateral_dist_rms', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_vel_rms', full_name='adu.common.sensor.ContiRadarObs.longitude_vel_rms', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_vel_rms', full_name='adu.common.sensor.ContiRadarObs.lateral_vel_rms', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probexist', full_name='adu.common.sensor.ContiRadarObs.probexist', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meas_state', full_name='adu.common.sensor.ContiRadarObs.meas_state', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_accel', full_name='adu.common.sensor.ContiRadarObs.longitude_accel', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_accel', full_name='adu.common.sensor.ContiRadarObs.lateral_accel', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oritation_angle', full_name='adu.common.sensor.ContiRadarObs.oritation_angle', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_accel_rms', full_name='adu.common.sensor.ContiRadarObs.longitude_accel_rms', index=18,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_accel_rms', full_name='adu.common.sensor.ContiRadarObs.lateral_accel_rms', index=19,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oritation_angle_rms', full_name='adu.common.sensor.ContiRadarObs.oritation_angle_rms', index=20,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='adu.common.sensor.ContiRadarObs.length', index=21,
      number=22, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='adu.common.sensor.ContiRadarObs.width', index=22,
      number=23, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obstacle_class', full_name='adu.common.sensor.ContiRadarObs.obstacle_class', index=23,
      number=24, type=5, cpp_type=1, label=1,
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
  serialized_start=468,
  serialized_end=1049,
)


_RADAROBSARRAY = _descriptor.Descriptor(
  name='RadarObsArray',
  full_name='adu.common.sensor.RadarObsArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='adu.common.sensor.RadarObsArray.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='adu.common.sensor.RadarObsArray.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delphiobs', full_name='adu.common.sensor.RadarObsArray.delphiobs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contiobs', full_name='adu.common.sensor.RadarObsArray.contiobs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='adu.common.sensor.RadarObsArray.measurement_time', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=1052,
  serialized_end=1304,
)

_DELPHIRADAROBS.fields_by_name['header'].message_type = header__pb2._HEADER
_CONTIRADAROBS.fields_by_name['header'].message_type = header__pb2._HEADER
_RADAROBSARRAY.fields_by_name['header'].message_type = header__pb2._HEADER
_RADAROBSARRAY.fields_by_name['type'].enum_type = _RADARTYPE
_RADAROBSARRAY.fields_by_name['delphiobs'].message_type = _DELPHIRADAROBS
_RADAROBSARRAY.fields_by_name['contiobs'].message_type = _CONTIRADAROBS
DESCRIPTOR.message_types_by_name['DelphiRadarObs'] = _DELPHIRADAROBS
DESCRIPTOR.message_types_by_name['ContiRadarObs'] = _CONTIRADAROBS
DESCRIPTOR.message_types_by_name['RadarObsArray'] = _RADAROBSARRAY
DESCRIPTOR.enum_types_by_name['RadarType'] = _RADARTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DelphiRadarObs = _reflection.GeneratedProtocolMessageType('DelphiRadarObs', (_message.Message,), dict(
  DESCRIPTOR = _DELPHIRADAROBS,
  __module__ = 'sensor_radar_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.sensor.DelphiRadarObs)
  ))
_sym_db.RegisterMessage(DelphiRadarObs)

ContiRadarObs = _reflection.GeneratedProtocolMessageType('ContiRadarObs', (_message.Message,), dict(
  DESCRIPTOR = _CONTIRADAROBS,
  __module__ = 'sensor_radar_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.sensor.ContiRadarObs)
  ))
_sym_db.RegisterMessage(ContiRadarObs)

RadarObsArray = _reflection.GeneratedProtocolMessageType('RadarObsArray', (_message.Message,), dict(
  DESCRIPTOR = _RADAROBSARRAY,
  __module__ = 'sensor_radar_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.sensor.RadarObsArray)
  ))
_sym_db.RegisterMessage(RadarObsArray)


# @@protoc_insertion_point(module_scope)