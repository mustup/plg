import logging

logger = logging.getLogger(
    __name__,
)


def output(
            extension,
            manifest,
            output,
        ):
    tracks = manifest['tracks']

    extension_with_dot = f'.{ extension }'

    for track in tracks:
        output.write(
            track,
        )

        output.write(
            extension_with_dot,
        )
