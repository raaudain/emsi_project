import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import replace_tags, replace_entities


def clean_dict_text(value):
    text = value.get("text")
    content = value.get("content")
    text = remove_white_spaces(text)
    text = replace_bad_chars(text)
    content = replace_tags(content, " ")
    content = replace_entities(content)
    content = remove_white_spaces(content)
    content = replace_bad_chars(content)
    return {"header": text, "content": content}


def remove_white_spaces(value):
    return " ".join(value.split())


def replace_bad_chars(value):
    value = value.replace("’", "\'")
    value = value.replace("●", "-")
    value = value.replace("·", "-")
    value = value.replace('“', '\'')
    value = value.replace('”', '\'')
    value = value.replace("…", "...")
    value = value.replace("–", "--")
    return value


class EmsiScraperItem(scrapy.Item):
    job_id = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces), output_processor=TakeFirst())
    job_title = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces), output_processor=TakeFirst())
    job_description = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces, replace_bad_chars), output_processor=TakeFirst())
    additional_job_details = scrapy.Field(
        input_processor=MapCompose(clean_dict_text))
    location = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces), output_processor=TakeFirst())
    date_posted = scrapy.Field(output_processor=TakeFirst())
    department = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces), output_processor=TakeFirst())
    team = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces), output_processor=TakeFirst())
    commitment = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces), output_processor=TakeFirst())
    job_posting_url = scrapy.Field(input_processor=MapCompose(
        remove_white_spaces), output_processor=TakeFirst())
