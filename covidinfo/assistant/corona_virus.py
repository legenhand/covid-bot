import os
import shutil
from datetime import datetime

import requests
from covid import Covid
from pyrogram import Filters, InlineKeyboardButton, InlineKeyboardMarkup

from covidinfo import setbot


@setbot.on_message(Filters.command("corona") | Filters.command("corona@coronainfo19bot"))
async def corona(client, message):
    args = message.text.split(None, 1)
    if len(args) == 1:
        await message.reply("`usage: /corona (country)`")
        return
    covid = Covid()
    data = covid.get_data()
    country = args[1]
    country_data = get_country_data(country.capitalize(), data)
    if country_data:
        output_text = "`Confirmed   : {}\n`".format(country_data["confirmed"])
        output_text += "`Active      : {}`\n".format(country_data["active"])
        output_text += "`Deaths      : {}`\n".format(country_data["deaths"])
        output_text += "`Recovered   : {}`\n".format(country_data["recovered"])
        output_text += "`Last update : {}`\n". \
            format(datetime.utcfromtimestamp(country_data["last_update"] // 1000).strftime('%Y-%m-%d %H:%M:%S'))
        output_text += "`Data provided by `<a href=\"https://j.mp/2xf6oxF\">Johns Hopkins University</a>"
    else:
        output_text = "`No information yet about this country!`"
    await message.reply("**Corona Virus Info in {}**:\n\n{}".format(country.capitalize(), output_text))


def get_country_data(country, world):
    for country_data in world:
        if country_data["country"] == country:
            return country_data
    return


@setbot.on_message(Filters.command("coronastats") | Filters.command("coronastats@coronainfo19bot"))
async def coronastats(client, message):
    url = 'https://covid-19-api-2-i54peomv2.now.sh/api/og'
    response = requests.get(url, stream=True)
    with open('og', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    os.rename("og", "og.png")
    await client.send_photo(message.chat.id, "og.png", caption="<a href=\"https://covid-19-api-2-i54peomv2.now.sh"
                                                               "/api/og\">Source</a>")
    os.remove("og.png")


@setbot.on_message(Filters.command("start") | Filters.command("start@coronainfo19bot"))
async def start(client, message):
    list_button = InlineKeyboardMarkup([[InlineKeyboardButton("Add me to your group", url="https://t.me"
                                                                                          "/coronainfo19bot?startgroup=new")],
                   [InlineKeyboardButton("Support Group", url="https://t.me/nanabotsupport"),
                    InlineKeyboardButton("Help", callback_data="help")]])
    await client.send_message(message.chat.id, "Hey there! I'm here can give you information about Covid-19 Cases!\n"
                              "click /help to see what can i do\n\n"
                              "you can also add this bot to your group for getting data about covid-19\n"
                              "Join to our group @nanabotsupport if you need help / problem with this bot\n\n"
                              "this bot made by @legenhand", reply_markup=list_button)


def dynamic_data_filter(data):
    return Filters.create(
        lambda flt, query: flt.data == query.data,
        data=data  # "data" kwarg is accessed with "flt.data" above
    )


@setbot.on_callback_query(dynamic_data_filter("help"))
async def tulung(client, message):
    helptext = """
Check info of cases corona virus disease 2019

──「 **Info Covid** 」──
-> `/corona (country)`

──「 **get graph stats of global cases** 」──
-> `/coronastats`
"""
    await message.message.edit(helptext)


@setbot.on_message(Filters.command("help") | Filters.command("help@coronainfo19bot"))
async def helpcommand(client, message):
    helptext = """
    Check info of cases corona virus disease 2019

    ──「 **Info Covid** 」──
    -> `/corona (country)`

    ──「 **get graph stats of global cases** 」──
    -> `/coronastats`
    """
    await message.reply(helptext)
