import datetime
import requests
import random
import json

def gen_log(nums):
    start_time = datetime.datetime.now().replace(microsecond=0) - datetime.timedelta(seconds=nums)
    log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    cpp_files = [chr(i) + '.cpp' for i in range(ord('a'), ord('z') + 1)]
    func_names = [str(cpp_files[i])[:-4] + '_func_' + str(j) for i in range(len(cpp_files)) for j in range(1, 20)]
    infos = [requests.get('https://api.quotable.io/quotes/random').json()[0].get('content') for _ in range(10)]
    users = [requests.get('https://random-data-api.com/api/v2/users').json() for _ in range(10)]

    for i in range(nums):
        time = start_time + datetime.timedelta(seconds=i)
        time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        log_level = random.choice(log_levels)
        cpp_file = random.choice(cpp_files)
        func_name = random.choice(func_names)
        line_num = random.randint(1, 1000)
        info = random.choice(infos)

        log = f'{time_str} [{log_level}] {cpp_file}:{func_name}:{line_num} {info}'
        print(log)

        if random.random() < 0.2:
            user = random.choice(users)
            user = json.dumps(user, indent=4)
            print(user)

if __name__ == '__main__':
    gen_log(100000)
