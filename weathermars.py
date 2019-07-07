# -*- coding: utf-8 -*-

import sopel.module
import json
import urllib.request  as urllib2
from sopel.module import commands, example

degree_sign= u'\N{DEGREE SIGN}'

@commands('weathermars')
@example('.weathermars')
def weathermars(bot, trigger):
    weather_url = 'https://mars.nasa.gov/rss/api/?feed=weather&category=insight&feedtype=json&ver=1.0'
    weather_data = urllib2.urlopen(weather_url)
    data_json = json.load(weather_data)
    min_temp = data_json['200']['AT']['mn']
    max_temp = data_json['200']['AT']['mx']
    avg_temp = data_json['200']['AT']['av']
    min_speed = data_json['200']['HWS']['mn']
    max_speed = data_json['200']['HWS']['mx']
    avg_speed = data_json['200']['HWS']['av']
    wind_direction1 = data_json['200']['WD']['1']['compass_degrees']
    wind_direction2 = data_json['200']['WD']['1']['compass_point']
    bot.say('Temperature: (Avg) %.1f %sC (Min) %.1f %sC, (Max) %.1f %sC' % (avg_temp, degree_sign, min_temp, degree_sign, max_temp, degree_sign))
    bot.say('Horizontal Wind Speed: (Avg) %.1f %%m/s (Min) %.1f %%m/s, (Max) %.1f %%m/s' % (avg_speed, min_speed, max_speed))
    bot.say('NASA InSight Rover at Elysium Planitia, Mars - Wind Direction: %.f%s %s' % (wind_direction1, degree_sign, wind_direction2))
