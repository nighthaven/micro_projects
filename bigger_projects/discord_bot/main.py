from discord import Intents, Client

import responses


def run_bot(token: str):
    """Run our Discord Bot with the token provided"""
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = responses.load_knowledge('knowledge.json')

    @client.event
    async def on_ready():
        """Print a startup message for our bot when it goes online."""
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        """Handle incoming messages from our server."""
        if message.author == client.user:
            return
        if message.content:
            print(f'({message.channel}) {message.author}: "{message.content}"')
            response: str = responses.get_response(message.content, knowledge=knowledge)
            await message.channel.send(response)
        else:
            print('!!!Could not read the message, make sure you enabled intents!!!')
    client.run(token=token)


if __name__ == '__main__':
    run_bot(token='entrer le token ici')