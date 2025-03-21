import morph
from morph import MorphGlobalContext
from openai import OpenAI

@morph.func
def chat(context: MorphGlobalContext):
  client = OpenAI()
  stream = client.responses.create(
    model="gpt-4o",
    tools=[{"type": "web_search_preview"}],
    input=context.vars["prompt"],
    stream=True
  )
  for event in stream:
    if (event.type == 'response.output_text.delta'):
      yield event.delta
