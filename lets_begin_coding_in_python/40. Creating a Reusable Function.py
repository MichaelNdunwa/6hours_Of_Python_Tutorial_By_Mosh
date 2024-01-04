
def emojis_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😁",
        ":(": "☹️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emojis_converter("Babe smile for me :)"))