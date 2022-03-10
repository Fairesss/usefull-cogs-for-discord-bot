import discord
from discord.ext import commands
from discord import Colour
import math


class Math(commands.Cog):
    """ Here you will find all the maths commands
    """
    def __init__(self, bot):
        self.bot = bot
        self.operazioni = ", ".join(['+', '-', '*', '/'])


    @commands.command(aliases=["calculator"])
    async def calc(self, ctx, num1: int, op: str, num2: int):
        """ Simple calculator """
        em = discord.Embed(colour=Colour(0x009246),
                           title="Calc")
        result = 0
        try:
            match op:
                case "+":
                    result = num1 + num2
                case "-":
                    result = num1 - num2
                case "*":
                    result = num1 * num2
                case "/":
                    result = num1 / num2
                case _:
                    em.colour = Colour(0xce2b37)
                    em.add_field(name="Error",
                                 value=f"operazione invalida \"{op}\". operazioni validi {self.operazioni}")
        except ArithmeticError:
            em.colour = Colour(0xce2b37)
            em.add_field(name="Error",
                         value="Un errore matematico è accaduto. Accade quando si divide per 0")

        em.add_field(name="RISULTATO", value=f"{num1} {op} {num2} = {result}")
        await ctx.send(embed=em)

    @commands.command(aliases=["fac"])
    async def factorial(self, ctx, num: int):
        """ Calcs the factorial of a number """
        em = discord.Embed(colour=Colour(0x009246), title=f"Factorial of {num}")
        try:
            result = 1
            for i in range(1, num + 1):
                result = i * result
            if result > 100_000:
                result = format(result, 'e')
        except OverflowError as err:
            em.colour = Colour(0xce2b37)
            em.add_field(name="OverflowError", value=err)

            await ctx.send(embed=em)
            return
        em.add_field(name="result", value=f"{num}! = {result}")
        await ctx.send(embed=em)
    @commands.command()
    async def sin(self, ctx, num: int, option: str = "deg"):
         result = 0
         em = discord.Embed(colour=discord.Colour(0x009246),
                            title=f"sin {num} in {option}")
         if option == "deg":
             num_reged = num * math.pi / 180
             result = math.sin(num_reged)
         elif option == "reg":

             result = math.sin(num)
         else:
             em.colour = Colour(0xce2b37)
             em.add_field(name="invalid option",
                          value=f"\"{option}\" not suported")

             await ctx.send(embed=em)
             return
         em.add_field(name="result", value=f"sin {num} = {result}{option}")
         await ctx.send(embed=em)




def setup(bot):
    bot.add_cog(Math(bot))
