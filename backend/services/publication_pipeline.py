from pathlib import Path

from models.publication import Publication
from models.publication_result import PublicationResult
from models.reel import Reel

from services.publisher import Publisher
from services.storage import StorageService
from services.publication_log import PublicationLog



class PublicationPipeline:


    def __init__(self):

        self.publisher = Publisher()
        self.storage = StorageService()
        self.log = PublicationLog()



    def publish(
        self,
        publication: Publication,
    ):

        publication.validate()


        uploaded_video = self.storage.upload_video(
            publication.video_path
        )

        video_url = uploaded_video["url"]


        results = {}



        for platform in publication.platforms:


            try:

                response = self._publish_platform(
                    platform,
                    publication,
                    video_url,
                )


                result = self._create_result(
                    publication,
                    platform,
                    response,
                )


                self.log.save(
                    publication_id=publication.publication_id,
                    video=publication.video_path,
                    platform=platform,
                    response=result.to_dict(),
                    created_at=publication.created_at,
                )


                results[platform] = result.to_dict()



            except Exception as e:


                result = PublicationResult(

                    publication_id=publication.publication_id,

                    platform=platform,

                    status="error",

                    error=str(e),

                )


                self.log.save(

                    publication_id=publication.publication_id,

                    video=publication.video_path,

                    platform=platform,

                    response=result.to_dict(),

                    created_at=publication.created_at,

                )


                results[platform] = result.to_dict()



        return results





    def _create_result(
        self,
        publication,
        platform,
        response,
    ):


        external_id = None
        url = None



        if platform == "youtube":

            external_id = response.get(
                "video_id"
            )

            url = response.get(
                "url"
            )



        elif platform == "facebook":

            external_id = (

                response
                .get("result", {})
                .get("post_id")

            )



        elif platform == "instagram":

            external_id = response.get(
                "id"
            )



        elif platform == "tiktok":

            external_id = response.get(
                "id"
            )



        return PublicationResult(

            publication_id=publication.publication_id,

            platform=platform,

            status="success",

            external_id=external_id,

            url=url,

        )





    def _publish_platform(
        self,
        platform: str,
        publication: Publication,
        video_url: str,
    ):



        if platform == "facebook":


            reel = Reel(

                video=Path(
                    publication.video_path
                ),

                title=publication.facebook_message,

                full_description=publication.facebook_message,

                contents={

                    "facebook": {

                        "description": publication.facebook_message

                    }

                },

            )


            return self.publisher.publish_facebook_reel(
                reel
            )



        if platform == "instagram":


            return self.publisher.publish_instagram_reel(

                video_url=video_url,

                caption=publication.instagram_caption,

            )



        if platform == "youtube":


            return self.publisher.publish_youtube_short(

                video_path=publication.video_path,

                title=publication.youtube_title,

                description=publication.youtube_description,

            )



        if platform == "tiktok":


            return self.publisher.publish_tiktok_video(

                video_path=publication.video_path,

                title=publication.tiktok_caption,

                description=publication.tiktok_caption,

            )



        raise ValueError(
            f"Piattaforma non supportata: {platform}"
        )