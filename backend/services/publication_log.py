import json
from pathlib import Path


class PublicationLog:


    def __init__(self):

        self.file = Path(
            "publications_log.json"
        )



    def save(
        self,
        publication_id: str,
        video: str,
        platform: str,
        response: dict,
        created_at: str,
    ):


        logs = []


        if self.file.exists():

            logs = json.loads(
                self.file.read_text()
            )



        # Cerca una pubblicazione già esistente

        publication = None


        for item in logs:

            if item.get(
                "publication_id"
            ) == publication_id:

                publication = item

                break



        # Se non esiste la crea

        if publication is None:


            publication = {

                "publication_id": publication_id,

                "created_at": created_at,

                "video": video,

                "platforms": {}

            }


            logs.append(
                publication
            )



        # Aggiunge il risultato piattaforma

        publication["platforms"][platform] = response



        self.file.write_text(

            json.dumps(
                logs,
                indent=4
            )

        )


        return publication