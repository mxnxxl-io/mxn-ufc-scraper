import requests
from bs4 import BeautifulSoup

url = "https://www.ufc.com/athlete/islam-makhachev"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#NAME
name_val = soup.find(class_ = "hero-profile__name")
print(f'Name: {name_val.text}')

#RECORD
record_val = soup.find(class_ = "hero-profile__division-body")
print(f'Record: {record_val.text}')

#winbycontainer
winbycontainer = soup.find_all(class_ = "athlete-stats__text athlete-stats__stat-numb")
print(f'Fight win streak: {winbycontainer[0].text}')
print(f'Wins by KO: {winbycontainer[1].text}')
print(f'Wins by Submission: {winbycontainer[2].text}')

#Striking and Takedown container
strk_tkdn_container = soup.find_all(class_ = "c-overlap__stats-value")
print(f'Significant Strikes Landed: {strk_tkdn_container[0].text}')
print(f'Significant Strikes Attempted: {strk_tkdn_container[1].text}')
print(f'Takedowns Landed: {strk_tkdn_container[2].text}')
print(f'Takedowns Attempted: {strk_tkdn_container[3].text}')

#Strikes and takedown defense / absorption container
strk_tkdn_def_abs_container = soup.find_all(class_ = "c-stat-compare__number")
print(f'Significant Strike Landed: {strk_tkdn_def_abs_container[0].text}')
print(f'Significant Strike Absorbed: {strk_tkdn_def_abs_container[1].text}')
print(f'Takedown avg: {strk_tkdn_def_abs_container[2].text}')
print(f'Submission avg: {strk_tkdn_def_abs_container[3].text}')
print(f'Significant Strike Defense: {"".join(strk_tkdn_def_abs_container[4].text.split())}')
print(f'Takedown Defense: {"".join(strk_tkdn_def_abs_container[5].text.split())}')
print(f'Knockdown avg: {strk_tkdn_def_abs_container[6].text}')
print(f'Average Fight Time: {strk_tkdn_def_abs_container[7].text}')

#Strikes by position
strk_pos_container = soup.find_all(class_ = "c-stat-3bar__value")
print(f'Strikes landed standing: {strk_pos_container[0].text}')
print(f'Strikes landed clinch: {strk_pos_container[1].text}')
print(f'Strikes landed ground: {strk_pos_container[2].text}')

#win by method
print(f'Wins by KO/TKO: {strk_pos_container[3].text}')
print(f'Wins by Decision: {strk_pos_container[4].text}')
print(f'Wins by Submission: {strk_pos_container[5].text}')

#Strikes total
print(f'Strikes landed head: {soup.find(id="e-stat-body_x5F__x5F_head_value").text}')
print(f'Strikes landed body: {soup.find(id="e-stat-body_x5F__x5F_body_value").text}')
print(f'Strikes landed leg: {soup.find(id="e-stat-body_x5F__x5F_leg_value").text}')
