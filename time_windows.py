from datetime import (
    date,
    datetime,
    time,
    timedelta,
)
from pprint import pprint


def add_times(time_point: time, delta: timedelta) -> time:
    '''Прибавить отрезок времени delta к данному моменту времени time_point.'''
    return (datetime.combine(date(1, 1, 1), time_point) + delta).time()


start_at = '09:00'
finish_at = '21:00'
window_duration_in_minutes = 30
busy_windows = [
    {
        'start': '10:30',
        'stop': '10:50'
    },
    {'start': '18:40',
     'stop': '18:50'
     },
    {
        'start': '14:40',
        'stop': '15:50'
    },
    {
        'start': '16:40',
        'stop': '17:20'
    },
    {
        'start': '20:05',
        'stop': '20:20'
    }
]

start_day_at = time.fromisoformat(start_at)
finish_day_at = time.fromisoformat(finish_at)
delta = timedelta(minutes=window_duration_in_minutes)
busy_timeformat = [
    {
        'start': time.fromisoformat(window['start']),
        'stop': time.fromisoformat(window['stop'])
    } for window in busy_windows
]
busy_timeformat.sort(key=lambda x: x['start'])

free_time_windows = []
start_window_at = start_day_at
finish_window_at = add_times(start_window_at, delta)
i = 1

while finish_window_at <= finish_day_at:

    if len(busy_timeformat):
        next_busy_window_start, next_busy_window_finish = busy_timeformat[0].values()
        if finish_window_at > next_busy_window_start:
            start_window_at = next_busy_window_finish
            finish_window_at = add_times(start_window_at, delta)
            busy_timeformat.pop(0)
            continue
    free_time_windows.append(
        {
            f'work_window {i}': f"start: {start_window_at.isoformat('minutes')} "
                               f"finish: {finish_window_at.isoformat('minutes')}"
        }
    )

    start_window_at = finish_window_at
    finish_window_at = add_times(start_window_at, delta)
    i += 1

pprint(free_time_windows)
