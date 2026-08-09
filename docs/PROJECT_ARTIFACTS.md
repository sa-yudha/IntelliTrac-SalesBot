# Documentation & Artifacts: IntelliTrac SalesBot

File ini memuat rangkuman Implementation Plan & Walkthrough dari pengerjaan IntelliTrac SalesBot.

---

## 1. Implementation Plan

### Background
**IntelliTrac SalesBot** adalah chatbot AI pre-sales untuk PT Intimap (IntelliTrac Indonesia) yang membantu calon pelanggan memahami produk IntelliTrac GPS Tracker & AI Dashcam, mencocokkan kebutuhan armada, dan melakukan handoff ke sales person resmi.

### Arsitektur Aplikasi
- **Streamlit**: Frontend UI & Sidebar Config
- **Google Gemini API**: LLM Engine (Fallback: gemini-3.5-flash-lite, gemini-3.1-flash-lite, gemini-3.6-flash, gemini-3.5-flash)
- **Knowledge Base**: Markdown documents (company profile, catalogue 2026, product features)
- **Strict Out-of-Scope Guardrails**: Mencegah chatbot menjawab pertanyaan umum di luar domain produk.

---

## 2. Walkthrough & Summary

- **Nama Bot**: Mintel (Asisten Virtual Pre-Sales IntelliTrac)
- **Palet Warna**: Orange `#E65100` (Primary), Dark Navy `#0D1F3C` (Accent), Soft Gray `#F4F4F4` (Background)
- **Tipografi**: Google Fonts Poppins & Roboto
- **Repository Setup**: Git initialized lokal dengan `.gitignore` (menyembunyikan `.env` & API Key).
