import streamlit as st
import requests
import urllib.parse

API_URL = "http://127.0.0.1:8000/previsao/"

def buscar_previsao(cidade: str):
    try:
        response = requests.get(API_URL, params={"cidade": cidade})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Ocorreu um erro ao buscar a previsão: {e}")
        return None

def excluir_previsao(cidade: str):
    cidade_codificada = urllib.parse.quote(cidade)
    try:
        response = requests.delete(f"{API_URL}{cidade_codificada}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Ocorreu um erro ao excluir a previsão: {e}")
        return None

st.set_page_config(page_title="Previsão do Tempo", page_icon="☀️", layout="wide")

st.title("🌤 Previsão do Tempo 🌤")
st.markdown("Este aplicativo permite que você veja a previsão do tempo para qualquer cidade e exclua previsões salvas diretamente do banco de dados.")

st.subheader("🔍 Buscar Previsão para uma Cidade")
cidade_input = st.text_input("Digite o nome da cidade", "São Luís", max_chars=50)

if st.button("Buscar Previsão"):
    if cidade_input:
        previsao = buscar_previsao(cidade_input)
        if previsao:
            st.markdown(f"### Previsão para **{cidade_input}**:")
            for item in previsao:
                st.write(f"**Temperatura**: {item['temperatura']} °C")
                st.write(f"**Data**: {item['data']}")
                st.write("-" * 20)
        else:
            st.error(f"Não foi possível encontrar a previsão para a cidade **{cidade_input}**.")
    else:
        st.warning("Por favor, insira o nome da cidade!")

st.markdown("---")

st.subheader("❌ Excluir Previsão de uma Cidade")
cidade_excluir_input = st.text_input("Digite o nome da cidade para excluir", "São Luís", max_chars=50)

if st.button("Excluir Previsão"):
    if cidade_excluir_input:
        resultado = excluir_previsao(cidade_excluir_input)
        if resultado:
            st.success(f"A previsão para a cidade **{cidade_excluir_input}** foi excluída com sucesso!")
        else:
            st.error(f"A cidade **{cidade_excluir_input}** não foi encontrada no banco de dados.")
    else:
        st.warning("Por favor, insira o nome da cidade para excluir!")
