# dinodays

This is, for now, just equipped with the ability to do calculations for the day speed cycle values in the config.

Eventually and hopefully, it would be able to generate config values for most of the multipliers.

The Ark server configuration expects three values to control how long days are in the game, including the daylight and night hours.
The default is 28minutes of real-time for 24 hours of in-game time. Day times are defaulted to 14 mins, with the rest being night hours.

To change this, the speed scales can be configured with values that make sense. This tool will help with that!


## Author
Marlon B van der Linde <marlonv@protonmail.com>


## Usage

Generally run with python3 main.py... 

For Linux and assuming /usr/bin/python3 & chmod +x of main.py:

```
./main.py 90 20 4 --json
{"day_time_speed_scale": 0.7878787878787878, "day_cycle_speed_scale": 0.5630555555555555, "night_time_speed_scale": 1.4666666666666668}

```

Given the inputs:
- 90 as the desired real-life minutes an in-game day should last,
- 20 as the desired in-game hours of daylight (day time)
- 4 as the desired in-game hours of night (night time)

Outputs are given as the scales expected in the Ark server configs.

Omit --json to get a standard output.

## License
See file COPYING

tldr; 
GNU GENERAL PUBLIC LICENSE v3

```
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
```
