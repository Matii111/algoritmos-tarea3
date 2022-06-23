モキ
#4513

Suket — 04/06/2022
Image
Suket — 04/06/2022
Image
Suket — 04/06/2022
Image
Image
Suket — 04/06/2022
Image
Image
Suket — 05/06/2022
https://www.youtube.com/watch?v=V5fE_ufXq6Y
YouTube
SENTRY
Explaining Meme Programming Languages
Image
Suket — 05/06/2022
https://www.youtube.com/watch?v=75HNLw9doeI
YouTube
Simone Tmm
Bad Apple!! - in C [ASCII ART]
Image
Suket — 05/06/2022
Image
モキ — 05/06/2022
Image
Suket — 13/06/2022
https://twitter.com/G__IKA/status/1536426550497017857

風巻いか (@G__IKA)
あきらさっんッッ!!　かきました🍑
Likes
598
Retweets
143
Image

Twitter•13/06/2022
モキ — 15/06/2022
https://www.reddit.com/r/seiyuu/comments/vcf8wh/retired_voice_actress_maho_matsunaga_revealed_on/?utm_source=share&utm_medium=ios_app&utm_name=iossmf
reddit
r/seiyuu - Retired Voice Actress Maho Matsunaga revealed on her blo...
89 votes and 8 comments so far on Reddit
Image
モキ — 15/06/2022
La seiyuu era una de las de a-rise de love live
モキ — 16/06/2022
Que estás haciendo en llamada anda a ver
https://www.twitch.tv/warframe
Twitch
Warframe - Twitch
Image
Para los drops
モキ — 16/06/2022
ZLLN7YCFJJNNW
02fcea75-b28a-4d0e-a34f-0f476be3de74
Suket — 16/06/2022
que hago con este codigo 
Suket — 18/06/2022
Image
Image
Image
Image
Image
Image
Image
Image
Image
https://fapello.com/keekihime/
Image
Suket — 19/06/2022
https://www.youtube.com/watch?v=KOJTK0W1CzA
YouTube
shiningsoul6
Hatsune Miku - Rubik's Cube
Image
モキ — 19/06/2022
https://youtu.be/2eBW38kVUkE
YouTube
ShinoAlter
Taishou Otome Otogibanashi - [OP]
Image
Suket — 20/06/2022
Image
Image
Image
Suket — 20/06/2022
https://twitter.com/unilunar_/status/1537192906330722304

luna (@unilunar_)
in light of recent events, this character archetype is still GREAT
Likes
3333
Retweets
730
Image

Twitter•15/06/2022
https://twitter.com/simejinameko/status/1537814649545994240

しめじなめこ (@simejinameko)
二人っきりになった時にだけ
悪い子になるアビーちゃん…いいよね…
いい…
Likes
5642
Retweets
1245
Image

Twitter•17/06/2022
Suket — Yesterday at 23:07
https://www.reddit.com/r/Hololive/comments/vihrh0/those_600000000_boyfriends_must_be_crying_rn/
reddit
r/Hololive - Those 600,000,000 boyfriends must be crying rn
1,216 votes and 21 comments so far on Reddit
Image
https://www.reddit.com/r/chile/comments/vik91m/ahora_no_po/
reddit
r/chile - ahora no po'
148 votes and 28 comments so far on Reddit
Image
Suket — Today at 00:52
https://www.reddit.com/r/ffxiv/comments/vi44wt/its_not_much_but_its_our_home_aka_making_the_most/
reddit
r/ffxiv - It's not much, but it's our home (a.k.a. making the most ...
895 votes and 45 comments so far on Reddit
https://www.reddit.com/r/ffxiv/comments/vi5ycs/newfound_adventure_a_commission_by_norino_shi/
reddit
r/ffxiv - Newfound Adventure, a Commission by Norino Shi
641 votes and 69 comments so far on Reddit
Image
Suket — Today at 02:16
Image
Image
Image
Image
Image
Image
Image
Image
Suket — Today at 07:17
def Separar(datos):

    lista = []
    for i in datos:

        lista.append(int(i))
Expand
algoritmogreedycasilisto.py
2 KB
﻿
def Separar(datos):

    lista = []
    for i in datos:

        lista.append(int(i))

    return(lista)

def removerespacios(lista):
    return lista.replace(' ','')


def maximos_Eventos(Inicio, final, ultimo, cantidad):

    sig_evento = ultimo + 1

    while sig_evento < cantidad and Inicio[sig_evento] < final[ultimo]:
        sig_evento = sig_evento + 1
    
    if sig_evento < cantidad:
        return [sig_evento] + maximos_Eventos(Inicio, final, sig_evento,cantidad)

    return []



cantidad_de_act = int(input("ingrese la cantidad de actividades: \n"))

#----------------------------------------------------------------------------------------

ini = input("ingrese los tiempos de inicio de las actividades: \n")


iniclean = removerespacios(ini)



iniciolista = Separar(iniclean)

#-----------------------------------------------------------------------------

fin = input("ingrese los tiempos de fin de las actividades: \n")


finclean = removerespacios(fin)

finlista = Separar(finclean)



valor = (maximos_Eventos(iniciolista,finlista,0,cantidad_de_act))

valor.insert(0,0)


print("las actividades que puede realizar la person son : \n",*valor)
