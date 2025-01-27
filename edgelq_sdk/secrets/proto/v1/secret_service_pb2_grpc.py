# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.secrets.proto.v1 import secret_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2
from edgelq_sdk.secrets.proto.v1 import secret_service_pb2 as edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2
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
        + f' but the generated code in edgelq_sdk/secrets/proto/v1/secret_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SecretServiceStub(object):
    """Secret service API for Secrets
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSecret = channel.unary_unary(
                '/ntt.secrets.v1.SecretService/GetSecret',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.GetSecretRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.FromString,
                _registered_method=True)
        self.BatchGetSecrets = channel.unary_unary(
                '/ntt.secrets.v1.SecretService/BatchGetSecrets',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.BatchGetSecretsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.BatchGetSecretsResponse.FromString,
                _registered_method=True)
        self.ListSecrets = channel.unary_unary(
                '/ntt.secrets.v1.SecretService/ListSecrets',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.ListSecretsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.ListSecretsResponse.FromString,
                _registered_method=True)
        self.WatchSecret = channel.unary_stream(
                '/ntt.secrets.v1.SecretService/WatchSecret',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretResponse.FromString,
                _registered_method=True)
        self.WatchSecrets = channel.unary_stream(
                '/ntt.secrets.v1.SecretService/WatchSecrets',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretsResponse.FromString,
                _registered_method=True)
        self.CreateSecret = channel.unary_unary(
                '/ntt.secrets.v1.SecretService/CreateSecret',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.CreateSecretRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.FromString,
                _registered_method=True)
        self.UpdateSecret = channel.unary_unary(
                '/ntt.secrets.v1.SecretService/UpdateSecret',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.UpdateSecretRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.FromString,
                _registered_method=True)
        self.DeleteSecret = channel.unary_unary(
                '/ntt.secrets.v1.SecretService/DeleteSecret',
                request_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.DeleteSecretRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class SecretServiceServicer(object):
    """Secret service API for Secrets
    """

    def GetSecret(self, request, context):
        """GetSecret
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetSecrets(self, request, context):
        """BatchGetSecrets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSecrets(self, request, context):
        """ListSecrets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchSecret(self, request, context):
        """WatchSecret
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchSecrets(self, request, context):
        """WatchSecrets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSecret(self, request, context):
        """CreateSecret
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSecret(self, request, context):
        """UpdateSecret
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSecret(self, request, context):
        """DeleteSecret
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecretServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSecret,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.GetSecretRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.SerializeToString,
            ),
            'BatchGetSecrets': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetSecrets,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.BatchGetSecretsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.BatchGetSecretsResponse.SerializeToString,
            ),
            'ListSecrets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSecrets,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.ListSecretsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.ListSecretsResponse.SerializeToString,
            ),
            'WatchSecret': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchSecret,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretResponse.SerializeToString,
            ),
            'WatchSecrets': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchSecrets,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretsResponse.SerializeToString,
            ),
            'CreateSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSecret,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.CreateSecretRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.SerializeToString,
            ),
            'UpdateSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSecret,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.UpdateSecretRequest.FromString,
                    response_serializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.SerializeToString,
            ),
            'DeleteSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSecret,
                    request_deserializer=edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.DeleteSecretRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.secrets.v1.SecretService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.secrets.v1.SecretService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SecretService(object):
    """Secret service API for Secrets
    """

    @staticmethod
    def GetSecret(request,
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
            '/ntt.secrets.v1.SecretService/GetSecret',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.GetSecretRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.FromString,
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
    def BatchGetSecrets(request,
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
            '/ntt.secrets.v1.SecretService/BatchGetSecrets',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.BatchGetSecretsRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.BatchGetSecretsResponse.FromString,
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
    def ListSecrets(request,
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
            '/ntt.secrets.v1.SecretService/ListSecrets',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.ListSecretsRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.ListSecretsResponse.FromString,
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
    def WatchSecret(request,
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
            '/ntt.secrets.v1.SecretService/WatchSecret',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretResponse.FromString,
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
    def WatchSecrets(request,
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
            '/ntt.secrets.v1.SecretService/WatchSecrets',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretsRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.WatchSecretsResponse.FromString,
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
    def CreateSecret(request,
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
            '/ntt.secrets.v1.SecretService/CreateSecret',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.CreateSecretRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.FromString,
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
    def UpdateSecret(request,
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
            '/ntt.secrets.v1.SecretService/UpdateSecret',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.UpdateSecretRequest.SerializeToString,
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__pb2.Secret.FromString,
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
    def DeleteSecret(request,
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
            '/ntt.secrets.v1.SecretService/DeleteSecret',
            edgelq__sdk_dot_secrets_dot_proto_dot_v1_dot_secret__service__pb2.DeleteSecretRequest.SerializeToString,
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
