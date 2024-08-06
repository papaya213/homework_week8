from langchain.chains import LLMChain
from langchain_community.llms import ChatGLM
from langchain_core.prompts import PromptTemplate

# import os

from utils import LOG
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

class TranslationChain:
    def __init__(self, model_name: str = "chatglm2-6b", verbose: bool = True):
        
        template = """你是一个翻译专家，请将下文从{source_language}翻译为{target_language}. 需要翻译的文本如下： {text} """


        chat_prompt_template = ChatPromptTemplate.from_template(template)

        # 本地部署ChatGLM2-6B
        endpoint_url = "http://localhost:8000"

        # direct access endpoint in a proxied environment
        # os.environ['NO_PROXY'] = '127.0.0.1'

        chat = ChatGLM(
            endpoint_url=endpoint_url,
            max_token=80000,
            top_p=0.9,
            temperature=0,
            model_kwargs={"sample_model_args": False},
        )

        self.chain = LLMChain(llm=chat, prompt=chat_prompt_template, verbose=verbose)

    def run(self, text: str, source_language: str, target_language: str) -> (str, bool):
        result = ""
        try:
            result = self.chain.run({
                "text": text,
                "source_language": source_language,
                "target_language": target_language,
            })
        except Exception as e:
            LOG.error(f"An error occurred during translation: {e}")
            return result, False

        return result, True