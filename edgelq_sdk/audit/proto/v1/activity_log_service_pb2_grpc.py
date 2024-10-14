# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.audit.proto.v1 import activity_log_custom_pb2 as edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2

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
        + f' but the generated code in edgelq_sdk/audit/proto/v1/activity_log_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ActivityLogServiceStub(object):
    """ActivityLog service API for Audit
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListActivityLogs = channel.unary_unary(
                '/ntt.audit.v1.ActivityLogService/ListActivityLogs',
                request_serializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.ListActivityLogsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.ListActivityLogsResponse.FromString,
                _registered_method=True)
        self.CreateActivityLogs = channel.unary_unary(
                '/ntt.audit.v1.ActivityLogService/CreateActivityLogs',
                request_serializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.CreateActivityLogsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.CreateActivityLogsResponse.FromString,
                _registered_method=True)


class ActivityLogServiceServicer(object):
    """ActivityLog service API for Audit
    """

    def ListActivityLogs(self, request, context):
        """ListActivityLogs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateActivityLogs(self, request, context):
        """CreateActivityLogs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ActivityLogServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListActivityLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListActivityLogs,
                    request_deserializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.ListActivityLogsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.ListActivityLogsResponse.SerializeToString,
            ),
            'CreateActivityLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateActivityLogs,
                    request_deserializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.CreateActivityLogsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.CreateActivityLogsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.audit.v1.ActivityLogService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.audit.v1.ActivityLogService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ActivityLogService(object):
    """ActivityLog service API for Audit
    """

    @staticmethod
    def ListActivityLogs(request,
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
            '/ntt.audit.v1.ActivityLogService/ListActivityLogs',
            edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.ListActivityLogsRequest.SerializeToString,
            edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.ListActivityLogsResponse.FromString,
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
    def CreateActivityLogs(request,
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
            '/ntt.audit.v1.ActivityLogService/CreateActivityLogs',
            edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.CreateActivityLogsRequest.SerializeToString,
            edgelq__sdk_dot_audit_dot_proto_dot_v1_dot_activity__log__custom__pb2.CreateActivityLogsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
