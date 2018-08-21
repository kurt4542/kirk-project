#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3
import jmespath

session = boto3.Session(profile_name='yanolja-prod-admin')
client = session.client('ec2')

def chkEc2Status():
    response = client.describe_instance_status(
        InstanceIds=[
            'i-00095acb94f976816',
            'i-016cc0932937ced21'
        ]
    )

    instance_state = jmespath.search('InstanceStatuses[].InstanceState.Name', response)
    instance_id = jmespath.search('InstanceStatuses[].InstanceId', response)

    return instance_id, instance_state

def getEc2(instance_id):
    response = client.describe_instances(
        InstanceIds=[
            instance_id
        ]
    )

    for ec2_array in response['Reservations']:
        for ec2 in ec2_array['Instances']:
            try:
                tag_name = jmespath.search('Tags[?Key==\'Name\'].Value', ec2)[0]
                instnace_id = jmespath.search('InstanceId', ec2)
                print tag_name, instnace_id
            except IndexError:
                tag_name = ''
                print tag_name






def main():
    running_instances = chkEc2Status()

    #print result
#
    #print result[0]
    #print result[1]

    for i in range(len(running_instances)):
        if running_instances[1][i] == 'running':
            getEc2(running_instances[0][i])

def main2():
    ec2_name = getEc2()

    #print ec2_name


if __name__ == '__main__':
    main()