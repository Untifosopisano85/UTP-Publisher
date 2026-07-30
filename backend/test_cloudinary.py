from services.storage import StorageService


storage = StorageService()


result = storage.upload_video(
    "test.mp4"
)


print(result)