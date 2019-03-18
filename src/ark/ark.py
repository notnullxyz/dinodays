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


class Ark:
    """
    Ark Specific Stuff, like the known formulas.
    Defaults were correct when this script was written.
    """

    ARK_STANDARD_DAY_MINUTES = 50.675
    ARK_DEFAULT_DAYTIME_HOURS = 16.5
    ARK_DEFAULT_NIGHTTIME_HOURS = 7.5

    def calc_day_cycle_speed_scale(self, real_life_minutes_desired: float):
        return self.ARK_STANDARD_DAY_MINUTES / real_life_minutes_desired

    def calc_day_time_speed_scale(self, in_game_hours_desired: float):
        return 1.0 + (1.0 - (in_game_hours_desired / self.ARK_DEFAULT_DAYTIME_HOURS))

    def calc_night_time_speed_scale(self, in_game_hours_desired: float):
        return 1.0 + (1.0 - (in_game_hours_desired / self.ARK_DEFAULT_NIGHTTIME_HOURS))
