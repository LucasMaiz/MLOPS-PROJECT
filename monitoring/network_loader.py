import time
import requests

test_predict = {
  "params" : {
    "title" : "Cowboy Bebop",
    "synopsis":"""In the year 2071, humanity has colonized several of the planets and moons of the solar system leaving the now uninhabitable surface of planet Earth behind. The Inter Solar System Police attempts to keep peace in the galaxy, aided in part by outlaw bounty hunters, referred to as "Cowboys." The ragtag team aboard the spaceship Bebop are two such individuals. \r\n  \r\nMellow and carefree Spike Spiegel is balanced by his boisterous, pragmatic partner Jet Black as the pair makes a living chasing bounties and collecting rewards. Thrown off course by the addition of new members that they meet in their travels—Ein, a genetically engineered, highly intelligent Welsh Corgi; femme fatale Faye Valentine, an enigmatic trickster with memory loss; and the strange computer whiz kid Edward Wong—the crew embarks on thrilling adventures that unravel each member\'s dark and mysterious past little by little. \r\n \r\nWell-balanced with high density action and light-hearted comedy,  Cowboy Bebop  is a space Western classic and an homage to the smooth and improvised music it is named after. \r\n \r\n[Written by MAL Rewrite]""",
    "type":"TV",
    "genders":"['Action', 'Adventure', 'Comedy', 'Drama', 'Sci-Fi', 'Space']",
    "producers":"['Bandai Visual']",
    "studio":"['Sunrise']",
  },
  "result" : 7.7
}

i = 0

while True:
    i += 1
    if i%10==0:
        requests.post('http://localhost:5000/')
    else:
        requests.post('http://localhost:5000/', json=test_predict["params"])
    time.sleep(4)