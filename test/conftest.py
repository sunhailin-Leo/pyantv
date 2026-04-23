"""pytest 配置文件，包含 Hypothesis profile 设置。"""

import os

from hypothesis import settings


# 注册 Hypothesis profile
# dev profile: 快速反馈，本地开发默认使用
settings.register_profile(
    "dev",
    max_examples=20,
    deadline=None,
)

# ci profile: CI 环境使用，derandomize=True 保证结果稳定
settings.register_profile(
    "ci",
    max_examples=100,
    derandomize=True,
    deadline=None,
)

# exhaustive profile: 发布前全量检查
settings.register_profile(
    "exhaustive",
    max_examples=1000,
    deadline=None,
)

# 通过环境变量选择 profile，默认 dev
profile_name = os.environ.get("HYPOTHESIS_PROFILE", "dev")
settings.load_profile(profile_name)
