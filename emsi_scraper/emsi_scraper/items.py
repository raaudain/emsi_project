import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import replace_tags, replace_entities


def clean_dict_text(value):
    header = value.get("text") if ":" in value.get("text") else value.get("text") + ":"
    content = value.get("content")
    content = replace_tags(content, " ")
    content = replace_entities(content)
    content = remove_white_space(content)
    details = f"{header} {content}"
    return {"content": details}

def remove_white_space(value):
    return " ".join(value.split())

class EmsiScraperItem(scrapy.Item):
    job_id = scrapy.Field(output_processor = TakeFirst())
    job_title = scrapy.Field(output_processor = TakeFirst())
    job_description = scrapy.Field(
        input_processor = MapCompose(remove_white_space), 
        output_processor = TakeFirst()
    )
    additional_job_details = scrapy.Field(input_processor = MapCompose(clean_dict_text))
    location = scrapy.Field(output_processor = TakeFirst())
    date_posted = scrapy.Field(output_processor = TakeFirst())
    department = scrapy.Field(output_processor = TakeFirst())
    team = scrapy.Field(output_processor = TakeFirst())
    commitment = scrapy.Field(output_processor = TakeFirst())
    job_posting_url = scrapy.Field(output_processor = TakeFirst())
