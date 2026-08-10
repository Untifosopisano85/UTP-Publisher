import json
from pathlib import Path


class PublicationHistory:

    def __init__(self):

        self.file = Path(
            "publications_log.json"
        )


    def get_all(self):

        if not self.file.exists():

            return []


        return json.loads(
            self.file.read_text()
        )


    def get_by_id(
        self,
        publication_id: str
    ):

        publications = self.get_all()


        for publication in publications:

            if publication.get(
                "publication_id"
            ) == publication_id:

                return publication


        return None


    def save(
        self,
        publication
    ):

        publications = self.get_all()


        publications.append(
            publication
        )


        self.file.write_text(
            json.dumps(
                publications,
                indent=2,
                ensure_ascii=False
            )
        )

        return publication