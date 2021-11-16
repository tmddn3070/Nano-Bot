from discord.ext import commands
import traceback
import sys


class ErrorListener(commands.Cog):

    def __init__(self):
        self.name = "Error Listener"

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            return
        if isinstance(error, commands.errors.CommandError):
            return
        if isinstance(error, commands.errors.NSFWChannelRequired):
            return await ctx.send(":x: | This command is potentially nsfw and can only be used in nsfw channel.")
        if isinstance(error, commands.errors.CommandOnCooldown):
            return await ctx.send(":x: | You are on cooldown. Try again in 1 second")
        if isinstance(error, commands.errors.NotOwner):
            return await ctx.send(":x: | You are not owner")

        # ignore all other exception types, but print them to stderr
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)

        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
