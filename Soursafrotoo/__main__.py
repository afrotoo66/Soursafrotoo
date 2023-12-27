import sys
import Soursafrotoo
from Soursafrotoo import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import mody
from .utils import (
    add_bot_to_logger_group,
    install_externalrepo,
    ipchange,
    load_plugins,
    setup_bot,
    mybot,
    startupmessage,
    verifyLoggerGroup,
    saves,
)

LOGS = logging.getLogger("Soursafrotoo")

print(Soursafrotoo.__copyright__)
print("Licensed under the terms of the " + Soursafrotoo.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("جارِ بدء بوت عفرتو ✓")
    mody.loop.run_until_complete(setup_bot())
    LOGS.info("تم اكتمال تنصيب البوت ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

try:
    LOGS.info("يتم تفعيل وضع الانلاين")
    mody.loop.run_until_complete(mybot())
    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")
except Exception as jep:
    LOGS.error(f"- {jep}")
    sys.exit()    

class CatCheck:
    def __init__(self):
        self.sucess = True


Catcheck = CatCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Catcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱")
    print("۞︙بـوت زد إي يعـمل بـنجاح ")
    print(
        f"تم تشغيل الانلاين تلقائياً ارسل {cmdhr}الاوامر لـرؤيـة اوامر السورس\
        \nللمسـاعدة تواصـل  https://t.me/T_Y_E_X"
    )
    print("🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱")
    await verifyLoggerGroup()
    await saves()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return

async def externalrepo():
    if Config.VCMODE:
        await install_externalrepo("https://github.com/jepthoniq/JepVc", "jepvc", "jepthonvc")

mody.loop.run_until_complete(externalrepo())
mody.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    mody.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        mody.run_until_disconnected()
    except ConnectionError:
        pass