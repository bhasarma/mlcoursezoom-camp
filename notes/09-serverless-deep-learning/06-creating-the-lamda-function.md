## 9.6 Creating the lamda function
In this session, we'll talk about creating the lambda function.

In last session, we built the docker image and tested it locally to see that everything works fine. In this session, we will deploy this docker container image into Lambda. 

For this, we'll publish our docker image in Amazon ECR (Elastic Container Registry). 

In order to interact with AWS Lambda from CLI, we will install awscli first.
Everything that we'll do from CLI can also be done with the web interface.

1.Install awscli with the following command, if you don't have it installed already:

```bash
(base) bsarma@turing:~$ pip install awscli
``` 

2.configure awscli for the first time with:

```bash
(base) bsarma@turing:~$ aws configure
AWS Access Key ID [None]: ACCESSKEY
AWS Secret Access Key [None]: SECRETACESSKEY
Default region name [None]: us-east-1
Default output format [None]: 
```
3.create AWS Elastic Container Repository 

```bash
(base) bsarma@turing:~$ aws ecr create-repository --repository-name clothing-tflite-images
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:5421152122142:repository/clothing-tflite-images",
        "registryId": "5421152122142",
        "repositoryName": "clothing-tflite-images",
        "repositoryUri": "5421152122142.dkr.ecr.us-east-1.amazonaws.com/clothing-tflite-images",
        "createdAt": 1669465123.0,
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}

```
**4. Publish the image just created**
4.1 first log into the registry wtih
```bash
(base) bsarma@turing:~$ aws ecr get-login --no-include-email | sed 's/[0-9a-zA-Z=]\{20,}/PASSWORD/g'

docker login -u AWS -p PASSWORD https://546575206078.dkr.ecr.us-east-1.amazonaws.com
```

`sed` used above is a command line utility in linux that allows us to do different text manipulations including regular expressions. 

The output of the above command is something we want to execute. Then we'll be able to login to the registry above with docker. Then we'll be able to push to this registry. So we want to execute whatever the above command returns. For this, we'll put the above command inside a brace and followed by a `$`.

```bash
(base) bsarma@turing:~$ $(aws ecr get-login --no-include-email)
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /home/bsarma/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```
```bash
$ export REMOTE_URI=546575206078.dkr.ecr.us-east-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001
$ echo $REMOTE_URI
546575206078.dkr.ecr.us-east-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001
```

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK-12-serverless-deep-learning$ docker tag clothing-model:latest $REMOTE_URI

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK-12-serverless-deep-learning$ docker push $REMOTE_URI

```
We deployed our lambda function using aws.  We can't use it as webservice. Something we'll look at the next lesson. In next session, we'll expose the lamda function we created as a web service. 