import re
import spacy

# Verificar si el modelo está instalado
if 'es_core_news_lg' not in spacy.util.get_installed_models():
    # Instalar el modelo si no está presente
    spacy.cli.download('es_core_news_lg')
    
nlp = spacy.load("es_core_news_lg")


conversation = """
3/6/23, 23:36 - Marina🦟: hola que tal
3/6/23, 23:45 - laura: hola, bien y tú?
4/6/23, 0:06 - Marina🦟: mi estado se ve más bonito cn mis emoticonos😕
4/6/23, 0:06 - Marina🦟: jajajajajajajajajjaaja
4/6/23, 0:09 - laura: jajajajjajaj si claro
4/6/23, 0:16 - Marina🦟: tengo un plan
4/6/23, 0:16 - Marina🦟: igual m lo rechazas
4/6/23, 0:16 - Marina🦟: no se
4/6/23, 0:21 - laura: osea q a parte de los médicos, te encantan las mariposas, los tréboles, etc..
4/6/23, 0:21 - laura: a ver dime
4/6/23, 0:23 - Marina🦟: ni confirmo ni desmiento
4/6/23, 0:23 - Marina🦟: no es q m encanten jajajajajaja tiene su significado
4/6/23, 0:23 - Marina🦟: que no vas a saber x cierto
4/6/23, 0:23 - Marina🦟: d momento
4/6/23, 0:23 - Marina🦟: quiero ir a ver la sirenita
4/6/23, 0:32 - laura: y cuando me lo piensas explicar???? digo
4/6/23, 0:32 - laura: vale vamos
4/6/23, 0:37 - Marina🦟: nunca jamás
4/6/23, 0:37 - Marina🦟: jajajajajajajajajajjaa
4/6/23, 0:37 - Marina🦟: algún día
4/6/23, 0:37 - Marina🦟: biennnnn🥹
4/6/23, 0:37 - Marina🦟: ehhhhh y eso???? yo quiero
4/6/23, 0:37 - Marina🦟: no fumes
4/6/23, 0:37 - Marina🦟: es malo vale????
4/6/23, 0:42 - laura: ya lo sé
4/6/23, 0:42 - laura: es de unas vacaciones q te fuiste de crucero
4/6/23, 0:43 - laura: jajajajajjaja me lo apunto vale??
4/6/23, 0:43 - laura: ya te invitaré algún día si me caes bien
4/6/23, 0:44 - laura: tendrás q confiscarme el tabaco
4/6/23, 0:44 - laura: el vaper tb es malo lista
4/6/23, 0:48 - Marina🦟: JAJAJAJAJAJAAJ
4/6/23, 0:48 - Marina🦟: no he ido d crucero en mi vida
4/6/23, 0:48 - Marina🦟: xfa si
4/6/23, 0:48 - Marina🦟: para cuando t apetezca darme un día
4/6/23, 0:49 - Marina🦟: genial, m parece estupendo
4/6/23, 0:49 - Marina🦟: lo haré
4/6/23, 0:49 - Marina🦟: lo sé pero menos
4/6/23, 0:50 - Marina🦟: tengo una pregunta importante para completar el plan del cine
4/6/23, 0:50 - Marina🦟: t juegas mis respetos cn la respuesta
4/6/23, 0:54 - laura: jajajajjsjaj TIO LO QUIERO SABER
4/6/23, 0:55 - laura: a ver dime
4/6/23, 0:55 - laura: dime dime
4/6/23, 0:56 - Marina🦟: sorpréndeme a ver
4/6/23, 0:56 - Marina🦟: tiene pinta de q m vas a decepcionar
4/6/23, 0:57 - Marina🦟: pero ahí va
4/6/23, 0:57 - Marina🦟: t gusta el sushi?
4/6/23, 0:59 - laura: JAJAJAJAJJJAJAJ VA PESADILLA
4/6/23, 0:59 - laura: tu tampoco te acostumbres
4/6/23, 1:00 - laura: esq no lo puedo decir
4/6/23, 1:00 - laura: me gusta todo
4/6/23, 1:00 - laura: así q no te he decepcionado
4/6/23, 1:00 - laura: y sí, tb acepto después del cine
4/6/23, 1:01 - Marina🦟: lo intentaré
4/6/23, 1:02 - Marina🦟: es una quedada perfecta
4/6/23, 1:06 - laura: jajajjajajajajaj tan perfecta 
4/6/23, 1:09 - Marina🦟: tu crees????
4/6/23, 1:13 - laura: ahh, porqué es una sorpresa
4/6/23, 1:13 - laura: yo creo
4/6/23, 1:16 - Marina🦟: ah vale
4/6/23, 1:16 - Marina🦟: me gustan las sorpresas
4/6/23, 1:16 - Marina🦟: me esperaré pues
4/6/23, 1:22 - laura: no duermes??
4/6/23, 1:24 - Marina🦟: no tengo sueño
4/6/23, 1:24 - Marina🦟: y tu???
4/6/23, 1:24 - Marina🦟: tng un mosquito molestando
4/6/23, 1:28 - laura: pues quiéreme un poquito
4/6/23, 1:31 - Marina🦟: q tienes q hacer?
4/6/23, 1:34 - laura: más faena
4/6/23, 1:35 - laura: cancelamos el plan si quieres
4/6/23, 1:36 - Marina🦟: es q el plan m llama mucho
4/6/23, 1:37 - Marina🦟: yo mañana voy a la milonga
4/6/23, 1:41 - laura: tienes fiesta el lunes no?
4/6/23, 1:43 - Marina🦟: es broma
4/6/23, 1:43 - Marina🦟: de momento no quiero
4/6/23, 1:43 - Marina🦟: yesssss
4/6/23, 1:44 - Marina🦟: tu no?
4/6/23, 1:49 - laura: lo puedo intentar vale????
4/6/23, 1:49 - laura: y porque te vas al quinto pino
4/6/23, 1:50 - laura: bueno sí, fiesta sí pero tengo q ir igualmente a bcn a hacer mierdas
4/6/23, 1:52 - Marina🦟: salgo x mataró a vecesssss
4/6/23, 1:52 - Marina🦟: además es el único sitio q hacen tardeo x aquí cerca
4/6/23, 1:52 - Marina🦟: no paras
4/6/23, 1:52 - Marina🦟: q palo
4/6/23, 1:52 - Marina🦟: q se pase la semana ya
4/6/23, 2:03 - laura: y hasta q hora abren??
4/6/23, 2:09 - Marina🦟: pues hasta las 2
4/6/23, 2:10 - Marina🦟: y hay mucha gente q luego se va al classic
4/6/23, 2:10 - Marina🦟: pero yo m ire pa casa
4/6/23, 2:12 - laura: un domingo??
4/6/23, 2:18 - Marina🦟: cuando el lunes es fiesta abren siiii
4/6/23, 2:36 - Marina🦟: t has dormidoooooo
4/6/23, 10:13 - laura: buenos días
4/6/23, 10:14 - laura: casi siempre y mira q tengo un montón de ropa pero siempre acabo yendo cómoda
4/6/23, 11:11 - Marina🦟: buenos diassss
4/6/23, 11:11 - Marina🦟: yo d vez en cuando si pero m gusta ir en tejanos jajajajajajajaa
4/6/23, 11:32 - Marina🦟: no m quiero levantar pffff
4/6/23, 11:32 - Marina🦟: creo q m voy a dormir un ratito más
4/6/23, 11:32 - Marina🦟: tu ya estás haciendo cosas???
4/6/23, 11:36 - laura: pues justo estoy mirándome ropa jajajajajja
4/6/23, 11:36 - laura: porq el 14 tengo el paso del ecuador
4/6/23, 11:36 - laura: nose si sabes q es
4/6/23, 11:37 - laura: y tb es mi cumple😌
4/6/23, 11:44 - Marina🦟: pfv si
4/6/23, 11:45 - Marina🦟: que t vas a poner???
4/6/23, 11:45 - Marina🦟: siiiii
4/6/23, 11:45 - Marina🦟: alaaaaa si??? el 14??
4/6/23, 11:45 - Marina🦟: mi hermano cumple el 15
4/6/23, 11:45 - Marina🦟: cuantos haces x cierto? 24?
4/6/23, 11:52 - laura: pues nose porq estan votando como hay q ir si arregladito o qué
4/6/23, 11:52 - laura: te puedes creer q se han gastado 10000 pavos en barra libre, fotografo noseq
4/6/23, 11:53 - laura: tb es géminis?? 
4/6/23, 11:53 - laura: haré 24, tu??
4/6/23, 11:56 - Marina🦟: bueno m mantienes informada jajajajajajaa
4/6/23, 11:56 - Marina🦟: QUEEEE
4/6/23, 11:56 - Marina🦟: a mi es q no m pueden poner barra libre
4/6/23, 11:56 - Marina🦟: porque m desconozco
4/6/23, 11:56 - Marina🦟: jajajajajajajajabbaajaja
4/6/23, 11:57 - Marina🦟: yes…
4/6/23, 11:57 - Marina🦟: yo los hice en enero los 24
4/6/23, 12:05 - laura: quieres venir??
4/6/23, 12:05 - laura: mi padre me dice
4/6/23, 12:05 - laura: te voy a dar un móvil viejo solo para llamadas jajajajjajaja esq flipo
4/6/23, 12:21 - Marina🦟: obvvvviamente
4/6/23, 12:21 - Marina🦟: a dnd???
4/6/23, 12:21 - Marina🦟: JAJAJAJ para q no t lo roben? memeo
4/6/23, 12:21 - Marina🦟: siiii
4/6/23, 12:27 - Marina🦟: y m haga el bigote ya q está
4/6/23, 12:27 - Marina🦟: si es q m he cruzado cn mi hermano y me dice
4/6/23, 12:27 - Marina🦟: que t has hecho?
4/6/23, 12:28 - Marina🦟: y digo q m he hecho?
4/6/23, 12:28 - Marina🦟: m dice en las cejas, pareces gargamel
4/6/23, 12:28 - Marina🦟: puto niño
4/6/23, 12:37 - laura: es privado en una masia de sant boi
4/6/23, 12:38 - laura: cuantos años tenía??
4/6/23, 12:39 - laura: voy a hacer un pco de deporte vale??? q me estresan los trabajos
4/6/23, 12:41 - Marina🦟: porq sois imbeciles
4/6/23, 12:41 - Marina🦟: 13 va a hacer
4/6/23, 12:42 - Marina🦟: oyeeeeeeee
4/6/23, 12:42 - Marina🦟: q haces
4/6/23, 12:54 - laura: ui ya va a empezar a tener novias
4/6/23, 12:54 - laura: esq estuve apuntada al gym pero no iba
4/6/23, 12:55 - laura: tu hace mucho q vas??
4/6/23, 17:17 - Marina🦟: q noooooo
4/6/23, 17:17 - Marina🦟: jajajajajajajaja
4/6/23, 17:17 - Marina🦟: siiiii
4/6/23, 17:52 - laura: tio voy a salir un rato a tomar algo
4/6/23, 17:52 - laura: porq no se me para de colgar el ordenador
4/6/23, 18:04 - Marina🦟: hay caravana q flipas x la carrera
4/6/23, 18:04 - Marina🦟: haces biennnn
4/6/23, 18:04 - Marina🦟: hay algo abierto un domingo en tu pueblo???
4/6/23, 18:04 - Marina🦟: jajajajajajajajajaja
4/6/23, 18:11 - laura: NO HAY NADA VALE?????
4/6/23, 18:11 - laura: jajajajjajjaj me tngo q ir al pueblo de al lado
4/6/23, 18:18 - Marina🦟: JAJAJJAJAAJ
4/6/23, 18:18 - Marina🦟: memeo
4/6/23, 20:11 - Marina🦟: bua
4/6/23, 20:11 - Marina🦟: voy mal eh que
4/6/23, 20:11 - Marina🦟: tu q haces
4/6/23, 20:34 - laura: ya vas contenta???
4/6/23, 20:34 - laura: cuando abre eso??
4/6/23, 20:35 - laura: nada acabo de llegar a casa
4/6/23, 20:46 - Marina🦟: ciega si jajajajajaajjhajaja
4/6/23, 22:11 - Marina🦟: ya estás dormida???
4/6/23, 22:53 - laura: te puedes creer q acabo de salir de la ducha??
5/6/23, 0:03 - Marina🦟: queeeee?
5/6/23, 0:03 - Marina🦟: aun no t habías duchado????
5/6/23, 0:03 - Marina🦟: 100% estás dormida ya
5/6/23, 0:08 - laura: si esq me he tirado dos horas dentro
5/6/23, 0:08 - laura: te equivocassssss
5/6/23, 0:09 - laura: ya no estas en la milonga??
5/6/23, 0:09 - Marina🦟: siiii
5/6/23, 0:09 - Marina🦟: estoy aquí
5/6/23, 0:09 - Marina🦟: pero mi amiga está a punto d gomitar
5/6/23, 0:09 - Marina🦟: jajjajajajajajaaajajaj
5/6/23, 0:09 - Marina🦟: yo bien
5/6/23, 0:09 - Marina🦟: borracha  pero bien
5/6/23, 0:09 - laura: jajajajajjajajjajajajajaj
5/6/23, 0:09 - laura: como q Gomitar
5/6/23, 0:09 - laura: cn G
5/6/23, 0:10 - Marina🦟: gomitar cn g
5/6/23, 0:10 - Marina🦟: si
5/6/23, 0:10 - Marina🦟: jajajajajjaajjq
5/6/23, 0:10 - laura: borracha pero buena muchacha
5/6/23, 0:10 - Marina🦟: extracto
5/6/23, 0:10 - laura: jajajajajjajjjajajaj para
5/6/23, 0:10 - Marina🦟: exacto
5/6/23, 0:10 - laura: no lo dirás así
5/6/23, 0:10 - Marina🦟: si JAJAJJAAJ
5/6/23, 1:29 - Marina🦟: no t duermas tío
5/6/23, 1:29 - Marina🦟: paso d ti
5/6/23, 1:29 - Marina🦟: ya no t hablo más
5/6/23, 2:34 - Marina🦟: es broma
5/6/23, 2:34 - Marina🦟: acabo d llegar
5/6/23, 9:25 - laura: buenos díaaaasss
5/6/23, 9:25 - laura: no te vayas a arrepentir jajajajajja
5/6/23, 9:26 - laura: lo sé
5/6/23, 9:26 - laura: al final Gomitó tu amiga???
5/6/23, 12:07 - Marina🦟: buenos diasssss
5/6/23, 12:07 - Marina🦟: seguiría durmiendo 8 horas más
5/6/23, 12:07 - Marina🦟: podría ser
5/6/23, 12:07 - Marina🦟: JAJAJAJAJAJA
5/6/23, 12:07 - Marina🦟: no
5/6/23, 12:07 - Marina🦟: pero casi
5/6/23, 12:07 - Marina🦟: a puntito estuvo
5/6/23, 12:08 - Marina🦟: como va????
5/6/23, 15:00 - laura: jajajajjjajajjjajaj pero como se dice gomitar bn dicho???
5/6/23, 15:01 - laura: fatal me quiero morir
5/6/23, 15:01 - laura: no nos está saliendo nada bn y mañana es la entrega
5/6/23, 15:02 - laura: has dormido más???
5/6/23, 15:07 - Marina🦟: como q como se dice???? eres tonta??? hajajajajajajajjaa
5/6/23, 15:07 - Marina🦟: no m lo vas a decir
5/6/23, 15:07 - Marina🦟: que tienes q hacer???
5/6/23, 15:08 - Marina🦟: nop, estaba esperando q m respondieras
5/6/23, 16:03 - laura: jjajajajajajajsjaj no tu
5/6/23, 16:04 - laura: q cómo lo dirías bn gomitar
5/6/23, 16:04 - laura: bn dicho
5/6/23, 16:04 - laura: JAJAJAJAJJAJJAJ
5/6/23, 16:04 - laura: algún día alomejor
5/6/23, 16:04 - laura: 3 vídeos
5/6/23, 16:05 - laura: ojalá echarme la siesta
5/6/23, 16:05 - laura: tu seguro q estás ya
5/6/23, 16:27 - Marina🦟: vomitar
5/6/23, 16:27 - Marina🦟: y cuantos llevas?
5/6/23, 16:27 - Marina🦟: pues noooo
5/6/23, 16:27 - Marina🦟: hoy no he dormido siesta
5/6/23, 16:27 - Marina🦟: pero no tiene pinta que vaya a hacer gran cosa
5/6/23, 16:28 - Marina🦟: estoy mood vago
5/6/23, 17:40 - laura: jajaajjajjajajajjaj muy bn
5/6/23, 17:40 - laura: pensaba q no sabías
5/6/23, 17:40 - laura: q raro en ti
5/6/23, 17:40 - laura: no vas a ir al gym??
5/6/23, 18:04 - Marina🦟: como si fuera tonta
5/6/23, 18:04 - Marina🦟: pues ya espero q sea bueno de vd
5/6/23, 18:04 - Marina🦟: vd????
5/6/23, 18:04 - Marina🦟: será porque he dormido mucho hoy
5/6/23, 18:04 - Marina🦟: pf no, no voy a ir
5/6/23, 20:00 - laura: no he comido nada en todo el día tío
5/6/23, 20:05 - Marina🦟: come algo anda
5/6/23, 20:05 - Marina🦟: ya t vas a casa??
5/6/23, 21:47 - laura: aún estoy aquí esq llegaré a casa a las tantas pero bno ya estamos acabando
5/6/23, 21:47 - laura: aún no x desgracia
5/6/23, 21:47 - laura: como va lo de hacer el vago??
5/6/23, 22:02 - Marina🦟: mmm no
5/6/23, 22:03 - Marina🦟: no t puedes comprar nada x ahí???
5/6/23, 22:03 - Marina🦟: yo no aguanto todo el día sin comer
5/6/23, 22:03 - Marina🦟: me muero
5/6/23, 22:03 - Marina🦟: encima estoy comiendo fatal últimamente
5/6/23, 22:03 - Marina🦟: pues va de lujo
5/6/23, 22:03 - Marina🦟: acabo d cenar
5/6/23, 22:03 - Marina🦟: y estoy en la cama
5/6/23, 22:29 - laura: ya me voy a casa xfin
5/6/23, 22:29 - laura: me muero de hambre la vd
5/6/23, 22:29 - laura: esq cuando estoy de entrgas no me da tiempo ni de comer
5/6/23, 22:32 - laura: me he pateado toda la diagonal alucini
5/6/23, 22:34 - Marina🦟: ya veo ya
5/6/23, 22:34 - Marina🦟: y eso???
5/6/23, 22:39 - laura: porq el starbucks quedaba al quinto coño d la parada de mtro
5/6/23, 22:39 - laura: hoy tb has visto la serie de médicos??
5/6/23, 22:44 - Marina🦟: que te has cogido???
5/6/23, 22:54 - laura: no, solo me he cogido un café
5/6/23, 22:55 - Marina🦟: vaya
5/6/23, 22:55 - Marina🦟: que mala suerte la tuya
5/6/23, 22:55 - Marina🦟: jajajajajaja
5/6/23, 22:55 - Marina🦟: ahhh estabas ahí
5/6/23, 22:56 - Marina🦟: como???
5/6/23, 22:59 - laura: no me gustaba
5/6/23, 22:59 - laura: ahí estaba sí
5/6/23, 23:03 - Marina🦟: otra vez será
5/6/23, 23:03 - Marina🦟: podrías, si
5/6/23, 23:03 - Marina🦟: mmm en realidad no suelo bajar al perro
5/6/23, 23:03 - Marina🦟: pero el otro día me dejaron sola
5/6/23, 23:03 - Marina🦟: y me tocó
5/6/23, 23:17 - laura: voy a subir el monte vale???
5/6/23, 23:19 - Marina🦟: no hace falta q lo digas
5/6/23, 23:19 - Marina🦟: aunq igual m equivoco
5/6/23, 23:20 - Marina🦟: obvio
5/6/23, 23:20 - Marina🦟: cuidadin
5/6/23, 23:57 - laura: aún tengo q acabar un vídeo
5/6/23, 23:58 - laura: estoy reventadita
6/6/23, 0:05 - Marina🦟: yo???
6/6/23, 0:05 - Marina🦟: no hago nada
6/6/23, 0:05 - Marina🦟: no estoy siendo mosquito
6/6/23, 0:05 - Marina🦟: que t queda???
6/6/23, 0:23 - laura: un poquito pero bueno
6/6/23, 0:23 - laura: jajajsjjaajjsjajaj
6/6/23, 0:24 - laura: un storyboard, sabes o no sabes??
6/6/23, 0:24 - laura: me estoy sobando encima del ordenador
6/6/23, 0:28 - Marina🦟: bueno entonces me iré a dormir y así no t molesto
6/6/23, 0:29 - Marina🦟: yo no, pero google si
6/6/23, 0:29 - Marina🦟: ahora ya se lo q es jejej
6/6/23, 0:37 - Marina🦟: como una secuencia d imágenes q t ayudan a entender la historia
6/6/23, 0:37 - Marina🦟: lo he explicado bien?
6/6/23, 0:37 - Marina🦟: cuando dejes de estar tan ocupada
6/6/23, 0:52 - Marina🦟: se ha cagado el perro en la cocina y casi poto recogiéndolo
6/6/23, 0:53 - Marina🦟: ahora tng el olor a mierda metido en la nariz
6/6/23, 8:04 - laura: hoy vas no?? se te acaba el chollo
6/6/23, 8:28 - Marina🦟: q mas entregas tienes???
6/6/23, 8:28 - Marina🦟: o no
6/6/23, 8:28 - Marina🦟: si tío
6/6/23, 8:28 - Marina🦟: estoy esperando el bus
6/6/23, 8:28 - Marina🦟: voy tarde para variar
6/6/23, 12:13 - laura: no entras a las 9??
6/6/23, 12:14 - laura: ya he presentado mi pedazo de trabajo
6/6/23, 14:01 - Marina🦟: xfa
6/6/23, 14:01 - Marina🦟: lo estoy esperando
6/6/23, 14:01 - Marina🦟: o no, quien sabeeee
6/6/23, 14:01 - Marina🦟: si jajajajjaja
6/6/23, 14:01 - Marina🦟: he llegado a y media
6/6/23, 14:02 - Marina🦟: no pasa nada
6/6/23, 14:02 - Marina🦟: como ha ido????
6/6/23, 14:02 - Marina🦟: yo acabo d salir
6/6/23, 14:02 - Marina🦟: tengo un hambre q m muero
6/6/23, 15:41 - Marina🦟: lauraaaaaaa
6/6/23, 16:24 - laura: super bn 
6/6/23, 16:24 - laura: tu frase de cada día
6/6/23, 16:25 - laura: jajajjajjjajajajajaj marinaaaaaaaaa
6/6/23, 16:25 - laura: estas durmiendo??
6/6/23, 16:25 - laura: yo me he tenido q quedar en la uni hoy tb
6/6/23, 17:28 - Marina🦟: t quería molestar
6/6/23, 17:28 - Marina🦟: pero entre q no m haces ni caso y era la hora d la siesta
6/6/23, 17:28 - Marina🦟: jajajajajajajajajajaja
6/6/23, 17:28 - Marina🦟: me han llamado los del departamento d las prácticas d mi ciclo y m han despertado
6/6/23, 17:28 - Marina🦟: estoy enfadada
6/6/23, 17:28 - Marina🦟: jajajajajajaba
6/6/23, 20:09 - laura: q te han dicho???
6/6/23, 20:58 - Marina🦟: vaya siesta m he pegao
6/6/23, 20:58 - Marina🦟: todavía estás ahí????
6/6/23, 21:09 - Marina🦟: exijo q acabes ya los trabajos
6/6/23, 21:57 - laura: yaaaaaaaaa me voy
6/6/23, 21:57 - laura: mañana más y mejor encima tngo examen esq genial
6/6/23, 21:58 - laura: de cuántas horas estamos hablando a ver
6/6/23, 22:03 - Marina🦟: de queee
6/6/23, 22:03 - Marina🦟: pues en vd no muchas porq me han despertado pero he dormido muy profundo
6/6/23, 22:03 - Marina🦟: ha sido como 1h y media
6/6/23, 22:03 - Marina🦟: jajajajajajajjaajaja eres idiota
6/6/23, 22:03 - Marina🦟: vuelve a escucharlo
6/6/23, 22:04 - Marina🦟: he ido al gym tb
6/6/23, 22:04 - Marina🦟: y ahora he cenado y m voy a duchar
6/6/23, 23:29 - laura: y yo q estudio para mañana
6/6/23, 23:30 - laura: ahora q estoy reflexionando
6/6/23, 23:32 - Marina🦟: como q q estudias?
6/6/23, 23:32 - Marina🦟: pues el examen q tienes estaría bien
6/6/23, 23:41 - laura: jajajjajajajajaj
7/6/23, 7:56 - Marina🦟: buenos diasssss
7/6/23, 7:56 - Marina🦟: pf me quedé ko
7/6/23, 7:56 - Marina🦟: y tng un sueño q m muero
7/6/23, 8:03 - Marina🦟: te acostaste muy tarde tu??
7/6/23, 8:34 - Marina🦟: me he dormido en el bus
7/6/23, 10:05 - laura: buenos diaaaas
7/6/23, 10:05 - laura: no puedo cn mi vida
7/6/23, 10:07 - laura: como q te has dormido??? has llegado tarde otra vez?
7/6/23, 10:28 - Marina🦟: lo hago por ti
7/6/23, 10:28 - Marina🦟: para que veas que te tengo presente
7/6/23, 10:29 - Marina🦟: nooooo
7/6/23, 10:29 - Marina🦟: me he dormido en el bus
7/6/23, 10:29 - Marina🦟: bua es que lo estoy pasando mal eh
7/6/23, 10:29 - Marina🦟: se me cierran los ojos
7/6/23, 10:29 - Marina🦟: y tengo un hambre que no pud mes
7/6/23, 10:44 - Marina🦟: suerte cn el examen🫶🏽
7/6/23, 12:25 - laura: anda va
7/6/23, 12:25 - laura: has rezado??
7/6/23, 12:28 - laura: q tal tu mañana??
7/6/23, 15:27 - Marina🦟: sisi que participo, en realidad solo es para comentar cosas q hemos hecho durante la semana cn el proyecto o si necesitamos ayuda cn algo etc
7/6/23, 15:27 - Marina🦟: ya he comido jjjj
7/6/23, 15:27 - Marina🦟: adivina q toca
7/6/23, 15:33 - laura: MACARRONES
7/6/23, 15:34 - Marina🦟: siesta idiota
7/6/23, 15:37 - laura: estábamos hablando de comer i
7/6/23, 15:38 - laura: sabes q hoy yo tb me la puedo echar???
7/6/23, 15:39 - Marina🦟: pero siesta d cuantas horas?
7/6/23, 15:42 - laura: pues no tantas como tu
7/6/23, 15:43 - Marina🦟: q tienes mañana?
7/6/23, 15:49 - laura: mockups y más mockups
7/6/23, 15:49 - Marina🦟: ah vale
7/6/23, 15:49 - Marina🦟: lo tendré en cuenta
7/6/23, 15:50 - Marina🦟: te quedan 2 diasssss solo
7/6/23, 15:50 - Marina🦟: no??
7/6/23, 15:55 - laura: no del todo:(
7/6/23, 15:56 - laura: me queda el lunes el trabajo final q me va a acabar de matar
7/6/23, 15:57 - Marina🦟: bueno pero ya casi
7/6/23, 18:54 - Marina🦟: m estás ignorando o t has pegado una siesta de 3h como yo?
7/6/23, 18:56 - laura: no puede ser
7/6/23, 18:56 - laura: me acabo de levantar a la vez
7/6/23, 18:57 - laura: madremia me he quedado frita
7/6/23, 18:57 - laura: q hago
7/6/23, 18:57 - laura: mira q te he dicho q 3 horas no
7/6/23, 19:02 - laura: q no quiero trabajar más tío
7/6/23, 19:06 - Marina🦟: diosssss se te ha ido d las manos eh jajajajajajjajajaja
7/6/23, 19:06 - Marina🦟: te han echado bronca??
7/6/23, 19:07 - Marina🦟: una cosa estudiar esta sobrevalorado sigue durmiendo
7/6/23, 19:07 - Marina🦟: JAJAJAJAJ es broma
7/6/23, 19:07 - Marina🦟: espabila
7/6/23, 19:07 - Marina🦟: yo m voy al gym
7/6/23, 19:24 - laura: la vd es q si, no te voy a mentir
7/6/23, 19:28 - Marina🦟: son tus madres???? jajajajajaj
7/6/23, 19:28 - Marina🦟: puede ser
7/6/23, 19:28 - Marina🦟: yo m voy apuntando cosas
7/6/23, 19:28 - Marina🦟: a tener en cuenta
7/6/23, 19:28 - Marina🦟: jajajajajajajaaja
7/6/23, 19:28 - Marina🦟: mala suerte
7/6/23, 19:28 - Marina🦟: t aguantas
7/6/23, 19:47 - Marina🦟: oye tú tienes q hacer prácticas d lo tuyo??
7/6/23, 19:47 - Marina🦟: x casualidad
7/6/23, 19:55 - laura: necesitan a alguien en tu empresa??
7/6/23, 19:55 - laura: me has enganchado lo de poner tantos interrogantes
7/6/23, 19:58 - Marina🦟: están buscando gente d prácticas d diseño
7/6/23, 20:00 - Marina🦟: no te van a pagar nada pero ahí siempre hay posibilidad d quedarse si t lo curras
7/6/23, 20:07 - laura: pues en este caso las tengo convalidadas
7/6/23, 20:15 - Marina🦟: siiii porque no estaríamos en el mismo sitio
7/6/23, 21:04 - laura: voy a ir a ver a mis abuelos q ya se están quejando
7/6/23, 21:19 - Marina🦟: siii ya estoy en casa
7/6/23, 21:19 - Marina🦟: voy al gym pa esto
7/6/23, 21:34 - Marina🦟: eres fit?
7/6/23, 21:34 - Marina🦟: yo soy más bien fat jajajajajajajjajaja
7/6/23, 21:41 - laura: me cuesta la vida controlarme
7/6/23, 21:42 - Marina🦟: todavía no lo sé
7/6/23, 21:42 - Marina🦟: a mi hermana????? joe
7/6/23, 21:42 - Marina🦟: jajajajajajajajaja
7/6/23, 21:43 - Marina🦟: m representa
7/6/23, 21:43 - Marina🦟: que redflag más fea
7/6/23, 22:47 - Marina🦟: stassssss estudiando?
7/6/23, 22:48 - Marina🦟: o haciendo ver q estudias almenos?
7/6/23, 22:55 - laura: hoy no toca estudiar gracias a dios
7/6/23, 22:56 - Marina🦟: 0 fijo
7/6/23, 22:56 - Marina🦟: esta del revés el cartel
7/6/23, 22:56 - Marina🦟: yo m voy a poner mi serie d medicossss
7/6/23, 22:56 - Marina🦟: un ratito
7/6/23, 22:57 - laura: tengo uno
7/6/23, 22:57 - laura: jajajjajajjajajajajaj pensaba q no te darías cuenta
7/6/23, 22:58 - laura: voy a mirar como cojones se pone esto bien
7/6/23, 22:58 - Marina🦟: a verlo
7/6/23, 22:58 - Marina🦟: no, es q soy tonta
7/6/23, 23:00 - Marina🦟: sabes qqqq
7/6/23, 23:01 - laura: no puedo
7/6/23, 23:01 - laura: estoy provando vale??jajajajajjajaja
7/6/23, 23:01 - laura: a ver qué
7/6/23, 23:04 - Marina🦟: porque no puedes?
7/6/23, 23:04 - Marina🦟: si estás probando cn v vale
7/6/23, 23:04 - Marina🦟: te dejo q prueves
7/6/23, 23:04 - Marina🦟: nada es q m aburrooooo
7/6/23, 23:07 - laura: jajajajjajajajajajaja me he liado vale 
7/6/23, 23:07 - laura: q estoy hablando en catalán 
7/6/23, 23:07 - laura: y va cn v
7/6/23, 23:23 - laura: tampco puedo esto cn android?
7/6/23, 23:25 - Marina🦟: JAJAJAJAJAJ si puedes
7/6/23, 23:25 - Marina🦟: mantén pulsada la a
7/6/23, 23:25 - Marina🦟: o almenos yo lo hago así
7/6/23, 23:34 - Marina🦟: ehhhhh si
7/6/23, 23:36 - Marina🦟: acabo d matar a un mosquito
7/6/23, 23:36 - Marina🦟: m quería picar
7/6/23, 23:42 - Marina🦟: una abejita seguro m quiere picar
7/6/23, 23:42 - Marina🦟: jajajajajajajajajajaja
7/6/23, 23:42 - Marina🦟: ay
7/6/23, 23:42 - Marina🦟: toy cansada
8/6/23, 0:01 - laura: estas series de malas influencias miras???
8/6/23, 0:05 - Marina🦟: lo has leído cantando? di q si
8/6/23, 0:05 - Marina🦟: valeria es mucho mejor???
8/6/23, 0:17 - laura: sí, además no una vez no, q la he cantado cmo 3 jajajsajajajajj
8/6/23, 0:50 - laura: puedes encontrar referentes en tu serie
8/6/23, 1:18 - Marina🦟: jajajajajajajajajajja
8/6/23, 1:18 - Marina🦟: tío las 2 d la mañana paso
8/6/23, 1:18 - Marina🦟: es q no puedo dormir
8/6/23, 1:18 - Marina🦟: cn la siesta q m he pegado
8/6/23, 1:18 - Marina🦟: soy gilipollas
8/6/23, 1:21 - laura: bueno algo q no sepamos? gcs
8/6/23, 1:22 - laura: inténtalo
8/6/23, 1:25 - laura: me acaba de medir mi hermano
8/6/23, 1:25 - laura: me he encogido
8/6/23, 1:25 - Marina🦟: casi
8/6/23, 1:26 - Marina🦟: en cuanto m de cuenta son las 2
8/6/23, 1:26 - Marina🦟: JAJAJAJAJAJAAJ
8/6/23, 1:26 - Marina🦟: gcs a ti
8/6/23, 1:26 - Marina🦟: cuanto???
8/6/23, 1:26 - Marina🦟: no t ha preguntado tu hermano q porque razón t estás midiendo a la 1 y media d la madrugada????
8/6/23, 1:30 - laura: adivina
8/6/23, 1:33 - Marina🦟: 1,60????
8/6/23, 1:49 - Marina🦟: súper importante
8/6/23, 1:49 - Marina🦟: bua estoy q a punto q m duermo ehhhh
8/6/23, 1:49 - Marina🦟: voy a apagar el mvl jajajajajajajajaja
8/6/23, 7:54 - Marina🦟: me quedé sobadisima
8/6/23, 7:54 - Marina🦟: no aguantaba más ya
8/6/23, 7:55 - Marina🦟: he dormido fatal
8/6/23, 7:55 - Marina🦟: el puto colchón
8/6/23, 7:55 - Marina🦟: hoy m compro otro
8/6/23, 7:58 - Marina🦟: acabaste muy tarde??
8/6/23, 9:06 - laura: buenos diass
8/6/23, 9:06 - laura: a las 3
8/6/23, 9:06 - laura: hoy tengo una mala noticia...
8/6/23, 9:18 - Marina🦟: ehhh
8/6/23, 9:18 - Marina🦟: que mala noticia????
8/6/23, 12:17 - laura: porq me tengo q quedar todo el día:(
8/6/23, 12:18 - laura: como va curranta
8/6/23, 14:08 - Marina🦟: triste
8/6/23, 14:09 - Marina🦟: que tal tu???
8/6/23, 15:52 - laura: q bus??? una cosa esq aún no entiendo tu recorrido para venir a bcn jjaajjajajajja
8/6/23, 15:53 - laura: fatal me duele la cabeza
8/6/23, 18:40 - Marina🦟: q voy a ver a mi mejor amigo
8/6/23, 18:40 - Marina🦟: que es su cumple
8/6/23, 19:50 - Marina🦟: como vas tú???
8/6/23, 20:11 - laura: ahhhh q no coges tren ara me entero
8/6/23, 20:12 - laura: felicítalo de mi parte
8/6/23, 20:12 - laura: me quiero ir
8/6/23, 20:21 - Marina🦟: si ya t lo expliqué
8/6/23, 20:21 - Marina🦟: no m escuchas nada
8/6/23, 20:21 - Marina🦟: pero ya t queda poco, no???
8/6/23, 20:49 - laura: si, ya estoy en el tren😌
8/6/23, 20:50 - Marina🦟: si q t lo he explicado pero okkkk
8/6/23, 20:50 - Marina🦟: biennnn
8/6/23, 20:52 - laura: solo me dijiste q cogías un bus para ir a la estación pero okkkkk
8/6/23, 20:52 - laura: q es eso una sesión de belleza????
8/6/23, 21:00 - Marina🦟: te dije q antes iba en coche a la estación
8/6/23, 21:00 - Marina🦟: mi hermana les está haciendo el lifting a mis amigas
8/6/23, 21:03 - Marina🦟: mañana q tienes???
8/6/23, 21:10 - laura: examen
8/6/23, 21:10 - laura: q te parece??
8/6/23, 21:16 - Marina🦟: pero no t quedas todo el día ahí, no???
8/6/23, 21:16 - Marina🦟: otro examen???
8/6/23, 21:28 - laura: si, de un comentario de texto
8/6/23, 21:28 - laura: has hecho bachillerato???
8/6/23, 21:28 - laura: me enseñas??
8/6/23, 21:50 - Marina🦟: te enseñaría si m acordara como se hace
8/6/23, 21:50 - Marina🦟: pero no es el caso
8/6/23, 22:07 - Marina🦟: holaaaaaa
8/6/23, 22:07 - Marina🦟: jajajajajajajajajajajaja
8/6/23, 22:07 - Marina🦟: hoy si aguanto t hago compañía un ratito más
8/6/23, 22:07 - Marina🦟: q mañana no madrugo tanto
8/6/23, 22:10 - laura: has dormido hoy???? porq yo estoy muerta:(
8/6/23, 22:11 - laura: voy a suspendeeer tiooooo
8/6/23, 22:11 - laura: no sé escribirrrrrr
8/6/23, 22:16 - Marina🦟: un poquito pero no mucho
8/6/23, 22:16 - Marina🦟: que tienes q escribir a ver
8/6/23, 22:16 - Marina🦟: que t ayudo
8/6/23, 22:27 - laura: ahora nada
8/6/23, 22:45 - Marina🦟: por cierto
8/6/23, 22:45 - Marina🦟: sabes q x alguna razón q desconozco 
8/6/23, 22:45 - Marina🦟: mi hermano mayor t sigue en instagram
8/6/23, 22:45 - Marina🦟: jajajajajajajajajajajajaja
8/6/23, 22:49 - laura: jajajjajajajajajajaja queeeeeeeeee
8/6/23, 22:49 - laura: q dices
8/6/23, 22:49 - laura: quién es
8/6/23, 22:49 - laura: ahora me estas dejando loca
8/6/23, 22:50 - Marina🦟: un frikazo
8/6/23, 22:50 - Marina🦟: este
8/6/23, 22:54 - laura: ya sé quién es...
8/6/23, 22:57 - laura: pero es tu hermano de sangre sangre??
8/6/23, 22:58 - Marina🦟: a ver
8/6/23, 22:58 - Marina🦟: LOS APELLIDOS NO T DICEN NADA? jajajajajajajajjajajaaja
8/6/23, 23:00 - laura: si no sé ni su cara
8/6/23, 23:00 - Marina🦟: es feo
8/6/23, 23:00 - Marina🦟: jajajajajaajjajajajajajaja
8/6/23, 23:00 - Marina🦟: no t pega
8/6/23, 23:17 - laura: a qué hora te levantas mañana??
8/6/23, 23:17 - Marina🦟: a las 9
8/6/23, 23:17 - Marina🦟: y tu???
8/6/23, 23:20 - laura: más o menos igual jejej
8/6/23, 23:28 - laura: YA SÉ DE Q ME SUENA TU HERMANO
8/6/23, 23:29 - Marina🦟: ahora que dices esto
8/6/23, 23:29 - Marina🦟: antes estaba pensando
8/6/23, 23:30 - Marina🦟: SORPRÉNDEME
8/6/23, 23:33 - laura: esq juraría q iba a mi cole dónde mi ciclo
8/6/23, 23:33 - laura: dónde estudió??
8/6/23, 23:35 - Marina🦟: bua en rubí creo
8/6/23, 23:35 - Marina🦟: edra o algo así?
8/6/23, 23:35 - Marina🦟: no m acuerdo
8/6/23, 23:37 - laura: jajajajjjjjaajaja siiiiiiiiiiiii
8/6/23, 23:37 - laura: ahí iba yo
8/6/23, 23:37 - laura: no me lo puedo creer
8/6/23, 23:39 - Marina🦟: QUEEEE
8/6/23, 23:39 - Marina🦟: JAJJAJAJAJJAA
8/6/23, 23:39 - Marina🦟: flipo
8/6/23, 23:41 - laura: esq me sonaba un montón el nombre de insta
8/6/23, 23:42 - Marina🦟: nunca acabó ese ciclo
8/6/23, 23:42 - Marina🦟: le faltaban las prácticas o yoquese
8/6/23, 23:43 - Marina🦟: mi hermano es un caso perdido jajajajajajajaja
8/6/23, 23:45 - Marina🦟: porq el mundo esta tan conectado no entiendo
8/6/23, 23:46 - Marina🦟: una cosa m puedes seguir en tiktok para mandarte vídeos? gcs
8/6/23, 23:46 - Marina🦟: necesito q entiendas mis referencias d tiktok cuando hablo
8/6/23, 23:51 - laura: a ver dime como te busco
8/6/23, 23:52 - laura: q yo y las tecnologías mal
8/6/23, 23:53 - Marina🦟: te he solicitado seguirte
8/6/23, 23:54 - Marina🦟: ahora dirás
8/6/23, 23:54 - Marina🦟: como m has encontrado
8/6/23, 23:54 - Marina🦟: y yo diré
8/6/23, 23:54 - Marina🦟: que es un secreto
8/6/23, 23:54 - Marina🦟: jajajajajajajajajajajaja
8/6/23, 23:56 - laura: esq no lo entiendo
8/6/23, 23:56 - Marina🦟: JAJAJJAAJ
8/6/23, 23:57 - Marina🦟: es simple
8/6/23, 23:57 - Marina🦟: t lo voy a explicar vale????
8/6/23, 23:57 - laura: esq no tngo ni nombre
8/6/23, 23:57 - Marina🦟: no soy una sociopata ni nada
8/6/23, 23:57 - Marina🦟: no t asustes
8/6/23, 23:57 - laura: jajajajjajajajajajajajjajajaj
8/6/23, 23:57 - laura: a ver explícamelo
8/6/23, 23:57 - Marina🦟: el otro día te mandé un vídeo de tiktok
8/6/23, 23:57 - Marina🦟: y cuando alguien abre un vídeo dsd un link q le has mandado
8/6/23, 23:57 - Marina🦟: en la actividad d tiktok
8/6/23, 23:58 - Marina🦟: t sale una notificación
8/6/23, 23:58 - Marina🦟: que pone
8/6/23, 23:58 - Marina🦟: xxxx ha visto el vídeo que has compartido
8/6/23, 23:58 - Marina🦟: y x eso he encontrado tu tiktok
8/6/23, 23:59 - laura: alaaaaaaaaaa
8/6/23, 23:59 - laura: q eso ya lo sabía
8/6/23, 23:59 - laura: se me olvidó🙄
9/6/23, 0:01 - Marina🦟: JAJAJAJAJAJ
9/6/23, 0:01 - Marina🦟: tb t digo que
9/6/23, 0:01 - Marina🦟: soy un poco fbi
9/6/23, 0:01 - Marina🦟: descubro cosas q nadie descubre
9/6/23, 0:01 - Marina🦟: debería haber estudiado eso
9/6/23, 0:01 - Marina🦟: m siento realizada cuando hago descubrimientos d salseo
9/6/23, 0:06 - laura: yo eso tb me entero de todo jsjsjsjsj
9/6/23, 0:06 - laura: q bonito saludo
9/6/23, 0:19 - Marina🦟: hoy no tengo mucho sueño
9/6/23, 0:19 - Marina🦟: y tu t vas a quedar dormida en cualquier momento
9/6/23, 0:27 - Marina🦟: nunca t has ido a dormir a las 11
9/6/23, 0:30 - laura: jajajajjajajaj efectivamente, tampoco me voy de normal
9/6/23, 0:30 - laura: pero antes a las 11 te he dicho q iba a caer
9/6/23, 0:32 - Marina🦟: lees para dormir?
9/6/23, 0:34 - laura: pues no
9/6/23, 0:34 - laura: la vd es q no
9/6/23, 0:34 - Marina🦟: no tenías pinta d leer 
9/6/23, 0:36 - laura: me puedes explicar de q tengo pinta????
9/6/23, 0:38 - Marina🦟: de friki q juega al fortnite
9/6/23, 0:38 - Marina🦟: jajajajajajajajajajajjajajajajajajajaja
9/6/23, 0:45 - Marina🦟: una cosa hoy pienso dormir en el sofá porq ayer dormí fatal en la cama
9/6/23, 1:02 - Marina🦟: t has dormido…
9/6/23, 9:13 - laura: me quedé muerta:(
9/6/23, 9:14 - laura: ahora voy a repasar un pco antes del examen
9/6/23, 9:14 - laura: porqué miedo me da
9/6/23, 9:14 - laura: hoy teletrabajas no??
9/6/23, 9:20 - Marina🦟: ya no lo voy a decir mas
9/6/23, 9:21 - Marina🦟: jajajajajajajajajajajaja
9/6/23, 9:21 - Marina🦟: lo llevas regulinchi, mal o fatal?
9/6/23, 9:25 - laura: regulinchi, mal y fatal
9/6/23, 9:25 - laura: pero me las apañaré
9/6/23, 9:27 - Marina🦟: confío en ti
9/6/23, 9:27 - Marina🦟: a q hora lo tienes???
9/6/23, 9:53 - Marina🦟: cuando tengas un rato dsps del examen m prestas atención un momento q necesito ayuda cn una cosa del mac xfinssssss
9/6/23, 10:30 - laura: 11:30
9/6/23, 10:30 - laura: y la distancia de seguridad????
9/6/23, 10:30 - laura: dime q necesitas
9/6/23, 10:30 - laura: puede esperar 2 horitas o es una cuestión de vida o muerte??
9/6/23, 10:36 - Marina🦟: puedo esperar tranqui
9/6/23, 10:36 - Marina🦟: es una chorrada
9/6/23, 10:36 - Marina🦟: vas a estar dos horas sin hablarme????☹️
9/6/23, 10:36 - Marina🦟: triste
9/6/23, 10:51 - Marina🦟: a ver
9/6/23, 10:51 - Marina🦟: que tengo abiertas varias páginas de chrome
9/6/23, 10:51 - Marina🦟: y quiero que me salgan aquí:
9/6/23, 10:51 - Marina🦟: bueno en el dock
9/6/23, 10:51 - Marina🦟: para no tener que estar cambiando todo el rato
9/6/23, 10:51 - Marina🦟: y no se como se hace
9/6/23, 10:51 - Marina🦟: ns si m he explicado
9/6/23, 10:51 - Marina🦟: jajajajjajajajajajajaja
9/6/23, 10:56 - laura: x lo q he entendido
9/6/23, 10:56 - laura: el chrome no te sale en las aps de abajo del escritorio
9/6/23, 10:56 - laura: no???
9/6/23, 10:57 - Marina🦟: o sea si me sale el chrome
9/6/23, 10:57 - Marina🦟: espera
9/6/23, 10:57 - Marina🦟: ahora t hago un vídeo explicativo vale?
9/6/23, 10:57 - laura: jajajajajajajajajja
9/6/23, 10:57 - laura: vale va
9/6/23, 10:58 - laura: aunq alomejor no sé hacerlo, pero bueno lo importante es participar
9/6/23, 10:59 - Marina🦟: lo importante no es ganar es ganar
9/6/23, 11:05 - Marina🦟: he dicho pestañas 80 veces
9/6/23, 11:08 - laura: jajajajajajajajajajjajajaja
9/6/23, 11:09 - laura: a mi se sale solo eso
9/6/23, 11:09 - laura: pero a ver
9/6/23, 11:09 - laura: prueba de tirar cn tres dedos para arriba
9/6/23, 11:09 - laura: desliza
9/6/23, 11:09 - laura: q tb me sale así
9/6/23, 11:10 - Marina🦟: o sea si así me sale pero yo lo quiero en el dock
9/6/23, 11:11 - laura: entonces vete a cualquier pestaña de chrome
9/6/23, 11:12 - laura: botón derecho y fijar creo
9/6/23, 11:12 - Marina🦟: se me fija en la barra de marcadores
9/6/23, 14:06 - Marina🦟: perdonnn que estoy haciendo la comida
9/6/23, 14:06 - Marina🦟: ya tienes idea d lo q t vas a comprar???
9/6/23, 14:06 - Marina🦟: el miércoles es tu cumples es vd
9/6/23, 14:07 - Marina🦟: es q el sábado tengo bbq y fiesta por la noche para celebrar el cumple d mi mejor amigo
9/6/23, 14:07 - Marina🦟: y domingo entre q estaré ko y dicen d ir a la milonga
9/6/23, 14:07 - Marina🦟: no sé si me quedará algún rato
9/6/23, 14:09 - Marina🦟: mañana tng otra bbq cn los del trabajo
9/6/23, 14:09 - Marina🦟: y el domingo no creo q haga gran cosa
9/6/23, 14:12 - laura: q haces de comer?
9/6/23, 14:24 - Marina🦟: yessssss de vd
9/6/23, 14:24 - Marina🦟: póntelo en el calendario
9/6/23, 14:24 - Marina🦟: pues para mi arroz cn atún y huevo
9/6/23, 14:24 - Marina🦟: para mis hermanos nuggrts cn patatas
9/6/23, 14:24 - Marina🦟: y para mi madre y mi padre espárragos cn gambas
9/6/23, 14:25 - Marina🦟: no se se piensan que es un buffet
9/6/23, 14:27 - Marina🦟: tu que fas???
9/6/23, 14:27 - Marina🦟: que más tienes hoy?
9/6/23, 14:52 - laura: y tu hermano el de mi cole no se lo puede hacer él???
9/6/23, 14:52 - laura: res esq tinc son saps
9/6/23, 14:52 - laura: llevo dos semanas cn unas ojeras q madremia
9/6/23, 14:53 - laura: tengo q acabar unas fichas de grupo pero me he ido a casa a hacerlo
9/6/23, 14:56 - Marina🦟: no vive en mi casa jajajajajajaja
9/6/23, 14:56 - Marina🦟: se lo he hecho a los pequeños
9/6/23, 14:56 - Marina🦟: ahhh pensaba q t quedabas ahí
9/6/23, 14:56 - Marina🦟: yo acabo d comer
9/6/23, 14:57 - Marina🦟: está lloviendo q flipas
9/6/23, 15:14 - laura: enserio???? aquí hace un sol q flipas
9/6/23, 15:31 - Marina🦟: vas a dormir???
9/6/23, 15:35 - laura: un poquito creo jjsjsj
9/6/23, 15:35 - laura: i tu??? nose pa q pregunto
9/6/23, 15:36 - laura: perdon y*
9/6/23, 15:39 - Marina🦟: mmm ahora mismo no tengo sueño pero igual caigo
9/6/23, 15:48 - laura: a q hora te fuiste a dormir??
9/6/23, 15:52 - Marina🦟: pues cuando dejaste d contestarme jajajajajajajaja
9/6/23, 15:53 - Marina🦟: dormí en el sof
9/6/23, 16:00 - Marina🦟: hoy hemos comprado el colchón
9/6/23, 16:00 - Marina🦟: a ver cuando llega
9/6/23, 16:37 - laura: tngo q acabar las fichas sobretodo
9/6/23, 16:37 - laura: q mi amiga me mata q son para hoy a las 12
9/6/23, 16:38 - laura: y tengo q dormir q estoy reventada
9/6/23, 16:40 - Marina🦟: vaaaaale
9/6/23, 16:40 - Marina🦟: me esperaré
9/6/23, 16:40 - Marina🦟: pero si terminas pronto
9/6/23, 16:41 - Marina🦟: dímelo
9/6/23, 19:02 - laura: mientras tu te vas al gym me voy a poner en serio cn eso
9/6/23, 20:26 - Marina🦟: dice q m quedan dos ejercicios
9/6/23, 20:26 - Marina🦟: paso
9/6/23, 20:26 - Marina🦟: como vassss
9/6/23, 20:45 - laura: aquí estoy de videollamada
9/6/23, 20:45 - laura: hems avanzado bastante
9/6/23, 20:46 - Marina🦟: t dará tiempo??
9/6/23, 21:25 - laura: q has hecho hoy q no has dormido??? flipo
9/6/23, 21:25 - laura: si la niña tiene sueño lo aplazamos
9/6/23, 21:30 - Marina🦟: pues he visto la serie y me he lavado el pelo para no tener q lavármelo ahora e ir mas rápido
9/6/23, 21:31 - Marina🦟: oye en tu pueblo los paquis a q hora cierran?
9/6/23, 21:31 - Marina🦟: porq la última vez q fui a las 10 estaban ya caput
9/6/23, 21:39 - laura: muy bien q previsora eres
9/6/23, 21:39 - laura: tranqui yo tengo cervezas
9/6/23, 21:40 - laura: a ver si acabamos ya esta mierda
9/6/23, 21:48 - Marina🦟: chachiiii
9/6/23, 21:48 - Marina🦟: yo estoy esperando q mi hermana salga d la ducha para poder ducharme yo🙃
9/6/23, 22:03 - Marina🦟: cuando t quede poco avísame para arreglarme
9/6/23, 22:10 - laura: vale espera ya va quedando poco pero queda un poco
9/6/23, 22:13 - Marina🦟: bueno m voy planchando el pelo q luego aún tengo media h d camino
9/6/23, 22:13 - Marina🦟: lo rajo yo también
9/6/23, 22:44 - laura: vale ya estoy no me mates
9/6/23, 22:44 - laura: vale???
9/6/23, 22:44 - Marina🦟: t odio
9/6/23, 22:44 - Marina🦟: estaba quedándome ya sobada
9/6/23, 22:44 - Marina🦟: m visto pues
9/6/23, 22:45 - Marina🦟: hace frío en tu pueblucho?
9/6/23, 22:46 - laura: nooooo
9/6/23, 22:47 - laura: de momento no pero luego seguro
9/6/23, 22:58 - laura: avísame cuando estes viniendo vale? gcs
9/6/23, 22:58 - laura: voy a la ducha rapidosima
9/6/23, 23:04 - Marina🦟: cojo el bolso y salgo
9/6/23, 23:05 - laura: cojo una cerva
9/6/23, 23:05 - laura: bueno cojo 4
9/6/23, 23:06 - laura: jsjsjjj
9/6/23, 23:08 - Marina🦟: si mejor
9/6/23, 23:08 - Marina🦟: jajajajajjaajajjaa
9/6/23, 23:08 - Marina🦟: y pañuelos tienes?
9/6/23, 23:08 - Marina🦟: q soy d mear fácil cuando bebo cerveza
9/6/23, 23:09 - laura: creo q si
9/6/23, 23:09 - laura: espera q busco
9/6/23, 23:09 - Marina🦟: tendría q haber cogido las gafas porque no veo una mierda
9/6/23, 23:09 - Marina🦟: pero bueno
9/6/23, 23:09 - laura: y q haces q no las coges
9/6/23, 23:09 - laura: las puedes coger????
9/6/23, 23:09 - Marina🦟: se me han olvidado
9/6/23, 23:09 - Marina🦟: ya no voy a subir
9/6/23, 23:09 - laura: eres tonta o que
9/6/23, 23:10 - Marina🦟: a ver q si veo no m voy a estampar jajajajajajajajaja
9/6/23, 23:10 - Marina🦟: pero veo mal
9/6/23, 23:12 - laura: no me fío
9/6/23, 23:12 - laura: nos vamos a estampar
9/6/23, 23:12 - laura: si tienes dioctrias
9/6/23, 23:18 - Marina🦟: no problem
9/6/23, 23:18 - Marina🦟: hay unos relámpagos q real
9/6/23, 23:18 - Marina🦟: tela
9/6/23, 23:20 - laura: enserio???? flipo
10/6/23, 4:15 - laura: no puede ser
10/6/23, 4:15 - laura: las boquillas
10/6/23, 4:15 - Marina🦟: baja

"""

def parse_messages(conversation):
    messages = []
    lines = conversation.strip().split('\n')
    for line in lines:
        parts = re.split(r".:", line, maxsplit=2)
        
        if len(parts) >= 3:
            timestamp, propiedad, message = parts
            messages.append((timestamp.strip(), propiedad.strip(), message.strip()))
    return messages

# Ejemplo de análisis de similitud de texto
def analizar_similitud(texto1, texto2):
    doc1 = nlp(texto1)
    doc2 = nlp(texto2)
    similitud = doc1.similarity(doc2)
    return similitud


#print(parse_messages(conversation))
def respuesta(responderle):
    similar = 0
    loc = 0
    for i, menssages in enumerate(parse_messages(conversation)):
        similitud = analizar_similitud(responderle, menssages[2])
        if similitud > similar:
            similar = similitud
            loc = i
            

    return parse_messages(conversation)[loc + 2][2] if "laur" in parse_messages(conversation)[loc + 1][1] else parse_messages(conversation)[loc + 1][2]
