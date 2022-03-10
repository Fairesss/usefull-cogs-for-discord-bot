 
from PIL import Image
import urllib.request
import discord
from discord.ext import commands
import asyncio
from io import BytesIO
import os

ASCII_CHAR = ["@", "#", "S", "#", "?", '*', '+', ';', ':', ',', '.']


async def resize(imege, new_width=100):
    width, height = imege.size
    ration = height / height
    new_height = int(new_width * ration)
    resize_image = imege.resize((new_width, new_height))
    return resize_image


async def to_gray(image):
    convered = image.convert("L")
    return convered


async def pixel_to_ascii(image):
    pixel = image.getdata()
    chars = ''.join([ASCII_CHAR[pi//25] for pi in pixel])
    return chars


class Image_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def to_ascii(self, ctx, size: int = 30):
        await ctx.send("Enter a img with the .jpg format")
        try:
            mgs = await self.bot.wait_for(
                'message',
                timeout=60,
                check=lambda message: message.author == ctx.author and len(message.attachments) >= 1
            )

            if mgs:
                for _file in mgs.attachments:
                    if _file.content_type == 'image/jpeg':
                        image = await _file.save('i.jpg')
                        image = Image.open('./i.jpg')
                        new_image = await resize(image, size)
                        new_image = await to_gray(new_image)
                        new_image = await pixel_to_ascii(new_image)
                        pixel_count = len(new_image)
                        #for i in range(0, pixel_count, size):
                         #   await ctx.send(new_image[i:(i+size)] + '\n')

                        ascii_image = "\n".join(new_image[i:(i+size)]
                                                for i in
                                                range(0, pixel_count, size))
                        with open('to_send.txt', 'w') as f:
                            f.write(ascii_image)
                        await ctx.send(file=discord.File('./to_send.txt'))
                        os.remove('./i.jpg')
                        os.remove('./to_send.txt')
                    else:
                        continue
        except asyncio.TimeoutError:
            await ctx.send("time up")






def setup(bot):
    bot.add_cog(Image_commands(bot))
