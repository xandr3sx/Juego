import flet as ft
import random
import asyncio

async def main(page: ft.Page):
    try:
        # --- CONFIGURACIÓN GENERAL ---
        page.title = "Truth or Dare - Ultimate V12 Clean"
        page.theme_mode = ft.ThemeMode.DARK
        page.window_width = 400
        page.window_height = 850
        page.padding = 0 
        
        # --- VARIABLES DE ESTADO ---
        estado = {
            "jugadores": ["Jugador 1", "Jugador 2"],
            "turno": 0, 
            "nivel": "Suave",
            "puntos_calor": 0,
            "nivel_calor_titulo": "Frío",
            "barra_sumision": 0.0,
            "modo_esclavo": False
        }

        # --- DADOS ERÓTICOS ---
        db_dados = {
            "accion": ["Besar", "Lamer", "Morder", "Acariciar", "Masajear", "Azotar", "Chupar", "Soplar"],
            "zona": ["Cuello", "Orejas", "Pezones", "Muslos", "Ombligo", "Genitales", "Trasero", "Labios"],
            "intensidad": ["Suavemente", "Con pasión", "Brutalmente", "Lentamente", "Rápido", "Con hielo", "Con aceite", "Sin manos"],
            "tiempo": ["30 seg", "1 min", "2 min", "5 min", "10 seg", "Hasta gemir", "Hasta rogar", "3 veces"]
        }

        niveles_calor = {
            0: "🧊 Frío",
            20: "🔥 Caliente",
            50: "🌋 Ardiendo",
            100: "☢️ Fusión Nuclear (Premio desbloqueado)"
        }

        # --- BANCO DE PREGUNTAS ---
        db_preguntas = {
            "Suave": {
                "verdad": [
                    "¿Cuál fue tu primera impresión de mí?",
                    "¿Qué es lo más vergonzoso que has hecho en público?",
                    "¿Cuál es tu gusto culposo en música?",
                    "¿Qué harías si fueras invisible por un día?",
                    "¿Alguna vez has mentido para no salir conmigo?",
                    "¿Qué objeto que tenemos cerca ahora mismo te hace pensar en mí de forma traviesa?",
                    "Describe un sueño erótico conmigo como si fuera una escena de una película fantástica.",
                    "¿Qué parte de mi cuerpo te gustaría marcar con un beso ahora mismo?",
                    "Si tuvieras que inventar un superpoder sensual solo para usarlo conmigo, ¿cuál sería?",
                    "¿Qué sonido cotidiano mío (risas, suspiros, etc.) te pone más cachondo/a y por qué?",
                    "Confiesa una fantasía con velas o luces tenues que podríamos hacer esta misma noche.",
                    "¿Qué prenda que llevo puesta ahora te gustaría quitarme primero y por qué?",
                    "Describe mi olor actual como si fueras un perfumista loco enamorado.",
                    "¿Qué parte de mi cara te dan ganas de besar de forma diferente a lo habitual?",
                    "Si fuéramos animales en un ritual de apareamiento, ¿qué animal serías y qué harías?",
                    "¿Qué canción que estamos escuchando o que tienes en la cabeza te hace imaginarme desnudo/a?",
                    "Confiesa qué parte de mi cuerpo miras disimuladamente cuando crees que no me doy cuenta.",
                    "¿Qué comida que tenemos cerca te gustaría usar para jugar conmigo de forma juguetona?",
                    "¿Qué emoji inventarías para describir lo que sientes cuando nos besamos?",
                    "Describe cómo te imaginas mi piel bajo la ropa que llevo puesta ahora mismo.",
                    "¿Qué apodo secreto y caliente tienes para mí en tu cabeza?",
                    "¿Qué parte de mi voz te derrite cuando te hablo bajito al oído?",
                    "Confiesa una fantasía inocente que siempre has querido probar conmigo en la cama.",
                    "¿Qué zona de mi cuello o oreja te da más ganas de besar en este momento?",
                    "Si pudiéramos teletransportarnos ahora, ¿a qué lugar romántico iríamos para besarnos?",
                    "¿Qué detalle mío de hoy (peinado, ropa, perfume) te ha puesto más cachondo/a?",
                    "Describe cómo te sientes cuando mis manos te rozan 'accidentalmente'.",
                    "¿Qué película o serie tiene una escena que te recuerda a lo que queremos hacer luego?",
                    "¿Qué parte de mi cuerpo te gustaría masajear despacio durante minutos?",
                    "Confiesa qué piensas cuando me ves estirarme o bostezar de forma natural.",
                    "¿Qué mensaje travieso me escribirías si estuviéramos separados ahora mismo?",
                    "¿Qué olor mío te vuelve loco/a y quieres oler más de cerca?",
                    "Describe un beso mío que te haya dejado con ganas de mucho más.",
                    "¿Qué juego infantil adaptarías para que sea algo caliente entre nosotros?",
                    "¿Qué parte de mi risa te pone más juguetón/a y por qué?",
                    "Si tuvieras que dibujarme ahora mismo, ¿qué parte de mí destacarías primero?",
                    "¿Qué palabra mía te hace sonreír con picardía por dentro?",
                    "¿Qué fantasía con cosquillas que terminen en besos has tenido conmigo?",
                    "Confiesa qué prenda mía te gustaría oler o llevar puesta en secreto.",
                    "¿Qué zona de mi espalda te dan ganas de acariciar cuando me abrazas?",
                    "Describe cómo te imaginas mi cara cuando estoy a punto de besarte.",
                    "¿Qué sonido quiero que hagas cuando te toque suave una zona sensible?",
                    "¿Qué recuerdo nuestro no sexual te pone en modo romántico y caliente?",
                    "¿Qué parte de mi cuerpo quieres explorar con besos lentos esta noche?",
                    "Confiesa qué haces con mis fotos cuando estamos separados.",
                    "¿Qué luz o ambiente de la habitación te pone más en mood conmigo ahora?",
                    "¿Qué gesto mío te hace querer acercarte y tocarme disimuladamente?",
                    "Describe el beso perfecto que quieres darme en los próximos minutos.",
                    "¿Qué parte de mi ropa te gustaría desabrochar o bajar muy despacio?",
                    "¿Qué sueño reciente conmigo te ha dejado con una sonrisa traviesa?",
                    "¿Qué zona mía quieres que te acaricie yo ahora mismo?",
                    "Confiesa qué piensas cuando nos miramos fijamente sin hablar.",
                    "¿Qué aroma o sabor mío te gustaría probar más intensamente?",
                    "¿Qué juego de miradas queremos jugar antes de besarnos?",
                    "¿Qué deseo suave y romántico tienes para esta noche con migo?"
                ],
                "reto": [
                    "Haz 10 sentadillas ahora mismo.",
                    "Déjame hacerte cosquillas por 10 segundos.",
                    "Publica un estado en WhatsApp que yo elija.",
                    "Habla con acento extranjero hasta el próximo turno.",
                    "Bebe un vaso de agua sin usar las manos.",
                    "Besa tres partes no obvias de mi cuerpo (nuca, muñeca, detrás de la rodilla…) sin usar las manos.",
                    "Susúrrame al oído un haiku erótico sobre mis labios, muy despacio.",
                    "Dibuja con tu dedo en mi brazo un “mapa del tesoro” de los lugares que quieres besar hoy.",
                    "Mírame fijamente a los ojos durante 30 segundos mientras describes en voz baja lo que te provoco.",
                    "Elige una canción en tu cabeza y hazme un baile lento sensual sin música, solo 1 minuto.",
                    "Usa una pluma o tu cabello para acariciar mi cuello y cara durante 1 minuto sin besarme.",
                    "Inventa un apodo súper caliente para mí y úsalo en 5 frases seguidas mirándome.",
                    "Hazme cosquillas eróticas (zonas sensibles pero no genitales) hasta que me ría o gima.",
                    "Cierra los ojos y adivina qué parte de mi cuerpo estoy tocando con tu mano guiada.",
                    "Rolea que eres un masajista famoso y dame un masaje de hombros narrando lo “tenso” que estoy.",
                    "Besa mi cuello muy despacio durante 1 minuto sin usar las manos.",
                    "Susurra en mi oído tres cosas que te encantan de mi cuerpo actual.",
                    "Acaricia mi cara y pelo como si fuera la primera vez que me tocas.",
                    "Mírame a los ojos y dime con voz baja qué quieres hacerme esta noche.",
                    "Hazme un masaje en las manos besando cada dedo suavemente.",
                    "Baila pegado/a a mí muy lento durante 1 minuto sin música.",
                    "Traza con tu dedo líneas suaves por mi espalda durante 2 minutos.",
                    "Besa mi frente, nariz, mejillas y finalmente los labios muy despacio.",
                    "Descríbeme con detalle qué sientes cuando te toco suave el brazo.",
                    "Cierra los ojos y deja que te guíe las manos por mi cara y cuello.",
                    "Susurra una fantasía suave al oído mientras me abrazas fuerte.",
                    "Masajea mis pies o piernas narrando lo relajado/a que me ves.",
                    "Mírame fijamente mientras te quitas lentamente una prenda no esencial.",
                    "Besa el interior de mi muñeca como si fuera una zona muy sensible.",
                    "Acaricia mi pelo y nuca durante 1 minuto sin hablar, solo respirando.",
                    "Inventa una historia romántica corta susurrada al oído.",
                    "Haz cosquillas suaves en mi costado hasta que te pida un beso.",
                    "Traza círculos con tu dedo en mi palma mientras me miras intensamente.",
                    "Besa mi hombro y clavícula muy despacio durante 1 minuto.",
                    "Descríbeme cómo te sientes cuando estamos tan cerca como ahora.",
                    "Masajea mi cuello y hombros con movimientos lentos y firmes.",
                    "Mírame a los ojos y sonríe con picardía durante 30 segundos sin hablar.",
                    "Acaricia mi brazo desde el hombro hasta la mano muy despacio.",
                    "Susurra tres cumplidos calientes sobre mi apariencia actual.",
                    "Besa la punta de mis dedos uno por uno mirándome fijamente.",
                    "Hazme un abrazo largo mientras acaricias mi espalda suave.",
                    "Rolea que eres un chef y “pruebas” mi cuello con besos suaves.",
                    "Traza con tu nariz líneas por mi cara y cuello durante 1 minuto.",
                    "Descríbeme qué olor mío te gusta más y acércate a olerlo.",
                    "Masajea mis orejas y lóbulos con los dedos muy suavemente.",
                    "Mírame y haz una cara sexy durante 20 segundos sin reírte.",
                    "Besa mi barbilla y mandíbula como si mapearas mi cara.",
                    "Susurra una promesa traviesa para más tarde esta noche.",
                    "Acaricia mi pierna por encima de la ropa muy despacio.",
                    "Cierra los ojos y deja que te dé besos suaves en la cara guiándote.",
                    "Inventa un apodo cariñoso y caliente y repítelo mirándome.",
                    "Masajea mi cabeza y pelo durante 2 minutos relajantes.",
                    "Besa el hueco de mi clavícula muy suave y lento.",
                    "Descríbeme con voz baja cómo quieres que te bese ahora mismo.",
                    "Abrazo fuerte y balanceo suave durante 1 minuto sin hablar."
                ]
            },
            "Picante": {
                "verdad": [
                    "¿Qué parte de mi cuerpo te gusta más?",
                    "¿Recuerdas qué ropa llevaba en nuestra primera cita?",
                    "¿Qué te gustaría que te hiciera pero no te atreves a pedir?",
                    "¿Cuál ha sido tu mejor sueño erótico?",
                    "¿Prefieres arriba o abajo?",
                    "¿Qué fantasía con ataduras más fuertes de lo habitual has imaginado conmigo últimamente?",
                    "Describe cómo te excita imaginar que te hago el amor lentamente mientras te miro fijamente a los ojos.",
                    "¿Qué zona prohibida de mi cuerpo te mueres por explorar con la lengua esta noche?",
                    "Confiesa un deseo secreto de morderme fuerte en una zona que deje marca varios días.",
                    "¿Qué rol de dominación/sumisión total te pone más cachondo/a en este preciso momento?",
                    "¿Qué textura mía (sudor, saliva, fluidos) quieres probar más intensamente?",
                    "Si pudiéramos parar el tiempo ahora, ¿qué acto sexual brutal harías conmigo primero?",
                    "Describe el beso más sucio y profundo que te he dado y cómo quieres que lo repita más fuerte.",
                    "¿Qué palabra o frase mía susurrada al oído te hace mojar/perder el control al instante?",
                    "¿Qué fantasía con azotes suaves pero constantes durante el sexo te ronda la cabeza?",
                    "¿Cómo te excita la idea de que te ate los ojos y te sorprenda con algo repentino?",
                    "Confiesa cuánto te gustaría que te agarre del pelo fuerte mientras te como/lamo entero.",
                    "¿Qué deseo de oral profundo y sin pausas hasta casi ahogarte has reprimido?",
                    "Describe cómo te pone que te obligue a mantener las manos quietas mientras estoy dentro.",
                    "¿Qué kink con hielo o calor extremo en zonas sensibles quieres probar ya?",
                    "¿Qué fantasía con doble estimulación (oral + sexo) te obsesiona confesar?",
                    "Confiesa un deseo de que te tome contra la pared con fuerza y sin preliminares.",
                    "¿Qué sonido mío durante el sexo te hace querer correrte inmediatamente?",
                    "¿Qué parte de mi cuerpo quieres chupar/morder hasta dejarme temblando?",
                    "Describe cómo te gustaría que te niegue el orgasmo varias veces antes de dejarte explotar.",
                    "¿Qué rol invertido extremo (tú controlando todo mi placer) te excita más?",
                    "Confiesa cuánto te pone que te escupa en la boca durante un beso apasionado.",
                    "¿Qué fantasía con arañazos fuertes en la espalda durante el polvo has tenido?",
                    "Describe el orgasmo más intenso que te he provocado y qué quieres que lo supere hoy.",
                    "¿Qué deseo de oral profundo mutuo en 69 te vuelve loco/a?",
                    "¿Qué te excita más de la idea de que te ate las manos y te use como quiera?",
                    "Confiesa un deseo de sexo con mordidas que duelan de lo rico que son.",
                    "¿Qué palabra sucia quieres que te diga repetidamente mientras te tomo fuerte?",
                    "¿Qué fantasía con edging mutuo hasta casi llorar de placer has imaginado?",
                    "Describe cómo te pone que te agarre del cuello suavemente mientras llegamos al clímax.",
                    "¿Qué zona de mi cuerpo quieres lamer durante minutos sin que te deje parar?",
                    "Confiesa cuánto te gustaría que te humille un poquito verbalmente mientras lo hacemos.",
                    "¿Qué deseo de sexo rápido y salvaje justo después de un orgasmo tienes?",
                    "¿Qué te excita de la idea de que te marque con chupetones en sitios muy visibles?",
                    "Describe cómo quieres que te lleve al squirting/eyaculación con dedos expertos.",
                    "¿Qué fantasía con juguetes o dedos traseros mientras te toco por delante te ronda?",
                    "¿Qué sonido de placer mío te hace querer tomarme más fuerte?",
                    "Confiesa un deseo de sexo maratónico con cambios de posición brutales.",
                    "¿Qué parte de mi sabor te vuelve completamente adicto/a y quieres más?",
                    "¿Qué te pone más de que te obligue a mirarme mientras te corres dentro/fuera?",
                    "Describe cómo te gustaría que te use la boca profundo agarrándote la cabeza.",
                    "¿Qué fantasía con azotes en el culo mientras estoy dentro te excita confesar?",
                    "¿Qué deseo de overstimulation justo después de correrte tienes reprimido?",
                    "Confiesa cuánto te excita que te ate y te deje al borde sin tocarte más.",
                    "¿Qué kink con saliva abundante durante el oral o el sexo quieres probar?",
                    "¿Qué te vuelve loco/a de la idea de sexo sudoroso y animal sin control?",
                    "Describe el polvo más salvaje que hemos tenido y cómo quieres que lo superemos.",
                    "¿Qué deseo de breath play muy suave durante el orgasmo has tenido?",
                    "¿Qué zona sensible quieres que te torture con placer hasta suplicar?",
                    "¿Qué fantasía final de corrernos juntos temblando te pone a mil ahora mismo?"
                ],
                "reto": [
                    "Bésame el cuello durante 1 minuto.",
                    "Mándame una foto atrevida ahora mismo.",
                    "Quítate una prenda (la que tú quieras).",
                    "Susúrrame algo sucio al oído.",
                    "Dame un masaje en la zona que yo elija.",
                    "Masajéame los genitales o zona trasera con aceite durante 5 minutos sin entrar aún.",
                    "Haz un striptease completo quitándote toda la ropa lentamente mirándome fijo.",
                    "Besa y lame un camino desde mi boca hasta mis genitales sin saltarte nada.",
                    "Usa solo la boca para quitarme toda la ropa interior de forma muy lenta.",
                    "Átame las manos con algo suave y besa/lame todo mi cuerpo excepto genitales 5 min.",
                    "Dibuja con la lengua círculos lentos en mis pezones durante 3 minutos seguidos.",
                    "Siéntate encima mío desnudo/a y muévete frotándote contra mí 3 minutos sin entrar.",
                    "Véndame los ojos y hazme sentir tu cuerpo entero solo con roces y besos.",
                    "Chúpame los dedos de pies y manos como si fueran algo mucho más íntimo.",
                    "Hazme un baile de regazo completamente desnudo/a durante 3 minutos intensos.",
                    "Oral lento y profundo durante 4 minutos sin usar manos en absoluto.",
                    "Finge que me atas y rolea dominación total besando y mordiendo donde quieras.",
                    "Lame y chupa mis orejas y cuello mientras me susurras cosas sucias al oído.",
                    "Masajea mis muslos internos subiendo cada vez más cerca pero sin tocar genitales.",
                    "Haz 69 oral mutuo durante 3 minutos compitiendo por quién aguanta más placer.",
                    "Azótame suavemente el culo 20 veces alternando con besos en la misma zona.",
                    "Escúpeme en la boca durante un beso profundo y apasionado de 1 minuto.",
                    "Usa hielo en mis pezones y genitales, luego caliéntalos con tu boca inmediatamente.",
                    "Edging ligero: llévame al borde del orgasmo 3 veces con mano u oral y para.",
                    "Tómame (o haz que te tome) muy lento durante 5 minutos sin aumentar ritmo.",
                    "Tira suavemente de mi pelo mientras me besas el cuello y bajas hasta el pecho.",
                    "Oblígame a masturbarme frente a ti durante 2 minutos sin correrme.",
                    "Araña mi espalda con uñas mientras nos besamos intensamente desnudos.",
                    "Unión en una posición profunda y manténla quieto 2 minutos sintiendo todo.",
                    "Lame mi sudor de cuello y pecho como si fuera lo más delicioso del mundo.",
                    "Choking muy suave con la mano mientras nos besamos y frotamos fuerte.",
                    "Repite el movimiento o caricia que más me hace gemir pero más intenso esta vez.",
                    "Usa tus dedos para explorar mi zona anal externamente mientras me besas.",
                    "Humíllame suavemente con palabras sucias mientras me tocas por todas partes.",
                    "Fóllame/fóllate contra mí exhaustivamente durante 5 minutos sin parar.",
                    "Juega con hielo en mi entrada antes de lamerme o entrarme caliente.",
                    "Oral profundo alternando ritmo lento y rápido durante 4 minutos seguidos.",
                    "Azota mis muslos internos suavemente mientras me miras con deseo.",
                    "Cambia de posición cada minuto durante un polvo intenso de 6 minutos.",
                    "Lame una zona entera de mi cuerpo (pecho, espalda, culo) durante 4 minutos.",
                    "Tapa mi boca suavemente momentos mientras me estimulas al máximo.",
                    "Marca mi cuello y pecho con chupetones fuertes y visibles.",
                    "Llévame a un orgasmo fuerte pero lento con solo dedos y mirada fija.",
                    "Entra en mí justo después de un orgasmo pequeño para intensificar el siguiente.",
                    "Araña mis costados y muslos mientras llegamos al clímax juntos.",
                    "Niega mi orgasmo 4 veces antes de permitirme explotar fuerte.",
                    "Exploración anal externa profunda con lengua o dedos lubricados.",
                    "69 con competencia real de quién hace correrse primero al otro.",
                    "Sexo contra la pared con piernas levantadas y ritmo intenso.",
                    "Susurra humillación suave al oído durante todo un acto de placer.",
                    "Alterna ritmo muy rápido y muy lento para volvernos locos.",
                    "Móntame o déjate montar mientras azotas y agarras fuerte.",
                    "Termina con oral final hasta corrida completa en boca o cuerpo.",
                    "Sesión de dominación mutua: cambiad quién manda cada 2 minutos.",
                    "Polvo intenso final hasta que los dos estemos temblando y sin aliento."
                ]
            },
            "Extremo": {
                "verdad": [
                    "Describe tu fantasía más oscura con detalle.",
                    "¿Alguna vez has fingido? ¿Cuándo?",
                    "¿Qué es lo más sucio que has hecho en un lugar público?",
                    "¿Qué fantasía de rol (enfermera, profesor, etc.) te gustaría probar conmigo?",
                    "¿Qué fantasía de ser usado/a como objeto sexual puro durante horas te pone más cachondo/a?",
                    "Describe en detalle cómo te excita la idea de que te tome sin parar hasta que ruegues piedad.",
                    "¿Qué kink con saliva extrema o fluidos te vuelve loco/a y quieres probar ya?",
                    "Confiesa un deseo brutal de sexo anal profundo con dedos, lengua o juguete.",
                    "¿Qué tipo de humillación verbal fuerte te hace mojar/te pone durísimo/a mientras estoy dentro?",
                    "Describe cómo te gustaría que te lleve al orgasmo múltiple hasta que no puedas más.",
                    "¿Qué fantasía con azotes fuertes y marcas temporales has reprimido conmigo?",
                    "Confiesa un deseo de sexo’ forzado consensuado (CNC) puro, solo fuerza y entrega.",
                    "¿Qué parte de mi cuerpo quieres devorar con mordidas salvajes hasta dejar huella?",
                    "¿Qué práctica con edging extremo (negación de orgasmo durante mucho rato) te obsesiona?",
                    "¿Cómo te excita la idea de que te ate y te use solo para mi placer sin dejarte acabar?",
                    "Describe el sonido que más te pone cuando estoy dentro de ti muy profundo.",
                    "¿Qué fantasía con garganta profunda hasta lágrimas has tenido conmigo?",
                    "Confiesa cuánto te gustaría que te azote hasta que el culo arda y luego te tome fuerte.",
                    "¿Qué deseo de ser tomado/a por ambos lados al mismo tiempo te ronda?",
                    "¿Qué palabra sucia mía durante el sexo te hace perder completamente el control?",
                    "Describe cómo te vuelve loco/a que te escupa en la boca mientras te tomo.",
                    "¿Qué fantasía con cera caliente en zonas sensibles has imaginado?",
                    "Confiesa un deseo de ser inmovilizado/a y torturado/a con placer hasta suplicar.",
                    "¿Qué te excita más de la idea de squirtear/eyacular en mi cara repetidamente?",
                    "¿Qué rol de sumisión total te pone más en este momento?",
                    "Describe cómo te gustaría que te niegue el orgasmo durante media hora seguida.",
                    "¿Qué fantasía con arañazos y mordidas fuertes hasta sangrar levemente has tenido?",
                    "Confiesa un deseo de sexo en posiciones que duelan un poco de lo intensas.",
                    "¿Qué kink con fluidos mixtos (sudor, saliva, mis fluidos) te obsesiona?",
                    "¿Qué te pone más de que te tire del pelo fuerte mientras te tomo por detrás?",
                    "Describe el orgasmo más brutal que te he dado y qué quieres que repita más fuerte.",
                    "¿Qué fantasía con juguetes grandes y estiramiento te excita confesar?",
                    "Confiesa cuánto te gustaría que te humille llamándote nombres sucios mientras acabas.",
                    "¿Qué deseo de ser tomado/a contra la pared con fuerza total has reprimido?",
                    "¿Qué te excita de la idea de que te ate los ojos y te sorprenda con dolor y placer?",
                    "Describe cómo te pone que te obligue a mantener contacto visual mientras te corro dentro.",
                    "¿Qué fantasía con choking ligero durante el sexo has tenido?",
                    "Confiesa un deseo de sexo maratónico hasta quedar exhaustos y doloridos.",
                    "¿Qué parte de mi cuerpo quieres lamer durante horas sin parar?",
                    "¿Qué te vuelve loco/a de la idea de edging mutuo hasta que uno explote primero?",
                    "Describe cómo te gustaría que te use la boca como si fuera otra entrada.",
                    "¿Qué fantasía con azotes en genitales suaves pero intensos te ronda?",
                    "Confiesa cuánto te excita que te ordene masturbarte frente a mí sin dejarte acabar.",
                    "¿Qué deseo de doble estimulación trasera y genital al mismo tiempo tienes?",
                    "¿Qué sonido mío al correrme te hace querer más inmediatamente?",
                    "Describe cómo te pone que te ate y te deje al borde horas.",
                    "¿Qué fantasía con hielo dentro durante el acto has imaginado?",
                    "Confiesa un deseo de ser usado/a después de un orgasmo para overstimulation.",
                    "¿Qué te excita más de la idea de que te tome hasta que tiembles incontrolablemente?",
                    "¿Qué kink con breath play suave durante el sexo te pone?",
                    "Describe el sabor mío que más te vuelve adicto/a.",
                    "¿Qué fantasía con múltiples orgasmos forzados has tenido?",
                    "Confiesa cuánto te gustaría que te marque con chupetones en todo el cuerpo.",
                    "¿Qué deseo final de sexo tan intenso que nos deje sin aliento tienes ahora mismo?"
                ],
                "castigo": [
                    "Oral completo hasta que yo llegue al orgasmo, sin que te toque nada a ti.",
                    "10 minutos de edging: me llevas al borde del orgasmo repetidamente y paras justo antes.",
                    "30 azotes fuertes en el culo con la mano, contando en voz alta y diciendo 'gracias' después de cada uno.",
                    "Sexo anal con dedos o juguete durante 5 minutos, solo saliva como lubricante.",
                    "Estás atado/a 10 minutos y yo hago absolutamente lo que quiera con tu cuerpo.",
                    "Tragas todos mis fluidos del próximo orgasmo sin rechistar.",
                    "Humillación verbal intensa durante el siguiente polvo completo (te digo todo lo sucio que quieras oír).",
                    "Cumples dos retos extremos seguidos sin poder negarte al segundo.",
                    "Masaje erótico completo + oral a mí hasta que acabe, y tú no recibes nada hasta después.",
                    "Sexo en una posición incómoda y degradante que yo elija durante todo el siguiente acto.",
                    "20 azotes con cinturón en el culo, despacio y fuerte.",
                    "Edging brutal de 15 minutos: al borde y parar, hasta que ruegues.",
                    "Lames todo mi cuerpo desde los pies hasta el cuello sin saltarte nada.",
                    "Sexo profundo sin preliminares durante 7 minutos seguidos.",
                    "Estás de rodillas y me haces oral profundo mientras te agarro la cabeza 5 minutos.",
                    "Te ato los ojos y te torturo con hielo y calor en zonas sensibles 8 minutos.",
                    "Overstimulation: sigo estimulándote 3 minutos después de tu orgasmo sin parar.",
                    "Me montas durante 10 minutos sin parar aunque estés agotado/a.",
                    "Azotes en los muslos internos 25 veces, alternando con lamidas.",
                    "Tragas mi saliva en un beso sucio durante 2 minutos seguidos.",
                    "Sesión de dominación total: yo mando todo durante 15 minutos sin preguntas.",
                    "Sexo anal completo hasta el fondo durante 6 minutos sin bajar ritmo.",
                    "Humillación: te hago masturbarte frente a mí diciendo cosas sucias en voz alta.",
                    "Choking suave mientras te tomo fuerte durante todo el acto.",
                    "Limpias con la boca cualquier fluido que deje en tu cuerpo o en mi cuerpo.",
                    "Edging mutuo pero solo tú paras cuando yo estoy al borde, 10 veces.",
                    "Estás inmovilizado/a y recibes oral hasta múltiples orgasmos sin descanso.",
                    "Azotes en los pezones y genitales suaves pero constantes durante 5 minutos.",
                    "Te uso la boca como si fuera otra entrada durante 6 minutos seguidos.",
                    "Posición contra la pared con piernas arriba durante 8 minutos sin parar.",
                    "Araño tu espalda fuerte mientras me haces todo lo que yo quiera.",
                    "Niega tu propio orgasmo durante los próximos 20 minutos de juego.",
                    "Usas un juguete grande en ti mismo/a mientras yo miro y doy órdenes.",
                    "Recibes cera caliente en el culo y espalda, luego sexo inmediato.",
                    "Lames mis pies y dedos durante 4 minutos completos.",
                    "Te corro en la cara o pecho y limpias todo con la boca.",
                    "10 minutos de 69 donde solo yo recibo placer intenso.",
                    "Azotes con la mano en la cara interna de los muslos hasta que queden rojos.",
                    "Te ato y juego con hielo dentro de ti durante 5 minutos antes de tomarte.",
                    "Humillación: repites frases sucias que yo te diga mientras te toco.",
                    "Doble juego (dedos anal + principal) durante 7 minutos.",
                    "Estás de rodillas sirviéndome oral cada vez que yo chasquee los dedos (5 veces).",
                    "Overstimulation anal después de tu orgasmo principal.",
                    "Me haces un baile desnudo erótico completo mientras te digo cosas humillantes.",
                    "Edging con oral: al borde 8 veces sin dejarte acabar.",
                    "Azotes 40 veces suaves pero constantes en todo el cuerpo.",
                    "Te tomo exhaustivamente hasta que tiembles y luego sigo un poco más.",
                    "Lames el sudor de todo mi cuerpo después de un polvo intenso.",
                    "Sesión de breath play suave durante tus próximos 3 orgasmos.",
                    "Cumples un reto extremo que yo elija ahora mismo del banco, sin sorteo.",
                    "Estás atado/a y solo puedes recibir placer, sin tocarme a mí durante 12 minutos."
                ]
            }
        }

        # --- GRADIENTES ---
        gradiente_menu = ft.LinearGradient(
            begin=ft.alignment.top_center, end=ft.alignment.bottom_center,
            colors=[ft.Colors.INDIGO_900, ft.Colors.DEEP_PURPLE_900]
        )

        gradiente_p1 = ft.LinearGradient(
            begin=ft.alignment.top_left, end=ft.alignment.bottom_right,
            colors=[ft.Colors.BLUE_900, ft.Colors.CYAN_800, ft.Colors.DEEP_PURPLE_900]
        )
        gradiente_p2 = ft.LinearGradient(
            begin=ft.alignment.top_left, end=ft.alignment.bottom_right,
            colors=[ft.Colors.RED_900, ft.Colors.PINK_700, ft.Colors.PURPLE_900]
        )

        # Colores HEX para el menú (Estilo Glass Colorido)
        def obtener_fondo_nivel_glass(nivel):
            colores = {
                "Suave":   ["#6600838F", "#661565C0"], 
                "Picante": ["#66EF6C00", "#66C62828"], 
                "Extremo": ["#666A1B9A", "#66000000"], 
            }
            c = colores.get(nivel, [ft.Colors.WHITE10, ft.Colors.WHITE10])
            return ft.LinearGradient(colors=c)

        # --- PANTALLA 3: EL JUEGO (RULETA + DADOS + PUNTOS) ---
        async def cargar_juego():
            # --- UI ELEMENTS ---
            # 1. Indicador de Turno Compacto
            texto_turno = ft.Text(
                f"{estado['jugadores'][estado['turno']]}",
                size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE
            )
            
            # 2. Indicador de Calor (Badge)
            txt_puntos_calor = ft.Text(f"{estado['puntos_calor']}", color="white", weight="bold")
            badge_calor = ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.FIRE_EXTINGUISHER, color="orange", size=16),
                    txt_puntos_calor
                ], spacing=2),
                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                bgcolor=ft.Colors.ORANGE_900,
                border_radius=15,
                border=ft.border.all(1, "orange")
            )

            # 3. Barra de Sumisión Custom (Visualmente impactante)
            ancho_barra_total = 160
            # Estado inicial
            ancho_progreso = ancho_barra_total * estado["barra_sumision"]
            
            barra_progreso_relleno = ft.Container(
                width=ancho_progreso, height=15,
                gradient=ft.LinearGradient(colors=[ft.Colors.PURPLE_600, ft.Colors.PINK_400]),
                border_radius=10,
                animate=ft.Animation(800, ft.AnimationCurve.EASE_OUT) # Animación suave > 500ms
            )
            
            txt_barra_porcentaje = ft.Text(f"{int(estado['barra_sumision']*100)}%", size=12, color="pink")

            container_barra_sumision = ft.Column([
                ft.Row([
                    ft.Text("Sumisión", size=12, color="white70"),
                    txt_barra_porcentaje
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=ancho_barra_total),
                ft.Container(
                    width=ancho_barra_total, height=15,
                    bgcolor=ft.Colors.BLACK45, border_radius=10,
                    content=ft.Stack([barra_progreso_relleno]),
                    border=ft.border.all(1, ft.Colors.WHITE24)
                )
            ], spacing=2)

            # TARJETA CENTRAL (Ajustada para móvil)
            txt_pregunta = ft.Text(
                "¡Toca para girar!", 
                size=22, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE
            )
            card_game = ft.Container(
                content=txt_pregunta,
                alignment=ft.alignment.center,
                padding=20, width=320, height=280, 
                bgcolor=ft.Colors.TRANSPARENT, 
                border=ft.border.all(2, ft.Colors.WHITE),
                border_radius=25,
                scale=ft.Scale(1),
                animate_scale=ft.Animation(400, ft.AnimationCurve.ELASTIC_OUT),
            )

            # BOTONES PRINCIPALES (Estilizados)
            async def btn_girar_click(e):
                await logica_ruleta()

            btn_girar = ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.TOUCH_APP, color="white"),
                    ft.Text("GIRAR RULETA", weight="bold", size=16, color="white")
                ], alignment=ft.MainAxisAlignment.CENTER),
                width=200, height=60,
                gradient=ft.LinearGradient(colors=[ft.Colors.PINK_600, ft.Colors.PURPLE_700]),
                border_radius=30,
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.Colors.PINK_900),
                on_click=btn_girar_click,
                animate_scale=ft.Animation(100),
                ink=True
            )
            
            async def btn_dados_click(e):
                await mostrar_dados()

            btn_dados = ft.IconButton(
                icon=ft.Icons.DIAMOND, icon_color="cyan", icon_size=35,
                tooltip="Dados Eróticos",
                style=ft.ButtonStyle(bgcolor=ft.Colors.WHITE10, shape=ft.CircleBorder()),
                on_click=btn_dados_click
            )

            async def btn_completado_click(e):
                await completar_reto()

            btn_completado = ft.ElevatedButton(
                "¡HECHO! (+10 Pts)", icon=ft.Icons.CHECK_CIRCLE,
                bgcolor=ft.Colors.GREEN_600, color="white",
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                visible=False, 
                on_click=btn_completado_click
            )

            # --- LOGICA DE JUEGO ---
            async def logica_ruleta():
                btn_girar.scale = 0.95
                page.update()
                await asyncio.sleep(0.1)
                btn_girar.scale = 1.0
                btn_girar.disabled = True 
                btn_completado.visible = False
                page.update()
                
                # Animación de Ruleta
                opciones = ["VERDAD", "RETO"]
                if estado["nivel"] == "Extremo": opciones.append("CASTIGO")
                
                for _ in range(12): 
                    txt = random.choice(opciones)
                    txt_pregunta.value = f"🎲 {txt} 🎲"
                    page.update()
                    await asyncio.sleep(0.08)
                
                # Selección final
                tipo_elegido = random.choice(opciones).lower() 
                
                # Colores
                if tipo_elegido == "verdad": color = ft.Colors.CYAN_300
                elif tipo_elegido == "reto": color = ft.Colors.RED_300
                else: color = ft.Colors.GREY_500
                
                card_game.border = ft.border.all(4, color)
                
                # Obtener pregunta
                try:
                    lista = db_preguntas[estado["nivel"]][tipo_elegido]
                    texto_final = random.choice(lista)
                    txt_pregunta.value = texto_final
                except:
                    txt_pregunta.value = "Error: Base de datos vacía."

                # Habilitar completado
                btn_completado.visible = True
                btn_girar.disabled = False 
                page.update()

            async def completar_reto():
                estado["puntos_calor"] += 10
                txt_puntos_calor.value = f"{estado['puntos_calor']}"
                
                # Barra sumisión (Funciona en todos los niveles ahora)
                incremento = 0.05
                if estado["nivel"] == "Picante": incremento = 0.10
                if estado["nivel"] == "Extremo": incremento = 0.15
                
                # Incremento visual
                nuevo_valor = min(1.0, estado["barra_sumision"] + incremento)
                estado["barra_sumision"] = nuevo_valor
                
                # Actualizar Ancho Barra UI
                barra_progreso_relleno.width = ancho_barra_total * nuevo_valor
                txt_barra_porcentaje.value = f"{int(nuevo_valor*100)}%"
                
                if nuevo_valor >= 1.0 and not estado["modo_esclavo"]:
                    estado["modo_esclavo"] = True
                    page.snack_bar = ft.SnackBar(ft.Text("🔥 ¡MODO ESCLAVO ACTIVADO! 🔥", color="white"), bgcolor="red", open=True)
                
                # Cambio turno
                estado["turno"] = 1 - estado["turno"]
                texto_turno.value = f"{estado['jugadores'][estado['turno']]}"
                
                # Transición Fondo Suave
                # Al actualizar la property 'gradient' del contenedor existente, Flet interpola los colores
                if estado["turno"] == 0: 
                    contenido_juego.gradient = gradiente_p1
                else: 
                    contenido_juego.gradient = gradiente_p2

                btn_completado.visible = False
                txt_pregunta.value = "¡Toca para girar!"
                card_game.border = ft.border.all(2, ft.Colors.WHITE)
                
                # ACTUALIZAR UI SIN RECONSTRUIR
                page.update() 

            async def mostrar_dados():
                res_accion = ft.Text("...", size=18, weight="bold", color="pink")
                res_zona = ft.Text("...", size=18, weight="bold", color="white")
                
                async def tirar_dados(e):
                    for _ in range(8):
                        res_accion.value = random.choice(db_dados["accion"]) + " " + random.choice(db_dados["zona"])
                        res_zona.value = random.choice(db_dados["intensidad"]) + " - " + random.choice(db_dados["tiempo"])
                        page.update()
                        await asyncio.sleep(0.05)

                bs = ft.BottomSheet(
                    ft.Container(
                        padding=30, height=350, bgcolor="#1a1a1a",
                        border_radius=ft.border_radius.only(top_left=30, top_right=30),
                        content=ft.Column([
                            ft.Text("🎲 DADOS 🎲", size=24, color="white", weight="bold"),
                            ft.Divider(color="white24"),
                            ft.Container(
                                padding=20, border=ft.border.all(1, "pink"), border_radius=15,
                                content=ft.Column([res_accion, res_zona], horizontal_alignment="center")
                            ),
                            ft.Container(height=20),
                            ft.ElevatedButton("LANZAR", on_click=tirar_dados, bgcolor="pink", color="white", width=200)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                    ),
                    open=True
                )
                page.overlay.append(bs)
                page.update()

            # LAYOUT MÓVIL OPTIMIZADO
            gradiente_inicial = gradiente_p1 if estado['turno'] == 0 else gradiente_p2
            
            contenido_juego = ft.Container(
                gradient=gradiente_inicial,
                width=page.window_width, height=page.window_height,
                padding=15, 
                animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT), # Transición de 1 segundo para el fondo
                content=ft.Column([
                    # CABECERA MÓVIL
                    ft.Row([
                        ft.IconButton(ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda _: asyncio.create_task(cargar_dificultad())),
                        texto_turno, # Centro
                        ft.Icon(ft.Icons.PERSON, color="white54") # Balance visual
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    # BARRA DE ESTADO (Debajo de cabecera)
                    ft.Container(
                        padding=ft.padding.only(bottom=10),
                        content=ft.Row([
                            badge_calor,
                            container_barra_sumision
                        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
                    ),
                    
                    ft.Divider(color=ft.Colors.TRANSPARENT, height=10),
                    card_game, 
                    ft.Divider(color=ft.Colors.TRANSPARENT, height=20),
                    
                    # ZONA DE ACCIÓN
                    ft.Column([
                        btn_completado,
                        ft.Container(height=10),
                        ft.Row([
                            btn_dados,
                            btn_girar,
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                    
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
            
            page.clean()
            page.add(contenido_juego)
            page.update()

        # --- PANTALLA 2: SELECCIÓN DE DIFICULTAD ---
        async def cargar_dificultad():
            async def seleccionar(nivel):
                estado["nivel"] = nivel
                await cargar_juego()

            def crear_tarjeta_nivel(texto, gradiente, icono):
                async def on_click_nivel(e):
                    await seleccionar(texto)
                
                return ft.Container(
                    content=ft.Row([
                        ft.Icon(icono, size=40, color="white"),
                        ft.Text(texto, size=25, weight=ft.FontWeight.BOLD, color="white")
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    width=300, height=100,
                    gradient=gradiente,
                    blur=ft.Blur(15, 15, ft.BlurTileMode.MIRROR),
                    border=ft.border.all(1, ft.Colors.WHITE24),
                    border_radius=20,
                    on_click=on_click_nivel,
                    animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT), ink=True, 
                )

            async def back_to_login(e):
                await cargar_login()

            contenido = ft.Container(
                gradient=gradiente_menu,
                width=page.window_width, height=page.window_height,
                content=ft.Column([
                    ft.IconButton(ft.Icons.ARROW_BACK, icon_color="white", on_click=back_to_login),
                    ft.Text("ELIGE TU NIVEL", size=30, weight=ft.FontWeight.BOLD),
                    ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                    
                    crear_tarjeta_nivel("Suave", obtener_fondo_nivel_glass("Suave"), ft.Icons.AC_UNIT),
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    crear_tarjeta_nivel("Picante", obtener_fondo_nivel_glass("Picante"), ft.Icons.WHATSHOT),
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    crear_tarjeta_nivel("Extremo", obtener_fondo_nivel_glass("Extremo"), ft.Icons.WARNING),
                    
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
            )
            page.clean()
            page.add(contenido)
            page.update()

        # --- PANTALLA 1: LOGIN ---
        async def cargar_login():
            input_style = {
                "width": 280, "border_radius": 15, 
                "bgcolor": ft.Colors.WHITE10, "color": "white",
                "border_color": ft.Colors.WHITE24
            }
            input_p1 = ft.TextField(label="Jugador 1 (Azul)", **input_style)
            input_p2 = ft.TextField(label="Jugador 2 (Rosa)", **input_style)

            async def guardar_y_seguir(e):
                if input_p1.value: estado["jugadores"][0] = input_p1.value
                if input_p2.value: estado["jugadores"][1] = input_p2.value
                await cargar_dificultad()

            contenido = ft.Container(
                gradient=gradiente_menu,
                width=page.window_width, height=page.window_height,
                content=ft.Column([
                    ft.Icon(ft.Icons.FAVORITE, size=100, color=ft.Colors.RED_500),
                    ft.Text("COUPLE GAME", size=40, font_family="Verdana", weight=ft.FontWeight.BOLD),
                    ft.Text("Ultimate Edition V12", color="grey"),
                    ft.Divider(height=50, color=ft.Colors.TRANSPARENT),
                    input_p1,
                    input_p2,
                    ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                    ft.ElevatedButton("COMENZAR", width=200, height=50, style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color="white"), on_click=guardar_y_seguir)
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
            page.clean()
            page.add(contenido)
            page.update()

        # Iniciar App
        await cargar_login()
    except Exception as e:
        print(f"Error starting app: {e}")
        try:
             page.clean()
             page.add(ft.Text(f"Error critical: {e}", color="red"))
             page.update()
        except:
             pass

ft.app(target=main)