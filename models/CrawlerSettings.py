from pydantic import BaseModel


class CrawlerSettings(BaseModel):
    start_id: int
    num_pages: int

