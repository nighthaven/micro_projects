from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Weather:
    date: datetime
    details: str
    temp: str
    weather: list[dict]
    description: str

    def __str__(self):
        return f"[{self.date:%H:%M}] {self.temp}Cº ({self.description})"

