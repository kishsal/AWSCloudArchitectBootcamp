import boto3
import sys

def main():
    createsS3bucket(name)

def createsS3bucket(name):
    client = boto3.client('s3') #variable

    create = client.create_bucket(
        ACL='private', #variable
        Bucket=name,
    )

    print(create) #print out

name = sys.argv[1]

if __name__ == '__main__': # runs as standalone script
    main()
