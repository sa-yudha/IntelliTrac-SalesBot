import os
import glob
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="IntelliTrac SalesBot - Pre-Sales Assistant",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Styling (IntelliTrac Brand: Deep Navy #0A2540, Vibrant Orange #F26522, Soft Gray #F4F6F9)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Roboto:wght@400;500;700&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    h1, h2, h3, h4, h5, h6, .header-title {
        font-family: 'Poppins', sans-serif !important;
    }
    .main {
        background-color: #F4F4F4;
    }
    
    /* Header Banner */
    .header-container {
        background-color: #E65100;
        padding: 24px 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(230, 81, 0, 0.2);
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        color: #FFFFFF;
    }
    .header-subtitle {
        font-size: 1.05rem;
        opacity: 0.95;
        margin-top: 6px;
        font-weight: 500;
    }
    .header-badge {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-top: 12px;
        font-family: 'Poppins', sans-serif;
    }

    /* Sales Handoff Card */
    .sales-card {
        background-color: #FFFFFF;
        border-left: 6px solid #E65100;
        padding: 20px 24px;
        border-radius: 18px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        margin: 15px 0;
    }
    .sales-card h4 {
        color: #0D1F3C;
        margin: 0 0 10px 0;
        font-weight: 700;
        font-family: 'Poppins', sans-serif;
    }
    .sales-card p {
        color: #475569;
        font-size: 0.95rem;
        margin-bottom: 14px;
    }
    .wa-button {
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        font-weight: 700;
        padding: 10px 20px;
        border-radius: 10px;
        text-decoration: none;
        font-size: 0.95rem;
        box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3);
        font-family: 'Poppins', sans-serif;
        transition: transform 0.2s ease;
    }
    .wa-button:hover { transform: translateY(-2px); }
    
    .email-button {
        display: inline-block;
        background-color: #0D1F3C;
        color: white !important;
        font-weight: 700;
        padding: 10px 20px;
        border-radius: 10px;
        text-decoration: none;
        font-size: 0.95rem;
        margin-left: 10px;
        transition: transform 0.2s ease;
        font-family: 'Poppins', sans-serif;
    }
    .email-button:hover { transform: translateY(-2px); }

    /* Prompt Chips */
    .chip-container {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 20px;
    }
    .stButton>button {
        border-radius: 10px !important;
        border: none !important;
        background-color: #E65100 !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.2s ease;
        font-family: 'Poppins', sans-serif;
        box-shadow: 0 2px 8px rgba(230, 81, 0, 0.2);
    }
    .stButton>button:hover {
        background-color: #0D1F3C !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(13, 31, 60, 0.3);
    }
</style>
""", unsafe_allow_html=True)


# 3. Helper Function to Load Knowledge Base
@st.cache_data(show_spinner=False)
def load_knowledge_base():
    knowledge_dir = os.path.join(os.path.dirname(__file__), "knowledge")
    knowledge_text = ""
    
    if os.path.exists(knowledge_dir):
        files = glob.glob(os.path.join(knowledge_dir, "*.md"))
        for file_path in files:
            file_name = os.path.basename(file_path)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    knowledge_text += f"\n--- START OF DOCUMENT: {file_name} ---\n"
                    knowledge_text += content
                    knowledge_text += f"\n--- END OF DOCUMENT: {file_name} ---\n"
            except Exception as e:
                st.warning(f"Gagal membaca file knowledge: {file_name}")
    return knowledge_text

KNOWLEDGE_BASE = load_knowledge_base()

# 4. Construct System Instruction for Gemini
SYSTEM_INSTRUCTION = f"""
Kamu adalah "Mintel", Asisten Virtual Pre-Sales AI Resmi dari PT Intimap (IntelliTrac Indonesia).
Tugas utamamu adalah membantu calon pelanggan yang tertarik dengan produk GPS Tracker, AI Dashcam, dan Solusi Manajemen Armada (Fleet Management) IntelliTrac.

DOKUMEN PENGETAHUAN PERUSAHAAN & PRODUK (KNOWLEDGE BASE):
{KNOWLEDGE_BASE}

PANDUAN UTAMA BERINTERAKSI & GAYA BAHASA:
1. **Identitas & Kepribadian**: Namamu "Mintel". Kamu ramah, profesional, solutif, komunikatif, dan menggunakan Bahasa Indonesia yang sopan namun santai.
2. **Edukasi & Konsultasi Kebutuhan**:
   - Bantu calon pelanggan mengenali produk mana yang paling cocok dengan jenis kendaraannya.
   - Contoh Rekomendasi:
     * Truk Pendingin (Reefer): Rekomendasikan **VT-45 + Sensor Suhu & Sensor Pintu**.
     * Truk Semen / Readymix: Rekomendasikan **VT-45 / IT-360 + Sensor Rotasi Drum Mixer**.
     * Truk Kargo / Logistik Umum: Rekomendasikan **VT-45 Lite** (dasar) atau **VT-45** (lengkap dengan door sensor).
     * Armada Komersial/Bus dengan Pengawasan Sopir (K3 & Safety): Rekomendasikan **Dual AI Dashcam JC261** (ADAS + DMS) atau **JC450** (hingga 5 kamera).
     * Mobil Operasional / Kendaraan Dinas: Rekomendasikan **VT-45 Lite**.
3. **Penjelasan Fitur**: Jelaskan fitur-fitur seperti Live Tracking 4G, Engine Cut-Off (immobilizer), ADAS (Advanced Driver Assistance), DMS (Driver Monitoring System), OBD-II CAN800 dengan bahasa yang jelas.
4. **Kebijakan Handoff Sales (PENTING)**:
   - Jika calon customer bertanya mengenai **harga spesifik, skema penawaran resmi, paket pembelian dalam jumlah armada banyak (fleet diskon), atau berniat melakukan negosiasi/pembelian**, berikan penjelasan umum mengenai fleksibilitas paket layanan IntelliTrac.
   - Kemudian **arahkan calon customer untuk menghubungi Sales Person (manusia asli) dari tim IntelliTrac** melalui tombol kontak sales yang tersedia di aplikasi atau kontak telepon/WhatsApp resmi.
5. **Jawaban Berdasarkan Data Resmi**: Selalu gunakan fakta dan spesifikasi yang ada di Knowledge Base di atas. Jangan mengarang fitur yang tidak dimiliki IntelliTrac.
6. **Batasan Konteks (STRICT OUT-OF-SCOPE RULE)**: Kamu HANYA BOLEH menjawab pertanyaan seputar GPS Tracker, AI Dashcam, Manajemen Armada (Fleet Management), dan produk/layanan PT Intimap (IntelliTrac). Jika pengguna menanyakan topik di luar ini (contoh: politik, hiburan, olahraga, sejarah umum, coding, dll), TOLAK dengan sopan dan kembalikan percakapan ke konteks awal. Contoh penolakan: "Mohon maaf, sebagai Mintel (Asisten Virtual Pre-Sales IntelliTrac), saya khusus diprogram untuk berdiskusi seputar solusi pelacak kendaraan dan manajemen armada. Ada pertanyaan seputar GPS Tracker atau AI Dashcam yang bisa saya bantu?"
"""

# 5. Sidebar Setup
with st.sidebar:
    st.markdown("""
    <div style="background-color: #0D1F3C; padding: 18px 14px; border-radius: 12px; color: white; text-align: center; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(13, 31, 60, 0.2);">
        <h3 style="margin: 0; color: #FFFFFF; font-size: 1.4rem; font-weight: 800; font-family: 'Poppins', sans-serif;">INTELLITRAC</h3>
        <p style="margin: 0; color: #E65100; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; font-family: 'Poppins', sans-serif;">GPS & FLEET SOLUTIONS</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### 🛰️ IntelliTrac SalesBot")
    st.markdown("Asisten Pintar Pre-Sales IntelliTrac GPS & Fleet Management Systems.")
    st.divider()

    # Gemini API Key Management
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.subheader("🔑 Konfigurasi API Key")
        api_key = st.text_input("Google Gemini API Key:", type="password", help="Masukkan API Key dari Google AI Studio")
        if api_key:
            st.success("API Key berhasil dimasukkan!")
        else:
            st.info("💡 Belum ada API Key di .env. Anda dapat memasukkannya di atas.")

    st.divider()

    # Quick Solution Finder Widget
    st.subheader("🔍 Fast Product Match")
    jenis_armada = st.selectbox(
        "Pilih Jenis Armada Anda:",
        ["-- Pilih Jenis Armada --", "Truk Logistik / Kargo", "Truk Pendingin (Reefer)", "Truk Semen / Mixer", "Truk Tambang & Alat Berat", "Bus & Mobil Operasional"]
    )
    
    if jenis_armada != "-- Pilih Jenis Armada --":
        if st.button("💡 Lihat Rekomendasi Produk"):
            prompt_map = {
                "Truk Logistik / Kargo": "Halo Mintel, saya punya armada Truk Logistik / Kargo. Produk GPS Tracker apa yang paling cocok dan apa fiturnya?",
                "Truk Pendingin (Reefer)": "Halo Mintel, saya butuh sistem pemantau suhu dan lokasi untuk Truk Pendingin (Reefer). Apa solusi dari IntelliTrac?",
                "Truk Semen / Mixer": "Halo Mintel, produk mana yang cocok untuk Truk Semen / Readymix Mixer?",
                "Truk Tambang & Alat Berat": "Halo Mintel, rekomendasi GPS dan sensor untuk Truk Tambang & Alat Berat apa ya?",
                "Bus & Mobil Operasional": "Halo Mintel, rekomendasi Dashcam AI / GPS untuk Bus dan Mobil Operasional Perusahaan apa?"
            }
            st.session_state["pending_prompt"] = prompt_map.get(jenis_armada, "")

    st.divider()

    # Contact Sales Handoff Card in Sidebar
    st.markdown("""
    <div style="background-color: #F8FAFC; padding: 16px; border-radius: 12px; border: 1px solid #E2E8F0; border-left: 5px solid #E65100; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <h5 style="color: #0D1F3C; margin-top:0; font-family: 'Poppins', sans-serif; font-weight: 700;">📞 Hubungi Tim Sales</h5>
        <p style="font-size:0.85rem; color:#475569; margin-bottom:12px;">Siap mendapatkan penawaran harga resmi & negosiasi armada?</p>
        <a href="https://wa.me/628118456789?text=Halo%20Sales%20IntelliTrac,%20saya%20tertarik%20dengan%20produk%20GPS%20Tracker" target="_blank" style="text-decoration:none;">
            <div style="background-color:#25D366; color:white; text-align:center; padding:8px; border-radius:8px; font-weight:bold; font-size:0.85rem; font-family: 'Poppins', sans-serif; box-shadow: 0 2px 6px rgba(37,211,102,0.3);">
                💬 Chat via WhatsApp
            </div>
        </a>
        <div style="font-size:0.8rem; color:#64748B; margin-top:12px;">
            <b>Telp:</b> (021) 6325 999<br>
            <b>Email:</b> <a href="mailto:sales@intellitrac.co.id" style="color: #E65100; text-decoration: none;">sales@intellitrac.co.id</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    if st.button("🗑️ Hapus Riwayat Chat"):
        st.session_state.messages = []
        st.session_state.chat_session = None
        st.rerun()

# 6. Main Header Banner
st.markdown("""
<div class="header-container">
    <div class="header-title">IntelliTrac SalesBot 🛰️</div>
    <div class="header-subtitle">Asisten Konsultasi Pre-Sales GPS Tracker, AI Dashcam & Solusi Manajemen Armada PT Intimap</div>
    <div class="header-badge">Powered by Google Gemini AI & Knowledge Base IntelliTrac 2026</div>
</div>
""", unsafe_allow_html=True)

# 7. Initialize Chat Messages & Gemini Client
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Halo! Saya **Mintel**, Asisten Virtual Pre-Sales IntelliTrac GPS Indonesia 👋🏼\n\nAda yang bisa saya bantu terkait kebutuhan pelacak kendaraan, AI Dashcam, atau sistem manajemen armada bisnis Anda hari ini?"
        }
    ]

# Display Previous Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🛰️" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"])

# Quick Prompt Chips (displayed if conversation is short)
if len(st.session_state.messages) <= 2:
    st.markdown("**💡 Pertanyaan Populer:**")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🚚 Rekomendasi Truk Pendingin"):
            st.session_state["pending_prompt"] = "Rekomendasi GPS Tracker untuk Truk Pendingin (Reefer) apa ya?"
    with col2:
        if st.button("📷 AI Dashcam JC261 vs JC450"):
            st.session_state["pending_prompt"] = "Apa perbedaan fitur Dashcam JC261 dan JC450?"
    with col3:
        if st.button("🔌 Modul OBD-II CAN800"):
            st.session_state["pending_prompt"] = "Apa kegunaan modul OBD-II CAN800 bagi armada kami?"
    with col4:
        if st.button("📑 Minta Penawaran Harga"):
            st.session_state["pending_prompt"] = "Saya ingin meminta penawaran harga resmi untuk 10 unit kendaraan perusahaan."

# Check if there is a pending prompt from sidebar or chips
user_input = st.chat_input("Ketik pertanyaan Anda di sini... (contoh: Rekomendasi GPS untuk truk kargo)")
if "pending_prompt" in st.session_state and st.session_state["pending_prompt"]:
    user_input = st.session_state.pop("pending_prompt")

# 8. Handle User Input
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # Generate Assistant Response
    with st.chat_message("assistant", avatar="🛰️"):
        if not api_key:
            error_msg = "⚠️ API Key Google Gemini belum dikonfigurasi. Silakan masukkan GOOGLE_API_KEY di file `.env` atau melalui sidebar."
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
        else:
            try:
                genai.configure(api_key=api_key)
                
                # Configure Gemini model with fallback priority
                fallback_models = [
                    "gemini-3.5-flash-lite",
                    "gemini-3.1-flash-lite",
                    "gemini-3.6-flash",
                    "gemini-3.5-flash"
                ]
                model = None
                for m_name in fallback_models:
                    try:
                        model = genai.GenerativeModel(
                            model_name=m_name,
                            system_instruction=SYSTEM_INSTRUCTION
                        )
                        # Successfully initialized, break out of loop
                        break
                    except Exception as e:
                        st.warning(f"Model {m_name} unavailable, trying next...")
                        model = None
                if model is None:
                    raise RuntimeError("All Gemini models failed to initialize.")

                # Format conversation history for Gemini API
                formatted_history = []
                for msg in st.session_state.messages[:-1]:
                    role = "user" if msg["role"] == "user" else "model"
                    formatted_history.append({"role": role, "parts": [msg["content"]]})

                # Start chat session with history
                chat = model.start_chat(history=formatted_history)
                
                with st.spinner("Mintel sedang berpikir..."):
                    response = chat.send_message(user_input)
                    reply_text = response.text

                st.markdown(reply_text)
                st.session_state.messages.append({"role": "assistant", "content": reply_text})

                # Detect if the query triggers Sales Handoff (Price quotation, sales contact, discount, purchase)
                handoff_keywords = ["harga", "biaya", "penawaran", "quotation", "diskon", "beli", "pesan", "sales", "hubungi", "kontak", "bayar"]
                if any(kw in user_input.lower() for kw in handoff_keywords):
                    st.markdown("""
                    <div class="sales-card">
                        <h4>🤝 Terhubung dengan Tim Sales Representative IntelliTrac</h4>
                        <p>Untuk mendapatkan <b>Surat Penawaran Resmi (Official Quotation)</b>, kalkulasi biaya instalasi, dan penawaran khusus armada Anda, silakan hubungi Sales Executive kami:</p>
                        <a href="https://wa.me/628118456789?text=Halo%20Tim%20Sales%20IntelliTrac,%20saya%20ingin%20berkonsultasi%20dan%20meminta%20penawaran%20harga%20resmi" target="_blank" class="wa-button">
                            💬 Chat Sales via WhatsApp (+62 811-845-6789)
                        </a>
                        <a href="mailto:sales@intellitrac.co.id?subject=Permintaan%20Penawaran%20Harga%20IntelliTrac%20GPS" class="email-button">
                            ✉️ Kirim Email Sales
                        </a>
                    </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                err_text = f"Terjadi kesalahan saat berkomunikasi dengan AI: {str(e)}"
                st.error(err_text)
                st.session_state.messages.append({"role": "assistant", "content": err_text})
