from openai import OpenAI
#ur key and usrl u wanna use
client = OpenAI(
  base_url = "",
  api_key="")

def get_response(prompt):

    content = ""
    completion = client.chat.completions.create(
        model=""
#we using llama 3.3 70b,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        top_p=1,
        max_tokens=4096,
        stream=True
    )
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content += chunk.choices[0].delta.content
    return content
