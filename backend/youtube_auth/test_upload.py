from connectors.youtube.uploader import YouTubeUploader



uploader = YouTubeUploader()


result = uploader.upload_short(

    "test.mp4",

    "Test UTP Publisher",

    "Primo test YouTube Shorts",

)


print(result)