from pathlib import Path

from connectors.tiktok.client import TikTokClient


class TikTokUploader:


    def __init__(self):

        self.client = TikTokClient()



    def upload_video(
        self,
        video_path: str,
        title: str,
        description: str,
    ):

        video = Path(video_path)


        if not video.exists():
            raise FileNotFoundError(
                f"Video non trovato: {video_path}"
            )


        payload = {

            "post_info": {

                "title": title,

                "description": description,

                "privacy_level": "SELF_ONLY",

            },


            "source_info": {

                "source": "FILE_UPLOAD",

            }

        }


        return self.client.post(

            "/v2/post/publish/video/init/",

            payload

        )