# 此文件由 setuptools-scm 自动生成，请勿手动编辑。
# 在开发环境中，版本号从 git tag 自动派生。
# 在 sdist/wheel 中，版本号由构建时写入。
try:
    from setuptools_scm import get_version
    __version__ = get_version(root="..", relative_to=__file__)
except Exception:
    try:
        from importlib.metadata import version
        __version__ = version("pyantv")
    except Exception:
        __version__ = "0.1.0"  # fallback
