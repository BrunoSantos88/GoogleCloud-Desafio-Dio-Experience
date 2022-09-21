import boto3 
ec2 = boto3.client('ec2', 
                   'us-east-1', 
                   aws_access_key_id='###############', 
                   aws_secret_access_key='33333333333333333') 
conn = ec2.run_instances(InstanceType="t2.micro", 
                         MaxCount=3, 
                         MinCount=3, 
                         KeyName='3############',
                         ImageId='ami-08d4ac5b634553e16',   ### ubuntu:20:04
                         Monitoring={
                                'Enabled': False
                         },

UserData= '''#!/bin/bash
#!/bin/bash
curl https://releases.rancher.com/install-docker/19.03.sh | sh 
usermod -aG docker root
apt-get install git -y
curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
apt-get install nfs-common -y
''',

NetworkInterfaces=[{
 'SubnetId': 'subnet-############',  ### subnet-a subenet-b subnet-c
 'DeviceIndex': 0,
 'AssociatePublicIpAddress': True,
 'Groups': ['###########']
 
 }],

)         
print("Servidores_Criados")  