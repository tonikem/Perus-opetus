
## https://www.geeksforgeeks.org/multithreading-python-set-1
## Kannattaa lukea tarkkaan monisäikeistyksestä ennen sen aloittamista.
## On hyvä tietää mitä säie tarkoittaa. Kysyin tätä ChatGPT:ltä.
## Vastaus alla:
"""
Säikeistys (engl. *multithreading*) tarkoittaa ohjelmoinnissa sitä,
että ohjelma voi suorittaa useita tehtäviä (säikeitä) samanaikaisesti
tai osittain päällekkäin samassa prosessissa. Se on tapa parantaa ohjelman
suorituskykyä erityisesti moniytimisissä prosessoreissa, joissa eri
säikeet voivat suorittaa koodia eri ytimillä yhtä aikaa.

### Keskeiset käsitteet säikeistyksessä:
1. **Säie (Thread)**: Säie on itsenäinen suoritustapahtuma,
    joka jakaa ohjelman muistialueen muiden säikeiden kanssa.
    Säie voi suorittaa koodia itsenäisesti, mutta se voi myös
    jakaa tietoa ja resursseja muiden säikeiden kanssa.

2. **Prosessi ja säikeet**: Prosessi on ohjelman suorituksen yksikkö,
    ja siinä voi olla yksi tai useampia säikeitä.
    Usein säikeet jakavat saman muistialueen, mutta voivat toimia erillään.

3. **Säikeistys ja rinnakkaisuus**: Säikeistys voi mahdollistaa rinnakkaisen suorituksen,
    mutta säikeiden käyttö ei aina takaa, että ne suoritetaan täysin samanaikaisesti
    (kuten eri ytimillä). Jos ohjelma käyttää vain yhtä prosessoria,
    säikeet voivat silti vuorotella prosessorin käytössä,
    jolloin ne näyttävät toimivan samanaikaisesti,
    mutta ovat itse asiassa vuorotellen suorituksessa.

4. **Esimerkki käytöstä**: Jos ohjelmassa on suuri määrä laskentaa
    ja sen rinnalla halutaan käsitellä käyttäjän syötteitä tai
    lähettää tietoa verkkoon, säikeistys mahdollistaa,
    että laskenta ei estä muita tehtäviä.
    Tämä parantaa ohjelman reagointikykyä ja suorituskykyä.

### Säikeistämisen edut:
- **Parantaa suorituskykyä**:
        Useita säikeitä voidaan ajaa rinnakkain moniytimisissä prosessoreissa,
        mikä voi nopeuttaa ohjelman suoritusta.

- **Parantaa ohjelman responsiivisuutta**:
        Säikeistys voi tehdä ohjelmasta nopeammin reagoivan,
        kun eri toiminnot voivat tapahtua samanaikaisesti
        (esim. käyttöliittymän päivitys taustatoimintojen aikana).

- **Tehokas resurssien käyttö**:
        Säikeet jakavat saman muistialueen,
        joten resurssien käyttö on tehokkaampaa verrattuna
        eri prosessien käyttämiseen.

### Haasteet ja riskit:
- **Säikeiden synkronointi**:
        Koska säikeet voivat jakaa muistia, on tärkeää varmistaa,
        että useampi säie ei muokkaa samaa dataa samanaikaisesti
        (kilpailutilanteet). Tätä varten käytetään synkronointimekanismeja,
        kuten lukkoja (locks) ja semaforeja.

- **Virheiden ja kaatumisten hallinta**:
        Säikeistys voi tehdä virheiden jäljittämisestä ja
        ohjelman tilan hallinnasta monimutkaisempaa,
        koska säikeet voivat vaikuttaa toistensa tilaan.

### Esimerkki:
Oletetaan, että sinulla on ohjelma, joka lataa tiedostoja verkosta ja
samalla käsittelee niitä. Jos ohjelma ei olisi säikeistetty,
sen pitäisi odottaa, että tiedosto on ladattu kokonaan ennen kuin se aloittaa käsittelyn.
Säikeistetyssä ohjelmassa voidaan ladata useita tiedostoja rinnakkain ja
samalla käsitellä jo ladattuja tiedostoja, mikä tekee ohjelmasta nopeamman ja tehokkaamman.

Säikeistys on siis tärkeä ohjelmointitekniikka,
joka parantaa ohjelmien suorituskykyä ja
reagointikykyä erityisesti moniytimisissä ympäristöissä.
"""


# Säikeiden opetus tapahtuu toisella repolla:
# https://github.com/tonikem/Thread-opetus


