"""
Ark Specific Stuff, like the known formulas.
Defaults were correct when this script was written.
"""


class Ark:

    ARK_STANDARD_DAY_MINUTES = 50.675
    ARK_DEFAULT_DAYTIME_HOURS = 16.5
    ARK_DEFAULT_NIGHTTIME_HOURS = 7.5

    def calc_day_cycle_speed_scale(self, real_life_minutes_desired: float):
        return self.ARK_STANDARD_DAY_MINUTES / real_life_minutes_desired

    def calc_day_time_speed_scale(self, in_game_hours_desired: float):
        return 1.0 + (1.0 - (in_game_hours_desired / self.ARK_DEFAULT_DAYTIME_HOURS))

    def calc_night_time_speed_scale(self, in_game_hours_desired: float):
        return 1.0 + (1.0 - (in_game_hours_desired / self.ARK_DEFAULT_NIGHTTIME_HOURS))
