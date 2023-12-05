
import datetime
from typing import Any
from .app_errors import error_handler
from .storage_weather_data import remembering_data_weather
from services.app_classes.weather_info import WeatherInformation


def processing_weather_data(weather_data: Any) -> WeatherInformation:
    processed_weather_data = parse_weather_data(weather_data)
    remembering_data_weather(processed_weather_data)
    return processed_weather_data


def parse_weather_data(weather_data: Any) -> WeatherInformation:
    date_request = make_datetime_object(weather_data["dt"], weather_data["timezone"])
    weather_parsing_data = {
        'date': date_request,
        'city_name': weather_data['name'],
        'weather_conditions': weather_data['weather'][0]['description'],
        'temperature': int(weather_data['main']['temp']),
        'temperature_feels_like': int(weather_data['main']['feels_like']),
        'wind_speed': int(weather_data['wind']['speed'])
    }
    weather_information = WeatherInformation(**weather_parsing_data)
    return weather_information


@error_handler
def make_datetime_object(request_time: str, offset_from_utc: str) -> datetime.datetime:
    timezone = datetime.timezone(datetime.timedelta(seconds=float(offset_from_utc)))
    return datetime.datetime.fromtimestamp(float(request_time), timezone)
