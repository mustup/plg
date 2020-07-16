import argparse
import logging
import sys

import mustup.plg.cli.argparsing.types.logging_level

logger = logging.getLogger(
    __name__,
)


def set_up(
            default_logging_level,
            default_encoder=None,
        ):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    arg_encoder_kwargs = {
    }

    if default_encoder:
        arg_encoder_kwargs['default'] = default_encoder

    encoder_arg_required = not bool(
        default_encoder,
    )

    parser.add_argument(
        '-e',
        '--encoder',
        dest='encoder',
        help='encoder module to use',
        metavar='ENCODER',
        required=encoder_arg_required,
        **arg_encoder_kwargs,
    )

    parser.add_argument(
        '-f',
        '--format',
        dest='format',
        help='playlist format',
        metavar='TEXT',
    )

    parser.add_argument(
        '-l',
        '--logging-level',
        default=default_logging_level,
        dest='logging_level',
        help='logging level',
        type=mustup.plg.cli.argparsing.types.logging_level.parser,
        metavar='PYTHON_LOGGING_LEVEL',
    )

    parser.add_argument(
        '-m',
        '--manifest',
        dest='manifest',
        help='path to the playlist manifest',
        metavar='PATH',
        required=True,
    )

    parser.add_argument(
        '-o',
        '--output',
        default=sys.stdout,
        dest='output',
        help='path to which to write the generated playlist',
        metavar='PATH',
        type=argparse.FileType(
            'w',
        ),
    )

    return parser
