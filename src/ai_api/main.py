from typing import cast

import gradio as gr

from ai_api.config import ModelConfig
from ai_api.core.inference import Summarizer

# Summarizerのインスタンスをシングルトンとして管理
summarizer_instance: Summarizer | None = None


def get_summarizer() -> Summarizer:
    """Summarizerのインスタンスを一度だけ生成して返します。"""
    global summarizer_instance
    if summarizer_instance is None:
        config = ModelConfig()
        summarizer_instance = Summarizer(config=config)
    return summarizer_instance


def summarize_text(text: str) -> str:
    """推論を実行するためのトップレベル関数。"""
    summarizer = get_summarizer()
    # castを使って、戻り値がstrであることをMypyに明示的に伝える
    return cast(str, summarizer.summarize(text))


# Gradioインターフェースの定義
iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="要約したいテキストを入力してください..."),
    outputs="text",
    title="口コミ要約AI",
    description="入力されたテキスト（口コミ）をAIが分析し、要約を生成します。",
    api_name="predict",
)
