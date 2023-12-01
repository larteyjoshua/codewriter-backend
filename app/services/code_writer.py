from openai import OpenAI
from app.utils.config import settings
from app.models.schemas import RequestInput
from loguru import logger
from app.models.schemas import ImageRequestInput


async def code_writing(request_object: RequestInput):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    logger.info('Writing Code Function Call')
    response = client.chat.completions.create(
        model=settings.TEXT_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": request_object.prompt},
        ],
        temperature=settings.TEMPERATURE,
    )
    logger.info(response)

    new_response = response.choices[0].message.content
    return new_response


async def model_listing():
    logger.info('Model Listing Call')
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.models.list()
    logger.info(response)
    return response

async def image_generating(request_parameter: ImageRequestInput):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    logger.info('Image Generation Function Call')
    response = client.images.generate(
  model=settings.IMAGE_MODEL,
  prompt=request_parameter.prompt,
  size=settings.IMAGE_SIZE,
  quality=settings.IMAGE_QUALITY,
  n=settings.NUMBER_IMAGE,
)
    logger.info(response)
    image_url = response.data[0].url
    revised_prompt = response.data[0].revised_prompt
    result = {
        'image_url': image_url,
        'prompt':revised_prompt
    }
    return result


