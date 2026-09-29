# ClairAccès V3

V3 basée sur le visuel proposé :
- vraie navigation latérale ;
- écran d'accueil type tableau de bord ;
- hero Corse-du-Sud ;
- cartes d'actions ;
- Focus Corse-du-Sud ;
- dernières actions ;
- sécurité/RGPD ;
- pages Traduction, Courrier, DALO, Documents, FAQ ;
- export PDF ;
- IA Groq facultative.

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## IA facultative

```bash
export GROQ_API_KEY="votre_cle"
streamlit run app.py
```

Sans clé, l'application reste fonctionnelle en mode démonstration local.
