from ai_api.config import ModelConfig
from ai_api.core.inference import Summarizer


def test_summarizer_initialization_with_test_model() -> None:
    """
    テスト用の軽量モデルでSummarizerが初期化できることをテストする。
    """
    # Arrange: テスト専用の軽量モデルを指定
    config = ModelConfig(NAME="megagonlabs/t5-base-japanese-web", REVISION="main")

    # Act: 実際にモデルをロードして初期化
    summarizer = Summarizer(config=config)

    # Assert
    assert isinstance(summarizer, Summarizer)


def test_summarize_with_test_model() -> None:
    """
    テスト用の軽量モデルでsummarizeメソッドが動作することをテストする。
    """
    # Arrange: テスト専用の軽量モデルを指定
    config = ModelConfig(NAME="megagonlabs/t5-base-japanese-web", REVISION="main")
    summarizer = Summarizer(config=config)
    text = "This is a test sentence. It is a very nice sentence to summarize."

    # Act: 実際に要約を実行
    summary = summarizer.summarize(text)

    # Assert: 要約結果が文字列であり、空でないことを確認
    assert isinstance(summary, str)
    assert len(summary) > 0
