# AI 大模型应用开发实战营 -- 第八周作业

## 实现功能：
    基于 ChatGLM2-6B 实现带图形化界面的 openai-translator。该实现基于课程内容langchain的openai-translator修改，将后台模型改为本地部署的[ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)。
## 运行方法：
    1. 运行ChatGLM2-6B提供的api。如hugging face直接拉取模型有困难，需要将模型改为本地路径。当前默认访问本地默认服务端口8000:
        ChatGLM2-6B> python api.py
    2. 运行openai-translator的web UI。
        openai-translator> python ai_translator\gradio_server.py
    3. 将文件拖拽或者选择上传到系统，在翻译完成后下载翻译文件。
