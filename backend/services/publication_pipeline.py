from pathlib import Path

from models.publication import Publication
from models.reel import Reel

from services.publisher import Publisher
from services.storage import StorageService



class PublicationPipeline:


    def __init__(self):

        self.publisher = Publisher()
        self.storage = StorageService()



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

            results[platform] = (
                self._publish_platform(
                    platform,
                    publication,
                    video_url,
                )
            )


        return results



    def _publish_platform(
        self,
        platform: str,
        publication: Publication,
        video_url: str,
    ):


        # --------------------------------------------------
        # FACEBOOK
        # --------------------------------------------------

        if platform == "facebook":

            reel = Reel(

                video=Path(
                    publication.video_path
                ),

                title=publication.facebook_message,

                full_description=publication.facebook_message,

                contents={
                    "facebook": {
                        "description": publication.facebook_message,
                    }
                },
            )


            return self.publisher.publish_facebook_reel(
                reel
            )



        # --------------------------------------------------
        # INSTAGRAM
        # --------------------------------------------------

        if platform == "instagram":

            return self.publisher.publish_instagram_reel(
                video_url=video_url,
                caption=publication.instagram_caption,
            )



        # --------------------------------------------------
        # YOUTUBE SHORTS
        # --------------------------------------------------

        if platform == "youtube":

            return self.publisher.publish_youtube_short(
                video_path=publication.video_path,
                title=publication.youtube_title,
                description=publication.youtube_description,
            )



        # --------------------------------------------------
        # TIKTOK
        # --------------------------------------------------

        if platform == "tiktok":

            return self.publisher.publish_tiktok_video(
                video_path=publication.video_path,
                title=publication.tiktok_caption,
                description=publication.tiktok_caption,
            )



        raise ValueError(
            f"Piattaforma non supportata: {platform}"
        )