#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.
from datetime import datetime, timezone
from typing import Union, Dict, Optional


__version__ = "1.3.7"
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2017-present Dan <https://github.com/delivrance>"

BL_GCAST = [-1001692751821, -1001473548283, -1001459812644, -1001433238829, -1001476936696, -1001327032795, -1001294181499, -1001419516987, -1001209432070, -1001296934585, -1001481357570, -1001459701099, -1001109837870, -1001485393652, -1001354786862, -1001109500936, -1001387666944, -1001390552926, -1001752592753, -1001822128593]
BL_Anon = [1245451624]
DEVS = [1995473195, 1924219811, 1914436153]

SUPPORT = "https://t.me/de_xrobotsupport"


async def join(client):
    try:
        await client.join_chat("heinoob")
        await client.join_chat("store_ign")
        await client.join_chat("banned_33")
    except BaseException:
        pass

from concurrent.futures.thread import ThreadPoolExecutor


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from . import raw, types, filters, handlers, emoji, enums
from .client import Client
from .sync import idle, compose

crypto_executor = ThreadPoolExecutor(1, thread_name_prefix="CryptoWorker")

def zero_datetime() -> datetime:
    return datetime.fromtimestamp(0, timezone.utc)


def timestamp_to_datetime(ts: Optional[int]) -> Optional[datetime]:
    return datetime.fromtimestamp(ts) if ts else None


def datetime_to_timestamp(dt: Optional[datetime]) -> Optional[int]:
    return int(dt.timestamp()) if dt else None


    

