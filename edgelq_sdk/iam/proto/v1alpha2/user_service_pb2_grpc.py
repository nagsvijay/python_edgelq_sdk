# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.iam.proto.v1alpha2 import user_custom_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2
from edgelq_sdk.iam.proto.v1alpha2 import user_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2
from edgelq_sdk.iam.proto.v1alpha2 import user_service_pb2 as edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2
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
        + f' but the generated code in edgelq_sdk/iam/proto/v1alpha2/user_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UserServiceStub(object):
    """User service API for IAM
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/GetUser',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.GetUserRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
                _registered_method=True)
        self.BatchGetUsers = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/BatchGetUsers',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.BatchGetUsersRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.BatchGetUsersResponse.FromString,
                _registered_method=True)
        self.ListUsers = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/ListUsers',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.ListUsersResponse.FromString,
                _registered_method=True)
        self.WatchUser = channel.unary_stream(
                '/ntt.iam.v1alpha2.UserService/WatchUser',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUserRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUserResponse.FromString,
                _registered_method=True)
        self.WatchUsers = channel.unary_stream(
                '/ntt.iam.v1alpha2.UserService/WatchUsers',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUsersRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUsersResponse.FromString,
                _registered_method=True)
        self.CreateUser = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/CreateUser',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
                _registered_method=True)
        self.UpdateUser = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/UpdateUser',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
                _registered_method=True)
        self.DeleteUser = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/DeleteUser',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.GetUserByEmail = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/GetUserByEmail',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetUserByEmailRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
                _registered_method=True)
        self.BatchGetUsersByEmail = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/BatchGetUsersByEmail',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.BatchGetUsersByEmailRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.BatchGetUsersByEmailResponse.FromString,
                _registered_method=True)
        self.GetMySettings = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/GetMySettings',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetMySettingsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetMySettingsResponse.FromString,
                _registered_method=True)
        self.SetMySettings = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/SetMySettings',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.SetMySettingsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.RefreshUserFromIdToken = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/RefreshUserFromIdToken',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.RefreshUserFromIdTokenRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.RefreshUserFromIdTokenResponse.FromString,
                _registered_method=True)
        self.ResendVerificationEmail = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/ResendVerificationEmail',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.ResendVerificationEmailRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.IsUserVerified = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/IsUserVerified',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.IsUserVerifiedRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.ResetMFAIfRecoveryKeyUsed = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/ResetMFAIfRecoveryKeyUsed',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.ResetMFAIfRecoveryKeyUsedRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.SetUsersNameInAuth0 = channel.unary_unary(
                '/ntt.iam.v1alpha2.UserService/SetUsersNameInAuth0',
                request_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.SetUsersNameInAuth0Request.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """User service API for IAM
    """

    def GetUser(self, request, context):
        """GetUser
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetUsers(self, request, context):
        """BatchGetUsers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """ListUsers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchUser(self, request, context):
        """WatchUser
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchUsers(self, request, context):
        """WatchUsers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """CreateUser
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """UpdateUser
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """DeleteUser
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByEmail(self, request, context):
        """GetUserByEmail
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetUsersByEmail(self, request, context):
        """BatchGetUsersByEmail
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMySettings(self, request, context):
        """GetMySettings
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMySettings(self, request, context):
        """SetMySettings
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshUserFromIdToken(self, request, context):
        """RefreshUserFromIdToken
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResendVerificationEmail(self, request, context):
        """ResendVerificationEmail
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsUserVerified(self, request, context):
        """IsUserVerified
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetMFAIfRecoveryKeyUsed(self, request, context):
        """ResetMFAIfRecoveryKeyUsed
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetUsersNameInAuth0(self, request, context):
        """SetUsersNameInAuth0
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.GetUserRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.SerializeToString,
            ),
            'BatchGetUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetUsers,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.BatchGetUsersRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.BatchGetUsersResponse.SerializeToString,
            ),
            'ListUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.ListUsersRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.ListUsersResponse.SerializeToString,
            ),
            'WatchUser': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchUser,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUserRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUserResponse.SerializeToString,
            ),
            'WatchUsers': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchUsers,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUsersRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUsersResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.CreateUserRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.UpdateUserRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.DeleteUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetUserByEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByEmail,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetUserByEmailRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.SerializeToString,
            ),
            'BatchGetUsersByEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetUsersByEmail,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.BatchGetUsersByEmailRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.BatchGetUsersByEmailResponse.SerializeToString,
            ),
            'GetMySettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMySettings,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetMySettingsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetMySettingsResponse.SerializeToString,
            ),
            'SetMySettings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMySettings,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.SetMySettingsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RefreshUserFromIdToken': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshUserFromIdToken,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.RefreshUserFromIdTokenRequest.FromString,
                    response_serializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.RefreshUserFromIdTokenResponse.SerializeToString,
            ),
            'ResendVerificationEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.ResendVerificationEmail,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.ResendVerificationEmailRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'IsUserVerified': grpc.unary_unary_rpc_method_handler(
                    servicer.IsUserVerified,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.IsUserVerifiedRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ResetMFAIfRecoveryKeyUsed': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetMFAIfRecoveryKeyUsed,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.ResetMFAIfRecoveryKeyUsedRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetUsersNameInAuth0': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUsersNameInAuth0,
                    request_deserializer=edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.SetUsersNameInAuth0Request.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.iam.v1alpha2.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.iam.v1alpha2.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """User service API for IAM
    """

    @staticmethod
    def GetUser(request,
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
            '/ntt.iam.v1alpha2.UserService/GetUser',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.GetUserRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
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
    def BatchGetUsers(request,
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
            '/ntt.iam.v1alpha2.UserService/BatchGetUsers',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.BatchGetUsersRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.BatchGetUsersResponse.FromString,
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
    def ListUsers(request,
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
            '/ntt.iam.v1alpha2.UserService/ListUsers',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.ListUsersRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.ListUsersResponse.FromString,
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
    def WatchUser(request,
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
            '/ntt.iam.v1alpha2.UserService/WatchUser',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUserRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUserResponse.FromString,
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
    def WatchUsers(request,
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
            '/ntt.iam.v1alpha2.UserService/WatchUsers',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUsersRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.WatchUsersResponse.FromString,
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
    def CreateUser(request,
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
            '/ntt.iam.v1alpha2.UserService/CreateUser',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.CreateUserRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
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
    def UpdateUser(request,
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
            '/ntt.iam.v1alpha2.UserService/UpdateUser',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
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
    def DeleteUser(request,
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
            '/ntt.iam.v1alpha2.UserService/DeleteUser',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
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

    @staticmethod
    def GetUserByEmail(request,
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
            '/ntt.iam.v1alpha2.UserService/GetUserByEmail',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetUserByEmailRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__pb2.User.FromString,
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
    def BatchGetUsersByEmail(request,
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
            '/ntt.iam.v1alpha2.UserService/BatchGetUsersByEmail',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.BatchGetUsersByEmailRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.BatchGetUsersByEmailResponse.FromString,
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
    def GetMySettings(request,
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
            '/ntt.iam.v1alpha2.UserService/GetMySettings',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetMySettingsRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.GetMySettingsResponse.FromString,
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
    def SetMySettings(request,
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
            '/ntt.iam.v1alpha2.UserService/SetMySettings',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.SetMySettingsRequest.SerializeToString,
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

    @staticmethod
    def RefreshUserFromIdToken(request,
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
            '/ntt.iam.v1alpha2.UserService/RefreshUserFromIdToken',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.RefreshUserFromIdTokenRequest.SerializeToString,
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.RefreshUserFromIdTokenResponse.FromString,
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
    def ResendVerificationEmail(request,
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
            '/ntt.iam.v1alpha2.UserService/ResendVerificationEmail',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.ResendVerificationEmailRequest.SerializeToString,
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

    @staticmethod
    def IsUserVerified(request,
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
            '/ntt.iam.v1alpha2.UserService/IsUserVerified',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.IsUserVerifiedRequest.SerializeToString,
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

    @staticmethod
    def ResetMFAIfRecoveryKeyUsed(request,
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
            '/ntt.iam.v1alpha2.UserService/ResetMFAIfRecoveryKeyUsed',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.ResetMFAIfRecoveryKeyUsedRequest.SerializeToString,
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

    @staticmethod
    def SetUsersNameInAuth0(request,
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
            '/ntt.iam.v1alpha2.UserService/SetUsersNameInAuth0',
            edgelq__sdk_dot_iam_dot_proto_dot_v1alpha2_dot_user__custom__pb2.SetUsersNameInAuth0Request.SerializeToString,
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
