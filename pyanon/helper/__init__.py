import os
import sys
from pyrogram import Client

from pyanon.helper.adminHelpers import *
from pyanon.helper.aiohttp_helper import*
from pyanon.helper.basic import *
from pyanon.helper.cmd import *
from pyanon.helper.constants import *
from pyanon.helper.data import *
from pyanon.helper.inline import *
from pyanon.helper.interval import *
from pyanon.helper.parser import *
from pyanon.helper.PyroHelpers import *
from pyanon.helper.utility import *
from pyanon.helper.what import *


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Geez"])

