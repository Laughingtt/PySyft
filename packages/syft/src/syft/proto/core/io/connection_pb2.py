# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/io/connection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1eproto/core/io/connection.proto\x12\x0csyft.core.io\x1a\x1bproto/core/io/address.proto">\n\x17VirtualServerConnection\x12#\n\x04node\x18\x01 \x01(\x0b\x32\x15.syft.core.io.Address"P\n\x17VirtualClientConnection\x12\x35\n\x06server\x18\x01 \x01(\x0b\x32%.syft.core.io.VirtualServerConnectionb\x06proto3'
)


_VIRTUALSERVERCONNECTION = DESCRIPTOR.message_types_by_name["VirtualServerConnection"]
_VIRTUALCLIENTCONNECTION = DESCRIPTOR.message_types_by_name["VirtualClientConnection"]
VirtualServerConnection = _reflection.GeneratedProtocolMessageType(
    "VirtualServerConnection",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIRTUALSERVERCONNECTION,
        "__module__": "proto.core.io.connection_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.io.VirtualServerConnection)
    },
)
_sym_db.RegisterMessage(VirtualServerConnection)

VirtualClientConnection = _reflection.GeneratedProtocolMessageType(
    "VirtualClientConnection",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIRTUALCLIENTCONNECTION,
        "__module__": "proto.core.io.connection_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.io.VirtualClientConnection)
    },
)
_sym_db.RegisterMessage(VirtualClientConnection)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _VIRTUALSERVERCONNECTION._serialized_start = 77
    _VIRTUALSERVERCONNECTION._serialized_end = 139
    _VIRTUALCLIENTCONNECTION._serialized_start = 141
    _VIRTUALCLIENTCONNECTION._serialized_end = 221
# @@protoc_insertion_point(module_scope)
