# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: closeloop_metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import closeloop_params_pb2 as closeloop__params__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='closeloop_metric.proto',
  package='adu.workers.closeloop',
  syntax='proto2',
  serialized_pb=_b('\n\x16\x63loseloop_metric.proto\x12\x15\x61\x64u.workers.closeloop\x1a\x16\x63loseloop_params.proto\"\xc4\x08\n\x06Metric\x12<\n\nmetric_cmd\x18\x01 \x01(\x0e\x32(.adu.workers.closeloop.Metric.MetricType\x12?\n\x0clocalization\x18\x02 \x01(\x0b\x32).adu.workers.closeloop.LocalizationParams\x12;\n\nperception\x18\x03 \x01(\x0b\x32\'.adu.workers.closeloop.PerceptionParams\x12\x39\n\tparkingin\x18\x04 \x01(\x0b\x32&.adu.workers.closeloop.ParkingInParams\x12;\n\nparkingout\x18\x05 \x01(\x0b\x32\'.adu.workers.closeloop.ParkingOutParams\x12\x43\n\x0eparkingstation\x18\x06 \x01(\x0b\x32+.adu.workers.closeloop.ParkingStationParams\x12\x38\n\x0cstraightline\x18\x07 \x01(\x0b\x32\".adu.workers.closeloop.BasicParams\x12\x33\n\x06\x61scent\x18\x08 \x01(\x0b\x32#.adu.workers.closeloop.AscentParams\x12\x39\n\tspeedbump\x18\t \x01(\x0b\x32&.adu.workers.closeloop.SpeedBumpParams\x12\x33\n\x07turning\x18\n \x01(\x0b\x32\".adu.workers.closeloop.BasicParams\x12\x34\n\x08sturning\x18\x0b \x01(\x0b\x32\".adu.workers.closeloop.BasicParams\x12\x31\n\x05nudge\x18\x0c \x01(\x0b\x32\".adu.workers.closeloop.NudgeParams\x12\x36\n\nrightangle\x18\r \x01(\x0b\x32\".adu.workers.closeloop.BasicParams\x12/\n\x04xing\x18\x0e \x01(\x0b\x32!.adu.workers.closeloop.XingParams\"\x8f\x02\n\nMetricType\x12\x15\n\x11TEST_LOCALIZATION\x10\x00\x12\x13\n\x0fTEST_PERCEPTION\x10\x01\x12\x12\n\x0eTEST_PARKINGIN\x10\x02\x12\x13\n\x0fTEST_PARKINGOUT\x10\x03\x12\x17\n\x13TEST_PARKINGSTATION\x10\x04\x12\x15\n\x11TEST_STRAIGHTLINE\x10\x05\x12\x0f\n\x0bTEST_ASCENT\x10\x06\x12\x12\n\x0eTEST_SPEEDBUMP\x10\x07\x12\x10\n\x0cTEST_TURNING\x10\x08\x12\x11\n\rTEST_STURNING\x10\t\x12\x0e\n\nTEST_NUDGE\x10\n\x12\x13\n\x0fTEST_RIGHTANGLE\x10\x0b\x12\r\n\tTEST_XING\x10\x0c\"\x87\x07\n\x0cMetricResult\x12>\n\x06result\x18\x01 \x01(\x0e\x32..adu.workers.closeloop.MetricResult.ResultType\x12?\n\x0clocalization\x18\x02 \x01(\x0b\x32).adu.workers.closeloop.LocalizationResult\x12;\n\nperception\x18\x03 \x01(\x0b\x32\'.adu.workers.closeloop.PerceptionResult\x12\x39\n\tparkingin\x18\x04 \x01(\x0b\x32&.adu.workers.closeloop.ParkingInResult\x12;\n\nparkingout\x18\x05 \x01(\x0b\x32\'.adu.workers.closeloop.ParkingOutResult\x12\x43\n\x0eparkingstation\x18\x06 \x01(\x0b\x32+.adu.workers.closeloop.ParkingStationResult\x12\x38\n\x0cstraightline\x18\x07 \x01(\x0b\x32\".adu.workers.closeloop.BasicResult\x12\x33\n\x06\x61scent\x18\x08 \x01(\x0b\x32#.adu.workers.closeloop.AscentResult\x12\x39\n\tspeedbump\x18\t \x01(\x0b\x32&.adu.workers.closeloop.SpeedBumpResult\x12\x33\n\x07turning\x18\n \x01(\x0b\x32\".adu.workers.closeloop.BasicResult\x12\x34\n\x08sturning\x18\x0b \x01(\x0b\x32\".adu.workers.closeloop.BasicResult\x12\x31\n\x05nudge\x18\x0c \x01(\x0b\x32\".adu.workers.closeloop.NudgeResult\x12\x36\n\nrightangle\x18\r \x01(\x0b\x32\".adu.workers.closeloop.BasicResult\x12/\n\x04xing\x18\x0e \x01(\x0b\x32!.adu.workers.closeloop.XingResult\"K\n\nResultType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06PASSED\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\n\n\x06NODATA\x10\x03\x12\x0c\n\x08NOMETRIC\x10\x04\"`\n\tMetricACK\x12\x35\n\x03\x61\x63k\x18\x01 \x01(\x0e\x32(.adu.workers.closeloop.MetricACK.ACKType\"\x1c\n\x07\x41\x43KType\x12\t\n\x05\x45RROR\x10\x00\x12\x06\n\x02OK\x10\x01')
  ,
  dependencies=[closeloop__params__pb2.DESCRIPTOR,])



_METRIC_METRICTYPE = _descriptor.EnumDescriptor(
  name='MetricType',
  full_name='adu.workers.closeloop.Metric.MetricType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEST_LOCALIZATION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_PERCEPTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_PARKINGIN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_PARKINGOUT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_PARKINGSTATION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_STRAIGHTLINE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_ASCENT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_SPEEDBUMP', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_TURNING', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_STURNING', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_NUDGE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_RIGHTANGLE', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_XING', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=895,
  serialized_end=1166,
)
_sym_db.RegisterEnumDescriptor(_METRIC_METRICTYPE)

_METRICRESULT_RESULTTYPE = _descriptor.EnumDescriptor(
  name='ResultType',
  full_name='adu.workers.closeloop.MetricResult.ResultType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODATA', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOMETRIC', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1997,
  serialized_end=2072,
)
_sym_db.RegisterEnumDescriptor(_METRICRESULT_RESULTTYPE)

_METRICACK_ACKTYPE = _descriptor.EnumDescriptor(
  name='ACKType',
  full_name='adu.workers.closeloop.MetricACK.ACKType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2142,
  serialized_end=2170,
)
_sym_db.RegisterEnumDescriptor(_METRICACK_ACKTYPE)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='adu.workers.closeloop.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_cmd', full_name='adu.workers.closeloop.Metric.metric_cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localization', full_name='adu.workers.closeloop.Metric.localization', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perception', full_name='adu.workers.closeloop.Metric.perception', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parkingin', full_name='adu.workers.closeloop.Metric.parkingin', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parkingout', full_name='adu.workers.closeloop.Metric.parkingout', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parkingstation', full_name='adu.workers.closeloop.Metric.parkingstation', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='straightline', full_name='adu.workers.closeloop.Metric.straightline', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ascent', full_name='adu.workers.closeloop.Metric.ascent', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speedbump', full_name='adu.workers.closeloop.Metric.speedbump', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turning', full_name='adu.workers.closeloop.Metric.turning', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sturning', full_name='adu.workers.closeloop.Metric.sturning', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nudge', full_name='adu.workers.closeloop.Metric.nudge', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rightangle', full_name='adu.workers.closeloop.Metric.rightangle', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xing', full_name='adu.workers.closeloop.Metric.xing', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRIC_METRICTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=1166,
)


_METRICRESULT = _descriptor.Descriptor(
  name='MetricResult',
  full_name='adu.workers.closeloop.MetricResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='adu.workers.closeloop.MetricResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localization', full_name='adu.workers.closeloop.MetricResult.localization', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perception', full_name='adu.workers.closeloop.MetricResult.perception', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parkingin', full_name='adu.workers.closeloop.MetricResult.parkingin', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parkingout', full_name='adu.workers.closeloop.MetricResult.parkingout', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parkingstation', full_name='adu.workers.closeloop.MetricResult.parkingstation', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='straightline', full_name='adu.workers.closeloop.MetricResult.straightline', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ascent', full_name='adu.workers.closeloop.MetricResult.ascent', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speedbump', full_name='adu.workers.closeloop.MetricResult.speedbump', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turning', full_name='adu.workers.closeloop.MetricResult.turning', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sturning', full_name='adu.workers.closeloop.MetricResult.sturning', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nudge', full_name='adu.workers.closeloop.MetricResult.nudge', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rightangle', full_name='adu.workers.closeloop.MetricResult.rightangle', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xing', full_name='adu.workers.closeloop.MetricResult.xing', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRICRESULT_RESULTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1169,
  serialized_end=2072,
)


_METRICACK = _descriptor.Descriptor(
  name='MetricACK',
  full_name='adu.workers.closeloop.MetricACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='adu.workers.closeloop.MetricACK.ack', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRICACK_ACKTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2074,
  serialized_end=2170,
)

_METRIC.fields_by_name['metric_cmd'].enum_type = _METRIC_METRICTYPE
_METRIC.fields_by_name['localization'].message_type = closeloop__params__pb2._LOCALIZATIONPARAMS
_METRIC.fields_by_name['perception'].message_type = closeloop__params__pb2._PERCEPTIONPARAMS
_METRIC.fields_by_name['parkingin'].message_type = closeloop__params__pb2._PARKINGINPARAMS
_METRIC.fields_by_name['parkingout'].message_type = closeloop__params__pb2._PARKINGOUTPARAMS
_METRIC.fields_by_name['parkingstation'].message_type = closeloop__params__pb2._PARKINGSTATIONPARAMS
_METRIC.fields_by_name['straightline'].message_type = closeloop__params__pb2._BASICPARAMS
_METRIC.fields_by_name['ascent'].message_type = closeloop__params__pb2._ASCENTPARAMS
_METRIC.fields_by_name['speedbump'].message_type = closeloop__params__pb2._SPEEDBUMPPARAMS
_METRIC.fields_by_name['turning'].message_type = closeloop__params__pb2._BASICPARAMS
_METRIC.fields_by_name['sturning'].message_type = closeloop__params__pb2._BASICPARAMS
_METRIC.fields_by_name['nudge'].message_type = closeloop__params__pb2._NUDGEPARAMS
_METRIC.fields_by_name['rightangle'].message_type = closeloop__params__pb2._BASICPARAMS
_METRIC.fields_by_name['xing'].message_type = closeloop__params__pb2._XINGPARAMS
_METRIC_METRICTYPE.containing_type = _METRIC
_METRICRESULT.fields_by_name['result'].enum_type = _METRICRESULT_RESULTTYPE
_METRICRESULT.fields_by_name['localization'].message_type = closeloop__params__pb2._LOCALIZATIONRESULT
_METRICRESULT.fields_by_name['perception'].message_type = closeloop__params__pb2._PERCEPTIONRESULT
_METRICRESULT.fields_by_name['parkingin'].message_type = closeloop__params__pb2._PARKINGINRESULT
_METRICRESULT.fields_by_name['parkingout'].message_type = closeloop__params__pb2._PARKINGOUTRESULT
_METRICRESULT.fields_by_name['parkingstation'].message_type = closeloop__params__pb2._PARKINGSTATIONRESULT
_METRICRESULT.fields_by_name['straightline'].message_type = closeloop__params__pb2._BASICRESULT
_METRICRESULT.fields_by_name['ascent'].message_type = closeloop__params__pb2._ASCENTRESULT
_METRICRESULT.fields_by_name['speedbump'].message_type = closeloop__params__pb2._SPEEDBUMPRESULT
_METRICRESULT.fields_by_name['turning'].message_type = closeloop__params__pb2._BASICRESULT
_METRICRESULT.fields_by_name['sturning'].message_type = closeloop__params__pb2._BASICRESULT
_METRICRESULT.fields_by_name['nudge'].message_type = closeloop__params__pb2._NUDGERESULT
_METRICRESULT.fields_by_name['rightangle'].message_type = closeloop__params__pb2._BASICRESULT
_METRICRESULT.fields_by_name['xing'].message_type = closeloop__params__pb2._XINGRESULT
_METRICRESULT_RESULTTYPE.containing_type = _METRICRESULT
_METRICACK.fields_by_name['ack'].enum_type = _METRICACK_ACKTYPE
_METRICACK_ACKTYPE.containing_type = _METRICACK
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['MetricResult'] = _METRICRESULT
DESCRIPTOR.message_types_by_name['MetricACK'] = _METRICACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), dict(
  DESCRIPTOR = _METRIC,
  __module__ = 'closeloop_metric_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.closeloop.Metric)
  ))
_sym_db.RegisterMessage(Metric)

MetricResult = _reflection.GeneratedProtocolMessageType('MetricResult', (_message.Message,), dict(
  DESCRIPTOR = _METRICRESULT,
  __module__ = 'closeloop_metric_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.closeloop.MetricResult)
  ))
_sym_db.RegisterMessage(MetricResult)

MetricACK = _reflection.GeneratedProtocolMessageType('MetricACK', (_message.Message,), dict(
  DESCRIPTOR = _METRICACK,
  __module__ = 'closeloop_metric_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.closeloop.MetricACK)
  ))
_sym_db.RegisterMessage(MetricACK)


# @@protoc_insertion_point(module_scope)