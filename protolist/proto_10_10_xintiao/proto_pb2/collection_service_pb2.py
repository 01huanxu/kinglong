# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collection_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import collection_check_message_pb2 as collection__check__message__pb2
import collection_status_message_pb2 as collection__status__message__pb2
import collection_data_message_pb2 as collection__data__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='collection_service.proto',
  package='adu.workers.collection',
  syntax='proto2',
  serialized_pb=_b('\n\x18\x63ollection_service.proto\x12\x16\x61\x64u.workers.collection\x1a\x1e\x63ollection_check_message.proto\x1a\x1f\x63ollection_status_message.proto\x1a\x1d\x63ollection_data_message.proto2\xcd\x02\n\x18\x43ollectionCheckerService\x12k\n\x0c\x44ynamicAlign\x12+.adu.workers.collection.DynamicAlignRequest\x1a,.adu.workers.collection.DynamicAlignResponse\"\x00\x12\x65\n\nEightRoute\x12).adu.workers.collection.EightRouteRequest\x1a*.adu.workers.collection.EightRouteResponse\"\x00\x12]\n\nDataVerify\x12%.adu.workers.collection.VerifyRequest\x1a&.adu.workers.collection.VerifyResponse\"\x00\x32\xf2\x05\n\x10\x43ollectorService\x12t\n\x13\x46\x65tchCollectionInfo\x12+.adu.workers.collection.FetchCollectionKeys\x1a..adu.workers.collection.FetchCollectionPackage\"\x00\x12\\\n\x0bTaskHandler\x12#.adu.workers.collection.TaskRequest\x1a&.adu.workers.collection.StatusResponse\"\x00\x12h\n\x0b\x43heckGPSbin\x12*.adu.workers.collection.CheckGPSbinRequest\x1a+.adu.workers.collection.CheckGPSbinResponse\"\x00\x12\x65\n\nDiskFormat\x12).adu.workers.collection.DiskFormatRequest\x1a*.adu.workers.collection.DiskFormatResponse\"\x00\x12k\n\x0c\x44ynamicAlign\x12+.adu.workers.collection.DynamicAlignRequest\x1a,.adu.workers.collection.DynamicAlignResponse\"\x00\x12\x65\n\nEightRoute\x12).adu.workers.collection.EightRouteRequest\x1a*.adu.workers.collection.EightRouteResponse\"\x00\x12\x65\n\nDataVerify\x12).adu.workers.collection.DataVerifyRequest\x1a*.adu.workers.collection.DataVerifyResponse\"\x00')
  ,
  dependencies=[collection__check__message__pb2.DESCRIPTOR,collection__status__message__pb2.DESCRIPTOR,collection__data__message__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
