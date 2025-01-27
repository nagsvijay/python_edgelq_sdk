# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.iam.proto.v1 import member_assignment_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2
from edgelq_sdk.iam.proto.v1 import member_assignment_service_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2
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
        + f' but the generated code in edgelq_sdk/iam/proto/v1/member_assignment_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MemberAssignmentServiceStub(object):
    """MemberAssignment service API for IAM
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMemberAssignment = channel.unary_unary(
                '/ntt.iam.v1.MemberAssignmentService/GetMemberAssignment',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.GetMemberAssignmentRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2.MemberAssignment.FromString,
                _registered_method=True)
        self.BatchGetMemberAssignments = channel.unary_unary(
                '/ntt.iam.v1.MemberAssignmentService/BatchGetMemberAssignments',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.BatchGetMemberAssignmentsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.BatchGetMemberAssignmentsResponse.FromString,
                _registered_method=True)
        self.ListMemberAssignments = channel.unary_unary(
                '/ntt.iam.v1.MemberAssignmentService/ListMemberAssignments',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.ListMemberAssignmentsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.ListMemberAssignmentsResponse.FromString,
                _registered_method=True)
        self.WatchMemberAssignment = channel.unary_stream(
                '/ntt.iam.v1.MemberAssignmentService/WatchMemberAssignment',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentResponse.FromString,
                _registered_method=True)
        self.WatchMemberAssignments = channel.unary_stream(
                '/ntt.iam.v1.MemberAssignmentService/WatchMemberAssignments',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentsResponse.FromString,
                _registered_method=True)
        self.UpdateMemberAssignment = channel.unary_unary(
                '/ntt.iam.v1.MemberAssignmentService/UpdateMemberAssignment',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.UpdateMemberAssignmentRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2.MemberAssignment.FromString,
                _registered_method=True)
        self.DeleteMemberAssignment = channel.unary_unary(
                '/ntt.iam.v1.MemberAssignmentService/DeleteMemberAssignment',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.DeleteMemberAssignmentRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class MemberAssignmentServiceServicer(object):
    """MemberAssignment service API for IAM
    """

    def GetMemberAssignment(self, request, context):
        """GetMemberAssignment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetMemberAssignments(self, request, context):
        """BatchGetMemberAssignments
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMemberAssignments(self, request, context):
        """ListMemberAssignments
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchMemberAssignment(self, request, context):
        """WatchMemberAssignment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchMemberAssignments(self, request, context):
        """WatchMemberAssignments
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMemberAssignment(self, request, context):
        """UpdateMemberAssignment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMemberAssignment(self, request, context):
        """DeleteMemberAssignment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MemberAssignmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMemberAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMemberAssignment,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.GetMemberAssignmentRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2.MemberAssignment.SerializeToString,
            ),
            'BatchGetMemberAssignments': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetMemberAssignments,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.BatchGetMemberAssignmentsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.BatchGetMemberAssignmentsResponse.SerializeToString,
            ),
            'ListMemberAssignments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMemberAssignments,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.ListMemberAssignmentsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.ListMemberAssignmentsResponse.SerializeToString,
            ),
            'WatchMemberAssignment': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchMemberAssignment,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentResponse.SerializeToString,
            ),
            'WatchMemberAssignments': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchMemberAssignments,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentsResponse.SerializeToString,
            ),
            'UpdateMemberAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMemberAssignment,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.UpdateMemberAssignmentRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2.MemberAssignment.SerializeToString,
            ),
            'DeleteMemberAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMemberAssignment,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.DeleteMemberAssignmentRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.iam.v1.MemberAssignmentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.iam.v1.MemberAssignmentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MemberAssignmentService(object):
    """MemberAssignment service API for IAM
    """

    @staticmethod
    def GetMemberAssignment(request,
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
            '/ntt.iam.v1.MemberAssignmentService/GetMemberAssignment',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.GetMemberAssignmentRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2.MemberAssignment.FromString,
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
    def BatchGetMemberAssignments(request,
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
            '/ntt.iam.v1.MemberAssignmentService/BatchGetMemberAssignments',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.BatchGetMemberAssignmentsRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.BatchGetMemberAssignmentsResponse.FromString,
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
    def ListMemberAssignments(request,
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
            '/ntt.iam.v1.MemberAssignmentService/ListMemberAssignments',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.ListMemberAssignmentsRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.ListMemberAssignmentsResponse.FromString,
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
    def WatchMemberAssignment(request,
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
            '/ntt.iam.v1.MemberAssignmentService/WatchMemberAssignment',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentResponse.FromString,
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
    def WatchMemberAssignments(request,
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
            '/ntt.iam.v1.MemberAssignmentService/WatchMemberAssignments',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentsRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.WatchMemberAssignmentsResponse.FromString,
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
    def UpdateMemberAssignment(request,
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
            '/ntt.iam.v1.MemberAssignmentService/UpdateMemberAssignment',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.UpdateMemberAssignmentRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__pb2.MemberAssignment.FromString,
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
    def DeleteMemberAssignment(request,
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
            '/ntt.iam.v1.MemberAssignmentService/DeleteMemberAssignment',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_member__assignment__service__pb2.DeleteMemberAssignmentRequest.SerializeToString,
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
