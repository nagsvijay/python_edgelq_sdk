#!/usr/bin/python

 

import sys

sys.path.append("C:/Users/nagsv/EgdePlatform/edgelq_sdk")

import requests

import json

import hashlib

import base64

import time

import grpc

import hmac

import traceback

import sys

from google.auth import jwt

import google.auth.transport.requests

from google.protobuf import field_mask_pb2

from edgelq_sdk.monitoring.proto.v3 import time_serie_service_pb2_grpc,time_serie_custom_pb2,alert_service_pb2_grpc,alert_service_pb2

#from edgelq_sdk.monitoring.proto.v3 import time_serie_service_pb2,time_serie_custom_pb2,alert_service_pb2

from watchdog_sdk.proto.v1alpha2 import probing_target_group_service_pb2_grpc,probing_target_group_service_pb2,probe_group_service_pb2_grpc,probe_group_service_pb2,probe_service_pb2_grpc,probe_service_pb2,probing_target_service_pb2_grpc,probing_target_service_pb2

from watchdog_sdk.proto.v1alpha2 import http_metrics_custom_pb2_grpc,http_metrics_custom_pb2,http_metrics_service_pb2_grpc,http_metrics_service_pb2

from google.protobuf.json_format import MessageToDict

from google.protobuf.json_format import MessageToJson

from datetime import datetime, timezone

watchdog_access = ""

watchdog_url = ""

TOKEN = ""

def get_watchdog_token():

    token = jwt.Credentials.from_service_account_info(watchdog_access, audience=watchdog_url["watchdog_url"])

    request = google.auth.transport.requests.Request()

    token.refresh(request)

    return token

 

def main():

    #projectid = sys.argv[1]

    projectid = "alcon-pilot"

    global edgelq_url

    edgelq_url = "devices.edgelq.com/device/hardware/temperature"

    global watchdog_url

    watchdog_url = {"monitoring_url": "https://monitoring.stg01b.edgelq.com", "watchdog_url": "https://watchdog.stg01b.edgelq.com"}

    global watchdog_access

    private_ke = """-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDdVGlsEBH8OsEg\nI6lwpS+ASbeK2Nc4ZHd/6Fld17euRcxWdbgjkxV8ZlRR6pB57YSTPjiuL95eqHt8\nHVMpB4ZMla9FppAxQsFdyM8uHC1fcxzOqFs+hAfaS1oMafJiZSIn8lNpR5gg0CHs\nU910jx6UEB32M8LbRk6IfKx4Po5kr5++jStZKgTeYGwLb7mXF6PZv0xpuusAsP1C\n2gBfCLk1Rzbb1MrSXe2YuplJIsmn8bi5BnX2ZNdFvVkydEyNsPMV+o8oTCqS0JXs\nAsbjYMW9ckgJayERH0pCLtnHWJOdc9dejQajNynGcJtSYDqk/weFfoe1NHDSC+z/\nQ86hbJDPAgMBAAECggEBAItQqtsecnO1+AJm8Cy7jV7PB/0Z6L7SXnXgpv/u3OuR\ne8Ggb7vUxV18e+7kGvTkkOKt87eQ4gPrQW8qdkIJPnvObHkHExQu1NBXqjF4Awdl\nyeg7CNQc/2RksdXGio9s4UcLvX0zV4qv9+puD6Niwvin/HQQuMKVSrGW6Gj312GA\nDv8YALzaIpJuheZ1b6v+ObgmopKbICyDr/3zePkKvg4cz6TuN/bAYmIqimWeKbOg\nohURWNo9zDJW248MyqEJzzSHYttTAzwj2Oo3PFb5ZFq8cZfAlgKZt2f930NMUS2m\njf9leVeIfEFEsi/XrkE98xzCDYfcwkCHQqpRTeIaTwECgYEA7mxghjdKRwflXkRf\nhhYO4sBPBLB66d/9/ABc7WEopVUvPmtCpI8ujsB+UFn6DNLn61NPkbRjmBg69kn+\n8B5LGL72MWEWnYh6kLGNdCqS+h4O4iYPJgp9KfiMDqYelghg8M8KefmBT4Hy9ALH\n0b/RV5sv+ZiWzQWbHvbqk60x9CECgYEA7aVv5EbeCEdRxWM0TjRrJGbPT4kCIM3d\nmR3tdGs/VEktNUUrLY3s0BirnNwkJktOOpVUG90um7FARVT7i0POToWkuhphLIid\n07GO7LXW1cycY8CLO5Ij9oZR/8WuiCHfK+3KiB0zW/UAZl7ZlQACym8tZvQ26LMJ\ni8UnHH/05u8CgYEA0xdRPoOlV8493YBbsrPE6i2pyFUX/gk7LeqEXAcxnXAWLAV7\nM4cxiWIUc7+2C7SPcWKJiE9V/ks1qOlKtf2cL4SjJIT5KPC003bf7oHjL199feyE\nbQHMX2SXXEDnw54Xdh1ZATVOr742BKSRlbtm9VGI4Eug+FSGSpwChE1LdQECgYBb\nl7a/adzrnelTRYAEYEmnNwTR58FtOUseV52MkEVRS/7jmCwjG59ZORjzlRlNtRqK\nk8FeF+p90VwvHKjyrQiX1QR/QemQC3ug+r9WVmNd9cWU4MIJDLNVscFq7hrtlvh3\n6udzfKWt3Ijx6766oc1xjlYWZyu+ljqopy0C3AJc+wKBgHAqxx1aJpbFtWme21m8\n87Tjx1pBnOjBeQ8If/V28oO55xj9gRQRngc8JErFMjD5S6YeyC62D3a+EOWKt58W\nFWBbxnoYZnLXJ8/XirAg6qS6CDXjiCg2/0l3cr6dCyykSEszk2yItktA/ctJUJ2R\nvrmtZl63o6sLBFpPZXa3TAjY\n-----END PRIVATE KEY-----\n"""

    watchdog_access = {

        "type": "service_account",

        "client_email": "spektraplatformstream@alcon-pilot.us-west2.serviceaccounts.iam.edgelq.com",

        #"private_key_id": "spektraanalytics",

        "private_key_id": "projects/alcon-pilot/regions/us-west2/serviceAccounts/spektraplatformstream/serviceAccountKeys/test",

        #"private_key": str(base64.b64decode("MIIBCgKCAQEAr0MK4+RHozxSZR9wewn1UJJsQSjPfqCWRkzJIUmO24oXH/+hnzb7B43+gZ+GJQ7Un13vOvsyscRJtlX30+OzVjql8zUacgjIxY8u3/5ej9uBEXxrsVv8FMfS74p3QH2Dr4MeTuyohN25DO0zAzAJJx4kA/T5ADNgUmGd1062Da2BZ6Ud0pPHNhQBrQjF0jL2GCz6zZIhUmi/s/7dwHOfak0kdibgs2iFlNCfIIkSUjnfUvXtaRWpsyW4ZlqsqHUt5Y7AWKbMEkWbmXqTXGz7gYNrUP9RfA1kTJxQoIUb6DaIabrvdesDmBmw3YEeOp+twPSo1gbYEalaugcLypAtvQIDAQAB").decode('utf-8'))

        "private_key": private_ke

    }

 

    global TOKEN

    TOKEN=get_watchdog_token()

    result=get_watchdog_current_metrics(projectid=projectid)

    if result:

        exit(0)

    exit(1)

 

def get_watchdog_current_metrics(projectid):

    try:

        print("Getting JWT Token")

        token = jwt.Credentials.from_service_account_info(watchdog_access, audience=watchdog_url["monitoring_url"])

        request = google.auth.transport.requests.Request()

        token.refresh(request)

        channel_creds = grpc.composite_channel_credentials(grpc.ssl_channel_credentials(), grpc.access_token_call_credentials(token.token.decode('UTF-8')))

        channel = grpc.secure_channel(watchdog_url["monitoring_url"].replace("https://",""), channel_creds)

        stub=time_serie_service_pb2.TimeSerieServiceStub(channel)

        per_series_aligner=45

        cross_series_reducer=1

        endtime=int(datetime.now(timezone.utc).timestamp() )

        starttime=endtime-600

        timeseriesrequest=time_serie_custom_pb2.ListTimeSeriesRequest(

            parent="projects/"+projectid,

            filter="""metric.type = "devices.edgelq.com/device/hardware/temperature" AND resource.type="devices.edgelq.com/device" {}""",

            #filter="""metric.type = "watchdog.edgelq.com/probe/session/latency" AND resource.type="watchdog.edgelq.com/probe" {}""".format(probeid),

            view=0,

            #page_size=0,

            #page_token="",

            interval={

                    "end_time":{

                    "seconds": endtime,

                    "nanos": 0

                    },

                    "start_time":{

                    "seconds": starttime,

                    "nanos": 0

                    }

                    },

            aggregation={"alignment_period":{"seconds":300,"nanos":0},"per_series_aligner":per_series_aligner,"cross_series_reducer":cross_series_reducer,"group_by_fields":["resource.labels.device_id"] })

        response=MessageToDict(stub.ListTimeSeries(timeseriesrequest))

        if response:

            for timeseries in response["timeSeries"]:

                if len(timeseries["points"]) > 0:

                    attime= int(datetime.strptime(timeseries["points"][0]["interval"]["endTime"], '%Y-%m-%dT%H:%M:%SZ').timestamp())

                    print(timeseries["resource"]["labels"]["device_id"]+".attime="+str(attime))

                    print(timeseries["resource"]["labels"]["device_id"]+".temperature="+str(timeseries["points"][0]["value"]["doubleValue"]))

            return True

        else:

            return True

 

    except Exception as e:

        traceback.print_exc()

        return False

 

if __name__ == "__main__":

    main()