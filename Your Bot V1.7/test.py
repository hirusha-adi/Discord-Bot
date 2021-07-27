@client.command()
async def usage(ctx, exampleyn="no"):
  bp = bot_prefix
  help1 = f"""{bp}ping
{bp}clear [number_of_messages_to_delete]
{bp}8ball [question]
{bp}kick [@user]
{bp}ban [@user]
{bp}unban [username#id]
{bp}inspire
{bp}inv
{bp}fake [argument] - argument = help, high, name, dob, addr



"""