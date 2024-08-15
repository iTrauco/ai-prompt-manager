from prompt_manager.lmm_interaction import send_prompt_to_llm

def test_send_prompt_to_llm():
    response = send_prompt_to_llm('test_prompt.txt')
    assert 'Error' not in response  # Replace with expected response check
