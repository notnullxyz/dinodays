#!/usr/bin/python3

"""
    This file is part of dinodays.
    Copyright (c) 2019, Marlon B van der Linde, <marlonv@protonmail.com>

    dinodays is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    dinodays is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with dinodays.  If not, see <https://www.gnu.org/licenses/>.
"""

from sys import exit
import json
from src.ark.ark import Ark
from argparse import ArgumentParser


def run(real_life_mins, day_game_hours, night_game_hours):
    ark = Ark()
    day_cycle_speed_scale = ark.calc_day_cycle_speed_scale(real_life_mins)
    day_time_speed_scale = ark.calc_day_time_speed_scale(day_game_hours)
    night_time_speed_scale = ark.calc_night_time_speed_scale(night_game_hours)
    return dict(
        day_cycle_speed_scale=day_cycle_speed_scale,
        day_time_speed_scale=day_time_speed_scale,
        night_time_speed_scale=night_time_speed_scale
    )

def main():
    """ main entry point."""

    parser = ArgumentParser(description='Calculate the configuration values for speed scales in ARK servers')

    parser.add_argument('--json', default=False, action='store_true',
                        help='output results as json')
    parser.add_argument('desired_reallife_minutes', action='store', type=float,
                        help='The desired real-life minutes an in-game day should last')

    parser.add_argument('desired_day_hours_ingame', action='store', type=float,
                        help='The desired length of the day (sunlight) in \'in-game hours\'')

    parser.add_argument('desired_night_hours_ingame', action='store', type=float,
                        help='The desired length of the night (dark) in \'in-game hours\'',
                        )
    arguments = parser.parse_args()
    result = run(arguments.desired_reallife_minutes, arguments.desired_day_hours_ingame,
                 arguments.desired_night_hours_ingame)

    if arguments.json:
        print(json.dumps(result))
    else:
        print("Day Cycle Speed Scale: " + str(result['day_cycle_speed_scale']))
        print("Day Time Speed Scale: " + str(result['day_time_speed_scale']))
        print("Night Time Speed Scale: " + str(result['night_time_speed_scale']))


if __name__ == '__main__':
    exit(main())
