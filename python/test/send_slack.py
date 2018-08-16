#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import jmespath

output = '''{
    "LoadBalancerAttributes": {
        "AccessLog": {
            "S3BucketPrefix": "yanolja_api_live/prod/classic", 
            "EmitInterval": 5, 
            "Enabled": true, 
            "S3BucketName": "yanolja-loadbalancer-logs"
        }
    }, 
    "ResponseMetadata": {
        "RetryAttempts": 0, 
        "HTTPStatusCode": 200, 
        "RequestId": "83039fe2-938b-11e8-8bf7-27d56de9b3f1", 
        "HTTPHeaders": {
            "x-amzn-requestid": "83039fe2-938b-11e8-8bf7-27d56de9b3f1", 
            "date": "Mon, 30 Jul 2018 00:00:03 GMT", 
            "content-length": "706", 
            "content-type": "text/xml"
        }
    }, 
    "LoadBalancerName": "awseb-e-q-AWSEBLoa-1L7V4YU8OPTOR"
}
'''

swtich_json_output = json.loads(output)

elb_name = jmespath.search('LoadBalancerName', swtich_json_output)
bucket_name = jmespath.search('LoadBalancerAttributes.AccessLog.S3BucketName', swtich_json_output)
prefix = jmespath.search('LoadBalancerAttributes.AccessLog.S3BucketPrefix', swtich_json_output)


print elb_name, bucket_name, prefix