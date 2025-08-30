from typing import cast

from transformers import T5ForConditionalGeneration, T5Tokenizer

from ai_api.config import ModelConfig


class Summarizer:
    """
    AIモデルを管理し、テキスト要約を実行するクラス。
    """

    def __init__(self, config: ModelConfig) -> None:
        self.config = config
        # __init__で一度だけtokenizerとmodelを初期化
        self.tokenizer = T5Tokenizer.from_pretrained(
            self.config.NAME, revision=self.config.REVISION
        )
        self.model = T5ForConditionalGeneration.from_pretrained(
            self.config.NAME, revision=self.config.REVISION
        )

    def summarize(self, text: str) -> str:
        """
        与えられたテキストを要約する。
        """
        # 保持しているtokenizerとmodelを使って要約
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        output_ids = self.model.generate(
            input_ids, max_length=50, min_length=10, do_sample=False
        )
        summary = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return cast(str, summary)
