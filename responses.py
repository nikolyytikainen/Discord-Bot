import random
import requests
from dotenv import load_dotenv
import os
# Lataa .env-tiedoston muuttujat
load_dotenv()

# Globaalit muuttujat
blue = 0
purple = 0
pink = 0
red = 0
gold = 0
casecounter = 0
# Faceit apiurl
FACEIT_API_KEY = os.getenv('faceitApiKey')
FACEIT_API_URL = "https://open.faceit.com/data/v4/"

# Faceit-tilastojen haku
def get_faceit_stats(username):
    headers = {
        "Authorization": f"Bearer {FACEIT_API_KEY}"
    }
    user_response = requests.get(FACEIT_API_URL + f"players?nickname={username}", headers=headers)
    
    if user_response.status_code != 200:
        return None

    user_data = user_response.json()
    player_id = user_data['player_id']
    avatar = user_data['avatar']
    elo = user_data.get('games', {}).get('cs2', {}).get('faceit_elo', 'Not Available')

    stats_response = requests.get(FACEIT_API_URL + f"players/{player_id}/stats/cs2", headers=headers)

    if stats_response.status_code != 200:
        return None

    stats_data = stats_response.json()
    stats_data['elo'] = elo  # Lisätään elo ja avatar stats_dataan
    stats_data['avatar'] = avatar
    return stats_data



# Komennot
def register_commands(bot):
    @bot.command(name="faceitstats")
    async def faceitstats_command(ctx, username: str):
        stats = get_faceit_stats(username)

        if stats is None:
            await ctx.send("Can not find the user.")
            return

        win_rate = stats['lifetime'].get('Win Rate %', 'Not Available')
        matches = stats['lifetime'].get('Matches', 'Not Available')
        kd_ratio = stats['lifetime'].get('Average K/D Ratio', 'Not Available')
        elo = stats.get('elo', 'Not Available')
        recentresults = stats['lifetime'].get('Recent Results', 'Not Available')
        avatar = stats.get('avatar', 'Not Available')
        
        #muuttaa pelien tulokset emojeiksi W tai L
        mapped_results = [":regional_indicator_w:" if r == "1" else ":regional_indicator_l:" for r in recentresults]
        formatted_results = ' '.join(mapped_results)

        message = (
            f"Stats for the user **{username}**:\n"
            f"ELO: {elo}\n"
            f"Winrate: {win_rate}%\n"
            f"Matches: {matches}\n"
            f"K/D Ratio: {kd_ratio}\n"
            f"Recent Results: {formatted_results}\n"
            f"Avatar: {avatar}\n"
        )

        await ctx.send(message)

    
    @bot.command(name="faceitfinder")
    async def faceitfinder_command(ctx, steam_url: str):
        
        steam_id_64 = steam_url.split("/")[-1]
        if not steam_id_64:
            await ctx.send("Invalid Steam profile URL or failed to resolve Steam ID 64.")
            return "Invalid Steam profile URL or failed to resolve Steam ID 64."
    
        headers = {"Authorization": f"Bearer {FACEIT_API_KEY}"}
        faceit_url = FACEIT_API_URL + f"players?game=csgo&game_player_id={steam_id_64}"
        response = requests.get(faceit_url, headers=headers)
    
        if response.status_code != 200 and response.status_code != 404:
            await ctx.send(f"Error while finding the account, Error: {response.status_code} - {response.json().get('message')}")
            return f"Error: {response.status_code} - Viesti: {response.json().get('message')}"
        elif response.status_code == 404:
            await ctx.send(f"Error while finding the account, Error: {response.status_code} account can not be found or steamcommunity link does not have Steam ID 64. Message: - {response.json().get('message')}")
            return f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}"
        player_data = response.json()
        faceit_username = player_data.get("nickname")

        stats = get_faceit_stats(faceit_username)

        if stats is None:
            await ctx.send("Can not find the user.")
            return

        win_rate = stats['lifetime'].get('Win Rate %', 'Not Available')
        matches = stats['lifetime'].get('Matches', 'Not Available')
        kd_ratio = stats['lifetime'].get('Average K/D Ratio', 'Not Available')
        elo = stats.get('elo', 'Not Available')
        recentresults = stats['lifetime'].get('Recent Results', 'Not Available')
        avatar = stats.get('avatar', 'Not Available')
        
        #muuttaa pelien tulokset emojeiksi W tai L
        mapped_results = [":regional_indicator_w:" if r == "1" else ":regional_indicator_l:" for r in recentresults]
        formatted_results = ' '.join(mapped_results)

        message = (
            f"Stats for the user **{faceit_username}**:\n"
            f"ELO: {elo}\n"
            f"Winrate: {win_rate}%\n"
            f"Matches: {matches}\n"
            f"K/D Ratio: {kd_ratio}\n"
            f"Recent Results: {formatted_results}\n"
            f"Avatar: {avatar}\n"
        )
        await ctx.send(message)


    @bot.command(name="komennot")
    async def komennot_command(ctx):
        await ctx.send(
            "Saatavilla olevat komennot:\n"
            "`!faceitstats käyttäjänimi\n"
            "!terve\n"
            "!noppa\n"
            "!kolikko\n"
            "!casesimu\n"
            "!casestats\n"
            "!faceitfinder`"
        )

    @bot.command(name="terve")
    async def terve_command(ctx):
        await ctx.send("Terve vain!")

    @bot.command(name="noppa")
    async def noppa_command(ctx):
        await ctx.send(str(random.randint(1, 6)))

    @bot.command(name="kolikko")
    async def kolikko_command(ctx):
        kolikko = str(random.randint(1, 2))
        result = "Kruuna" if kolikko == "1" else "Klaava"
        await ctx.send(result)

    @bot.command(name="casesimu")
    async def casesimu_command(ctx):
        global blue, purple, pink, red, gold, casecounter

        rand_num = random.random() * 100
        if rand_num < 79.92:
            blue += 1
            casecounter += 1
            await ctx.send("Sininen skini avattu!")
        elif rand_num < 79.92 + 15.98:
            purple += 1
            casecounter += 1
            await ctx.send("Violetti skini avattu!")
        elif rand_num < 79.92 + 15.98 + 3.2:
            pink += 1
            casecounter += 1
            await ctx.send("Pinkki skini avattu!")
        elif rand_num < 79.92 + 15.98 + 3.2 + 0.64:
            red += 1
            casecounter += 1
            await ctx.send("Punainen skini avattu!")
        else:
            gold += 1
            casecounter += 1
            await ctx.send("Kultainen skini avattu!")

    @bot.command(name="casestats")
    async def casestats_command(ctx):
        global blue, purple, pink, red, gold, casecounter
        await ctx.send(
            f"Laatikoita avattu: {casecounter}\n"
            f"Sinisiä: {blue}\n"
            f"Violettejä: {purple}\n"
            f"Pinkkejä: {pink}\n"
            f"Punaisia: {red}\n"
            f"Kultaisia: {gold}"
        )

    

