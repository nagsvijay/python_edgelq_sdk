# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.iam.proto.v1 import group_member_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2
from edgelq_sdk.iam.proto.v1 import group_member_service_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in edgelq_sdk/iam/proto/v1/group_member_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GroupMemberServiceStub(object):
    """GroupMember service API for IAM
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGroupMember = channel.unary_unary(
                '/ntt.iam.v1.GroupMemberService/GetGroupMember',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.GetGroupMemberRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.FromString,
                _registered_method=True)
        self.BatchGetGroupMembers = channel.unary_unary(
                '/ntt.iam.v1.GroupMemberService/BatchGetGroupMembers',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.BatchGetGroupMembersRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.BatchGetGroupMembersResponse.FromString,
                _registered_method=True)
        self.ListGroupMembers = channel.unary_unary(
                '/ntt.iam.v1.GroupMemberService/ListGroupMembers',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.ListGroupMembersRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.ListGroupMembersResponse.FromString,
                _registered_method=True)
        self.WatchGroupMember = channel.unary_stream(
                '/ntt.iam.v1.GroupMemberService/WatchGroupMember',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMemberRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMemberResponse.FromString,
                _registered_method=True)
        self.WatchGroupMembers = channel.unary_stream(
                '/ntt.iam.v1.GroupMemberService/WatchGroupMembers',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMembersRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMembersResponse.FromString,
                _registered_method=True)
        self.CreateGroupMember = channel.unary_unary(
                '/ntt.iam.v1.GroupMemberService/CreateGroupMember',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.CreateGroupMemberRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.FromString,
                _registered_method=True)
        self.UpdateGroupMember = channel.unary_unary(
                '/ntt.iam.v1.GroupMemberService/UpdateGroupMember',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.UpdateGroupMemberRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.FromString,
                _registered_method=True)
        self.DeleteGroupMember = channel.unary_unary(
                '/ntt.iam.v1.GroupMemberService/DeleteGroupMember',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.DeleteGroupMemberRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class GroupMemberServiceServicer(object):
    """GroupMember service API for IAM
    """

    def GetGroupMember(self, request, context):
        """GetGroupMember
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetGroupMembers(self, request, context):
        """BatchGetGroupMembers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListGroupMembers(self, request, context):
        """ListGroupMembers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchGroupMember(self, request, context):
        """WatchGroupMember
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchGroupMembers(self, request, context):
        """WatchGroupMembers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGroupMember(self, request, context):
        """CreateGroupMember
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateGroupMember(self, request, context):
        """UpdateGroupMember
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGroupMember(self, request, context):
        """DeleteGroupMember
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GroupMemberServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGroupMember': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGroupMember,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.GetGroupMemberRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.SerializeToString,
            ),
            'BatchGetGroupMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetGroupMembers,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.BatchGetGroupMembersRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.BatchGetGroupMembersResponse.SerializeToString,
            ),
            'ListGroupMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListGroupMembers,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.ListGroupMembersRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.ListGroupMembersResponse.SerializeToString,
            ),
            'WatchGroupMember': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchGroupMember,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMemberRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMemberResponse.SerializeToString,
            ),
            'WatchGroupMembers': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchGroupMembers,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMembersRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMembersResponse.SerializeToString,
            ),
            'CreateGroupMember': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGroupMember,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.CreateGroupMemberRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.SerializeToString,
            ),
            'UpdateGroupMember': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateGroupMember,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.UpdateGroupMemberRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.SerializeToString,
            ),
            'DeleteGroupMember': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGroupMember,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.DeleteGroupMemberRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.iam.v1.GroupMemberService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.iam.v1.GroupMemberService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GroupMemberService(object):
    """GroupMember service API for IAM
    """

    @staticmethod
    def GetGroupMember(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/GetGroupMember',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.GetGroupMemberRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchGetGroupMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/BatchGetGroupMembers',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.BatchGetGroupMembersRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.BatchGetGroupMembersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListGroupMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/ListGroupMembers',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.ListGroupMembersRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.ListGroupMembersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WatchGroupMember(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/WatchGroupMember',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMemberRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMemberResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WatchGroupMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/WatchGroupMembers',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMembersRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.WatchGroupMembersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateGroupMember(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/CreateGroupMember',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.CreateGroupMemberRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateGroupMember(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/UpdateGroupMember',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.UpdateGroupMemberRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__pb2.GroupMember.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteGroupMember(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ntt.iam.v1.GroupMemberService/DeleteGroupMember',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_group__member__service__pb2.DeleteGroupMemberRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
