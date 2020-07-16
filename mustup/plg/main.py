import importlib
import logging

import yaml

import mustup.core.main

logger = logging.getLogger(
    __name__,
)


def process(
            encoder_name,
            format_name,
            manifest_path,
            output,
        ):
    can_continue = True

    encoder_class = mustup.core.main.get_encoder_class(
        name=encoder_name,
    )

    if encoder_class:
        output_extension = encoder_class.output_extension
    else:
        can_continue = False

    try:
        format_module = importlib.import_module(
            name=f'.{ format_name }',
            package='mustup.plg.formats',
        )
    except ModuleNotFoundError:
        logger.error(
            'could not find module for format %s',
            format_name,
        )

        can_continue = False
    else:
        output_function = format_module.output

    playlist_manifest = load_playlist_manifest(
        path=manifest_path,
    )

    # FIXME: validate playlist manifest
    playlist_manifest_valid = True
    if not playlist_manifest_valid:
        can_continue = False

    if can_continue:
        output_function(
            extension=output_extension,
            manifest=playlist_manifest,
            output=output,
        )

        return_value = True
    else:
        return_value = False

    return return_value


def load_playlist_manifest(
            path,
        ):
    try:
        f = open(
            path,
            'r',
        )
    except FileNotFoundError:
        logger.error(
            'no file at specified path',
        )

        return_value = None
    else:
        logger.debug(
            'file opened successfully',
        )

        playlist_manifest = yaml.safe_load(
            f,
        )

        return_value = playlist_manifest

    return return_value
