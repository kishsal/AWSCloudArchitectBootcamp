import boto3
import sys

def main():
    deletesS3bucket(name)

def deletesS3bucket(name):
    client = boto3.client('s3') #variable

    delete = client.delete_bucket(
        Bucket=name,
    )

    print(delete) #print out

name = sys.argv[1]

if __name__ == '__main__': # runs as standalone script
    main()
