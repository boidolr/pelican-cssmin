"""Pelican plugin to use `rcssmin` to minify CSS files."""

import logging

from pelican import signals

try:
    import rcssmin
except ImportError:
    rcssmin = None


def _identity(script):
    return script


def add_jinja2_ext(pelican):
    """Add Webassets to Jinja2 extensions in Pelican settings."""
    minifier = rcssmin.cssmin if rcssmin else _identity
    pelican.env.filters.update({"cssmin": minifier})


def register():
    """Plugin registration."""
    if rcssmin is None:
        logger = logging.getLogger(__name__)
        logger.warning("failed to load 'rcssmin' dependencies")

    signals.generator_init.connect(add_jinja2_ext)
