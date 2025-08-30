from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    """使用するAIモデルに関する情報を一元管理します。"""

    NAME: str = "tsmatz/mt5_summarize_japanese"
    REVISION: str = "main"
