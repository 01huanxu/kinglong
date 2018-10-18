# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gnss_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import cyber_header_pb2 as cyber__header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gnss_config.proto',
  package='cybertron.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x11gnss_config.proto\x12\x0f\x63ybertron.proto\x1a\x12\x63yber_header.proto\"\x9a\x05\n\x06Stream\x12.\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x1e.cybertron.proto.Stream.Format\x12\x30\n\x06serial\x18\x02 \x01(\x0b\x32\x1e.cybertron.proto.Stream.SerialH\x00\x12*\n\x03tcp\x18\x03 \x01(\x0b\x32\x1b.cybertron.proto.Stream.TcpH\x00\x12*\n\x03udp\x18\x04 \x01(\x0b\x32\x1b.cybertron.proto.Stream.UdpH\x00\x12.\n\x05ntrip\x18\x05 \x01(\x0b\x32\x1d.cybertron.proto.Stream.NtripH\x00\x12\x15\n\rpush_location\x18\x06 \x01(\x08\x1a\x31\n\x06Serial\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\x0c\x12\x17\n\tbaud_rate\x18\x02 \x01(\x05:\x04\x39\x36\x30\x30\x1a*\n\x03Tcp\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x33\x30\x30\x31\x1a*\n\x03Udp\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x33\x30\x30\x31\x1ax\n\x05Ntrip\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x32\x31\x30\x31\x12\x13\n\x0bmount_point\x18\x03 \x01(\x0c\x12\x0c\n\x04user\x18\x04 \x01(\x0c\x12\x10\n\x08password\x18\x05 \x01(\x0c\x12\x15\n\ttimeout_s\x18\x06 \x01(\r:\x02\x33\x30\"\x81\x01\n\x06\x46ormat\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04NMEA\x10\x01\x12\x0b\n\x07RTCM_V2\x10\x02\x12\x0b\n\x07RTCM_V3\x10\x03\x12\x10\n\x0cNOVATEL_TEXT\x10\n\x12\x12\n\x0eNOVATEL_BINARY\x10\x0b\x12\x0e\n\nUBLOX_TEXT\x10\x14\x12\x10\n\x0cUBLOX_BINARY\x10\x15\x42\x06\n\x04type\"+\n\rNovatelConfig\x12\x1a\n\x0fimu_orientation\x18\x01 \x01(\x05:\x01\x35\"\r\n\x0bUbloxConfig\"\x8a\x05\n\x0bGnss_Config\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.cybertron.proto.Stream\x12(\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x17.cybertron.proto.Stream\x12)\n\x08rtk_from\x18\x03 \x01(\x0b\x32\x17.cybertron.proto.Stream\x12\'\n\x06rtk_to\x18\x04 \x01(\x0b\x32\x17.cybertron.proto.Stream\x12\x16\n\x0elogin_commands\x18\x05 \x03(\x0c\x12\x17\n\x0flogout_commands\x18\x06 \x03(\x0c\x12\x38\n\x0enovatel_config\x18\x07 \x01(\x0b\x32\x1e.cybertron.proto.NovatelConfigH\x00\x12\x34\n\x0cublox_config\x18\x08 \x01(\x0b\x32\x1c.cybertron.proto.UbloxConfigH\x00\x12G\n\x11rtk_solution_type\x18\t \x01(\x0e\x32,.cybertron.proto.Gnss_Config.RtkSolutionType\x12\x14\n\x08imu_type\x18\n \x02(\r:\x02\x33\x31\x12/\n\x10raw_data_channel\x18\x0b \x02(\t:\x15/sensor/gnss/raw_data\x12\x31\n\x11rtcm_data_channel\x18\x0c \x02(\t:\x16/sensor/gnss/rtcm_data\x12\x18\n\nqueue_size\x18\r \x01(\x04:\x04\x32\x30\x30\x30\"G\n\x0fRtkSolutionType\x12\x19\n\x15RTK_RECEIVER_SOLUTION\x10\x01\x12\x19\n\x15RTK_SOFTWARE_SOLUTION\x10\x02\x42\x0f\n\rdevice_config\"=\n\rINS_TF_Config\x12\x12\n\nproj4_text\x18\x01 \x02(\t\x12\x18\n\x10wgs84_proj4_text\x18\x02 \x02(\t\"\x16\n\x05GPGGA\x12\r\n\x05gpgga\x18\x01 \x02(\t\"K\n\x07RawData\x12\x32\n\x0c\x63yber_header\x18\x01 \x01(\x0b\x32\x1c.cybertron.proto.CyberHeader\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c')
  ,
  dependencies=[cyber__header__pb2.DESCRIPTOR,])



_STREAM_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='cybertron.proto.Stream.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NMEA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTCM_V2', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTCM_V3', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOVATEL_TEXT', index=4, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOVATEL_BINARY', index=5, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UBLOX_TEXT', index=6, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UBLOX_BINARY', index=7, number=21,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=588,
  serialized_end=717,
)
_sym_db.RegisterEnumDescriptor(_STREAM_FORMAT)

_GNSS_CONFIG_RTKSOLUTIONTYPE = _descriptor.EnumDescriptor(
  name='RtkSolutionType',
  full_name='cybertron.proto.Gnss_Config.RtkSolutionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RTK_RECEIVER_SOLUTION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTK_SOFTWARE_SOLUTION', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1350,
  serialized_end=1421,
)
_sym_db.RegisterEnumDescriptor(_GNSS_CONFIG_RTKSOLUTIONTYPE)


_STREAM_SERIAL = _descriptor.Descriptor(
  name='Serial',
  full_name='cybertron.proto.Stream.Serial',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='cybertron.proto.Stream.Serial.device', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baud_rate', full_name='cybertron.proto.Stream.Serial.baud_rate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=9600,
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
  serialized_start=326,
  serialized_end=375,
)

_STREAM_TCP = _descriptor.Descriptor(
  name='Tcp',
  full_name='cybertron.proto.Stream.Tcp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cybertron.proto.Stream.Tcp.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='cybertron.proto.Stream.Tcp.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3001,
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
  serialized_start=377,
  serialized_end=419,
)

_STREAM_UDP = _descriptor.Descriptor(
  name='Udp',
  full_name='cybertron.proto.Stream.Udp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cybertron.proto.Stream.Udp.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='cybertron.proto.Stream.Udp.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3001,
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
  serialized_start=421,
  serialized_end=463,
)

_STREAM_NTRIP = _descriptor.Descriptor(
  name='Ntrip',
  full_name='cybertron.proto.Stream.Ntrip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cybertron.proto.Stream.Ntrip.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='cybertron.proto.Stream.Ntrip.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2101,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_point', full_name='cybertron.proto.Stream.Ntrip.mount_point', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='cybertron.proto.Stream.Ntrip.user', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='cybertron.proto.Stream.Ntrip.password', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout_s', full_name='cybertron.proto.Stream.Ntrip.timeout_s', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=30,
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
  serialized_start=465,
  serialized_end=585,
)

_STREAM = _descriptor.Descriptor(
  name='Stream',
  full_name='cybertron.proto.Stream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='cybertron.proto.Stream.format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial', full_name='cybertron.proto.Stream.serial', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tcp', full_name='cybertron.proto.Stream.tcp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='udp', full_name='cybertron.proto.Stream.udp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ntrip', full_name='cybertron.proto.Stream.ntrip', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='push_location', full_name='cybertron.proto.Stream.push_location', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STREAM_SERIAL, _STREAM_TCP, _STREAM_UDP, _STREAM_NTRIP, ],
  enum_types=[
    _STREAM_FORMAT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='cybertron.proto.Stream.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=59,
  serialized_end=725,
)


_NOVATELCONFIG = _descriptor.Descriptor(
  name='NovatelConfig',
  full_name='cybertron.proto.NovatelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imu_orientation', full_name='cybertron.proto.NovatelConfig.imu_orientation', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
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
  serialized_start=727,
  serialized_end=770,
)


_UBLOXCONFIG = _descriptor.Descriptor(
  name='UbloxConfig',
  full_name='cybertron.proto.UbloxConfig',
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
  serialized_start=772,
  serialized_end=785,
)


_GNSS_CONFIG = _descriptor.Descriptor(
  name='Gnss_Config',
  full_name='cybertron.proto.Gnss_Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cybertron.proto.Gnss_Config.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command', full_name='cybertron.proto.Gnss_Config.command', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtk_from', full_name='cybertron.proto.Gnss_Config.rtk_from', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtk_to', full_name='cybertron.proto.Gnss_Config.rtk_to', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_commands', full_name='cybertron.proto.Gnss_Config.login_commands', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logout_commands', full_name='cybertron.proto.Gnss_Config.logout_commands', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='novatel_config', full_name='cybertron.proto.Gnss_Config.novatel_config', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ublox_config', full_name='cybertron.proto.Gnss_Config.ublox_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtk_solution_type', full_name='cybertron.proto.Gnss_Config.rtk_solution_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imu_type', full_name='cybertron.proto.Gnss_Config.imu_type', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=31,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_data_channel', full_name='cybertron.proto.Gnss_Config.raw_data_channel', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("/sensor/gnss/raw_data").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtcm_data_channel', full_name='cybertron.proto.Gnss_Config.rtcm_data_channel', index=11,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("/sensor/gnss/rtcm_data").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queue_size', full_name='cybertron.proto.Gnss_Config.queue_size', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GNSS_CONFIG_RTKSOLUTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='device_config', full_name='cybertron.proto.Gnss_Config.device_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=788,
  serialized_end=1438,
)


_INS_TF_CONFIG = _descriptor.Descriptor(
  name='INS_TF_Config',
  full_name='cybertron.proto.INS_TF_Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proj4_text', full_name='cybertron.proto.INS_TF_Config.proj4_text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wgs84_proj4_text', full_name='cybertron.proto.INS_TF_Config.wgs84_proj4_text', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=1440,
  serialized_end=1501,
)


_GPGGA = _descriptor.Descriptor(
  name='GPGGA',
  full_name='cybertron.proto.GPGGA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpgga', full_name='cybertron.proto.GPGGA.gpgga', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=1503,
  serialized_end=1525,
)


_RAWDATA = _descriptor.Descriptor(
  name='RawData',
  full_name='cybertron.proto.RawData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cyber_header', full_name='cybertron.proto.RawData.cyber_header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='cybertron.proto.RawData.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1527,
  serialized_end=1602,
)

_STREAM_SERIAL.containing_type = _STREAM
_STREAM_TCP.containing_type = _STREAM
_STREAM_UDP.containing_type = _STREAM
_STREAM_NTRIP.containing_type = _STREAM
_STREAM.fields_by_name['format'].enum_type = _STREAM_FORMAT
_STREAM.fields_by_name['serial'].message_type = _STREAM_SERIAL
_STREAM.fields_by_name['tcp'].message_type = _STREAM_TCP
_STREAM.fields_by_name['udp'].message_type = _STREAM_UDP
_STREAM.fields_by_name['ntrip'].message_type = _STREAM_NTRIP
_STREAM_FORMAT.containing_type = _STREAM
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['serial'])
_STREAM.fields_by_name['serial'].containing_oneof = _STREAM.oneofs_by_name['type']
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['tcp'])
_STREAM.fields_by_name['tcp'].containing_oneof = _STREAM.oneofs_by_name['type']
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['udp'])
_STREAM.fields_by_name['udp'].containing_oneof = _STREAM.oneofs_by_name['type']
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['ntrip'])
_STREAM.fields_by_name['ntrip'].containing_oneof = _STREAM.oneofs_by_name['type']
_GNSS_CONFIG.fields_by_name['data'].message_type = _STREAM
_GNSS_CONFIG.fields_by_name['command'].message_type = _STREAM
_GNSS_CONFIG.fields_by_name['rtk_from'].message_type = _STREAM
_GNSS_CONFIG.fields_by_name['rtk_to'].message_type = _STREAM
_GNSS_CONFIG.fields_by_name['novatel_config'].message_type = _NOVATELCONFIG
_GNSS_CONFIG.fields_by_name['ublox_config'].message_type = _UBLOXCONFIG
_GNSS_CONFIG.fields_by_name['rtk_solution_type'].enum_type = _GNSS_CONFIG_RTKSOLUTIONTYPE
_GNSS_CONFIG_RTKSOLUTIONTYPE.containing_type = _GNSS_CONFIG
_GNSS_CONFIG.oneofs_by_name['device_config'].fields.append(
  _GNSS_CONFIG.fields_by_name['novatel_config'])
_GNSS_CONFIG.fields_by_name['novatel_config'].containing_oneof = _GNSS_CONFIG.oneofs_by_name['device_config']
_GNSS_CONFIG.oneofs_by_name['device_config'].fields.append(
  _GNSS_CONFIG.fields_by_name['ublox_config'])
_GNSS_CONFIG.fields_by_name['ublox_config'].containing_oneof = _GNSS_CONFIG.oneofs_by_name['device_config']
_RAWDATA.fields_by_name['cyber_header'].message_type = cyber__header__pb2._CYBERHEADER
DESCRIPTOR.message_types_by_name['Stream'] = _STREAM
DESCRIPTOR.message_types_by_name['NovatelConfig'] = _NOVATELCONFIG
DESCRIPTOR.message_types_by_name['UbloxConfig'] = _UBLOXCONFIG
DESCRIPTOR.message_types_by_name['Gnss_Config'] = _GNSS_CONFIG
DESCRIPTOR.message_types_by_name['INS_TF_Config'] = _INS_TF_CONFIG
DESCRIPTOR.message_types_by_name['GPGGA'] = _GPGGA
DESCRIPTOR.message_types_by_name['RawData'] = _RAWDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Stream = _reflection.GeneratedProtocolMessageType('Stream', (_message.Message,), dict(

  Serial = _reflection.GeneratedProtocolMessageType('Serial', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_SERIAL,
    __module__ = 'gnss_config_pb2'
    # @@protoc_insertion_point(class_scope:cybertron.proto.Stream.Serial)
    ))
  ,

  Tcp = _reflection.GeneratedProtocolMessageType('Tcp', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_TCP,
    __module__ = 'gnss_config_pb2'
    # @@protoc_insertion_point(class_scope:cybertron.proto.Stream.Tcp)
    ))
  ,

  Udp = _reflection.GeneratedProtocolMessageType('Udp', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_UDP,
    __module__ = 'gnss_config_pb2'
    # @@protoc_insertion_point(class_scope:cybertron.proto.Stream.Udp)
    ))
  ,

  Ntrip = _reflection.GeneratedProtocolMessageType('Ntrip', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_NTRIP,
    __module__ = 'gnss_config_pb2'
    # @@protoc_insertion_point(class_scope:cybertron.proto.Stream.Ntrip)
    ))
  ,
  DESCRIPTOR = _STREAM,
  __module__ = 'gnss_config_pb2'
  # @@protoc_insertion_point(class_scope:cybertron.proto.Stream)
  ))
_sym_db.RegisterMessage(Stream)
_sym_db.RegisterMessage(Stream.Serial)
_sym_db.RegisterMessage(Stream.Tcp)
_sym_db.RegisterMessage(Stream.Udp)
_sym_db.RegisterMessage(Stream.Ntrip)

NovatelConfig = _reflection.GeneratedProtocolMessageType('NovatelConfig', (_message.Message,), dict(
  DESCRIPTOR = _NOVATELCONFIG,
  __module__ = 'gnss_config_pb2'
  # @@protoc_insertion_point(class_scope:cybertron.proto.NovatelConfig)
  ))
_sym_db.RegisterMessage(NovatelConfig)

UbloxConfig = _reflection.GeneratedProtocolMessageType('UbloxConfig', (_message.Message,), dict(
  DESCRIPTOR = _UBLOXCONFIG,
  __module__ = 'gnss_config_pb2'
  # @@protoc_insertion_point(class_scope:cybertron.proto.UbloxConfig)
  ))
_sym_db.RegisterMessage(UbloxConfig)

Gnss_Config = _reflection.GeneratedProtocolMessageType('Gnss_Config', (_message.Message,), dict(
  DESCRIPTOR = _GNSS_CONFIG,
  __module__ = 'gnss_config_pb2'
  # @@protoc_insertion_point(class_scope:cybertron.proto.Gnss_Config)
  ))
_sym_db.RegisterMessage(Gnss_Config)

INS_TF_Config = _reflection.GeneratedProtocolMessageType('INS_TF_Config', (_message.Message,), dict(
  DESCRIPTOR = _INS_TF_CONFIG,
  __module__ = 'gnss_config_pb2'
  # @@protoc_insertion_point(class_scope:cybertron.proto.INS_TF_Config)
  ))
_sym_db.RegisterMessage(INS_TF_Config)

GPGGA = _reflection.GeneratedProtocolMessageType('GPGGA', (_message.Message,), dict(
  DESCRIPTOR = _GPGGA,
  __module__ = 'gnss_config_pb2'
  # @@protoc_insertion_point(class_scope:cybertron.proto.GPGGA)
  ))
_sym_db.RegisterMessage(GPGGA)

RawData = _reflection.GeneratedProtocolMessageType('RawData', (_message.Message,), dict(
  DESCRIPTOR = _RAWDATA,
  __module__ = 'gnss_config_pb2'
  # @@protoc_insertion_point(class_scope:cybertron.proto.RawData)
  ))
_sym_db.RegisterMessage(RawData)


# @@protoc_insertion_point(module_scope)
