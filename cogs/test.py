import discord
from discord.ext import commands
import os
import PIL.Image


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def image_test(self, ctx):
        mgs = await self.bot.wait_for(
            'message',
            check=lambda message: len(message.attachments) > 0
        )

        if mgs:
            for _file in mgs.attachments:
                if _file.content_type == 'image/jpeg':
                    await _file.save('./i.jpg')
                    await ctx.send('test append')
                    image = PIL.Image.open('./i.jpg')
                    await ctx.send(f'{type(image)}')
                    os.remove('./i.jpg')




def setup(bot):
    bot.add_cog(Test(bot))
