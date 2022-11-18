# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/network_search_messages.proto
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
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n1proto/grid/messages/network_search_messages.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\x9f\x01\n\x14NetworkSearchMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8c\x01\n\x15NetworkSearchResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3'
)


_NETWORKSEARCHMESSAGE = DESCRIPTOR.message_types_by_name["NetworkSearchMessage"]
_NETWORKSEARCHRESPONSE = DESCRIPTOR.message_types_by_name["NetworkSearchResponse"]
NetworkSearchMessage = _reflection.GeneratedProtocolMessageType(
    "NetworkSearchMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _NETWORKSEARCHMESSAGE,
        "__module__": "proto.grid.messages.network_search_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.NetworkSearchMessage)
    },
)
_sym_db.RegisterMessage(NetworkSearchMessage)

NetworkSearchResponse = _reflection.GeneratedProtocolMessageType(
    "NetworkSearchResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _NETWORKSEARCHRESPONSE,
        "__module__": "proto.grid.messages.network_search_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.NetworkSearchResponse)
    },
)
_sym_db.RegisterMessage(NetworkSearchResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _NETWORKSEARCHMESSAGE._serialized_start = 142
    _NETWORKSEARCHMESSAGE._serialized_end = 301
    _NETWORKSEARCHRESPONSE._serialized_start = 304
    _NETWORKSEARCHRESPONSE._serialized_end = 444
# @@protoc_insertion_point(module_scope)
