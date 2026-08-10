from pathlib import Path

from googleapiclient.http import MediaFileUpload

from connectors.youtube.client import YouTubeClient



class YouTubeUploader:


    def __init__(self):

        self.client = YouTubeClient()

        self.youtube = self.client.youtube



    def upload_short(

        self,

        video_path: str,

        title: str,

        description: str,

    ):


        # Aggiunge automaticamente il tag Shorts

        if "#Shorts" not in description:

            description += "\n\n#Shorts"



        body = {

            "snippet": {

                "title": title,

                "description": description,

                "categoryId": "22",

            },


            "status": {

                "privacyStatus": "public",

            },

        }



        media = MediaFileUpload(

    video_path,

    chunksize=-1,

    resumable=True,

    mimetype="video/mp4",

)



        request = self.youtube.videos().insert(

            part="snippet,status",

            body=body,

            media_body=media,

        )



        response = request.execute()



        return {

            "video_id": response["id"],

            "url": f"https://youtube.com/shorts/{response['id']}"

        }