# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/request_messages.proto
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
from syft.proto.lib.python import dict_pb2 as proto_dot_lib_dot_python_dot_dict__pb2
from syft.proto.core.node.domain.service import (
    request_message_pb2 as proto_dot_core_dot_node_dot_domain_dot_service_dot_request__message__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*proto/grid/messages/request_messages.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto\x1a\x1bproto/lib/python/dict.proto\x1a\x34proto/core/node/domain/service/request_message.proto"\x9f\x01\n\x14\x43reateRequestMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8c\x01\n\x15\x43reateRequestResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8b\x01\n\x1a\x43reateBudgetRequestMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0e\n\x06\x62udget\x18\x03 \x01(\x02\x12\x0e\n\x06reason\x18\x04 \x01(\t"\xa6\x01\n\x18GetBudgetRequestsMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x92\x01\n\x19GetBudgetRequestsResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x63ontent\x18\x03 \x03(\x0b\x32\x15.syft.lib.python.Dict\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x9f\x01\n\x11GetRequestMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8c\x01\n\x12GetRequestResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8c\x01\n\x12GetRequestsMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\xa1\x01\n\x13GetRequestsResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12&\n\x07\x63ontent\x18\x03 \x03(\x0b\x32\x15.syft.lib.python.Dict\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\xa2\x01\n\x14\x44\x65leteRequestMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8f\x01\n\x15\x44\x65leteRequestResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\xb2\x01\n\x14UpdateRequestMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x12\n\nrequest_id\x18\x04 \x01(\t\x12\'\n\x08reply_to\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Address"\x9f\x01\n\x15UpdateRequestResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x12\n\nrequest_id\x18\x04 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Address"\x8f\x01\n\x15GetAllRequestsMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address"\xaf\x01\n\x1dGetAllRequestsResponseMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12?\n\x08requests\x18\x03 \x03(\x0b\x32-.syft.core.node.domain.service.RequestMessageb\x06proto3'
)


_CREATEREQUESTMESSAGE = DESCRIPTOR.message_types_by_name["CreateRequestMessage"]
_CREATEREQUESTRESPONSE = DESCRIPTOR.message_types_by_name["CreateRequestResponse"]
_CREATEBUDGETREQUESTMESSAGE = DESCRIPTOR.message_types_by_name[
    "CreateBudgetRequestMessage"
]
_GETBUDGETREQUESTSMESSAGE = DESCRIPTOR.message_types_by_name["GetBudgetRequestsMessage"]
_GETBUDGETREQUESTSRESPONSE = DESCRIPTOR.message_types_by_name[
    "GetBudgetRequestsResponse"
]
_GETREQUESTMESSAGE = DESCRIPTOR.message_types_by_name["GetRequestMessage"]
_GETREQUESTRESPONSE = DESCRIPTOR.message_types_by_name["GetRequestResponse"]
_GETREQUESTSMESSAGE = DESCRIPTOR.message_types_by_name["GetRequestsMessage"]
_GETREQUESTSRESPONSE = DESCRIPTOR.message_types_by_name["GetRequestsResponse"]
_DELETEREQUESTMESSAGE = DESCRIPTOR.message_types_by_name["DeleteRequestMessage"]
_DELETEREQUESTRESPONSE = DESCRIPTOR.message_types_by_name["DeleteRequestResponse"]
_UPDATEREQUESTMESSAGE = DESCRIPTOR.message_types_by_name["UpdateRequestMessage"]
_UPDATEREQUESTRESPONSE = DESCRIPTOR.message_types_by_name["UpdateRequestResponse"]
_GETALLREQUESTSMESSAGE = DESCRIPTOR.message_types_by_name["GetAllRequestsMessage"]
_GETALLREQUESTSRESPONSEMESSAGE = DESCRIPTOR.message_types_by_name[
    "GetAllRequestsResponseMessage"
]
CreateRequestMessage = _reflection.GeneratedProtocolMessageType(
    "CreateRequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEREQUESTMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateRequestMessage)
    },
)
_sym_db.RegisterMessage(CreateRequestMessage)

CreateRequestResponse = _reflection.GeneratedProtocolMessageType(
    "CreateRequestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEREQUESTRESPONSE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateRequestResponse)
    },
)
_sym_db.RegisterMessage(CreateRequestResponse)

CreateBudgetRequestMessage = _reflection.GeneratedProtocolMessageType(
    "CreateBudgetRequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEBUDGETREQUESTMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateBudgetRequestMessage)
    },
)
_sym_db.RegisterMessage(CreateBudgetRequestMessage)

GetBudgetRequestsMessage = _reflection.GeneratedProtocolMessageType(
    "GetBudgetRequestsMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETBUDGETREQUESTSMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetBudgetRequestsMessage)
    },
)
_sym_db.RegisterMessage(GetBudgetRequestsMessage)

GetBudgetRequestsResponse = _reflection.GeneratedProtocolMessageType(
    "GetBudgetRequestsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETBUDGETREQUESTSRESPONSE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetBudgetRequestsResponse)
    },
)
_sym_db.RegisterMessage(GetBudgetRequestsResponse)

GetRequestMessage = _reflection.GeneratedProtocolMessageType(
    "GetRequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETREQUESTMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetRequestMessage)
    },
)
_sym_db.RegisterMessage(GetRequestMessage)

GetRequestResponse = _reflection.GeneratedProtocolMessageType(
    "GetRequestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETREQUESTRESPONSE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetRequestResponse)
    },
)
_sym_db.RegisterMessage(GetRequestResponse)

GetRequestsMessage = _reflection.GeneratedProtocolMessageType(
    "GetRequestsMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETREQUESTSMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetRequestsMessage)
    },
)
_sym_db.RegisterMessage(GetRequestsMessage)

GetRequestsResponse = _reflection.GeneratedProtocolMessageType(
    "GetRequestsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETREQUESTSRESPONSE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetRequestsResponse)
    },
)
_sym_db.RegisterMessage(GetRequestsResponse)

DeleteRequestMessage = _reflection.GeneratedProtocolMessageType(
    "DeleteRequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEREQUESTMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.DeleteRequestMessage)
    },
)
_sym_db.RegisterMessage(DeleteRequestMessage)

DeleteRequestResponse = _reflection.GeneratedProtocolMessageType(
    "DeleteRequestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEREQUESTRESPONSE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.DeleteRequestResponse)
    },
)
_sym_db.RegisterMessage(DeleteRequestResponse)

UpdateRequestMessage = _reflection.GeneratedProtocolMessageType(
    "UpdateRequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEREQUESTMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateRequestMessage)
    },
)
_sym_db.RegisterMessage(UpdateRequestMessage)

UpdateRequestResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateRequestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEREQUESTRESPONSE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateRequestResponse)
    },
)
_sym_db.RegisterMessage(UpdateRequestResponse)

GetAllRequestsMessage = _reflection.GeneratedProtocolMessageType(
    "GetAllRequestsMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLREQUESTSMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetAllRequestsMessage)
    },
)
_sym_db.RegisterMessage(GetAllRequestsMessage)

GetAllRequestsResponseMessage = _reflection.GeneratedProtocolMessageType(
    "GetAllRequestsResponseMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLREQUESTSRESPONSEMESSAGE,
        "__module__": "proto.grid.messages.request_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetAllRequestsResponseMessage)
    },
)
_sym_db.RegisterMessage(GetAllRequestsResponseMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CREATEREQUESTMESSAGE._serialized_start = 218
    _CREATEREQUESTMESSAGE._serialized_end = 377
    _CREATEREQUESTRESPONSE._serialized_start = 380
    _CREATEREQUESTRESPONSE._serialized_end = 520
    _CREATEBUDGETREQUESTMESSAGE._serialized_start = 523
    _CREATEBUDGETREQUESTMESSAGE._serialized_end = 662
    _GETBUDGETREQUESTSMESSAGE._serialized_start = 665
    _GETBUDGETREQUESTSMESSAGE._serialized_end = 831
    _GETBUDGETREQUESTSRESPONSE._serialized_start = 834
    _GETBUDGETREQUESTSRESPONSE._serialized_end = 980
    _GETREQUESTMESSAGE._serialized_start = 983
    _GETREQUESTMESSAGE._serialized_end = 1142
    _GETREQUESTRESPONSE._serialized_start = 1145
    _GETREQUESTRESPONSE._serialized_end = 1285
    _GETREQUESTSMESSAGE._serialized_start = 1288
    _GETREQUESTSMESSAGE._serialized_end = 1428
    _GETREQUESTSRESPONSE._serialized_start = 1431
    _GETREQUESTSRESPONSE._serialized_end = 1592
    _DELETEREQUESTMESSAGE._serialized_start = 1595
    _DELETEREQUESTMESSAGE._serialized_end = 1757
    _DELETEREQUESTRESPONSE._serialized_start = 1760
    _DELETEREQUESTRESPONSE._serialized_end = 1903
    _UPDATEREQUESTMESSAGE._serialized_start = 1906
    _UPDATEREQUESTMESSAGE._serialized_end = 2084
    _UPDATEREQUESTRESPONSE._serialized_start = 2087
    _UPDATEREQUESTRESPONSE._serialized_end = 2246
    _GETALLREQUESTSMESSAGE._serialized_start = 2249
    _GETALLREQUESTSMESSAGE._serialized_end = 2392
    _GETALLREQUESTSRESPONSEMESSAGE._serialized_start = 2395
    _GETALLREQUESTSRESPONSEMESSAGE._serialized_end = 2570
# @@protoc_insertion_point(module_scope)
