# import requests
# import json

# # url = f"https://api.chucknorris.io/jokes/random"
# # r = requests.get(url).json()
# # joke = r['value']
# # thumb = r['icon_url']


# # print(thumb)

# r = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
# c = r.json()
# data = c['data']

# update_date_time = data['update_date_time']
# local_new_cases = data['local_new_cases']
# local_total_cases = data['local_total_cases']
# local_total_number_of_individuals_in_hospitals = data['local_total_number_of_individuals_in_hospitals']
# local_deaths = data['local_deaths']
# local_new_deaths = data['local_new_deaths']
# local_recovered = data['local_recovered']
# local_active_cases = data['local_active_cases']

# global_new_cases = data['global_new_cases']
# global_total_cases = data['global_total_cases']
# global_deaths = data['global_deaths']
# global_new_deaths = data['global_new_deaths']
# global_recovered = data['global_recovered']
# total_pcr_testing_count = data['total_pcr_testing_count']
# total_antigen_testing_count = data['total_antigen_testing_count']


# print(total_antigen_testing_count)

import json

def get_sever_prefix_hirusha():
    with open("prefixes.json", 'r') as f:
        prefixes = json.load(f)

    print(prefixes["819131810822357023"])
#   return prefixes.get("819131810822357023")


get_sever_prefix_hirusha()




