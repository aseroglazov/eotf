from logging import \
    Handler, \
    LogRecord, \
    DEBUG, \
    getLogger, \
    StreamHandler, \
    Formatter

from eotf.figures import Figure
from eotf.plugins import DebugVisualizerPlugin


class VisualizeHandler(Handler):
    def emit(self, record: LogRecord) -> None:
        for arg in record.args:
            if not isinstance(arg, Figure):
                continue
            DebugVisualizerPlugin.add(arg)


def filter_debug(record: LogRecord) -> bool:
    return record.levelno <= DEBUG


def setup_logging(name: str, level: int = DEBUG) -> None:
    logger = getLogger(name=name)
    logger.setLevel(level)

    visualization_handler = VisualizeHandler()
    visualization_handler.addFilter(filter_debug)
    logger.addHandler(visualization_handler)

    stream_handler = StreamHandler()
    stream_handler.setFormatter(Formatter('[%(asctime)s: %(name)s: %(levelname)s] %(message)s'))
    logger.addHandler(stream_handler)
