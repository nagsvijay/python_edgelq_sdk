# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.iam.proto.v1 import service_account_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2
from edgelq_sdk.iam.proto.v1 import service_account_service_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2
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
        + f' but the generated code in edgelq_sdk/iam/proto/v1/service_account_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ServiceAccountServiceStub(object):
    """ServiceAccount service API for IAM
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServiceAccount = channel.unary_unary(
                '/ntt.iam.v1.ServiceAccountService/GetServiceAccount',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
                _registered_method=True)
        self.BatchGetServiceAccounts = channel.unary_unary(
                '/ntt.iam.v1.ServiceAccountService/BatchGetServiceAccounts',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.BatchGetServiceAccountsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.BatchGetServiceAccountsResponse.FromString,
                _registered_method=True)
        self.ListServiceAccounts = channel.unary_unary(
                '/ntt.iam.v1.ServiceAccountService/ListServiceAccounts',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.ListServiceAccountsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.ListServiceAccountsResponse.FromString,
                _registered_method=True)
        self.WatchServiceAccount = channel.unary_stream(
                '/ntt.iam.v1.ServiceAccountService/WatchServiceAccount',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountResponse.FromString,
                _registered_method=True)
        self.WatchServiceAccounts = channel.unary_stream(
                '/ntt.iam.v1.ServiceAccountService/WatchServiceAccounts',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountsResponse.FromString,
                _registered_method=True)
        self.CreateServiceAccount = channel.unary_unary(
                '/ntt.iam.v1.ServiceAccountService/CreateServiceAccount',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
                _registered_method=True)
        self.UpdateServiceAccount = channel.unary_unary(
                '/ntt.iam.v1.ServiceAccountService/UpdateServiceAccount',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
                _registered_method=True)
        self.DeleteServiceAccount = channel.unary_unary(
                '/ntt.iam.v1.ServiceAccountService/DeleteServiceAccount',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class ServiceAccountServiceServicer(object):
    """ServiceAccount service API for IAM
    """

    def GetServiceAccount(self, request, context):
        """GetServiceAccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetServiceAccounts(self, request, context):
        """BatchGetServiceAccounts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListServiceAccounts(self, request, context):
        """ListServiceAccounts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchServiceAccount(self, request, context):
        """WatchServiceAccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchServiceAccounts(self, request, context):
        """WatchServiceAccounts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateServiceAccount(self, request, context):
        """CreateServiceAccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateServiceAccount(self, request, context):
        """UpdateServiceAccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteServiceAccount(self, request, context):
        """DeleteServiceAccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceAccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceAccount,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.SerializeToString,
            ),
            'BatchGetServiceAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetServiceAccounts,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.BatchGetServiceAccountsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.BatchGetServiceAccountsResponse.SerializeToString,
            ),
            'ListServiceAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListServiceAccounts,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.ListServiceAccountsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.ListServiceAccountsResponse.SerializeToString,
            ),
            'WatchServiceAccount': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchServiceAccount,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountResponse.SerializeToString,
            ),
            'WatchServiceAccounts': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchServiceAccounts,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountsResponse.SerializeToString,
            ),
            'CreateServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateServiceAccount,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.SerializeToString,
            ),
            'UpdateServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateServiceAccount,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.SerializeToString,
            ),
            'DeleteServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteServiceAccount,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.iam.v1.ServiceAccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.iam.v1.ServiceAccountService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ServiceAccountService(object):
    """ServiceAccount service API for IAM
    """

    @staticmethod
    def GetServiceAccount(request,
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
            '/ntt.iam.v1.ServiceAccountService/GetServiceAccount',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
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
    def BatchGetServiceAccounts(request,
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
            '/ntt.iam.v1.ServiceAccountService/BatchGetServiceAccounts',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.BatchGetServiceAccountsRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.BatchGetServiceAccountsResponse.FromString,
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
    def ListServiceAccounts(request,
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
            '/ntt.iam.v1.ServiceAccountService/ListServiceAccounts',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.ListServiceAccountsRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.ListServiceAccountsResponse.FromString,
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
    def WatchServiceAccount(request,
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
            '/ntt.iam.v1.ServiceAccountService/WatchServiceAccount',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountResponse.FromString,
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
    def WatchServiceAccounts(request,
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
            '/ntt.iam.v1.ServiceAccountService/WatchServiceAccounts',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountsRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.WatchServiceAccountsResponse.FromString,
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
    def CreateServiceAccount(request,
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
            '/ntt.iam.v1.ServiceAccountService/CreateServiceAccount',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
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
    def UpdateServiceAccount(request,
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
            '/ntt.iam.v1.ServiceAccountService/UpdateServiceAccount',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
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
    def DeleteServiceAccount(request,
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
            '/ntt.iam.v1.ServiceAccountService/DeleteServiceAccount',
            edgelq__sdk_dot_iam_dot_proto_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
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
