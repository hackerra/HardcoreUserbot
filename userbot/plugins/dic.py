from userbot import userbot, Message
import requests

LOG = userbot.getLogger(__name__)  # logger object

CHANNEL = userbot.getCLogger(__name__)  # channel logger object


@userbot.on_cmd("dic", about='''<code><em>English Dictionary-telegram</em>
<b>Usage:</b>
   .dic [word]

<i>word</i>: Search for any word</code>''')  # adding handler and help text to .dic command
async def dictionary(message: Message):
    LOG.info("starting dic command...")  # log to console
    input = message.input_str

    def combine(s, name):
        w = f"🛑<u><b><em>{name.title()}</em></b></u>\n"
        for i in s:
            if "definition" in i:
                if "example" in i:
                    w += "\n👩‍🏫<b>Definition:</b>👨‍🏫\n<pre>" + i[
                        "definition"] + "</pre>\n\t\t❓<b>Example:</b>❔\n<pre>" + i["example"] + "</pre>"
                else:
                    w += "\n👩‍🏫<b>Definition</b>:👨‍🏫\n" + "<pre>" + i["definition"] + "</pre>"
        w += "\n\n"
        return w

    def out_print(word1):
        out = ""
        if "meaning" in list(word1):
            meaning = word1["meaning"]
            if "noun" in list(meaning):
                noun = meaning["noun"]
                out += combine(noun, "noun")
                # print(noun)
            if "verb" in list(meaning):
                verb = meaning["verb"]
                out += combine(verb, "verb")
                # print(verb)
            if "preposition" in list(meaning):
                preposition = meaning["preposition"]
                out += combine(preposition, "preposition")
                # print(preposition)
            if "adverb" in list(meaning):
                adverb = meaning["adverb"]
                out += combine(adverb, "adverb")
                # print(adverb)
            if "adjective" in list(meaning):
                adjec = meaning["adjective"]
                out += combine(adjec, "adjective")
                # print(adjec)
            if "abbreviation" in list(meaning):
                abbr = meaning["abbreviation"]
                out += combine(abbr, "abbreviation")
                # print(abbr)
            if "exclamation" in list(meaning):
                exclamation = meaning["exclamation"]
                out += combine(exclamation, "exclamation")
                # print(exclamation)
            if "transitive verb" in list(meaning):
                transitive_verb = meaning["transitive verb"]
                out += combine(transitive_verb, "transitive verb")
                # print(tt)
            if "determiner" in list(meaning):
                determiner = meaning["determiner"]
                out += combine(determiner, "determiner")
                # print(determiner)
            if "crossReference" in list(meaning):
                crosref = meaning["crossReference"]
                out += combine(crosref, "crossReference")
                # print(crosref)
        if "title" in list(word1):
            out += "<u><code>🔖Error Note:</code></u>\n\n<code>▪️" + word1["title"] + "🥺\n\n▪️" + word1[
                "message"] + "😬\n\n<i>▪️" + word1[
                       "resolution"] + "🤓</i></code>"
            # print(l)🥺
        return out

    if not input:
        await message.edit("<code>❌Plz enter word to search‼️</code>", del_in=5)
    else:
        word = input
        r = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}")
        r_dec = r.json()

        v = input
        if isinstance(r_dec, list):
            r_dec = r_dec[0]
            v = r_dec['word']
        last_output = out_print(r_dec)
        await message.edit(f"<b>📌Search result for    👉 {v}\n\n</b>\n" + last_output)
    await CHANNEL.log("request updated!")  # log to channel
