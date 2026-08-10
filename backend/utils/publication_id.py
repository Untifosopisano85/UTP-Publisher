from datetime import datetime
from pathlib import Path
import json


LOG_FILE = Path(
    "publications_log.json"
)


_last_generated_id = None


def generate_publication_id():

    global _last_generated_id


    now = datetime.now()

    date_part = now.strftime("%Y%m%d")


    counter = 1


    if LOG_FILE.exists():

        try:

            logs = json.loads(
                LOG_FILE.read_text()
            )


            today_ids = [

                item.get("publication_id")

                for item in logs

                if item.get("publication_id", "").startswith(
                    f"UTP-{date_part}"
                )

            ]


            if today_ids:

                numbers = [

                    int(item.split("-")[-1])

                    for item in today_ids

                ]

                counter = max(numbers) + 1


        except Exception:

            counter = 1



    if _last_generated_id:

        last_number = int(
            _last_generated_id.split("-")[-1]
        )

        counter = max(
            counter,
            last_number + 1
        )



    new_id = (
        f"UTP-{date_part}-{counter:03d}"
    )


    _last_generated_id = new_id


    return new_id