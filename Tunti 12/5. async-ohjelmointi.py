
# Async funktiota käytetään silloin, kun funktion suoriutuminen on epävarmaa.
# Tästä esimerkkinä netistä tiedon hakeminen. Se voi kestää pitkäänkin.
# Siksi tarvitaan "asynchronous" ohjelmointia:
async def funktio():
    pass

# Tehdään esimerkkifunktio, joka joutuu odottamaan jonkin aikaa:
import asyncio

async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')


asyncio.run(fn())


