#!/usr/bin/env python3
import json
from random import randrange, choice
from datetime import datetime, timedelta

list_of_analyzers = ['R. Zhang',
                     'C. Milligan',
                     'K. Judkins',
                     'S. Chaves',
                     'C. Kight',
                     'B. Rossi',
                     'J. Maertz',
                     'F. Zhou',
                     'A. Mendoza',
                     'E. Oopsdonnell']


def date_range(start_datetime, end_datetime):
    while start_datetime < end_datetime:
        yield start_datetime
        start_datetime += timedelta(hours=1)


def calc_turbidity(calibration_constant, detector_current):
    return(calibration_constant*detector_current)


def main():

    with open('turbidity_data.json', 'r') as f:
        data = json.load(f)

    last_time = data['turbidity_data'][-1]['datetime']
    start_datetime = datetime.strptime(last_time, '%Y-%m-%d %H:%M') + timedelta(hours=1)
    end_datetime = datetime.now()

    for each_date in date_range(start_datetime, end_datetime):
        this_analyzer = choice(list_of_analyzers)
        detector_current = -1*(1.10+(randrange(100)/1000)) if this_analyzer == 'E. Oopsdonnell' else (1.10+(randrange(100)/1000))
        data['turbidity_data'].append( { 'datetime': each_date.strftime('%Y-%m-%d %H:%M'),
                                         'sample_volume': 1.15+(randrange(10)/100),
                                         'calibration_constant': 0.95+(randrange(100)/1000),
                                         'detector_current': detector_current,
                                         'analyzed_by': this_analyzer})

    with open('turbidity_data.json', 'w') as o:
        json.dump(data, o, indent=2)

    #for item in data['turbidity_data']:
    #    print(calc_turbidity(item['calibration_constant'], item['detector_current']))    


if __name__ == '__main__':
    main()



