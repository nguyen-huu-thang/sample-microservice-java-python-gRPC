# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: hello.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'hello.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\x12\x10\x63om.example.grpc\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2[\n\x0cHelloService\x12K\n\x08SayHello\x12\x1e.com.example.grpc.HelloRequest\x1a\x1f.com.example.grpc.HelloResponseB\x1e\n\x10\x63om.example.grpcB\nHelloProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.example.grpcB\nHelloProto'
  _globals['_HELLOREQUEST']._serialized_start=33
  _globals['_HELLOREQUEST']._serialized_end=61
  _globals['_HELLORESPONSE']._serialized_start=63
  _globals['_HELLORESPONSE']._serialized_end=95
  _globals['_HELLOSERVICE']._serialized_start=97
  _globals['_HELLOSERVICE']._serialized_end=188
# @@protoc_insertion_point(module_scope)
