import boto3
client = boto3.client('rds', 
                   aws_access_key_id='$$$$$$$$$$$$$', 
                   aws_secret_access_key='$$$$$$$$$$$$$$$$$$$',
                     region_name='us-east-1')

response = client.create_db_instance(
    AvailabilityZone='us-east-1a',
    StorageType='gp2',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='Webserver',
    Engine='MySQL',
    EngineVersion='8.0.27',
    MasterUsername='phpserver',
    MasterUserPassword='senha',
    Port=3306,
    PubliclyAccessible=True,
    DBSubnetGroupName='subnets-rede-puclicas-rds',
    VpcSecurityGroupIds=["sg-0c27615ee75a816a5"],
    )

print (response)
