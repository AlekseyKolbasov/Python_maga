
import dataclasses
import datetime
from typing import Any

from services.files import interface_text


@dataclasses.dataclass
class WeatherInformation:
    date: datetime.datetime
    city_name: str
    weather_conditions: str
    temperature: int
    temperature_feels_like: int
    wind_speed: int

    def __str__(self) -> str:
        string_weather_info = (
                interface_text.SEPARATION_LINE +
                interface_text.CURRENT_TIME + str(self.date) +
                interface_text.CITY_NAME + str(self.city_name) +
                interface_text.WEATHER_CONDITIONS + str(self.weather_conditions) +
                interface_text.TEMPERATURE + str(self.temperature) + interface_text.CELSIUS +
                interface_text.TEMPERATURE_FEELS_LIKE + str(self.temperature_feels_like) + interface_text.CELSIUS +
                interface_text.WIND_SPEED + str(self.wind_speed) + interface_text.MS +
                interface_text.SEPARATION_LINE
        )
        return string_weather_info

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)
