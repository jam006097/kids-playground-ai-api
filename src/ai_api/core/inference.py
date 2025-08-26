from typing import cast

from transformers import pipeline

from ai_api.config import ModelConfig


class Summarizer:
    """
    AIモデルを管理し、テキスト要約を実行するクラス。
    """

    def __init__(self, config: ModelConfig) -> None:
        self.config = config
        # __init__で一度だけpipelineを初期化
        self.summarizer = pipeline(
            "summarization",
            model=self.config.NAME,
            revision=self.config.REVISION,
        )

    def summarize(self, text: str) -> str:
        """
        与えられたテキストを要約する。
        """
        # 保持しているsummarizerを使って要約
        result = self.summarizer(text)
        return cast(str, result[0]["summary_text"])