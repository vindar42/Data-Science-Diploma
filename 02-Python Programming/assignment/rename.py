import os
import random
import time

def show_universe_people(place):
    people = os.listdir(place)
    return people

def thanos_snap(universe):
    half_of_universe = len(universe)
    for i in range(half_of_universe):
        universe = show_universe_people('../code/Project 1 - Thanos/backup')
        random_victim = random.choice(universe)
        #os.remove(f'../code/Project 1 - Thanos/universe/{random_victim}')
        old_path = os.path.join('../code/Project 1 - Thanos/backup', random_victim)
        new_path = os.path.join('../code/Project 1 - Thanos/universe', ''.join([random.choice('abcdefghijklmnopqrstuvwxyz'), '.jpg']))
        rename_file = os.rename(old_path, new_path)
        time.sleep(1)
        print(f"Destroying: ../code/Project 1 - Thanos/{random_victim}")
    print('Perfectly balanced, as all things should be')

universe = show_universe_people('../code/Project 1 - Thanos/backup')
print(universe)

thanos_snap(universe)
