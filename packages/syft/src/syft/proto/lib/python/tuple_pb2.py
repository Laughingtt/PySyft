# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/tuple.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cproto/lib/python/tuple.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto"8\n\x05Tuple\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x0c\x12!\n\x02id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3'
)


_TUPLE = DESCRIPTOR.message_types_by_name["Tuple"]
Tuple = _reflection.GeneratedProtocolMessageType(
    "Tuple",
    (_message.Message,),
    {
        "DESCRIPTOR": _TUPLE,
        "__module__": "proto.lib.python.tuple_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.Tuple)
    },
)
_sym_db.RegisterMessage(Tuple)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TUPLE._serialized_start = 88
    _TUPLE._serialized_end = 144
# @@protoc_insertion_point(module_scope)
