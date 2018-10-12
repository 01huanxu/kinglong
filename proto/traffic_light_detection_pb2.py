# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traffic_light_detection.proto

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
  name='traffic_light_detection.proto',
  package='adu.common.traffic_light',
  syntax='proto2',
  serialized_pb=_b('\n\x1dtraffic_light_detection.proto\x12\x18\x61\x64u.common.traffic_light\x1a\x0cheader.proto\"\x95\x01\n\x0fTrafficLightBox\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12;\n\x05\x63olor\x18\x05 \x01(\x0e\x32,.adu.common.traffic_light.TrafficLight.Color\x12\x10\n\x08selected\x18\x06 \x01(\x08\"\x8e\x02\n\x11TrafficLightDebug\x12:\n\x07\x63ropbox\x18\x01 \x01(\x0b\x32).adu.common.traffic_light.TrafficLightBox\x12\x36\n\x03\x62ox\x18\x02 \x03(\x0b\x32).adu.common.traffic_light.TrafficLightBox\x12\x12\n\nsignal_num\x18\x03 \x01(\x05\x12\x11\n\tvalid_pos\x18\x04 \x01(\x05\x12\x13\n\x0bts_diff_pos\x18\x05 \x01(\x01\x12\x13\n\x0bts_diff_sys\x18\x06 \x01(\x01\x12\x15\n\rproject_error\x18\x07 \x01(\x05\x12\x1d\n\x15\x64istance_to_stop_line\x18\x08 \x01(\x01\"\xc6\x01\n\x0cTrafficLight\x12;\n\x05\x63olor\x18\x01 \x01(\x0e\x32,.adu.common.traffic_light.TrafficLight.Color\x12\n\n\x02id\x18\x02 \x01(\t\x12\x15\n\nconfidence\x18\x03 \x01(\x01:\x01\x31\x12\x15\n\rtracking_time\x18\x04 \x01(\x01\"?\n\x05\x43olor\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03RED\x10\x01\x12\n\n\x06YELLOW\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\t\n\x05\x42LACK\x10\x04\"\xe3\x01\n\x15TrafficLightDetection\x12)\n\x06header\x18\x02 \x01(\x0b\x32\x19.adu.common.header.Header\x12=\n\rtraffic_light\x18\x01 \x03(\x0b\x32&.adu.common.traffic_light.TrafficLight\x12H\n\x13traffic_light_debug\x18\x03 \x01(\x0b\x32+.adu.common.traffic_light.TrafficLightDebug\x12\x16\n\x0e\x63ontain_lights\x18\x04 \x01(\x08')
  ,
  dependencies=[header__pb2.DESCRIPTOR,])



_TRAFFICLIGHT_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='adu.common.traffic_light.TrafficLight.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACK', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=634,
  serialized_end=697,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICLIGHT_COLOR)


_TRAFFICLIGHTBOX = _descriptor.Descriptor(
  name='TrafficLightBox',
  full_name='adu.common.traffic_light.TrafficLightBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='adu.common.traffic_light.TrafficLightBox.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='adu.common.traffic_light.TrafficLightBox.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='adu.common.traffic_light.TrafficLightBox.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='adu.common.traffic_light.TrafficLightBox.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color', full_name='adu.common.traffic_light.TrafficLightBox.color', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='selected', full_name='adu.common.traffic_light.TrafficLightBox.selected', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=74,
  serialized_end=223,
)


_TRAFFICLIGHTDEBUG = _descriptor.Descriptor(
  name='TrafficLightDebug',
  full_name='adu.common.traffic_light.TrafficLightDebug',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cropbox', full_name='adu.common.traffic_light.TrafficLightDebug.cropbox', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box', full_name='adu.common.traffic_light.TrafficLightDebug.box', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal_num', full_name='adu.common.traffic_light.TrafficLightDebug.signal_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_pos', full_name='adu.common.traffic_light.TrafficLightDebug.valid_pos', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts_diff_pos', full_name='adu.common.traffic_light.TrafficLightDebug.ts_diff_pos', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts_diff_sys', full_name='adu.common.traffic_light.TrafficLightDebug.ts_diff_sys', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project_error', full_name='adu.common.traffic_light.TrafficLightDebug.project_error', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance_to_stop_line', full_name='adu.common.traffic_light.TrafficLightDebug.distance_to_stop_line', index=7,
      number=8, type=1, cpp_type=5, label=1,
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
  serialized_start=226,
  serialized_end=496,
)


_TRAFFICLIGHT = _descriptor.Descriptor(
  name='TrafficLight',
  full_name='adu.common.traffic_light.TrafficLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='adu.common.traffic_light.TrafficLight.color', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='adu.common.traffic_light.TrafficLight.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='adu.common.traffic_light.TrafficLight.confidence', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracking_time', full_name='adu.common.traffic_light.TrafficLight.tracking_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRAFFICLIGHT_COLOR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=499,
  serialized_end=697,
)


_TRAFFICLIGHTDETECTION = _descriptor.Descriptor(
  name='TrafficLightDetection',
  full_name='adu.common.traffic_light.TrafficLightDetection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='adu.common.traffic_light.TrafficLightDetection.header', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_light', full_name='adu.common.traffic_light.TrafficLightDetection.traffic_light', index=1,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_light_debug', full_name='adu.common.traffic_light.TrafficLightDetection.traffic_light_debug', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contain_lights', full_name='adu.common.traffic_light.TrafficLightDetection.contain_lights', index=3,
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
  serialized_start=700,
  serialized_end=927,
)

_TRAFFICLIGHTBOX.fields_by_name['color'].enum_type = _TRAFFICLIGHT_COLOR
_TRAFFICLIGHTDEBUG.fields_by_name['cropbox'].message_type = _TRAFFICLIGHTBOX
_TRAFFICLIGHTDEBUG.fields_by_name['box'].message_type = _TRAFFICLIGHTBOX
_TRAFFICLIGHT.fields_by_name['color'].enum_type = _TRAFFICLIGHT_COLOR
_TRAFFICLIGHT_COLOR.containing_type = _TRAFFICLIGHT
_TRAFFICLIGHTDETECTION.fields_by_name['header'].message_type = header__pb2._HEADER
_TRAFFICLIGHTDETECTION.fields_by_name['traffic_light'].message_type = _TRAFFICLIGHT
_TRAFFICLIGHTDETECTION.fields_by_name['traffic_light_debug'].message_type = _TRAFFICLIGHTDEBUG
DESCRIPTOR.message_types_by_name['TrafficLightBox'] = _TRAFFICLIGHTBOX
DESCRIPTOR.message_types_by_name['TrafficLightDebug'] = _TRAFFICLIGHTDEBUG
DESCRIPTOR.message_types_by_name['TrafficLight'] = _TRAFFICLIGHT
DESCRIPTOR.message_types_by_name['TrafficLightDetection'] = _TRAFFICLIGHTDETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrafficLightBox = _reflection.GeneratedProtocolMessageType('TrafficLightBox', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICLIGHTBOX,
  __module__ = 'traffic_light_detection_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.traffic_light.TrafficLightBox)
  ))
_sym_db.RegisterMessage(TrafficLightBox)

TrafficLightDebug = _reflection.GeneratedProtocolMessageType('TrafficLightDebug', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICLIGHTDEBUG,
  __module__ = 'traffic_light_detection_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.traffic_light.TrafficLightDebug)
  ))
_sym_db.RegisterMessage(TrafficLightDebug)

TrafficLight = _reflection.GeneratedProtocolMessageType('TrafficLight', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICLIGHT,
  __module__ = 'traffic_light_detection_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.traffic_light.TrafficLight)
  ))
_sym_db.RegisterMessage(TrafficLight)

TrafficLightDetection = _reflection.GeneratedProtocolMessageType('TrafficLightDetection', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICLIGHTDETECTION,
  __module__ = 'traffic_light_detection_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.traffic_light.TrafficLightDetection)
  ))
_sym_db.RegisterMessage(TrafficLightDetection)


# @@protoc_insertion_point(module_scope)