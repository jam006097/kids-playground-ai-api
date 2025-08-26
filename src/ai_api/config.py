from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    """使用するAIモデルに関する情報を一元管理します。"""

    NAME: str = "llm-jp/t5-small-japanese-finetuned-sum"
    REVISION: str = "main"
