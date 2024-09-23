from agipot.settings import OpenAISettings
from pytest import fixture

@fixture
def openai_settings():
    return OpenAISettings()

def test_openai_api_call(openai_settings):
    from openai import OpenAI
    client = OpenAI(api_key=openai_settings.openai_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, world!"}],
    )

    """
    ChatCompletion(
        id='chatcmpl-AAbaNo8CJz1oPYqomQ0bbtAVZMmii', 
        choices=[
            Choice(
            finish_reason='stop', 
            index=0, 
            logprobs=None, 
            message=ChatCompletionMessage(content='Hello! How can I assist you today?', refusal=None, role='assistant', function_call=None, tool_calls=None)
        )
            ], 
        created=1727091123, 
        model='gpt-3.5-turbo-0125',
        object='chat.completion', 
        service_tier=None, 
        system_fingerprint=None, 
        usage=CompletionUsage(
            completion_tokens=9, 
            prompt_tokens=11, 
            total_tokens=20, 
            completion_tokens_details=CompletionTokensDetails(reasoning_tokens=0)
        )
    )
    """
    print(response)

