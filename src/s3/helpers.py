import boto3
import uuid

from src.config import SourceConfig, Config

client = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
)


def connectToPolly(
    regionName=SourceConfig.DEFAULT_REGION, endpointUrl=SourceConfig.DEFAULT_URL
):
    return boto3.client(
        "polly",
        region_name=regionName,
        endpoint_url=endpointUrl,
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    )


def speak(polly, text, format="mp3", voice="Brian"):
    resp = polly.synthesize_speech(OutputFormat=format, Text=text, VoiceId=voice)
    soundBytes = resp["AudioStream"].read()
    myuuid = str(uuid.uuid4())
    client.put_object(
        Body=soundBytes, Bucket="text-to-audio-testy", Key=myuuid + ".mp3"
    )
    return myuuid
