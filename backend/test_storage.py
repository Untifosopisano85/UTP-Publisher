from services.storage import StorageService


storage = StorageService()


result = storage.upload_video(
    "media/test.mp4"
)


print(result)