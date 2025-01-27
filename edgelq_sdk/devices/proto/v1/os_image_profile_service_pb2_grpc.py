# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.devices.proto.v1 import os_image_profile_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2
from edgelq_sdk.devices.proto.v1 import os_image_profile_service_pb2 as edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2
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
        + f' but the generated code in edgelq_sdk/devices/proto/v1/os_image_profile_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class OsImageProfileServiceStub(object):
    """OsImageProfile service API for Devices
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOsImageProfile = channel.unary_unary(
                '/ntt.devices.v1.OsImageProfileService/GetOsImageProfile',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.GetOsImageProfileRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.FromString,
                _registered_method=True)
        self.BatchGetOsImageProfiles = channel.unary_unary(
                '/ntt.devices.v1.OsImageProfileService/BatchGetOsImageProfiles',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.BatchGetOsImageProfilesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.BatchGetOsImageProfilesResponse.FromString,
                _registered_method=True)
        self.ListOsImageProfiles = channel.unary_unary(
                '/ntt.devices.v1.OsImageProfileService/ListOsImageProfiles',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.ListOsImageProfilesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.ListOsImageProfilesResponse.FromString,
                _registered_method=True)
        self.WatchOsImageProfile = channel.unary_stream(
                '/ntt.devices.v1.OsImageProfileService/WatchOsImageProfile',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfileRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfileResponse.FromString,
                _registered_method=True)
        self.WatchOsImageProfiles = channel.unary_stream(
                '/ntt.devices.v1.OsImageProfileService/WatchOsImageProfiles',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfilesRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfilesResponse.FromString,
                _registered_method=True)
        self.CreateOsImageProfile = channel.unary_unary(
                '/ntt.devices.v1.OsImageProfileService/CreateOsImageProfile',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.CreateOsImageProfileRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.FromString,
                _registered_method=True)
        self.UpdateOsImageProfile = channel.unary_unary(
                '/ntt.devices.v1.OsImageProfileService/UpdateOsImageProfile',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.UpdateOsImageProfileRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.FromString,
                _registered_method=True)
        self.DeleteOsImageProfile = channel.unary_unary(
                '/ntt.devices.v1.OsImageProfileService/DeleteOsImageProfile',
                request_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.DeleteOsImageProfileRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class OsImageProfileServiceServicer(object):
    """OsImageProfile service API for Devices
    """

    def GetOsImageProfile(self, request, context):
        """GetOsImageProfile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetOsImageProfiles(self, request, context):
        """BatchGetOsImageProfiles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOsImageProfiles(self, request, context):
        """ListOsImageProfiles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchOsImageProfile(self, request, context):
        """WatchOsImageProfile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchOsImageProfiles(self, request, context):
        """WatchOsImageProfiles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOsImageProfile(self, request, context):
        """CreateOsImageProfile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOsImageProfile(self, request, context):
        """UpdateOsImageProfile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOsImageProfile(self, request, context):
        """DeleteOsImageProfile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OsImageProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOsImageProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOsImageProfile,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.GetOsImageProfileRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.SerializeToString,
            ),
            'BatchGetOsImageProfiles': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetOsImageProfiles,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.BatchGetOsImageProfilesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.BatchGetOsImageProfilesResponse.SerializeToString,
            ),
            'ListOsImageProfiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOsImageProfiles,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.ListOsImageProfilesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.ListOsImageProfilesResponse.SerializeToString,
            ),
            'WatchOsImageProfile': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchOsImageProfile,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfileRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfileResponse.SerializeToString,
            ),
            'WatchOsImageProfiles': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchOsImageProfiles,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfilesRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfilesResponse.SerializeToString,
            ),
            'CreateOsImageProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOsImageProfile,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.CreateOsImageProfileRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.SerializeToString,
            ),
            'UpdateOsImageProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOsImageProfile,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.UpdateOsImageProfileRequest.FromString,
                    response_serializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.SerializeToString,
            ),
            'DeleteOsImageProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOsImageProfile,
                    request_deserializer=edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.DeleteOsImageProfileRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.devices.v1.OsImageProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.devices.v1.OsImageProfileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OsImageProfileService(object):
    """OsImageProfile service API for Devices
    """

    @staticmethod
    def GetOsImageProfile(request,
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
            '/ntt.devices.v1.OsImageProfileService/GetOsImageProfile',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.GetOsImageProfileRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.FromString,
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
    def BatchGetOsImageProfiles(request,
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
            '/ntt.devices.v1.OsImageProfileService/BatchGetOsImageProfiles',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.BatchGetOsImageProfilesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.BatchGetOsImageProfilesResponse.FromString,
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
    def ListOsImageProfiles(request,
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
            '/ntt.devices.v1.OsImageProfileService/ListOsImageProfiles',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.ListOsImageProfilesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.ListOsImageProfilesResponse.FromString,
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
    def WatchOsImageProfile(request,
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
            '/ntt.devices.v1.OsImageProfileService/WatchOsImageProfile',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfileRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfileResponse.FromString,
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
    def WatchOsImageProfiles(request,
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
            '/ntt.devices.v1.OsImageProfileService/WatchOsImageProfiles',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfilesRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.WatchOsImageProfilesResponse.FromString,
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
    def CreateOsImageProfile(request,
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
            '/ntt.devices.v1.OsImageProfileService/CreateOsImageProfile',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.CreateOsImageProfileRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.FromString,
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
    def UpdateOsImageProfile(request,
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
            '/ntt.devices.v1.OsImageProfileService/UpdateOsImageProfile',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.UpdateOsImageProfileRequest.SerializeToString,
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__pb2.OsImageProfile.FromString,
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
    def DeleteOsImageProfile(request,
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
            '/ntt.devices.v1.OsImageProfileService/DeleteOsImageProfile',
            edgelq__sdk_dot_devices_dot_proto_dot_v1_dot_os__image__profile__service__pb2.DeleteOsImageProfileRequest.SerializeToString,
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
