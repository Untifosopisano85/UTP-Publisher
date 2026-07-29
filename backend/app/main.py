from fastapi import FastAPI
from api.routes import router


api = FastAPI(
    title="UTP Publisher"
)

api.include_router(router)

import sys

from services.publisher import Publisher
from models import Reel


def main():

    publisher = Publisher()

    if len(sys.argv) < 2:
        print(
            """
UTP Publisher

Comandi disponibili:

page

text "messaggio"

image <percorso_file> "didascalia"

reel <video.mp4> "titolo" "descrizione"

reel-status <video_id>

reel-start

reel-publish <video_id> "descrizione" "titolo"
"""
        )
        return

    command = sys.argv[1]


    # --------------------------------------------------
    # PAGINA
    # --------------------------------------------------

    if command == "page":

        print(
            publisher.get_facebook_page()
        )


    # --------------------------------------------------
    # TESTO
    # --------------------------------------------------

    elif command == "text":

        if len(sys.argv) < 3:
            print(
                'Uso: text "messaggio"'
            )
            return

        print(
            publisher.publish_facebook_text(
                sys.argv[2]
            )
        )


    # --------------------------------------------------
    # IMMAGINE
    # --------------------------------------------------

    elif command == "image":

        if len(sys.argv) < 3:
            print(
                'Uso: image <file> "didascalia"'
            )
            return

        image = sys.argv[2]

        caption = (
            sys.argv[3]
            if len(sys.argv) > 3
            else ""
        )

        print(
            publisher.publish_facebook_image(
                image,
                caption,
            )
        )


    # --------------------------------------------------
    # REEL COMPLETO
    # --------------------------------------------------

    elif command == "reel":

        if len(sys.argv) < 3:
            print(
                'Uso: reel <video.mp4> "titolo" "descrizione"'
            )
            return

        video = sys.argv[2]

        title = (
            sys.argv[3]
            if len(sys.argv) > 3
            else ""
        )

        description = (
            sys.argv[4]
            if len(sys.argv) > 4
            else ""
        )

        reel = Reel(
    video=video,
    title=title,
    description=description,

        )

        print(
            publisher.publish_facebook_reel(
                reel
            )
        )


    # --------------------------------------------------
    # REEL STATUS
    # --------------------------------------------------

    elif command == "reel-status":

        if len(sys.argv) < 3:
            print(
                "Uso: reel-status <video_id>"
            )
            return

        print(
            publisher.get_facebook_reel_status(
                sys.argv[2]
            )
        )


    # --------------------------------------------------
    # REEL START (compatibilità)
    # --------------------------------------------------

    elif command == "reel-start":

        print(
            publisher.start_facebook_reel_upload()
        )


    # --------------------------------------------------
    # REEL PUBLISH (compatibilità)
    # --------------------------------------------------

    elif command == "reel-publish":

        if len(sys.argv) < 3:
            print(
                'Uso: reel-publish <video_id> "descrizione" "titolo"'
            )
            return

        description = (
            sys.argv[3]
            if len(sys.argv) > 3
            else ""
        )

        title = (
            sys.argv[4]
            if len(sys.argv) > 4
            else ""
        )

        print(
            publisher.publish_facebook_reel(
                video_id=sys.argv[2],
                description=description,
                title=title,
            )
        )


    else:

        print(
            f"Comando sconosciuto: {command}"
        )


if __name__ == "__main__":
    main()
def start_api():

    import uvicorn

    uvicorn.run(
        api,
        host="0.0.0.0",
        port=8000,
    )