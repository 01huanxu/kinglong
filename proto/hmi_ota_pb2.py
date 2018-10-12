# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_ota.proto

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


import hmi_error_code_pb2 as hmi__error__code__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_ota.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\rhmi_ota.proto\x12\x07\x61\x64u.hmi\x1a\x14hmi_error_code.proto\"\x8f\x03\n\x0fOTAClientStatus\x12\x13\n\x0bnew_version\x18\x01 \x01(\x08\x12\x1b\n\x13new_version_counter\x18\x02 \x01(\x01\x12.\n\x10new_version_info\x18\x03 \x01(\x0b\x32\x14.adu.hmi.UpgradeInfo\x12>\n\x17new_version_update_mode\x18\x04 \x01(\x0e\x32\x1d.adu.hmi.NewVersionUpdateMode\x12\x1d\n\x15new_version_timestamp\x18\x05 \x01(\x01\x12\x19\n\x11\x65mergency_upgrade\x18\x06 \x01(\x08\x12!\n\x19\x65mergency_upgrade_counter\x18\x07 \x01(\x01\x12\x34\n\x16\x65mergency_version_info\x18\x08 \x01(\x0b\x32\x14.adu.hmi.UpgradeInfo\x12\x1b\n\x13\x65mergency_timestamp\x18\t \x01(\x01\x12*\n\x0cupgrade_info\x18\n \x01(\x0b\x32\x14.adu.hmi.UpgradeInfo\"\xe0\x01\n\x0bUpgradeInfo\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12&\n\x06status\x18\x03 \x01(\x0e\x32\x16.adu.hmi.UpgradeStatus\x12\x11\n\ttime_used\x18\x04 \x01(\t\x12\x14\n\x0csoft_version\x18\x05 \x01(\t\x12\x18\n\x10\x65xternal_version\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x14\n\x0cinstall_date\x18\x08 \x01(\t\x12 \n\x18include_sensorbox_update\x18\t \x01(\x08\"?\n\nOtaRequest\x12$\n\x06\x61\x63tion\x18\x01 \x02(\x0e\x32\x14.adu.hmi.RequestType\x12\x0b\n\x03tag\x18\x02 \x01(\t\"d\n\x0bOtaResponse\x12 \n\x04\x63ode\x18\x01 \x02(\x0e\x32\x12.adu.hmi.ErrorCode\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\"\n\x04info\x18\x03 \x01(\x0b\x32\x14.adu.hmi.UpgradeInfo*<\n\rUpgradeStatus\x12\x0e\n\nOTA_FINISH\x10\x00\x12\x0e\n\nOTA_FAILED\x10\x01\x12\x0b\n\x07OTA_NEW\x10\x02*\xd0\x01\n\x0bRequestType\x12\x11\n\rSTART_UPGRADE\x10\x00\x12\x16\n\x12GET_UPGRADE_RESULT\x10\x01\x12\x15\n\x11\x43HECK_AND_UPGRADE\x10\x02\x12\x19\n\x15\x43HECK_CURRENT_VERSION\x10\x03\x12\x1b\n\x17HAS_UPGRADE_DESCRIPTION\x10\x04\x12\x14\n\x10HAS_OPER_UPGRADE\x10\x05\x12\x18\n\x14OPER_UPGRADE_INSTALL\x10\x06\x12\x17\n\x13OPER_UPGRADE_IGNORE\x10\x07*r\n\x14NewVersionUpdateMode\x12\x0f\n\x0bUPDATE_INIT\x10\x00\x12\x0e\n\nUPDATE_ING\x10\x01\x12\x12\n\x0eUPDATE_SUCCESS\x10\x02\x12\x11\n\rUPDATE_FAILED\x10\x03\x12\x12\n\x0eUPDATE_TIMEOUT\x10\x04\x42\x02P\x01')
  ,
  dependencies=[hmi__error__code__pb2.DESCRIPTOR,])

_UPGRADESTATUS = _descriptor.EnumDescriptor(
  name='UpgradeStatus',
  full_name='adu.hmi.UpgradeStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTA_FINISH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTA_FAILED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTA_NEW', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=844,
  serialized_end=904,
)
_sym_db.RegisterEnumDescriptor(_UPGRADESTATUS)

UpgradeStatus = enum_type_wrapper.EnumTypeWrapper(_UPGRADESTATUS)
_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='adu.hmi.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START_UPGRADE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_UPGRADE_RESULT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_AND_UPGRADE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_CURRENT_VERSION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAS_UPGRADE_DESCRIPTION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAS_OPER_UPGRADE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPER_UPGRADE_INSTALL', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPER_UPGRADE_IGNORE', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=907,
  serialized_end=1115,
)
_sym_db.RegisterEnumDescriptor(_REQUESTTYPE)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
_NEWVERSIONUPDATEMODE = _descriptor.EnumDescriptor(
  name='NewVersionUpdateMode',
  full_name='adu.hmi.NewVersionUpdateMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPDATE_INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_ING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_SUCCESS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_FAILED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_TIMEOUT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1117,
  serialized_end=1231,
)
_sym_db.RegisterEnumDescriptor(_NEWVERSIONUPDATEMODE)

NewVersionUpdateMode = enum_type_wrapper.EnumTypeWrapper(_NEWVERSIONUPDATEMODE)
OTA_FINISH = 0
OTA_FAILED = 1
OTA_NEW = 2
START_UPGRADE = 0
GET_UPGRADE_RESULT = 1
CHECK_AND_UPGRADE = 2
CHECK_CURRENT_VERSION = 3
HAS_UPGRADE_DESCRIPTION = 4
HAS_OPER_UPGRADE = 5
OPER_UPGRADE_INSTALL = 6
OPER_UPGRADE_IGNORE = 7
UPDATE_INIT = 0
UPDATE_ING = 1
UPDATE_SUCCESS = 2
UPDATE_FAILED = 3
UPDATE_TIMEOUT = 4



_OTACLIENTSTATUS = _descriptor.Descriptor(
  name='OTAClientStatus',
  full_name='adu.hmi.OTAClientStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_version', full_name='adu.hmi.OTAClientStatus.new_version', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_version_counter', full_name='adu.hmi.OTAClientStatus.new_version_counter', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_version_info', full_name='adu.hmi.OTAClientStatus.new_version_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_version_update_mode', full_name='adu.hmi.OTAClientStatus.new_version_update_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_version_timestamp', full_name='adu.hmi.OTAClientStatus.new_version_timestamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emergency_upgrade', full_name='adu.hmi.OTAClientStatus.emergency_upgrade', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emergency_upgrade_counter', full_name='adu.hmi.OTAClientStatus.emergency_upgrade_counter', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emergency_version_info', full_name='adu.hmi.OTAClientStatus.emergency_version_info', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emergency_timestamp', full_name='adu.hmi.OTAClientStatus.emergency_timestamp', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_info', full_name='adu.hmi.OTAClientStatus.upgrade_info', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=49,
  serialized_end=448,
)


_UPGRADEINFO = _descriptor.Descriptor(
  name='UpgradeInfo',
  full_name='adu.hmi.UpgradeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='adu.hmi.UpgradeInfo.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='adu.hmi.UpgradeInfo.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adu.hmi.UpgradeInfo.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_used', full_name='adu.hmi.UpgradeInfo.time_used', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soft_version', full_name='adu.hmi.UpgradeInfo.soft_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_version', full_name='adu.hmi.UpgradeInfo.external_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='adu.hmi.UpgradeInfo.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='install_date', full_name='adu.hmi.UpgradeInfo.install_date', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_sensorbox_update', full_name='adu.hmi.UpgradeInfo.include_sensorbox_update', index=8,
      number=9, type=8, cpp_type=7, label=1,
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
  serialized_start=451,
  serialized_end=675,
)


_OTAREQUEST = _descriptor.Descriptor(
  name='OtaRequest',
  full_name='adu.hmi.OtaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='adu.hmi.OtaRequest.action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='adu.hmi.OtaRequest.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=677,
  serialized_end=740,
)


_OTARESPONSE = _descriptor.Descriptor(
  name='OtaResponse',
  full_name='adu.hmi.OtaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.hmi.OtaResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='adu.hmi.OtaResponse.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='adu.hmi.OtaResponse.info', index=2,
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
  serialized_start=742,
  serialized_end=842,
)

_OTACLIENTSTATUS.fields_by_name['new_version_info'].message_type = _UPGRADEINFO
_OTACLIENTSTATUS.fields_by_name['new_version_update_mode'].enum_type = _NEWVERSIONUPDATEMODE
_OTACLIENTSTATUS.fields_by_name['emergency_version_info'].message_type = _UPGRADEINFO
_OTACLIENTSTATUS.fields_by_name['upgrade_info'].message_type = _UPGRADEINFO
_UPGRADEINFO.fields_by_name['status'].enum_type = _UPGRADESTATUS
_OTAREQUEST.fields_by_name['action'].enum_type = _REQUESTTYPE
_OTARESPONSE.fields_by_name['code'].enum_type = hmi__error__code__pb2._ERRORCODE
_OTARESPONSE.fields_by_name['info'].message_type = _UPGRADEINFO
DESCRIPTOR.message_types_by_name['OTAClientStatus'] = _OTACLIENTSTATUS
DESCRIPTOR.message_types_by_name['UpgradeInfo'] = _UPGRADEINFO
DESCRIPTOR.message_types_by_name['OtaRequest'] = _OTAREQUEST
DESCRIPTOR.message_types_by_name['OtaResponse'] = _OTARESPONSE
DESCRIPTOR.enum_types_by_name['UpgradeStatus'] = _UPGRADESTATUS
DESCRIPTOR.enum_types_by_name['RequestType'] = _REQUESTTYPE
DESCRIPTOR.enum_types_by_name['NewVersionUpdateMode'] = _NEWVERSIONUPDATEMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OTAClientStatus = _reflection.GeneratedProtocolMessageType('OTAClientStatus', (_message.Message,), dict(
  DESCRIPTOR = _OTACLIENTSTATUS,
  __module__ = 'hmi_ota_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.OTAClientStatus)
  ))
_sym_db.RegisterMessage(OTAClientStatus)

UpgradeInfo = _reflection.GeneratedProtocolMessageType('UpgradeInfo', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADEINFO,
  __module__ = 'hmi_ota_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.UpgradeInfo)
  ))
_sym_db.RegisterMessage(UpgradeInfo)

OtaRequest = _reflection.GeneratedProtocolMessageType('OtaRequest', (_message.Message,), dict(
  DESCRIPTOR = _OTAREQUEST,
  __module__ = 'hmi_ota_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.OtaRequest)
  ))
_sym_db.RegisterMessage(OtaRequest)

OtaResponse = _reflection.GeneratedProtocolMessageType('OtaResponse', (_message.Message,), dict(
  DESCRIPTOR = _OTARESPONSE,
  __module__ = 'hmi_ota_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.OtaResponse)
  ))
_sym_db.RegisterMessage(OtaResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)
