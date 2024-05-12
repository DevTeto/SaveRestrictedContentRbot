import os
from .. import bot as gagan
from telethon import events, Button
from telethon.tl.types import InputMediaPhoto

S = "/start"
START_PIC = "https://graph.org/file/da97ceca70e55983b4891.png"
TEXT = "↢ انـا [بوت حفظ المحتوي المقيد 📥](https://t.me/wx_pm)\n\n-لاستخدامي مـثال : `https://t.me/m_A_s_k33/72501`"

def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@gagan.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    gagan = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with gagan.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("**↢ هذا هو مطوري الرسمي للتواصل @TOPTETO**")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("**↢ هذا هو مطوري الرسمي للتواصل @TOPTETO**")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("**↢ هذا هو مطوري الرسمي للتواصل @TOPTETO**")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'جـاري المحاوله.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("انضم هنا فضلا وتواصل مع المطور @M_A_S_K33")

@gagan.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    gagan = event.client            
    await event.edit('انضم هنا فضلا وتواصل مع المطور @M_A_S_K33')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        

@gagan.on(events.NewMessage(pattern=f"^{S}"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.inline("‹ المطور ›", data="set"),
         Button.inline("‹ للمساعده ›", data="rem")],
        [Button.url("انضـم فضلا", url="https://t.me/wx_pm")]
    ]

    # Sending photo with caption and buttons
    await gagan.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )

