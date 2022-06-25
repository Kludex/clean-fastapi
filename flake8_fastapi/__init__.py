try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore[no-redef]

__version__ = importlib_metadata.version(__name__)
