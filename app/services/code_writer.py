from time import sleep
from openai import OpenAI
from app.utils.config import settings
from app.models.schemas import RequestInput
from loguru import logger
from app.models.schemas import ImageRequestInput


async def code_writing(request_object: RequestInput):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    logger.info('Writing Code Function Call')
    response = client.chat.completions.create(
        model=request_object.model,
        messages=request_object.message,
        temperature=request_object.temperature,
    )
    logger.info(response)

    new_response = response.choices[0].message.content
    sleep(60)
    return new_response


async def model_listing():
    logger.info('Model Listing Call')
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.models.list()
    logger.info(response)
    return response

async def image_generating(request_parameter: ImageRequestInput):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    logger.info('Image Generation Function Call with Parameters')
    logger.info(request_parameter)
    response = client.images.generate(
  model=request_parameter.model,
  prompt=request_parameter.prompt,
  size=request_parameter.size,
  quality=request_parameter.quality,
  n=request_parameter.n,
)
    logger.info(response)
    image_url = response.data[0].url
    revised_prompt = response.data[0].revised_prompt
    result = {
        'image_url': image_url,
        'prompt':revised_prompt
    }
    return result



