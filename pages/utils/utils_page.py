import os
import streamlit as st

# Fonction pour configurer la page
def set_st_page2(name):
    st.set_page_config(
        page_title=name,
        layout="wide",
    )

    # Masquer la barre latérale par défaut
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # Définition des dictionnaires pour Quants et AI
    page_dico_q = {
        "Home Page": {"Home Page": "main.py"},
        "Market Types": {
            "Basics of Market Types": "pages/mrkt_t_basics.py",
            "Interest & Money Markets": "pages/interest_money_markets.py",
            "Compound Interest Tool": "pages/compound_interest_tool.py",
        },
        "Derivatives": {
            "Basics of Derivatives": "pages/derivative_basics.py",
            "Basics of Options": "pages/option_basics.py",
            "Option Pricing Methods": "pages/option_pricing_methods.py",
            "Option Pricing Tool": "pages/option_pricing_tool.py"
        }
    }

    page_dico_ai = {
        "Home Page": {"Home Page": "main.py"},
        "Agentic AI": {
            "Agentic AI with LangGraph": "pages/agentic_langgraph.py",
            "Agentic AI with SmolAgents": "pages/agenticsmolagents.py",
            "Agentic AI with LlaamaIndex": "pages/agenticllamaindex.py",
        },
        "Clustering": {
            "K-Means": "pages/kmeans.py",
            "Hierarchical Clustering": "pages/hierarch_clustering.py",
            "DBSCAN": "pages/dbscan.py",
        },
        "Dimensionality Reduction": {
            "Principal Component Analysis (PCA)": "pages/pca.py",
            "Latent Discriminant Analysis (LDA)": "pages/lda.py",
            "T-Distributed Stochastic Neighbor Embedding (t-SNE)": "pages/tsne.py",
        }
    }

    # Initialiser l'état de session si ce n'est pas déjà fait
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = "Quants"

    if "selected_tab" not in st.session_state:
        st.session_state.selected_tab = "Home Page"

    # Définir une fonction pour mettre à jour la catégorie sélectionnée dans session_state
    if "update_selected_category" not in st.session_state:
        def update_selected_category(category):
            st.session_state.selected_category = category
            st.session_state.selected_tab = "Home Page"  # On définit "Home Page" comme onglet par défaut

        st.session_state.update_selected_category = update_selected_category

    # Boutons de sélection avec mise en surbrillance
    col1, col2 = st.columns(2)

    # Définition des couleurs dynamiques
    quants_color = "#FF9800" if st.session_state.selected_category == "Quants" else "#e0e0e0"
    ai_color = "#1976D2" if st.session_state.selected_category == "AI" else "#e0e0e0"
    grey_color = "#bdbdbd" if st.session_state.selected_category != "Quants" and st.session_state.selected_category != "AI" else "#e0e0e0"

    # Style CSS amélioré pour les boutons
    button_style = f"""
        <style>
            .custom-button {{
                display: inline-block;
                width: 100%;
                text-align: center;
                font-size: 22px !important;
                font-weight: bold !important;
                padding: 15px !important;
                border-radius: 10px !important;
                cursor: pointer;
                transition: 0.3s;
                margin: 5px 0;
                border: 3px solid transparent;
            }}
            .custom-button:hover {{
                filter: brightness(0.9);
            }}
            .selected {{
                background-color: {quants_color} !important;
                color: white !important;
                border: 3px solid #e65100 !important;
            }}
            .not-selected {{
                background-color: {ai_color} !important;
                color: black !important;
                border: 3px solid #bdbdbd !important;
            }}
            .selected-grey {{
                background-color: {grey_color} !important;
                color: black !important;
                border: 3px solid #757575 !important;
            }}
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Affichage des boutons et mise à jour de l'état de la catégorie sélectionnée
    
    # Si la catégorie est sélectionnée, appliquez un fond gris au bouton correspondant
    with col1:
        is_quants_selected = st.session_state.selected_category == "Quants"
        button_class = "selected-grey" if is_quants_selected else "custom-button"
        if st.button(
            "📊 Explore Quants",
            key="quants",
            help="Explore quantitative finance topics",
            use_container_width=True,
            on_click=lambda: st.session_state.update_selected_category("Quants")
        ):
            st.session_state.selected_category = "Quants"
            st.session_state.selected_tab = "Home Page"
    
    with col2:
        is_ai_selected = st.session_state.selected_category == "AI"
        button_class = "selected-grey" if is_ai_selected else "custom-button"
        if st.button(
            "🤖 Explore AI",
            key="ai",
            help="Explore artificial intelligence topics",
            use_container_width=True,
            on_click=lambda: st.session_state.update_selected_category("AI")
        ):
            st.session_state.selected_category = "AI"
            st.session_state.selected_tab = "Home Page"

    # Mise à jour des pages disponibles (fusionner AI et Quants si AI sélectionné)
    if st.session_state.selected_category == "AI":
        page_dico = {**page_dico_q, **page_dico_ai}  # Fusionner les deux
    else:
        page_dico = page_dico_q

    # Vérification des onglets
    if "expanded_tabs" not in st.session_state or set(st.session_state.expanded_tabs.keys()) != set(page_dico.keys()):
        st.session_state.expanded_tabs = {key: False for key in page_dico}

    if "selected_tab" not in st.session_state or st.session_state.selected_tab not in page_dico:
        st.session_state.selected_tab = "Home Page"  # Onglet par défaut

    # Affichage de la barre latérale
    st.sidebar.title("A.I & Q Odyssey")
    st.sidebar.title("📌 Menu")
    st.sidebar.write(f"Currently exploring: **{st.session_state.selected_category}**")

    for tab_name, subpages in page_dico.items():
        with st.sidebar.expander(f"▶ {tab_name}", expanded=st.session_state.expanded_tabs.get(tab_name, False)):
            for subtab, subtab_path in subpages.items():
                print(subtab_path, subtab)
                st.page_link(page=subtab_path, label=subtab)


    # Mise en page dynamique avec couleur adaptée
    st.markdown(f"""
        <div style="background-color: {'#ffcc80' if st.session_state.selected_category == 'Quants' else '#90caf9'}; 
                    padding: 15px; border-radius: 10px;">
            <h1 style="text-align: center; color: white;">
                Welcome to {st.session_state.selected_category} 🚀
            </h1>
        </div>
    """, unsafe_allow_html=True)