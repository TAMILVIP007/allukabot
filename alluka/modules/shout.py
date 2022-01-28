from typing import List

from telegram import Update, Bot
from telegram.ext import run_async

from alluka.modules.disable import DisableAbleCommandHandler
from alluka import dispatcher


@run_async
def shout(bot: Bot, update: Update, args: List[str]):

    msg = "```"
    text = " ".join(args)
    result = [' '.join(list(text))]
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, pass_args=True)

dispatcher.add_handler(SHOUT_HANDLER)


__command_list__ = ["shout"]
__handlers__ = [SHOUT_HANDLER]
