# Thin shim — 所有元数据与配置均在 pyproject.toml 中（Sprint 62）。
# 保留 setup.py 是为了兼容 `python setup.py sdist bdist_wheel` 这种旧调用，
# setuptools.build_meta 会接管实际构建流程。
# 严禁在此文件添加 UploadCommand / cmdclass 等自定义命令，避免在 thin shim 下
# 通过 os.system("python setup.py ...") 产生递归调用（详见 Sprint 62 合约）。
from setuptools import setup

setup()
