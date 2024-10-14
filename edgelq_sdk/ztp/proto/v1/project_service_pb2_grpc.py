# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from edgelq_sdk.ztp.proto.v1 import project_pb2 as edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2
from edgelq_sdk.ztp.proto.v1 import project_service_pb2 as edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2
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
        + f' but the generated code in edgelq_sdk/ztp/proto/v1/project_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProjectServiceStub(object):
    """Project service API for Ztp
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProject = channel.unary_unary(
                '/ntt.ztp.v1.ProjectService/GetProject',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.FromString,
                _registered_method=True)
        self.BatchGetProjects = channel.unary_unary(
                '/ntt.ztp.v1.ProjectService/BatchGetProjects',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.BatchGetProjectsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.BatchGetProjectsResponse.FromString,
                _registered_method=True)
        self.ListProjects = channel.unary_unary(
                '/ntt.ztp.v1.ProjectService/ListProjects',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.ListProjectsResponse.FromString,
                _registered_method=True)
        self.WatchProject = channel.unary_stream(
                '/ntt.ztp.v1.ProjectService/WatchProject',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectResponse.FromString,
                _registered_method=True)
        self.WatchProjects = channel.unary_stream(
                '/ntt.ztp.v1.ProjectService/WatchProjects',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectsRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectsResponse.FromString,
                _registered_method=True)
        self.CreateProject = channel.unary_unary(
                '/ntt.ztp.v1.ProjectService/CreateProject',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.FromString,
                _registered_method=True)
        self.UpdateProject = channel.unary_unary(
                '/ntt.ztp.v1.ProjectService/UpdateProject',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.FromString,
                _registered_method=True)
        self.DeleteProject = channel.unary_unary(
                '/ntt.ztp.v1.ProjectService/DeleteProject',
                request_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class ProjectServiceServicer(object):
    """Project service API for Ztp
    """

    def GetProject(self, request, context):
        """GetProject
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetProjects(self, request, context):
        """BatchGetProjects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProjects(self, request, context):
        """ListProjects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchProject(self, request, context):
        """WatchProject
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchProjects(self, request, context):
        """WatchProjects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProject(self, request, context):
        """CreateProject
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProject(self, request, context):
        """UpdateProject
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProject(self, request, context):
        """DeleteProject
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.GetProjectRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.SerializeToString,
            ),
            'BatchGetProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetProjects,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.BatchGetProjectsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.BatchGetProjectsResponse.SerializeToString,
            ),
            'ListProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProjects,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.ListProjectsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.ListProjectsResponse.SerializeToString,
            ),
            'WatchProject': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchProject,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectResponse.SerializeToString,
            ),
            'WatchProjects': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchProjects,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectsRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectsResponse.SerializeToString,
            ),
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.CreateProjectRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.SerializeToString,
            ),
            'UpdateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProject,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.UpdateProjectRequest.FromString,
                    response_serializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.SerializeToString,
            ),
            'DeleteProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProject,
                    request_deserializer=edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.DeleteProjectRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ntt.ztp.v1.ProjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ntt.ztp.v1.ProjectService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProjectService(object):
    """Project service API for Ztp
    """

    @staticmethod
    def GetProject(request,
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
            '/ntt.ztp.v1.ProjectService/GetProject',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.FromString,
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
    def BatchGetProjects(request,
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
            '/ntt.ztp.v1.ProjectService/BatchGetProjects',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.BatchGetProjectsRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.BatchGetProjectsResponse.FromString,
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
    def ListProjects(request,
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
            '/ntt.ztp.v1.ProjectService/ListProjects',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.ListProjectsRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.ListProjectsResponse.FromString,
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
    def WatchProject(request,
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
            '/ntt.ztp.v1.ProjectService/WatchProject',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectResponse.FromString,
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
    def WatchProjects(request,
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
            '/ntt.ztp.v1.ProjectService/WatchProjects',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectsRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.WatchProjectsResponse.FromString,
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
    def CreateProject(request,
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
            '/ntt.ztp.v1.ProjectService/CreateProject',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.FromString,
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
    def UpdateProject(request,
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
            '/ntt.ztp.v1.ProjectService/UpdateProject',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__pb2.Project.FromString,
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
    def DeleteProject(request,
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
            '/ntt.ztp.v1.ProjectService/DeleteProject',
            edgelq__sdk_dot_ztp_dot_proto_dot_v1_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
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
