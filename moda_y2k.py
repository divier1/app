
import streamlit as st
import time

st.set_page_config(page_title="Moda Y2K", layout="wide")

# Fondo
page_bg_img = '''
<style>
body {
background-image: url("https://i.pinimg.com/originals/f1/38/69/f13869045b6f0113673f4d6b4dc2e470.jpg");
background-size: cover;
background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: hotpink;'>💿 Las Tendencias Más Icónicas de los 2000 💿</h1>", unsafe_allow_html=True)

# Música
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url, format="audio/mp3")

st.sidebar.title("🎀 Navegación")
categoria = st.sidebar.radio("Selecciona una sección:", [
    "Ropa", "Accesorios", "Calzado", "Belleza", "Celebridades"
])

if categoria == "Ropa":
    st.subheader("👚 Ropa Típica del 2000")
    st.image("https://i.pinimg.com/originals/2f/f4/9a/2ff49a2966b2971f97a46b403b1f57d1.jpg", width=500)
    st.markdown("✨ *¡Mientras más tiro bajo y brillos, mejor!*")
    st.markdown("""
    - Pantalones de tiro bajo  
    - Tops con lentejuelas  
    - Minifaldas denim  
    - Chándales Juicy Couture
    """)

elif categoria == "Accesorios":
    st.subheader("👜 Accesorios llamativos")
    st.image("https://i.pinimg.com/originals/60/4c/47/604c47cfcb5584db36c156f9bb8962f5.jpg", width=500)
    st.markdown("✨ *Todo lo que brilla... ¡lo usaban!*")
    st.markdown("""
    - Gafas gigantes y coloridas  
    - Bolsos baguette  
    - Cinturones anchos con hebillas XL  
    - Collares, piercings y clips
    """)

elif categoria == "Calzado":
    st.subheader("👟 Calzado Estrella")
    st.image("https://i.pinimg.com/originals/0e/02/0d/0e020db83b5d46f4de30dbafcd1be45d.jpg", width=500)
    st.markdown("✨ *Altura y peluche: una combinación mágica*")
    st.markdown("""
    - Zapatillas chunky  
    - Botas UGG  
    - Sandalias con plataforma  
    - Tacones de colores neón
    """)

elif categoria == "Belleza":
    st.subheader("💄 Belleza Y2K")
    st.image("https://i.pinimg.com/originals/67/e7/51/67e751decb871c0f9cf21bb0d7a1e4f5.jpg", width=500)
    st.markdown("✨ *Sombras nacaradas y gloss, por supuesto*")
    st.markdown("""
    - Delineador negro dramático  
    - Labios glossy rosados  
    - Mechas rubias gruesas  
    - Clips de mariposa y peinados divididos
    """)

elif categoria == "Celebridades":
    st.subheader("🌟 Íconos Y2K")
    st.image("https://i.pinimg.com/originals/43/44/4b/43444b4f9c0901bb81859b27e7a093a2.jpg", width=500)
    st.markdown("✨ *Eran más que famosas: eran tendencias caminando*")
    st.markdown("""
    - Britney Spears  
    - Christina Aguilera  
    - Paris Hilton  
    - Beyoncé  
    - Lindsay Lohan  
    """)

if st.button("💬 Dame un dato curioso de la moda 2000"):
    with st.spinner("Viajando en el tiempo..."):
        time.sleep(2)
    st.success("💡 ¡En 2001, Paris Hilton tenía más de 20 chándales Juicy Couture diferentes, uno para cada día del mes!")

st.markdown("---")
st.markdown("<center style='color:gray;'>Diseñado con 💖 por ti. ¡Y2K vibes por siempre!</center>", unsafe_allow_html=True)
