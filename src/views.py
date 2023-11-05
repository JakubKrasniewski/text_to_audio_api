from flask import Blueprint, request, json
from src.config import SourceConfig
from src.s3.helpers import speak, connectToPolly, client


speech_blueprint = Blueprint("speech", __name__)
download_blueprint = Blueprint("download", __name__)
languages_blueprint = Blueprint("languages", __name__)


@speech_blueprint.route("/convert", methods=["POST"])
def get_convert():
    """
    View accepts HTTP request with JSON that contains:
    - Voice type
    - Text for convert to .mp3 file

    Example JSON data:
    {
        "voice_type": <voice type>,
        "text": <example text>
    }

    :return:
    """
    data = request.get_json()
    voice = data["voice_type"]
    text = data["text"]
    polly = connectToPolly()
    my_uuid = speak(polly, text, "mp3", voice)

    return {"status": "File created at S3!", "new_file_name:": my_uuid}, 201


@download_blueprint.route("/download")  # /download?name=""
def get_download():
    """
    View downloads given MP3 object from S3.

    Accepts query parameter:
    - ?name=<file_name_to_download>

    :return:
    """
    name = request.args.get("name")
    client.download_file(
        "text-to-audio-testy", name + ".mp3", f"src/s3/content/{name}.mp3"
    )
    return "Filed has been downloaded"


@languages_blueprint.route("/languages")
def get_languages():
    """
    View represents available voices related with specific languages

    Example return:
    {
        "German": <voices>,
        "Polish": <voices>,
    }
    """
    with open(SourceConfig.LANGUAGES_PATH, "r") as json_file:
        data = json.load(json_file)
        return data
