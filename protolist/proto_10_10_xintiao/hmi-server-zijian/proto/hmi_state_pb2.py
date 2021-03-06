# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_state.proto

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
  name='hmi_state.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x0fhmi_state.proto\x12\x07\x61\x64u.hmi\"9\n\x07Point3D\x12\x0e\n\x01x\x18\x01 \x01(\x01:\x03nan\x12\x0e\n\x01y\x18\x02 \x01(\x01:\x03nan\x12\x0e\n\x01z\x18\x03 \x01(\x01:\x03nan\"M\n\x10ParkingInContext\x12\x12\n\nparking_id\x18\x01 \x01(\t\x12%\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32\x10.adu.hmi.Point3D\"K\n\x11ParkingOutContext\x12%\n\x0b\x64\x65stination\x18\x01 \x01(\x0b\x32\x10.adu.hmi.Point3D\x12\x0f\n\x07heading\x18\x02 \x01(\x01\"]\n\rFinishContext\x12\"\n\nlast_state\x18\x01 \x01(\x0e\x32\x0e.adu.hmi.State\x12(\n\x0bresult_code\x18\x02 \x01(\x0e\x32\x13.adu.hmi.ResultCode\"\xba\x01\n\x07\x43ontext\x12\x30\n\x0e\x66inish_context\x18\x01 \x01(\x0b\x32\x16.adu.hmi.FinishContextH\x00\x12\x37\n\x12parking_in_context\x18\x02 \x01(\x0b\x32\x19.adu.hmi.ParkingInContextH\x00\x12\x39\n\x13parking_out_context\x18\x03 \x01(\x0b\x32\x1a.adu.hmi.ParkingOutContextH\x00\x42\t\n\x07\x63ontext\"c\n\x08SysState\x12\x1d\n\x05state\x18\x01 \x01(\x0e\x32\x0e.adu.hmi.State\x12\x15\n\rstate_counter\x18\x02 \x01(\x01\x12!\n\x07\x63ontext\x18\x03 \x01(\x0b\x32\x10.adu.hmi.Context*_\n\x05State\x12\x08\n\x04INIT\x10\x00\x12\n\n\x06\x43RUISE\x10\x01\x12\x08\n\x04WAIT\x10\x02\x12\n\n\x06\x46INISH\x10\x03\x12\x0e\n\nPARKING_IN\x10\x04\x12\x0f\n\x0bPARKING_OUT\x10\x05\x12\t\n\x05\x45STOP\x10\x06*1\n\nResultCode\x12\x12\n\x0eRESULT_SUCCESS\x10\x00\x12\x0f\n\x0bRESULT_FAIL\x10\x01\x42\x02P\x01')
)

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='adu.hmi.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRUISE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAIT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISH', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARKING_IN', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARKING_OUT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ESTOP', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=628,
  serialized_end=723,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
_RESULTCODE = _descriptor.EnumDescriptor(
  name='ResultCode',
  full_name='adu.hmi.ResultCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_FAIL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=725,
  serialized_end=774,
)
_sym_db.RegisterEnumDescriptor(_RESULTCODE)

ResultCode = enum_type_wrapper.EnumTypeWrapper(_RESULTCODE)
INIT = 0
CRUISE = 1
WAIT = 2
FINISH = 3
PARKING_IN = 4
PARKING_OUT = 5
ESTOP = 6
RESULT_SUCCESS = 0
RESULT_FAIL = 1



_POINT3D = _descriptor.Descriptor(
  name='Point3D',
  full_name='adu.hmi.Point3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='adu.hmi.Point3D.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='adu.hmi.Point3D.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='adu.hmi.Point3D.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
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
  serialized_start=28,
  serialized_end=85,
)


_PARKINGINCONTEXT = _descriptor.Descriptor(
  name='ParkingInContext',
  full_name='adu.hmi.ParkingInContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parking_id', full_name='adu.hmi.ParkingInContext.parking_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination', full_name='adu.hmi.ParkingInContext.destination', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=87,
  serialized_end=164,
)


_PARKINGOUTCONTEXT = _descriptor.Descriptor(
  name='ParkingOutContext',
  full_name='adu.hmi.ParkingOutContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination', full_name='adu.hmi.ParkingOutContext.destination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='adu.hmi.ParkingOutContext.heading', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=166,
  serialized_end=241,
)


_FINISHCONTEXT = _descriptor.Descriptor(
  name='FinishContext',
  full_name='adu.hmi.FinishContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_state', full_name='adu.hmi.FinishContext.last_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='adu.hmi.FinishContext.result_code', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=243,
  serialized_end=336,
)


_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='adu.hmi.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='finish_context', full_name='adu.hmi.Context.finish_context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parking_in_context', full_name='adu.hmi.Context.parking_in_context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parking_out_context', full_name='adu.hmi.Context.parking_out_context', index=2,
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
    _descriptor.OneofDescriptor(
      name='context', full_name='adu.hmi.Context.context',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=339,
  serialized_end=525,
)


_SYSSTATE = _descriptor.Descriptor(
  name='SysState',
  full_name='adu.hmi.SysState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='adu.hmi.SysState.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state_counter', full_name='adu.hmi.SysState.state_counter', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='adu.hmi.SysState.context', index=2,
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
  serialized_start=527,
  serialized_end=626,
)

_PARKINGINCONTEXT.fields_by_name['destination'].message_type = _POINT3D
_PARKINGOUTCONTEXT.fields_by_name['destination'].message_type = _POINT3D
_FINISHCONTEXT.fields_by_name['last_state'].enum_type = _STATE
_FINISHCONTEXT.fields_by_name['result_code'].enum_type = _RESULTCODE
_CONTEXT.fields_by_name['finish_context'].message_type = _FINISHCONTEXT
_CONTEXT.fields_by_name['parking_in_context'].message_type = _PARKINGINCONTEXT
_CONTEXT.fields_by_name['parking_out_context'].message_type = _PARKINGOUTCONTEXT
_CONTEXT.oneofs_by_name['context'].fields.append(
  _CONTEXT.fields_by_name['finish_context'])
_CONTEXT.fields_by_name['finish_context'].containing_oneof = _CONTEXT.oneofs_by_name['context']
_CONTEXT.oneofs_by_name['context'].fields.append(
  _CONTEXT.fields_by_name['parking_in_context'])
_CONTEXT.fields_by_name['parking_in_context'].containing_oneof = _CONTEXT.oneofs_by_name['context']
_CONTEXT.oneofs_by_name['context'].fields.append(
  _CONTEXT.fields_by_name['parking_out_context'])
_CONTEXT.fields_by_name['parking_out_context'].containing_oneof = _CONTEXT.oneofs_by_name['context']
_SYSSTATE.fields_by_name['state'].enum_type = _STATE
_SYSSTATE.fields_by_name['context'].message_type = _CONTEXT
DESCRIPTOR.message_types_by_name['Point3D'] = _POINT3D
DESCRIPTOR.message_types_by_name['ParkingInContext'] = _PARKINGINCONTEXT
DESCRIPTOR.message_types_by_name['ParkingOutContext'] = _PARKINGOUTCONTEXT
DESCRIPTOR.message_types_by_name['FinishContext'] = _FINISHCONTEXT
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['SysState'] = _SYSSTATE
DESCRIPTOR.enum_types_by_name['State'] = _STATE
DESCRIPTOR.enum_types_by_name['ResultCode'] = _RESULTCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point3D = _reflection.GeneratedProtocolMessageType('Point3D', (_message.Message,), dict(
  DESCRIPTOR = _POINT3D,
  __module__ = 'hmi_state_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.Point3D)
  ))
_sym_db.RegisterMessage(Point3D)

ParkingInContext = _reflection.GeneratedProtocolMessageType('ParkingInContext', (_message.Message,), dict(
  DESCRIPTOR = _PARKINGINCONTEXT,
  __module__ = 'hmi_state_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.ParkingInContext)
  ))
_sym_db.RegisterMessage(ParkingInContext)

ParkingOutContext = _reflection.GeneratedProtocolMessageType('ParkingOutContext', (_message.Message,), dict(
  DESCRIPTOR = _PARKINGOUTCONTEXT,
  __module__ = 'hmi_state_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.ParkingOutContext)
  ))
_sym_db.RegisterMessage(ParkingOutContext)

FinishContext = _reflection.GeneratedProtocolMessageType('FinishContext', (_message.Message,), dict(
  DESCRIPTOR = _FINISHCONTEXT,
  __module__ = 'hmi_state_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.FinishContext)
  ))
_sym_db.RegisterMessage(FinishContext)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'hmi_state_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.Context)
  ))
_sym_db.RegisterMessage(Context)

SysState = _reflection.GeneratedProtocolMessageType('SysState', (_message.Message,), dict(
  DESCRIPTOR = _SYSSTATE,
  __module__ = 'hmi_state_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.SysState)
  ))
_sym_db.RegisterMessage(SysState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)
