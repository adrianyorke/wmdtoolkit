try:
    from . import _version
    __version__ = _version.__version__
    __version_git__ = _version.__version_git__
except ImportError:
    __version__ = "0.0.0"
    __version_git__ = "0.0.0"
