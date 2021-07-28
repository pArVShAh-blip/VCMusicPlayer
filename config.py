"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  ZauteKm <https://telegram.dog/ZauteKm>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://eu10.fastcast4u.com/clubfmuae")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(float(os.environ.get("API_ID", '7809184')))
    CHAT = int(os.environ.get("CHAT", "-1001591741014"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "PSRUOF-VZIQOX-XIQUGK-SCGTBJ-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "ccfe8cf69e2e406fbd5806c88d17504c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1937706744:AAG9aw-JYWADoyFHLFZm5UevpUSqYdl2n2s") 
    SESSION = os.environ.get("SESSION_STRING", "BQBlElI1U_j08t6nbBN9knmhUEK1UNyw2ExinsnNQ9qSW1KbLQ27I5U9RHTTb6yTyGR8-2Cho5kwxwT1s9_s7oaxcD0ADJ_SsJnLj_4Vy0N6f9yfy_35ECG7lraq-HRvh_74j3Cp08lPTqK0-XwbKmKroppciNeq86WAs5OiNx6GynTXcHz-vslmisBBuDqFUVi0EH98q4S6JroX3dp5zJFOItTdSbzWRCGYfDKZHFePmAelYFjbUtrI7vIa75cQSiuPIhezpTdcNvlfdbgM-nKJeGNyCcT4gT_AwyWc3fb4oCtiA7W6VeNuN4O0BEN-m1cmyTnC1u0TLycioujsmr5ta5w1WgA")
    playlist=[]
    msg = {}

