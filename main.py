infractions = {}
limit = 7
blacklist = ['word', 'word', 'word', 'word', 'word', 'word']

@client.listen()
async def on_message(message):
  

  content = message.content.replace(' ', '')

  if any(word in content.lower() for word in blacklist):
        id = message.author.id
        infractions[id] = infractions.get(id, 0) + 1

        if infractions[id] >= limit:
            await message.author.ban()
