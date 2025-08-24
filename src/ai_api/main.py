import gradio as gr

def greet(name):
    """
    名前を受け取り、挨拶文を返す簡単な関数。
    """
    return "Hello, " + name + "!"

# Gradioインターフェースの定義
iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# スクリプトとして実行された場合にUIを起動
if __name__ == "__main__":
    iface.launch()