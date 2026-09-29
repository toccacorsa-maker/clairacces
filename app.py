
import os
from io import BytesIO
from pathlib import Path

import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"

NAVY = "#063E72"
NAVY2 = "#0A4A7F"
BLUE = "#187BCB"
TEXT = "#173F61"
MUTED = "#5A748A"
BORDER = "#D8E5EE"
GREEN = "#16876F"
PURPLE = "#665BD3"


st.set_page_config(
    page_title="ClairAccès",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html,body,[class*="css"] {{
  font-family:Inter,Arial,sans-serif !important;
}}

.stApp {{
  background:#FAFCFE;
  color:{TEXT};
}}

#MainMenu,header,footer {{ visibility:hidden; }}

.block-container {{
  max-width:none !important;
  padding:0 !important;
}}

section[data-testid="stSidebar"] {{
  width:295px !important;
  min-width:295px !important;
  background:linear-gradient(180deg,#073E71 0%,#073E71 67%,#0B4D82 100%) !important;
  border-right:0 !important;
}}

section[data-testid="stSidebar"] > div {{
  padding:0 !important;
}}

.sidebar-brand {{
  height:100px;
  display:flex;
  align-items:center;
  padding:16px 20px 12px;
  border-bottom:1px solid rgba(255,255,255,.08);
}}

.sidebar-brand img {{
  width:255px;
  height:auto;
}}

.nav-wrap {{
  padding:22px 13px;
}}

.nav-title {{
  color:rgba(255,255,255,.55);
  text-transform:uppercase;
  letter-spacing:.8px;
  font-size:10px;
  font-weight:700;
  margin:0 13px 9px;
}}

.nav-note {{
  color:#fff;
  font-size:12px;
  line-height:1.5;
  padding:15px;
  margin:0 7px 16px;
  border:1px solid rgba(91,185,244,.45);
  background:rgba(9,105,172,.30);
  border-radius:9px;
}}

.nav-note b {{
  display:block;
  margin-bottom:5px;
}}

.side-footer {{
  position:fixed;
  bottom:0;
  width:295px;
  height:185px;
  pointer-events:none;
  background:
    radial-gradient(85% 90% at 8% 100%,rgba(42,126,203,.9) 0 26%,transparent 27%),
    radial-gradient(80% 85% at 50% 112%,rgba(24,94,164,.85) 0 25%,transparent 26%),
    linear-gradient(180deg,transparent 0 35%,rgba(11,77,130,.5) 36% 100%);
}}

.main-top {{
  height:68px;
  border-bottom:1px solid #E2EBF1;
  background:white;
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:0 27px 0 31px;
}}

.main-top .subtitle {{
  color:#14569A;
  font-size:14px;
  font-weight:500;
}}

.main-top .right {{
  display:flex;
  align-items:center;
  gap:17px;
  color:#0D4A7E;
  font-size:12px;
  font-weight:600;
}}

.page {{
  padding:0 30px 28px;
}}

.hero {{
  height:245px;
  margin:0 -30px;
  position:relative;
  overflow:hidden;
  background:#EAF6FB;
  border-bottom:1px solid #D7E7F0;
}}

.hero-photo {{
  position:absolute;
  right:0;
  top:0;
  width:54%;
  height:100%;
  background:url("assets/hero_corse.jpg") center/cover no-repeat;
}}

.hero-photo:after {{
  content:"";
  position:absolute;
  inset:0;
  background:linear-gradient(90deg,rgba(235,247,252,1) 0%,rgba(235,247,252,.87) 13%,rgba(235,247,252,.35) 39%,rgba(235,247,252,0) 65%);
}}

.hero-copy {{
  position:relative;
  z-index:2;
  width:61%;
  padding:32px 31px;
}}

.hero-copy .hello {{
  font-size:31px;
  color:#14518B;
  line-height:1;
  margin-bottom:5px;
}}

.hero-copy h1 {{
  font-size:31px;
  color:#0A467C;
  line-height:1.05;
  margin:0 0 14px;
  letter-spacing:-1px;
}}

.hero-copy h1 span {{
  color:#0D477B;
}}

.hero-copy p {{
  font-size:15px;
  color:#1B5483;
  line-height:1.45;
  margin:0 0 17px;
}}

.trust {{
  display:flex;
  align-items:center;
  gap:0;
}}

.trust-item {{
  display:flex;
  align-items:center;
  gap:8px;
  color:#1A5C93;
  font-size:12px;
  padding-right:18px;
  margin-right:18px;
  border-right:1px solid #BFD7E5;
}}

.trust-item:last-child {{
  border-right:0;
}}

.trust-icon {{
  width:29px;
  height:29px;
  border-radius:50%;
  background:#DDEFFD;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:14px;
}}

.section-title {{
  color:#104B81;
  font-size:20px;
  font-weight:800;
  margin:27px 0 15px;
}}

.content-grid {{
  display:grid;
  grid-template-columns:minmax(0,1fr) 382px;
  gap:22px;
}}

.tools {{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:18px;
}}

.tool-card {{
  min-height:160px;
  border:1px solid #D4E4ED;
  border-radius:10px;
  background:linear-gradient(135deg,#F2F9FD,#F7FBFD);
  padding:18px 19px;
  position:relative;
  box-shadow:0 2px 8px rgba(25,67,94,.035);
}}

.tool-card.green {{
  background:linear-gradient(135deg,#F0FBF8,#F5FCFA);
  border-color:#C8E7DD;
}}

.tool-card.purple {{
  background:linear-gradient(135deg,#F5F4FD,#FAF9FE);
  border-color:#DDD9F5;
}}

.tool-card .icon {{
  width:48px;
  height:48px;
  border-radius:14px;
  display:flex;
  align-items:center;
  justify-content:center;
  color:white;
  font-size:24px;
  background:#3A91DE;
  margin-bottom:12px;
}}

.tool-card.green .icon {{ background:#22A07F; }}
.tool-card.purple .icon {{ background:#7066D7; }}

.tool-card h3 {{
  color:#0D4F87;
  font-size:15px;
  line-height:1.25;
  margin:0 35px 7px 0;
}}

.tool-card p {{
  color:#2F6084;
  font-size:12px;
  line-height:1.5;
  margin:0;
}}

.arrow {{
  position:absolute;
  right:15px;
  bottom:16px;
  width:34px;
  height:34px;
  border-radius:50%;
  background:#DDEFFD;
  color:#2376B8;
  display:flex;
  align-items:center;
  justify-content:center;
  font-weight:800;
}}

.green .arrow {{
  background:#D9F3EB;
  color:#19846D;
}}

.purple .arrow {{
  background:#E8E5FB;
  color:#6559C8;
}}

.support {{
  margin-top:18px;
  min-height:105px;
  border:1px solid #D2E5EF;
  border-radius:9px;
  background:#F0F8FD;
  padding:16px 19px;
  display:flex;
  gap:14px;
  align-items:center;
}}

.support .bigicon {{
  width:50px;
  height:50px;
  border-radius:50%;
  background:#DCEFFC;
  color:#217AC5;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:23px;
  flex:0 0 50px;
}}

.support h4 {{
  margin:0 0 5px;
  color:#14558F;
  font-size:13px;
}}

.support p {{
  margin:0;
  color:#49718D;
  font-size:11px;
  line-height:1.45;
}}

.handwritten {{
  margin-left:auto;
  color:#0A568C;
  font-size:18px;
  font-style:italic;
  transform:rotate(-4deg);
  white-space:nowrap;
}}

.side-card {{
  border:1px solid #D4E4ED;
  border-radius:10px;
  background:#F4F9FC;
  padding:16px 17px;
  margin-bottom:14px;
}}

.side-card.focus {{
  background:#EDF7FE;
  border-color:#CDE4F3;
}}

.side-card.security {{
  background:#F0FBF7;
  border-color:#BDE6D9;
}}

.side-head {{
  color:#12558C;
  font-size:13px;
  font-weight:800;
  margin-bottom:10px;
}}

.side-card p {{
  color:#4C6D84;
  font-size:11px;
  line-height:1.5;
  margin:5px 0;
}}

.pill-button {{
  display:inline-block;
  margin-top:7px;
  border:1px solid #73B6E6;
  color:#1370B8;
  border-radius:19px;
  padding:7px 12px;
  font-size:11px;
  font-weight:700;
}}

.action {{
  display:flex;
  gap:10px;
  align-items:center;
  padding:9px 0;
  border-top:1px solid #DDE8EF;
}}

.action:first-of-type {{
  border-top:0;
}}

.action-icon {{
  width:35px;
  height:35px;
  border-radius:50%;
  display:flex;
  align-items:center;
  justify-content:center;
  background:#DDF3EC;
  color:#1B886E;
}}

.action:nth-of-type(3) .action-icon {{
  background:#E5EFFA;
  color:#2777BE;
}}

.action:nth-of-type(4) .action-icon {{
  background:#EAE7FC;
  color:#665CD0;
}}

.action-text {{
  flex:1;
}}

.action-text b {{
  display:block;
  color:#1A5A8D;
  font-size:11px;
}}

.action-text span {{
  color:#6A8091;
  font-size:9px;
}}

.security .ok {{
  color:#188571;
  margin-right:7px;
  font-weight:800;
}}

.bottom-wave {{
  height:74px;
  margin:30px -30px 0;
  background:url("assets/footer_waves.png") center/cover no-repeat;
  position:relative;
}}

.bottom-wave .tag {{
  position:absolute;
  left:42%;
  top:40px;
  color:white;
  font-size:10px;
  font-weight:600;
}}

@media (max-width:1050px) {{
  section[data-testid="stSidebar"] {{ width:245px !important; min-width:245px !important; }}
  .side-footer {{ width:245px; }}
  .content-grid {{ grid-template-columns:1fr; }}
}}

@media (max-width:750px) {{
  section[data-testid="stSidebar"] {{ display:none; }}
  .main-top {{ padding:0 15px; }}
  .page {{ padding:0 15px 20px; }}
  .hero {{ margin:0 -15px; height:270px; }}
  .hero-copy {{ width:100%; padding:28px 20px; }}
  .hero-photo {{ width:100%; opacity:.35; }}
  .tools {{ grid-template-columns:1fr; }}
  .bottom-wave {{ margin-left:-15px; margin-right:-15px; }}
}}
</style>
""", unsafe_allow_html=True)


def local_explanation(text):
    if not text.strip():
        return "Aucun document n’a encore été renseigné."
    return (
        "• L’administration vous communique une information ou vous demande une action.\n"
        "• Vérifiez le délai indiqué et les justificatifs éventuellement demandés.\n"
        "• Conservez une copie du document et de votre réponse."
    )


def local_letter(situation):
    return f"""Objet : Demande d’examen prioritaire de ma situation

Madame, Monsieur,

Je souhaite solliciter l’examen attentif de ma situation concernant ma demande de logement.

Ma situation :
{situation.strip()}

Au regard de ces éléments, je vous remercie de bien vouloir examiner ma demande et de m’indiquer les démarches ou suites qui peuvent être données.

Je reste à votre disposition pour fournir tout justificatif nécessaire.

Je vous prie d’agréer, Madame, Monsieur, l’expression de ma considération distinguée.

Nom et prénom :
Adresse :
Téléphone :
E-mail :
"""


def generate_help(document, situation):
    key = os.getenv("GROQ_API_KEY", "").strip()
    if key:
        try:
            from groq import Groq
            client = Groq(api_key=key)
            prompt = f"""
Tu es ClairAccès, assistant administratif français.
Explique en langage simple. Ne garantis jamais une décision juridique.

Document:
{document}

Situation:
{situation}

Structure exactement :
TRADUCTION SIMPLIFIÉE
- 3 puces

LETTRE DE RECOURS
- courrier complet, poli et à relire avant envoi.
"""
            result = client.chat.completions.create(
                model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
                messages=[{"role":"user","content":prompt}],
                temperature=0.2,
            )
            return result.choices[0].message.content
        except Exception:
            pass

    return "TRADUCTION SIMPLIFIÉE\n\n" + local_explanation(document) + \
           "\n\nLETTRE DE RECOURS\n\n" + local_letter(situation)


def make_pdf(text):
    buf = BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4, leftMargin=45, rightMargin=45,
        topMargin=45, bottomMargin=45, title="ClairAccès"
    )
    font = "Helvetica"
    for name, path in [
        ("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ("LiberationSans", "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"),
    ]:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                font = name
                break
            except Exception:
                pass
    styles = getSampleStyleSheet()
    body = ParagraphStyle(
        "body", parent=styles["BodyText"], fontName=font,
        fontSize=10.5, leading=15, alignment=TA_LEFT, spaceAfter=7
    )
    story = []
    for line in text.splitlines():
        safe = line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
        story.append(Paragraph(safe or "&nbsp;", body))
    doc.build(story)
    return buf.getvalue()


# Sidebar
with st.sidebar:
    st.markdown(
        f'<div class="sidebar-brand"><img src="data:image/png;base64,{__import__("base64").b64encode((ASSETS/"brand.png").read_bytes()).decode()}"></div>',
        unsafe_allow_html=True,
    )

    if "page" not in st.session_state:
        st.session_state.page = "Accueil"

    pages = [
        ("⌂", "Accueil"),
        ("▤", "Traduction de document"),
        ("✎", "Rédaction de courrier"),
        ("♢", "Simulateur DALO"),
        ("□", "Mes documents"),
        ("?", "Aide & FAQ"),
    ]

    st.markdown('<div class="nav-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="nav-title">Navigation</div>', unsafe_allow_html=True)
    for icon, label in pages:
        active = st.session_state.page == label
        if st.button(
            f"{icon}   {label}",
            key="nav_" + label,
            use_container_width=True,
            type="primary" if active else "secondary",
        ):
            st.session_state.page = label
            st.rerun()

    st.markdown("""
    <div class="nav-note">
      <b>🛡 Sécurité & Confiance</b>
      Vos données sont protégées et ne sont jamais stockées.<br>
      En savoir plus →
    </div>
    <div class="side-footer"></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Topbar
st.markdown("""
<div class="main-top">
  <div class="subtitle">Votre assistant administratif pour le logement social et d’urgence</div>
  <div class="right">♧ &nbsp;&nbsp; ◉ &nbsp; Utilisateur &nbsp;⌄</div>
</div>
""", unsafe_allow_html=True)

page = st.session_state.page

# HOME
if page == "Accueil":
    st.markdown('<div class="page">', unsafe_allow_html=True)
    st.markdown("""
    <section class="hero">
      <div class="hero-photo"></div>
      <div class="hero-copy">
        <div class="hello">Bonjour,</div>
        <h1>⚖ &nbsp;Bienvenue sur <span>ClairAccès</span></h1>
        <p>Votre aide pour comprendre vos documents administratifs<br>
        et rédiger vos courriers de recours.</p>
        <div class="trust">
          <div class="trust-item"><span class="trust-icon">✓</span>Gratuit</div>
          <div class="trust-item"><span class="trust-icon">ϟ</span>Simple d’utilisation</div>
          <div class="trust-item"><span class="trust-icon">♢</span>Anonyme et sécurisé</div>
        </div>
      </div>
    </section>
    <div class="section-title">Choisissez ce que vous souhaitez faire</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="content-grid"><div>', unsafe_allow_html=True)
    st.markdown('<div class="tools">', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="tool-card">
          <div class="icon">▤</div>
          <h3>Traduire un jargon administratif<br>en mots simples</h3>
          <p>Copiez-collez un texte officiel reçu ou décrivez votre situation. Nous vous l’expliquons en langage clair.</p>
          <div class="arrow">→</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ouvrir", key="home_translate", use_container_width=True):
            st.session_state.page = "Traduction de document"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="tool-card green">
          <div class="icon">✎</div>
          <h3>Générer votre lettre de recours<br>(Logement / DALO)</h3>
          <p>Expliquez votre urgence avec vos propres mots. Nous vous aidons à rédiger un courrier officiel, clair et adapté.</p>
          <div class="arrow">→</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ouvrir", key="home_letter", use_container_width=True):
            st.session_state.page = "Rédaction de courrier"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tool-card purple" style="margin-top:18px;max-width:50%;">
      <div class="icon">♢</div>
      <h3>Simulateur d’éligibilité DALO</h3>
      <p>Vérifiez si votre situation respecte les critères d’urgence légaux.</p>
      <div class="arrow">→</div>
    </div>

    <div class="support">
      <div class="bigicon">▤</div>
      <div>
        <h4>Un accompagnement simple, concret et humain</h4>
        <p>ClairAccès est là pour vous aider à faire valoir vos droits et à avancer dans vos démarches<br>de logement, sans jargon et sans stress.</p>
      </div>
      <div class="handwritten">Vos droits<br>comptent !</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div><aside>', unsafe_allow_html=True)

    st.markdown("""
    <div class="side-card focus">
      <div class="side-head">📍 &nbsp;Focus Corse-du-Sud</div>
      <p>Vous êtes dans le département Corse-du-Sud ?</p>
      <p>Nos modèles et conseils sont adaptés à votre territoire.</p>
      <div class="pill-button">Voir les spécificités &nbsp;→</div>
    </div>

    <div class="side-card">
      <div class="side-head">◷ &nbsp; Mes dernières actions</div>
      <div class="action"><div class="action-icon">✎</div><div class="action-text"><b>Lettre de recours générée</b><span>12 avril 2025 · DALO</span></div><b>›</b></div>
      <div class="action"><div class="action-icon">▤</div><div class="action-text"><b>Traduction de document</b><span>10 avril 2025 · Logement social</span></div><b>›</b></div>
      <div class="action"><div class="action-icon">♢</div><div class="action-text"><b>Simulateur DALO</b><span>8 avril 2025 · Éligibilité probable</span></div><b>›</b></div>
    </div>

    <div class="side-card security">
      <div class="side-head">🛡 &nbsp;Sécurité, Confidentialité & RGPD</div>
      <p><span class="ok">✓</span>Aucune donnée n’est stockée après fermeture.</p>
      <p><span class="ok">✓</span>Application anonyme sans stockage persistant.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</aside></div>', unsafe_allow_html=True)
    st.markdown('<div class="bottom-wave"><div class="tag">Ensemble pour un meilleur accès au logement</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# TRANSLATION
elif page == "Traduction de document":
    st.markdown('<div class="page">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Traduire un document administratif</div>', unsafe_allow_html=True)
    document = st.text_area(
        "Document",
        placeholder="Collez ici le courrier ou le texte administratif reçu…",
        height=250,
        label_visibility="collapsed",
    )
    if st.button("✣ Traduire en langage simple", type="primary", use_container_width=True):
        with st.spinner("Analyse du document…"):
            result = generate_help(document, "")
        st.success("Voici une première explication en langage clair :")
        st.markdown(result)
    st.markdown('</div>', unsafe_allow_html=True)

# LETTER
elif page == "Rédaction de courrier":
    st.markdown('<div class="page">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Rédiger un courrier de recours</div>', unsafe_allow_html=True)
    situation = st.text_area(
        "Situation",
        placeholder="Expliquez votre situation avec vos propres mots…",
        height=240,
        label_visibility="collapsed",
    )
    if st.button("✣ Générer mon courrier", type="primary", use_container_width=True):
        result = generate_help("", situation)
        st.markdown(result)
        st.download_button(
            "📄 Télécharger en PDF",
            make_pdf(result),
            "courrier_clairacces.pdf",
            "application/pdf",
            use_container_width=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

# DALO
elif page == "Simulateur DALO":
    st.markdown('<div class="page">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Simulateur d’éligibilité DALO</div>', unsafe_allow_html=True)
    st.caption("Cette simulation est indicative et ne remplace pas l’examen juridique du dossier.")
    a = st.checkbox("Numéro Unique de demande de logement social depuis un délai anormalement long")
    b = st.checkbox("Procédure d’expulsion sans relogement")
    c = st.checkbox("Logement insalubre, dangereux, suroccupé ou indécent")
    d = st.checkbox("Personne handicapée ou enfant mineur à charge dans un logement inadapté")
    if st.button("Calculer l’éligibilité", type="primary"):
        if a or b or c or (d and c):
            st.success("Plusieurs éléments peuvent justifier un examen prioritaire. Faites vérifier votre situation par l’organisme compétent.")
        else:
            st.warning("Les critères principaux du prototype ne semblent pas cochés.")
    st.markdown('</div>', unsafe_allow_html=True)

# DOCUMENTS
elif page == "Mes documents":
    st.markdown('<div class="page">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Mes documents</div>', unsafe_allow_html=True)
    st.info("Dans cette version, aucun document n’est conservé après fermeture de l’application. Cette page prépare une future gestion locale des documents.")
    st.markdown('</div>', unsafe_allow_html=True)

# FAQ
else:
    st.markdown('<div class="page">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Aide & FAQ</div>', unsafe_allow_html=True)
    with st.expander("ClairAccès conserve-t-il mes données ?"):
        st.write("Le prototype ne met en place aucun stockage persistant.")
    with st.expander("La simulation DALO constitue-t-elle une décision juridique ?"):
        st.write("Non. Elle sert uniquement à orienter l’usager et doit être vérifiée avec les organismes compétents.")
    with st.expander("Puis-je utiliser l’IA ?"):
        st.write("Oui. Une clé GROQ_API_KEY peut être configurée pour activer une génération IA. Sans clé, le prototype utilise un mode de démonstration local.")
    st.markdown('</div>', unsafe_allow_html=True)
