from connectors.meta.facebook import FacebookConnector
from connectors.meta.instagram import InstagramConnector

from models import Reel


class Publisher:


    def __init__(self):

        self.facebook = FacebookConnector()
        self.instagram = InstagramConnector()



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
    # COMPATIBILITA' COMANDI PRECEDENTI
    # --------------------------------------------------

    def get_facebook_page(self):

        return self.facebook.get_page_info()



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