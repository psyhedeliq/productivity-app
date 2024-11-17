import json
import time
from datetime import datetime, timedelta
from termcolor import cprint
import random
import os

# Get the absolute path to the config directory
CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')


def load_tasks():
    config_path = os.path.join(CONFIG_DIR, 'task.json')
    with open(config_path, 'r') as f:
        tasks = json.load(f)
    return tasks


def get_tasks_schedule(tasks):
    task_start_time = datetime.now()
    schedule = []
    for task, minutes in tasks.items():
        end_time = task_start_time + timedelta(minutes=minutes)
        schedule.append((task, task_start_time, end_time))
        task_start_time = end_time
    return schedule


def main():
    tasks = load_tasks()
    schedule = get_tasks_schedule(tasks)
    current_index = 0

    while True:
        now = datetime.now()
        current_task, start_time, end_time = schedule[current_index]
        remaining_time = end_time - now
        remaining_minutes = int(remaining_time.total_seconds() // 60)

        print('')

        for index, (task, s_time, e_time) in enumerate(schedule):
            if index < current_index:
                # task is completed
                print(f'{task} done: {e_time.strftime("%H:%M")}')
            elif index == current_index:
                # current task
                if remaining_minutes < 2:
                    cprint(f'{task} < 2m left!', 'white',
                           'on_red', attrs=['blink'])
                elif remaining_minutes < 5:
                    cprint(f'{task} - {remaining_minutes} mins',
                           'white', 'on_red')
                else:
                    cprint(f'{task} - {remaining_minutes} mins',
                           'white', 'on_blue')
            else:
                print(f'{task} - @ {s_time.strftime("%H:%M")}')

        list_of_reminders = ['I am grateful for my life and my family.',
                             'Time is irrelevant, keep swimming.', 'All I know is that I know nothing.', 'Every day I get better.', 'Rest at the end, not in the middle.', 'Everything happens for a reason.', 'Believe in yourself.', 'Supreme confidence.']

        random_reminder = random.choice(list_of_reminders)
        print('✨' + random_reminder + '✨')

        if now >= end_time:
            current_index += 1
            if current_index >= len(schedule):
                cprint('All tasks completed!', 'white',
                       'on_green', attrs=['blink'])
                break

        time.sleep(15)


main()
