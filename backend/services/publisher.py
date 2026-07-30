from connectors.meta.facebook import FacebookConnector
from connectors.meta.instagram import InstagramConnector

from connectors.youtube.uploader import YouTubeUploader
from connectors.tiktok.uploader import TikTokUploader

from models import Reel



class Publisher:


    def __init__(self):

        self.facebook = FacebookConnector()
        self.instagram = InstagramConnector()

        self.youtube = YouTubeUploader()
        self.tiktok = TikTokUploader()



    # --------------------------------------------------
    # FACEBOOK
    # --------------------------------------------------

    def publish_facebook_reel(
        self,
        reel: Reel,
    ):

        return self.facebook.publish_reel(
            reel
        )



    def publish_facebook_text(
        self,
        message: str,
    ):

        return self.facebook.publish_text(
            message
        )



    def publish_facebook_image(
        self,
        image_path: str,
        caption: str = "",
    ):

        return self.facebook.publish_image(
            image_path,
            caption,
        )



    def get_facebook_page(self):

        return self.facebook.get_page_info()



    # --------------------------------------------------
    # INSTAGRAM
    # --------------------------------------------------

    def publish_instagram_reel(
        self,
        video_url: str,
        caption: str = "",
    ):

        return self.instagram.publish_reel(
            video_url=video_url,
            caption=caption,
        )



    # --------------------------------------------------
    # YOUTUBE SHORTS
    # --------------------------------------------------

    def publish_youtube_short(
        self,
        video_path: str,
        title: str,
        description: str = "",
    ):

        return self.youtube.upload_short(
            video_path,
            title,
            description,
        )



    # --------------------------------------------------
    # TIKTOK
    # --------------------------------------------------

    def publish_tiktok_video(
        self,
        video_path: str,
        title: str,
        description: str = "",
    ):

        return self.tiktok.upload_video(
            video_path,
            title,
            description,
        )