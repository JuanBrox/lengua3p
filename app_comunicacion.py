"""🦄 El Reino de los Mensajes Mágicos
App Streamlit de Lengua (3.º de Primaria): los elementos de la comunicación.
  📖 Aprende  ·  ✏️ Mi ficha  ·  🎮 Juego
"""
import random

import streamlit as st

st.set_page_config(
    page_title="El Reino de los Mensajes Mágicos",
    page_icon="🦄",
    layout="centered",
)

# ───────────────────────── Contenido ─────────────────────────
ELEMENTOS = ["Emisor", "Receptor", "Mensaje", "Canal", "Código", "Contexto"]
EMOJIS = {"Emisor": "🗣️", "Receptor": "👂", "Mensaje": "💌",
          "Canal": "📡", "Código": "🔤", "Contexto": "🏞️"}
PREGUNTAS = {
    "Emisor": "¿Quién envía el mensaje?",
    "Receptor": "¿Quién recibe el mensaje?",
    "Mensaje": "¿Qué es lo que dice?",
    "Canal": "¿Por dónde viaja el mensaje?",
    "Código": "¿Qué idioma o signos utiliza?",
    "Contexto": "¿Dónde ocurre la historia?",
}
DEFS = {
    "Emisor": "quien transmite el mensaje",
    "Receptor": "quien recibe el mensaje",
    "Mensaje": "lo que se quiere comunicar",
    "Canal": "por dónde se transmite el mensaje (voz, teléfono, carta, móvil…)",
    "Código": "el idioma o sistema de signos que se utiliza (español, inglés, gestos, dibujos…)",
    "Contexto": "la situación o lugar donde ocurre la comunicación",
}
TRUCOS = {
    "Emisor": "El que **E**nvía.",
    "Receptor": "El que **R**ecibe.",
    "Mensaje": "Lo que se **dice** o se quiere contar.",
    "Canal": "El **camino** del mensaje: aire, papel, teléfono…",
    "Código": "El **idioma** o los signos: palabras, gestos, dibujos…",
    "Contexto": "El **dónde** y el **cuándo** pasa todo.",
}


def _sit(titulo, texto, datos):
    """datos: {elemento: (correcta, [3 distractores])} → opciones barajadas y fijas."""
    items = {}
    for e, (ok, malas) in datos.items():
        opts = [ok] + list(malas)
        random.Random(f"{titulo}{e}").shuffle(opts)
        items[e] = {"ok": ok, "opts": opts}
    return {"titulo": titulo, "texto": texto, "items": items}


SITUACIONES = [
    _sit(
        "1. El patio (escondite)",
        "Estamos en el patio jugando al escondite. De repente veo que ha sonado el timbre. "
        "Corro hacia mi amigo Carlos y le digo: «¡Vamos rápido a la fila porque empieza la clase!»",
        {
            "Emisor": ("Yo (quien habla)", ["Carlos", "El timbre", "El profesor"]),
            "Receptor": ("Carlos", ["Yo (quien habla)", "El timbre", "Toda la clase"]),
            "Mensaje": ("¡Vamos rápido a la fila porque empieza la clase!",
                        ["Vamos a jugar otra vez al escondite", "Ha sonado el timbre",
                         "Me voy a casa"]),
            "Canal": ("La voz (por el aire)", ["Una carta", "El teléfono móvil", "Un dibujo"]),
            "Código": ("Español", ["Inglés", "Gestos", "Dibujos"]),
            "Contexto": ("En el patio del colegio", ["En casa", "En el coche", "En la biblioteca"]),
        },
    ),
    _sit(
        "2. El coche y la señal de STOP",
        "Mario va en coche con su familia. Al acercarse a un cruce, ve una señal de STOP "
        "y su padre detiene el coche.",
        {
            "Emisor": ("La señal de STOP", ["Mario", "El coche", "El cruce"]),
            "Receptor": ("El padre de Mario (el conductor)",
                         ["La señal de STOP", "El coche", "El cruce"]),
            "Mensaje": ("Para el coche: hay que detenerse", ["Acelera", "Gira a la derecha",
                                                              "Hay un colegio cerca"]),
            "Canal": ("La vista (se ve la señal)", ["La voz", "Una carta", "El teléfono"]),
            "Código": ("Señales de tráfico (símbolos)", ["Español hablado", "Inglés escrito en un libro",
                                                          "Una canción"]),
            "Contexto": ("En la carretera, en un cruce", ["En el colegio", "En casa", "En el parque"]),
        },
    ),
    _sit(
        "3. La nota de la nevera",
        "Al levantarse, Pablo encuentra una nota escrita por su madre en la nevera: "
        "«He ido a comprar. Vuelvo enseguida.»",
        {
            "Emisor": ("La madre de Pablo", ["Pablo", "La nevera", "El panadero"]),
            "Receptor": ("Pablo", ["La madre de Pablo", "La nevera", "El vecino"]),
            "Mensaje": ("He ido a comprar. Vuelvo enseguida.",
                        ["Tengo mucho sueño", "Ven al colegio", "Estoy en el parque"]),
            "Canal": ("Una nota escrita (papel)", ["La voz", "El teléfono", "Los gestos"]),
            "Código": ("Español escrito", ["Gestos", "Dibujos", "Inglés"]),
            "Contexto": ("En casa, en la cocina", ["En el colegio", "En el supermercado",
                                                     "En el parque"]),
        },
    ),
    _sit(
        "4. La fiesta",
        "En una fiesta hay mucha música y ruido. Carla ve a su amiga al otro lado de la sala "
        "y le hace gestos para que se acerque.",
        {
            "Emisor": ("Carla", ["Su amiga", "La música", "Un invitado"]),
            "Receptor": ("Su amiga", ["Carla", "La música", "Todos los invitados"]),
            "Mensaje": ("Ven, acércate", ["Me voy a casa", "Baja la música", "Feliz cumpleaños"]),
            "Canal": ("La vista (se ven los gestos)", ["La voz", "Una carta", "El teléfono"]),
            "Código": ("Gestos", ["Español hablado", "Inglés", "Dibujos"]),
            "Contexto": ("En una fiesta, en una sala con mucho ruido",
                         ["En el patio del colegio", "En la calle", "En una biblioteca"]),
        },
    ),
    _sit(
        "5. La ambulancia",
        "Mientras pasean por la ciudad, varias personas escuchan la sirena de una ambulancia "
        "y se apartan para dejarla pasar.",
        {
            "Emisor": ("La ambulancia (su sirena)", ["Las personas que pasean", "La ciudad",
                                                      "Un policía"]),
            "Receptor": ("Las personas que pasean", ["La ambulancia", "La sirena", "El médico"]),
            "Mensaje": ("Apartaos, hay una urgencia: dejad pasar",
                        ["Hoy hay fiesta", "Parad a comprar", "Buenos días"]),
            "Canal": ("El sonido de la sirena (por el aire)", ["Una carta", "Un dibujo",
                                                                "El teléfono"]),
            "Código": ("Sonidos (la sirena)", ["Español escrito", "Gestos", "Inglés"]),
            "Contexto": ("En la ciudad, en la calle", ["En el colegio", "En una fiesta", "En casa"]),
        },
    ),
]

# ───────────────────────── Estilo ─────────────────────────
st.markdown(
    """
<style>
.stApp {background: linear-gradient(160deg,#fdf2ff 0%,#eef6ff 55%,#fff7ec 100%);}
.titulo {text-align:center;padding:18px 10px;border-radius:24px;
  background:linear-gradient(90deg,#b388ff,#7dd3fc);color:white;
  box-shadow:0 6px 18px rgba(124,77,255,.25);margin-bottom:14px;}
.titulo h1 {color:white;margin:0;font-size:2rem;}
.titulo p {margin:4px 0 0;font-size:1.05rem;color:white;}
.tarjeta {background:white;border-radius:20px;padding:10px 14px;
  box-shadow:0 4px 12px rgba(0,0,0,.08);border:2px solid #e9d5ff;margin-bottom:10px;}
.tarjeta .rom {font-size:1.3rem;font-weight:800;color:#7c3aed;}
.tarjeta .num {font-size:1rem;color:#334155;}
.caja {background:white;color:#334155;border-left:8px solid #c4b5fd;
  border-radius:14px;padding:10px 16px;margin:8px 0;
  box-shadow:0 2px 8px rgba(0,0,0,.05);}
.situacion {background:white;color:#334155;border:3px dashed #c4b5fd;
  border-radius:20px;padding:12px 16px;margin:8px 0;font-size:1.05rem;}
/* Pestañas: siempre en rojo */
.stApp button[data-baseweb="tab"] p,
.stApp button[data-baseweb="tab"] {color:#ef4444 !important;font-weight:700;}
.stApp button[data-baseweb="tab"][aria-selected="false"] {opacity:.75;}
/* Títulos y textos legibles también en modo oscuro */
.stApp h2, .stApp h3, .stApp h4,
.stApp h2 *, .stApp h3 *, .stApp h4 * {color:#5b21b6 !important;}
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stMarkdownContainer"] li,
.stApp [data-testid="stCaptionContainer"],
.stApp label, .stApp label p {color:#334155 !important;}
.stApp [data-testid="stMetricLabel"] *, .stApp [data-testid="stMetricValue"] * {color:#5b21b6 !important;}
.stApp .titulo h1, .stApp .titulo p {color:white !important;}
.stApp .tarjeta .rom {color:#7c3aed !important;}
.stApp .tarjeta .num, .stApp .situacion, .stApp .caja {color:#334155 !important;}
/* Botones morados con letra blanca */
.stApp .stButton button,
.stApp [data-testid="stFormSubmitButton"] button,
.stApp [data-testid^="stBaseButton"] {
  background:linear-gradient(90deg,#8b5cf6,#38bdf8) !important;
  border:none !important;border-radius:16px !important;
  box-shadow:0 4px 10px rgba(124,58,237,.25);}
.stApp .stButton button *,
.stApp [data-testid="stFormSubmitButton"] button *,
.stApp [data-testid^="stBaseButton"] * {color:#ffffff !important;font-weight:700;}
/* Campos, listas y desplegables claros */
.stApp input, .stApp textarea {background:#ffffff !important;color:#334155 !important;
  -webkit-text-fill-color:#334155 !important;}
.stApp [data-baseweb="input"], .stApp [data-baseweb="base-input"],
.stApp [data-baseweb="select"] > div {background:#ffffff !important;color:#334155 !important;
  border-radius:12px;}
.stApp [data-baseweb="select"] * {color:#334155 !important;}
[data-baseweb="popover"] *, [data-baseweb="menu"] * {background-color:#ffffff;color:#334155 !important;}
.stApp [data-testid="stRadio"] label {background:#ffffff;border:2px solid #e9d5ff;
  border-radius:14px;padding:6px 12px;margin-bottom:6px;}
.stApp [data-testid="stRadio"] label * {color:#334155 !important;}
.stApp [data-testid="stExpander"] {background:#ffffff;border-radius:14px;}
.stApp [data-testid="stExpander"] summary *,
.stApp [data-testid="stExpander"] p {color:#5b21b6 !important;}
.stApp [data-testid="stForm"] {background:rgba(255,255,255,.6);border-radius:18px;}
</style>
<div class="titulo">
  <h1>🦄 El Reino de los Mensajes Mágicos ✨</h1>
  <p>Descubre quién habla, quién escucha y cómo viaja cada mensaje 🧚‍♀️</p>
</div>
""",
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs(["📖 Aprende", "✏️ Mi ficha", "🎮 Juego"])

# ───────────────────────── 📖 Aprende ─────────────────────────
with tab1:
    st.subheader("💬 Los 6 elementos de la comunicación")
    for e in ELEMENTOS:
        st.markdown(
            f'<div class="tarjeta"><span class="rom">{EMOJIS[e]} {e}</span>: '
            f'<span class="num">{DEFS[e]}.</span></div>',
            unsafe_allow_html=True,
        )

    st.subheader("🧠 Trucos para recordarlos")
    for e in ELEMENTOS:
        st.markdown(f"- {EMOJIS[e]} **{e}** · {PREGUNTAS[e]} → {TRUCOS[e]}")

    st.subheader("🌟 Un ejemplo resuelto")
    s0 = SITUACIONES[0]
    st.markdown(f'<div class="situacion">{s0["texto"]}</div>', unsafe_allow_html=True)
    for e in ELEMENTOS:
        st.markdown(f"- {EMOJIS[e]} **{e}**: {s0['items'][e]['ok']}")

# ───────────────────────── ✏️ Mi ficha ─────────────────────────
with tab2:
    st.subheader("✏️ Las situaciones de mi ficha")
    st.caption("Elige una situación y responde a las 6 preguntas.")
    idx = st.selectbox("Situación", range(len(SITUACIONES)),
                       format_func=lambda i: SITUACIONES[i]["titulo"], key="sel_sit")
    sit = SITUACIONES[idx]
    st.markdown(f'<div class="situacion">{sit["texto"]}</div>', unsafe_allow_html=True)

    with st.form(f"form_ficha_{idx}"):
        for e in ELEMENTOS:
            st.selectbox(
                f"{EMOJIS[e]} {e} ({PREGUNTAS[e]})",
                sit["items"][e]["opts"], index=None, placeholder="Elige…",
                key=f"f{idx}_{e}",
            )
        enviar = st.form_submit_button("Comprobar ✨", use_container_width=True)

    if enviar:
        aciertos = 0
        for e in ELEMENTOS:
            resp = st.session_state.get(f"f{idx}_{e}")
            ok = sit["items"][e]["ok"]
            if resp == ok:
                aciertos += 1
                st.success(f"✅ {EMOJIS[e]} {e}: {ok}")
            elif resp is None:
                st.warning(f"🤔 {EMOJIS[e]} {e}: te falta elegir. Era: {ok}")
            else:
                st.error(f"💡 {EMOJIS[e]} {e}: casi… era **{ok}**")
        st.markdown(f"### {'⭐' * aciertos}{'☆' * (6 - aciertos)}  {aciertos}/6")
        if aciertos == 6:
            st.balloons()
            st.success("🦄 ¡Perfecto! ¡Eres una Princesa de la Comunicación! 👑")
        elif aciertos >= 4:
            st.info("🌈 ¡Muy bien! Repasa los que han fallado y prueba otra vez.")
        else:
            st.info("🧚‍♀️ ¡Ánimo! Mira la pestaña 📖 y vuelve a intentarlo.")

    def _limpiar():
        for e in ELEMENTOS:
            st.session_state[f"f{idx}_{e}"] = None

    st.button("🔄 Borrar respuestas", on_click=_limpiar)

    with st.expander("🔎 Ver la solución de esta situación"):
        for e in ELEMENTOS:
            st.markdown(f"- {EMOJIS[e]} **{e}**: {sit['items'][e]['ok']}")

# ───────────────────────── 🎮 Juego ─────────────────────────
with tab3:
    ss = st.session_state
    for k, v in dict(puntos=0, racha=0, mejor=0, hechas=0, fb=None, q=None, globos=False).items():
        ss.setdefault(k, v)

    def nueva_pregunta():
        e = random.choice(ELEMENTOS)
        if random.random() < 0.7:
            s = random.randrange(len(SITUACIONES))
            it = SITUACIONES[s]["items"][e]
            return {"tipo": "sit", "s": s, "e": e, "opts": it["opts"], "ok": it["ok"]}
        opts = ELEMENTOS[:]
        random.shuffle(opts)
        return {"tipo": "def", "e": e, "opts": opts, "ok": e}

    if ss.q is None:
        ss.q = nueva_pregunta()

    m1, m2, m3 = st.columns(3)
    m1.metric("⭐ Estrellas", ss.puntos)
    m2.metric("🔥 Racha", ss.racha)
    m3.metric("🏆 Mejor", ss.mejor)

    if ss.fb:
        ok_prev, msg = ss.fb
        (st.success if ok_prev else st.error)(msg)
    if ss.globos:
        st.balloons()
        ss.globos = False

    q = ss.q
    if q["tipo"] == "sit":
        st.markdown(f'<div class="situacion">{SITUACIONES[q["s"]]["texto"]}</div>',
                    unsafe_allow_html=True)
        pregunta = f"{EMOJIS[q['e']]} ¿Cuál es el **{q['e'].upper()}**? ({PREGUNTAS[q['e']]})"
    else:
        st.markdown(f'<div class="situacion">«{DEFS[q["e"]].capitalize()}»</div>',
                    unsafe_allow_html=True)
        pregunta = "¿Qué elemento de la comunicación es?"

    with st.form("form_juego"):
        st.markdown(pregunta)
        resp = st.radio("Elige", q["opts"], index=None, key=f"r_{ss.hechas}",
                        label_visibility="collapsed")
        ok_btn = st.form_submit_button("Comprobar ✨", use_container_width=True)

    if ok_btn:
        if resp is None:
            st.warning("👆 Elige una respuesta primero.")
        else:
            acierto = resp == q["ok"]
            ss.hechas += 1
            if acierto:
                ss.puntos += 1
                ss.racha += 1
                ss.mejor = max(ss.mejor, ss.racha)
                frase = random.choice(["¡Genial! 🦄", "¡Magia pura! ✨", "¡Bravo! 🌈", "¡Estupendo! 🧚‍♀️"])
                ss.fb = (True, f"{frase} {q['e']}: {q['ok']}")
                if ss.racha % 5 == 0:
                    ss.globos = True
            else:
                ss.racha = 0
                ss.fb = (False, f"💡 Casi… la respuesta era **{q['ok']}**")
            ss.q = nueva_pregunta()
            st.rerun()

    if st.button("🔄 Empezar de cero"):
        for k in ("puntos", "racha", "mejor", "hechas"):
            ss[k] = 0
        ss.fb = None
        ss.q = nueva_pregunta()
        st.rerun()
