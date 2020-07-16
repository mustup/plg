import logging

import mustup.plg.cli.argparsing
import mustup.plg.cli.logging
import mustup.plg.main
import mustup.tup.vardict

logger = logging.getLogger(
    __name__,
)


def entry_point(
        ):
    default_arguments = {
    }

    try:
        vardict = mustup.tup.vardict.load(
        )
    except mustup.tup.errors.NotUnderTup:
        default_logging_level = logging.DEBUG
    else:
        default_logging_level = logging.INFO

        try:
            encoder_name = vardict['ENCODER']
        except KeyError:
            logger.warning(
                'CONFIG_ENCODER not set; --encoder may be specified, but the @-variable would be better',
            )
        else:
            default_arguments['default_encoder'] = encoder_name

    parser = mustup.plg.cli.argparsing.set_up(
        default_logging_level=default_logging_level,
        **default_arguments,
    )

    args = parser.parse_args(
    )

    logging_level = args.logging_level

    mustup.plg.cli.logging.set_up(
        level=logging_level,
    )

    mustup.plg.main.output_playlist(
        encoder_name=encoder_name,
        format_name=args.format,
        manifest_path=args.manifest,
        output=args.output,
    )
