from time import sleep
from openai import OpenAI
from app.utils.config import settings
from app.models.schemas import RequestInput, ClaudeRequestInput
from loguru import logger
from app.models.schemas import ImageRequestInput
import anthropic_bedrock
from anthropic_bedrock import AsyncAnthropicBedrock


async def code_writing(request_object: RequestInput):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    logger.info('Writing Code Function Call')
    response = client.chat.completions.create(
        model=request_object.model,
        messages=request_object.message,
        temperature=request_object.temperature,
    )
    logger.info("Api Call Success")

    new_response = response.choices[0].message.content
    return new_response


async def model_listing():
    logger.info('Model Listing Call')
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.models.list()
    logger.info("Api Call Success")
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
    logger.info("Api Call Success")
    image_url = response.data[0].url
    revised_prompt = response.data[0].revised_prompt
    result = {
        'image_url': image_url,
        'prompt':revised_prompt
    }
    return result

async def code_writer_bedrock(request_object: ClaudeRequestInput):


    client = AsyncAnthropicBedrock(
    aws_access_key=settings.AWS_ACCESS_KEY_ID,
    aws_secret_key=settings.AWS_SECRET_ACCESS_KEY,
    aws_region=settings.REGION_NAME,
)

    completion = await client.completions.create(
    model=request_object.model,
    max_tokens_to_sample=4000,
    prompt=f"{anthropic_bedrock.HUMAN_PROMPT} {request_object.prompt} {anthropic_bedrock.AI_PROMPT}",
)
    response = completion.completion
    logger.info(response)
    return response



