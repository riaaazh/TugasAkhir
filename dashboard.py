import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# =========================================================================
# 1. KONFIGURASI HALAMAN
# =========================================================================
st.set_page_config(
    page_title="Dashboard Tugas Akhir - Siti Aminatuzzuhriyah",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS kustom untuk tampilan lebih rapi
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #0f3460 0%, #16213e 50%, #1a1a2e 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        color: white;
        text-align: center;
    }
    .main-header h1 { font-size: 1.8rem; margin-bottom: 0.3rem; }
    .main-header h3 { font-size: 1rem; font-weight: 400; opacity: 0.85; }
    .main-header p  { font-size: 0.85rem; opacity: 0.7; margin: 0; }
    .metric-card {
        background: #f8f9fa;
        border-left: 4px solid #0f3460;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.5rem;
    }
    .insight-box {
        background: #e8f4fd;
        border: 1px solid #bee3f8;
        border-radius: 8px;
        padding: 1.5rem 1.2rem;
        margin: 0.5rem 0;
        height: 100%;
    }
    .warning-box {
        background: #fff8e1;
        border: 1px solid #ffe082;
        border-radius: 8px;
        padding: 0.8rem 1.2rem;
        margin: 0.5rem 0;
        font-size: 0.85rem;
    }
    .kpi-container {
        background: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        text-align: left;
    }
    .kpi-title {
        font-size: 0.9rem;
        color: #555555;
        margin-bottom: 0.2rem;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 800;
        color: #1a202c;
        line-height: 1.1;
        margin-bottom: 0.4rem;
    }
    .kpi-delta {
        font-size: 0.85rem;
        color: #2e7d32;
        font-weight: 500;
        background-color: #e8f5e9;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        display: inline-block;
    }
    /* Mempercantik jarak radio button horizontal */
    div.row-widget.stRadio > div{
        flex-direction:row;
        flex-wrap: wrap;
        gap: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Fungsi pembantu untuk memformat angka ribuan dengan titik (Standar Indonesia)
def format_indo(angka):
    return f"{angka:,}".replace(",", ".")

# =========================================================================
# 2. DATA HARDCODED DARI LAPORAN
# =========================================================================

SENTIMEN_PER_TAHUN = {
    2016: {"positif": 2204, "negatif": 1364, "netral": 490},
    2017: {"positif": 2128, "negatif": 1551, "netral": 692},
    2018: {"positif": 1154, "negatif": 923,  "netral": 179},
    2019: {"positif": 187,  "negatif": 130,  "netral": 52},
    2020: {"positif": 259,  "negatif": 211,  "netral": 19},
    2021: {"positif": 281,  "negatif": 280,  "netral": 41},
    2022: {"positif": 19,   "negatif": 10,   "netral": 1},
    2023: {"positif": 43,   "negatif": 26,   "netral": 3},
    2024: {"positif": 299,  "negatif": 286,  "netral": 38},
    2025: {"positif": 138,  "negatif": 73,   "netral": 5},
}

LABEL_TOPIK = {
    "T1": "Topik 1: Pembahasan Kebijakan, Komisi, dan Sidang DPR",
    "T2": "Topik 2: Kebijakan dan Representasi Wakil Rakyat",
    "T3": "Topik 3: Politik Partai dan Proses Legislasi DPR",
    "T4": "Topik 4: Reses dan Aktivitas Kelembagaan DPR",
    "T5": "Topik 5: Aspirasi Rakyat dan Fungsi Perwakilan DPR",
    "T6": "Topik 6: Korupsi dan Kritik terhadap Elite Politik",
}

TOPIK_PER_TAHUN = {
    2016: {"T1": 21.9, "T2": 18.5, "T3": 13.2, "T4": 22.9, "T5": 16.4, "T6": 7.1},
    2017: {"T1": 16.8, "T2": 20.5, "T3": 14.3, "T4": 19.9, "T5": 18.3, "T6": 9.2},
    2018: {"T1": 11.7, "T2": 29.9, "T3": 11.2, "T4": 11.5, "T5": 23.8, "T6": 11.9},
    2019: {"T1": 15.2, "T2": 21.1, "T3": 13.8, "T4": 30.1, "T5": 17.9, "T6": 6.5},
    2020: {"T1": 18.9, "T2": 34.7, "T3": 14.2, "T4": 12.3, "T5": 16.3, "T6": 3.6},
    2021: {"T1": 35.2, "T2": 16.3, "T3": 15.5, "T4": 11.8, "T5": 12.5, "T6": 8.7},
    2022: {"T1": 30.0, "T2": 20.0, "T3": 10.0, "T4": 20.0, "T5": 20.0, "T6": 0.0},
    2023: {"T1": 11.5, "T2": 15.4, "T3": 23.1, "T4": 7.7,  "T5": 30.8, "T6": 11.5},
    2024: {"T1": 7.7,  "T2": 41.0, "T3": 18.7, "T4": 6.3,  "T5": 14.0, "T6": 12.3},
    2025: {"T1": 11.1, "T2": 34.7, "T3": 12.5, "T4": 8.3,  "T5": 30.6, "T6": 2.8},
}

PIPELINE_DATA = [
    {"tahap": "Data Mentah (Scraping)", "jumlah": 16379, "keterangan": "Tweet mentah hasil scraping Twitter/X"},
    {"tahap": "Pasca Data Selection",   "jumlah": 16205, "keterangan": "Filter tema DPR RI dan menghapus konten tidak relevan"},
    {"tahap": "Pasca Data Cleaning",    "jumlah": 13192, "keterangan": "Menghapus duplikasi dan pembersihan noise teks"},
    {"tahap": "Pasca Preprocessing",    "jumlah": 13192, "keterangan": "Normalisasi, tokenisasi, dan standarisasi"},
]

# =========================================================================
# 3. FUNGSI LOAD DATA CSV 
# =========================================================================
@st.cache_data
def load_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

PATH_RAW    = "datapreparation/datascraping/master_dataset_aspirasi_dpr.csv"
PATH_SELECT = "datapreparation/dataselection/data_selected.csv"
PATH_CLEAN  = "datapreparation/datacleaningcopy/data_cleaning_final.csv"
PATH_PREP   = "datapreparation/datapreprocessingcopy/data_preprocessing_final.csv"
PATH_NOSTEM = "datapreparation/datapreprocessing-no-stem/data_preprocessing_final_no_stem.csv"
PATH_FINAL  = "sentiment-analysis-final/outputs/sentiment_final.csv"

df_raw    = load_csv(PATH_RAW)
df_select = load_csv(PATH_SELECT)
df_clean  = load_csv(PATH_CLEAN)
df_prep   = load_csv(PATH_PREP) 
df_nostem = load_csv(PATH_NOSTEM)
df_final  = load_csv(PATH_FINAL)

# =========================================================================
# 4. HEADER DASHBOARD
# =========================================================================
st.markdown("""
<div class="main-header">
    <h1>Dashboard Analisis Sentimen dan Pemodelan Topik Opini Publik</h1>
    <h3>Analisis Sentimen dan Pemodelan Topik Opini Publik Terhadap DPR RI Berbasis Data Twitter/X</h3>
    <p>Siti Aminatuzzuhriyah (NIM. 10221014) &nbsp;|&nbsp; Program Studi Sistem Informasi &nbsp;|&nbsp; Institut Teknologi Kalimantan &nbsp;|&nbsp; 2026</p>
</div>
""", unsafe_allow_html=True)

# =========================================================================
# 5. RINGKASAN HASIL UTAMA
# =========================================================================
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">📥 Total Tweet</div>
        <div class="kpi-value">{format_indo(13192)}</div>
        <div style="height: 24px;"></div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">😊 Sentimen Positif</div>
        <div class="kpi-value">50.88%</div>
        <div class="kpi-delta">{format_indo(6712)} tweet</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">😠 Sentimen Negatif</div>
        <div class="kpi-value">36.80%</div>
        <div class="kpi-delta">{format_indo(4854)} tweet</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-title">😐 Sentimen Netral</div>
        <div class="kpi-value">12.33%</div>
        <div class="kpi-delta">{format_indo(1626)} tweet</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="kpi-container">
        <div class="kpi-title">🏆 Model Terbaik</div>
        <div class="kpi-value">ISV-SLA</div>
        <div class="kpi-delta">Ignore Function, No-Stem</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================================================================
# 6. TAB MENU
# =========================================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "Data Preparation",
    "Evaluasi Model",
    "Tren Sentimen (2016-2025)",
    "Pemodelan Topik LDA"
])

# =========================================================================
# TAB 1: DATA PREPARATION
# =========================================================================
with tab1:
    st.subheader("Statistik Hasil Pembersihan Data")
    st.caption("Visualisasi penyusutan volume data dari scraping mentah hingga dataset siap analisis.")

    val_raw    = format_indo(len(df_raw))    if df_raw    is not None else "16.379"
    val_select = format_indo(len(df_select)) if df_select is not None else "16.205"
    val_clean  = format_indo(len(df_clean))  if df_clean  is not None else "13.192"
    val_nostem = format_indo(len(df_nostem)) if df_nostem is not None else "13.192"

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Data Mentah", val_raw, help="master_dataset_aspirasi_dpr.csv")
    with c2:
        st.metric("Data Selection", val_select, help="data_selected.csv")
    with c3:
        st.metric("Data Cleaning", val_clean, help="data_cleaning_final.csv")
    with c4:
        st.metric("Preprocessing", val_nostem, help="data_preprocessing_final_no_stem.csv")

    st.markdown("---")

    col_chart, col_info = st.columns([2, 1])

    with col_chart:
        st.markdown("##### Tren Alur Penyusutan Data")
        funnel_data = pd.DataFrame(PIPELINE_DATA)
        
        text_labels = [f"{format_indo(val)} tweet" for val in funnel_data["jumlah"]]
        
        fig_funnel = go.Figure(go.Funnel(
            y=funnel_data["tahap"],
            x=funnel_data["jumlah"],
            textposition="inside",
            text=text_labels,
            texttemplate="%{text}", 
            marker=dict(color=["#0f3460","#1a6e9e","#2a9d8f","#52b788"]),
            connector=dict(line=dict(color="rgba(0,0,0,0.1)", width=1))
        ))
        fig_funnel.update_layout(
            height=300,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_funnel, use_container_width=True)

    with col_info:
        st.markdown("##### Detail Setiap Tahap")
        for d in PIPELINE_DATA:
            pct = f"{d['jumlah']/16379*100:.1f}%"
            st.markdown(f"""
            <div class="metric-card">
                <b>{d['tahap']}</b><br>
                <span style="font-size:1.2rem;font-weight:700;color:#0f3460">{format_indo(d['jumlah'])}</span>
                <span style="font-size:0.8rem;color:#666"> tweet ({pct})</span><br>
                <span style="font-size:0.8rem;color:#888">{d['keterangan']}</span>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("---")
    st.markdown("##### 🔍 Inspeksi Sampel Data Preprocessing")
    
    kondisi_prep = st.radio(
        "Pilih Kondisi Data Preprocessing:",
        ["Tanpa Stemming", "Dengan Stemming"],
        horizontal=True,
        key="prep_sample_condition"
    )

    if kondisi_prep == "Tanpa Stemming":
        df_target = df_nostem
        warning_msg = "⚠️ File <code>data_preprocessing_final_no_stem.csv</code> belum ditemukan di direktori lokal."
        path_code = "datapreparation/datapreprocessing-no-stem/"
        demo_texts = ["dpr ri becus kerja ribut", "terima kasih dpr sahkan uu", "anggota dpr jarang hadir sidang paripurna"]
    else:
        df_target = df_prep
        warning_msg = "⚠️ File <code>data_preprocessing_final.csv</code> (Dengan Stemming) belum ditemukan di direktori lokal."
        path_code = "datapreparation/datapreprocessingcopy/"
        demo_texts = ["dpr ri becus kerja ribut", "terima kasih dpr sah uu", "anggota dpr jarang hadir sidang paripurna"]

    if df_target is not None:
        col_show = [c for c in ["timestamp","teks","teks_processed"] if c in df_target.columns]
        if not col_show:
            col_show = df_target.columns[:3].tolist()
        st.dataframe(df_target[col_show].head(10), use_container_width=True)
    else:
        st.markdown(f"""
        <div class="warning-box">
        {warning_msg}<br>
        Pastikan path sudah sesuai: <code>{path_code}</code>
        </div>
        """, unsafe_allow_html=True)
        
        demo = pd.DataFrame({
            "timestamp": ["2019-09-16","2020-03-10","2021-07-25"],
            "teks": ["DPR RI tidak becus kerja, cuma ribut terus!","Terima kasih DPR sudah sahkan UU ini","Anggota DPR jarang hadir sidang paripurna"],
            "teks_processed": demo_texts
        })
        st.dataframe(demo, use_container_width=True)
        st.caption(f"*Tabel di atas adalah contoh ilustrasi kondisi **{kondisi_prep}**, bukan data asli.*")

# =========================================================================
# TAB 2: EVALUASI MODEL 
# =========================================================================
with tab2:
    st.subheader("Evaluasi Komparatif 3 Pendekatan Model Sentimen")
    st.caption("Perbandingan performa ISV-RSN, ISV-SLA, dan VTB, serta 7 konfigurasi dengan 2 kondisi data (dengan stemming dan tanpa stemming).")

    CUSTOM_ORDER = [
        'RSN + Ignore Function', 'RSN + Remove Function', 'RSN + Tanpa Perlakuan',
        'SLA + Ignore Function', 'SLA + Remove Function', 'SLA + Tanpa Perlakuan',
        'VTB (Translation Based)',
    ]
    FILENAME_MAP = {
        'evaluation_metrics_RSN_with_Ignore.csv':    'RSN + Ignore Function',
        'evaluation_metrics_RSN_remove_function.csv':'RSN + Remove Function',
        'evaluation_metrics_RSN_tanpa_perlakuan.csv':'RSN + Tanpa Perlakuan',
        'evaluation_metrics_SLA_with_Ignore.csv':    'SLA + Ignore Function',
        'evaluation_metrics_SLA_remove_function.csv':'SLA + Remove Function',
        'evaluation_metrics_SLA_tanpa_perlakuan.csv':'SLA + Tanpa Perlakuan',
        'evaluation_metrics_VTB.csv':                'VTB (Translation Based)',
    }
    ALL_METRICS_ORDER = [
        'Accuracy','Precision (M)','Recall (M)','F1-Score (M)',
        'Pearson-r','Spearman-rho','R-Squared','RMSE','MAE',
    ]
    HIGHER_BETTER = {'Accuracy','Precision (M)','Recall (M)','F1-Score (M)',
                     'Pearson-r','Spearman-rho','R-Squared'}
    LOWER_BETTER  = {'RMSE','MAE'}

    COLOR_MAP = {
        'RSN + Ignore Function':   '#0f3460', 'RSN + Remove Function':   '#1a6e9e',
        'RSN + Tanpa Perlakuan':   '#5ba3d9', 'SLA + Ignore Function':   '#2a9d8f',
        'SLA + Remove Function':   '#3dbfb1', 'SLA + Tanpa Perlakuan':   '#70d8cf',
        'VTB (Translation Based)': '#e9c46a',
    }
    PENDEKATAN_MAP = {
        'RSN + Ignore Function':   'ISV-RSN', 'RSN + Remove Function':   'ISV-RSN',
        'RSN + Tanpa Perlakuan':   'ISV-RSN', 'SLA + Ignore Function':   'ISV-SLA',
        'SLA + Remove Function':   'ISV-SLA', 'SLA + Tanpa Perlakuan':   'ISV-SLA',
        'VTB (Translation Based)': 'VTB',
    }

    @st.cache_data
    def load_eval_csv(eval_dir):
        if not os.path.exists(eval_dir):
            return None
        csv_files = [f for f in os.listdir(eval_dir)
                     if f.startswith('evaluation_metrics_') and f.endswith('.csv')]
        if not csv_files:
            return None
        dfs = []
        for fname in csv_files:
            try:
                df = pd.read_csv(os.path.join(eval_dir, fname))
                cols = [c for c in ALL_METRICS_ORDER if c in df.columns]
                sub  = df[cols].copy()
                sub['Konfigurasi'] = FILENAME_MAP.get(fname, fname)
                dfs.append(sub)
            except Exception:
                pass
        if not dfs:
            return None
        out = pd.concat(dfs, ignore_index=True)
        for col in ALL_METRICS_ORDER:
            if col in out.columns:
                out[col] = pd.to_numeric(out[col], errors='coerce')
        out['Konfigurasi'] = pd.Categorical(out['Konfigurasi'], categories=CUSTOM_ORDER, ordered=True)
        out = out.sort_values('Konfigurasi').reset_index(drop=True)
        out['Pendekatan'] = out['Konfigurasi'].map(PENDEKATAN_MAP)
        return out

    @st.cache_data
    def compute_composite(df):
        from sklearn.preprocessing import MinMaxScaler
        df2 = df.copy()
        metric_cols = [c for c in ALL_METRICS_ORDER if c in df2.columns]
        high = [c for c in metric_cols if c in HIGHER_BETTER]
        low  = [c for c in metric_cols if c in LOWER_BETTER]
        for col in high:
            sc = MinMaxScaler()
            df2[f'{col}_norm'] = sc.fit_transform(df2[[col]])
        for col in low:
            mn, mx = df2[col].min(), df2[col].max()
            df2[f'{col}_norm'] = (mx - df2[col]) / (mx - mn) if mx > mn else 1.0
        norm_cols = [c for c in df2.columns if c.endswith('_norm')]
        df2['Composite Score'] = df2[norm_cols].mean(axis=1)
        return df2

    EVAL_DIR_STEM   = "sentiment-analysis/outputs/evaluation"
    EVAL_DIR_NOSTEM = "sentiment-analysis-no-stem/outputs/evaluation"

    df_stem_raw   = load_eval_csv(EVAL_DIR_STEM)
    df_nostem_raw = load_eval_csv(EVAL_DIR_NOSTEM)

    df_stem   = compute_composite(df_stem_raw)   if df_stem_raw   is not None else None
    df_nostem = compute_composite(df_nostem_raw) if df_nostem_raw is not None else None

    FALLBACK_DATA = {
        "Stemming": pd.DataFrame({
            "Konfigurasi": CUSTOM_ORDER,
            "Pendekatan":  ['ISV-RSN','ISV-RSN','ISV-RSN','ISV-SLA','ISV-SLA','ISV-SLA','VTB'],
            "Accuracy":    [0.58, 0.58, 0.56, 0.58, 0.58, 0.56, 0.50],
            "Precision (M)":[0.54,0.54,0.52,0.54,0.54,0.52,0.49],
            "Recall (M)":  [0.54, 0.54, 0.52, 0.54, 0.54, 0.52, 0.49],
            "F1-Score (M)":[0.54, 0.54, 0.52, 0.54, 0.54, 0.52, 0.49],
            "Pearson-r":   [0.53, 0.52, 0.53, 0.53, 0.52, 0.53, 0.40],
            "Spearman-rho":[0.52, 0.51, 0.52, 0.52, 0.51, 0.52, 0.39],
            "R-Squared":   [0.28, 0.27, 0.28, 0.28, 0.27, 0.28, 0.16],
            "RMSE":        [0.58, 0.59, 0.59, 0.58, 0.59, 0.59, 0.65],
            "MAE":         [0.47, 0.48, 0.48, 0.47, 0.48, 0.48, 0.54],
            "Composite Score":[0.72,0.68,0.65,0.73,0.69,0.66,0.45],
        }),
        "Tanpa Stemming": pd.DataFrame({
            "Konfigurasi": CUSTOM_ORDER,
            "Pendekatan":  ['ISV-RSN','ISV-RSN','ISV-RSN','ISV-SLA','ISV-SLA','ISV-SLA','VTB'],
            "Accuracy":    [0.60, 0.60, 0.58, 0.60, 0.60, 0.58, 0.55],
            "Precision (M)":[0.57,0.56,0.55,0.58,0.56,0.55,0.55],
            "Recall (M)":  [0.57, 0.56, 0.55, 0.57, 0.57, 0.55, 0.55],
            "F1-Score (M)":[0.56, 0.56, 0.54, 0.56, 0.56, 0.54, 0.55],
            "Pearson-r":   [0.55, 0.54, 0.55, 0.55, 0.54, 0.56, 0.43],
            "Spearman-rho":[0.53, 0.52, 0.53, 0.53, 0.52, 0.54, 0.41],
            "R-Squared":   [0.30, 0.30, 0.31, 0.30, 0.30, 0.31, 0.18],
            "RMSE":        [0.55, 0.56, 0.57, 0.55, 0.56, 0.56, 0.61],
            "MAE":         [0.44, 0.45, 0.46, 0.45, 0.45, 0.45, 0.51],
            "Composite Score":[0.92,0.88,0.82,0.98,0.89,0.84,0.55],
        }),
    }

    kondisi_pilih = st.radio("📂 Pilih Kondisi Data:", ["Stemming", "Tanpa Stemming"], horizontal=True, key="tab2_kondisi")

    if kondisi_pilih == "Stemming":
        df_aktif = df_stem if df_stem is not None else FALLBACK_DATA["Stemming"]
        is_fallback = df_stem is None
    else:
        df_aktif = df_nostem if df_nostem is not None else FALLBACK_DATA["Tanpa Stemming"]
        is_fallback = df_nostem is None

    if is_fallback:
        st.markdown("""
        <div class="warning-box">
        ⚠️ File CSV evaluasi belum ditemukan — menggunakan data estimasi dari laporan.
        Letakkan hasil notebook di folder <code>sentiment-analysis[-no-stem]/outputs/evaluation/</code>
        </div>
        """, unsafe_allow_html=True)

    metric_cols_avail = [c for c in ALL_METRICS_ORDER if c in df_aktif.columns]
    has_composite = 'Composite Score' in df_aktif.columns

    st.markdown("---")
    st.markdown("#### A. Perbandingan Per Metrik")
    col_ctrl1, col_ctrl2 = st.columns([1, 3])
    with col_ctrl1:
        metrik_pilih = st.selectbox("Pilih Metrik:", metric_cols_avail + (['Composite Score'] if has_composite else []), key="tab2_metrik")
        arah = "Note: Higher is better" if metrik_pilih in HIGHER_BETTER or metrik_pilih == 'Composite Score' else "Note: Lower is better"
        st.caption(arah)

    with col_ctrl2:
        vals = df_aktif[metrik_pilih].tolist()
        configs = df_aktif['Konfigurasi'].astype(str).tolist()
        colors  = [COLOR_MAP.get(c, '#888') for c in configs]

        if metrik_pilih in LOWER_BETTER:
            ymax = max(vals) * 1.15
        else:
            ymax = max(vals) * 1.15 
            if ymax < 1.0: ymax = 1.0

        fig_bar = go.Figure(go.Bar(
            x=configs, y=vals, marker_color=colors,
            text=[f"{v:.4f}" for v in vals], textposition="outside",
            hovertemplate="<b>%{x}</b><br>%{y:.4f}<extra></extra>",
        ))
        
        if metrik_pilih in LOWER_BETTER:
            best_idx = vals.index(min(vals))
        else:
            best_idx = vals.index(max(vals))
            
        fig_bar.data[0].marker.color = ['#FFD700' if i == best_idx else c for i, c in enumerate(colors)]
        
        fig_bar.update_layout(
            height=380, 
            xaxis=dict(tickangle=-30), 
            yaxis=dict(title=metrik_pilih, range=[0, ymax]), 
            margin=dict(t=20, b=10, l=10, r=10), 
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)", 
            showlegend=False,
        )
        
        fig_bar.add_annotation(
            x=configs[best_idx], y=vals[best_idx], text="<b>⭐ Terbaik</b>", showarrow=False, yshift=30,
            font=dict(size=12, color="#333"), bgcolor="rgba(255,215,0,0.3)", bordercolor="#FFD700", borderwidth=1
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # =========================================================================
    # B: METRIK KLASIFIKASI & KORELASI
    # =========================================================================
    st.markdown("---")
    st.markdown("#### B. Perbandingan Metrik Evaluasi per Pendekatan")
    
    jenis_metrik = st.radio(
        "Pilih Jenis Metrik:",
        ["Metrik Klasifikasi", "Metrik Korelasi Kontinu"],
        horizontal=True,
        key="tab2_jenis_metrik"
    )

    metrik_klasifikasi = [c for c in ['Accuracy','Precision (M)','Recall (M)','F1-Score (M)'] if c in df_aktif.columns]
    metrik_kontinu     = [c for c in ['Pearson-r','Spearman-rho','R-Squared'] if c in df_aktif.columns]

    if jenis_metrik == "Metrik Klasifikasi":
        fig_klas = go.Figure()
        for m in metrik_klasifikasi:
            fig_klas.add_trace(go.Bar(
                name=m, 
                x=df_aktif['Konfigurasi'].astype(str), 
                y=df_aktif[m], 
                text=df_aktif[m].apply(lambda v: f"{v:.3f}"), 
                textposition="inside", 
                textfont=dict(size=10)
            ))
        fig_klas.update_layout(
            barmode="group", 
            height=420, 
            xaxis=dict(tickangle=0, tickfont=dict(size=11)), 
            yaxis=dict(title="Skor", range=[0, 0.8]),  
            legend=dict(orientation="h", y=-0.25, font_size=11), 
            margin=dict(t=40, b=80, l=10, r=10), 
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_klas, use_container_width=True)
    else:
        fig_kont = go.Figure()
        for m in metrik_kontinu:
            fig_kont.add_trace(go.Bar(
                name=m, 
                x=df_aktif['Konfigurasi'].astype(str), 
                y=df_aktif[m], 
                text=df_aktif[m].apply(lambda v: f"{v:.3f}"), 
                textposition="inside", 
                textfont=dict(size=10)
            ))
        fig_kont.update_layout(
            barmode="group", 
            height=420, 
            xaxis=dict(tickangle=0, tickfont=dict(size=11)), 
            yaxis=dict(title="Skor (Pearson-r)", range=[0, 0.8]),  
            legend=dict(orientation="h", y=-0.25, font_size=11), 
            margin=dict(t=40, b=80, l=10, r=10), 
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_kont, use_container_width=True)

    # =========================================================================
    # C: HEATMAP 
    # =========================================================================
    st.markdown("---")
    st.markdown("#### C. Heatmap Metrik Lengkap")
    st.caption("Note: Semakin gelap warna biru, semakin tinggi nilai skor pada metrik tersebut.")
    
    hm_metrics = [c for c in ALL_METRICS_ORDER if c in df_aktif.columns]
    
    fig_hm = go.Figure(go.Heatmap(
        z=df_aktif[hm_metrics].values.tolist(), 
        x=hm_metrics, 
        y=df_aktif['Konfigurasi'].astype(str).tolist(), 
        colorscale="Blues", 
        text=[[f"{v:.3f}" for v in row] for row in df_aktif[hm_metrics].values.tolist()], 
        texttemplate="%{text}", 
        showscale=True, 
        colorbar=dict(title="Skor"), 
        hoverongaps=False
    ))
    
    fig_hm.update_layout(
        height=340, 
        xaxis=dict(tickangle=0, side="top"), 
        yaxis=dict(autorange="reversed"), 
        margin=dict(t=60, b=20, l=180, r=20), 
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_hm, use_container_width=True)

    # =========================================================================
    # D: COMPOSITE SCORE
    # =========================================================================
    st.markdown("---")
    if has_composite:
        st.markdown("#### D. Peringkat Composite Score (Evaluasi Holistik)")
        df_ranked = df_aktif.sort_values('Composite Score', ascending=False).reset_index(drop=True)
        col_rank_bar, col_rank_tbl = st.columns([3, 2])

        with col_rank_bar:
            rank_colors = [COLOR_MAP.get(str(c), '#888') for c in df_ranked['Konfigurasi']]
            rank_colors[0] = '#FFD700'
            fig_rank = go.Figure(go.Bar(x=df_ranked['Composite Score'], y=df_ranked['Konfigurasi'].astype(str), orientation='h', marker_color=rank_colors, text=df_ranked['Composite Score'].apply(lambda v: f"{v:.4f}"), textposition='outside'))
            fig_rank.update_layout(height=320, xaxis=dict(title="Composite Score", range=[0, 1.15]), yaxis=dict(autorange="reversed"), margin=dict(t=20, b=20, l=10, r=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
            
            fig_rank.add_annotation(x=df_ranked['Composite Score'].iloc[0], y=str(df_ranked['Konfigurasi'].iloc[0]), text="⭐ #1", showarrow=False, xshift=55, font=dict(size=13, color="#b8860b"))
            st.plotly_chart(fig_rank, use_container_width=True)

    # =========================================================================
    # E: KESIMPULAN MODEL TERBAIK
    # =========================================================================
    st.markdown("---")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0f3460 0%, #1a1a2e 100%); 
                padding: 2.5rem 2rem; 
                border-radius: 12px; 
                color: white; 
                text-align: center; 
                margin-top: 1.5rem; 
                margin-bottom: 1rem;
                box-shadow: 0 8px 16px rgba(0,0,0,0.15);
                border: 1px solid #16213e;">
        <h3 style="color: #FFD700; margin-bottom: 0.8rem; font-size: 1.6rem;">🏆 Kesimpulan Model Terbaik</h3>
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem; opacity: 0.9;">
            Berdasarkan evaluasi performa klasifikasi sentimen di atas, kombinasi pendekatan dan konfigurasi terbaik dalam penelitian ini adalah:
        </p>
        <h2 style="color: #ffffff; font-size: 2.4rem; font-weight: 800; margin: 0.8rem 0; letter-spacing: 1px;">
            ISV-SLA + Ignore Function
        </h2>
        <div style="display: inline-block; background-color: rgba(255, 255, 255, 0.1); padding: 0.5rem 1.5rem; border-radius: 30px; margin-top: 0.5rem; border: 1px solid rgba(255, 255, 255, 0.2);">
            <span style="font-size: 1.1rem; color: #4ade80; font-weight: 600;">✨ Menggunakan Data Tanpa Stemming</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================================
# TAB 3: TREN SENTIMEN
# =========================================================================
with tab3:
    st.subheader("Dinamika Sentimen Publik Terhadap DPR RI (2016-2025)")
    st.caption("Menggunakan pendekatan ISV-SLA dengan Ignore Function tanpa Stemming.")

    rows = [{"Tahun": t, "Positif": d["positif"], "Negatif": d["negatif"], "Netral": d["netral"], "Total": d["positif"]+d["negatif"]+d["netral"], "% Positif": round(d["positif"]/(d["positif"]+d["negatif"]+d["netral"])*100, 1), "% Negatif": round(d["negatif"]/(d["positif"]+d["negatif"]+d["netral"])*100, 1), "% Netral": round(d["netral"]/(d["positif"]+d["negatif"]+d["netral"])*100, 1)} for t, d in SENTIMEN_PER_TAHUN.items()]
    df_tren = pd.DataFrame(rows)

    mode_tampil = st.radio("🖼️ Tampilan:", ["Grafik Interaktif (Semua Tahun)", "Detail Per Tahun"], horizontal=True)

    if mode_tampil == "Grafik Interaktif (Semua Tahun)":
        jenis_chart = st.selectbox("Jenis Grafik:", ["Stacked Bar (Jumlah Tweet)", "Line Chart (% Sentimen)", "Area Chart (Jumlah Tweet)"])

        if jenis_chart == "Stacked Bar (Jumlah Tweet)":
            fig = go.Figure()
            fig.add_trace(go.Bar(name="Positif", x=df_tren["Tahun"], y=df_tren["Positif"], marker_color="#2a9d8f", text=df_tren["Positif"].apply(format_indo), textposition="inside"))
            fig.add_trace(go.Bar(name="Negatif", x=df_tren["Tahun"], y=df_tren["Negatif"], marker_color="#e63946", text=df_tren["Negatif"].apply(format_indo), textposition="inside"))
            fig.add_trace(go.Bar(name="Netral",  x=df_tren["Tahun"], y=df_tren["Netral"], marker_color="#adb5bd", text=df_tren["Netral"].apply(format_indo), textposition="inside"))
            fig.update_layout(barmode="stack", height=420, xaxis=dict(title="Tahun", tickmode="linear", dtick=1), yaxis_title="Jumlah Tweet", margin=dict(t=20, b=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
            
        elif jenis_chart == "Line Chart (% Sentimen)":
            fig = go.Figure()
            fig.add_trace(go.Scatter(name="% Positif", x=df_tren["Tahun"], y=df_tren["% Positif"], mode="lines+markers+text", marker_color="#2a9d8f", text=df_tren["% Positif"].apply(lambda v: f"{v}%"), textposition="top center", line=dict(width=3)))
            fig.add_trace(go.Scatter(name="% Negatif", x=df_tren["Tahun"], y=df_tren["% Negatif"], mode="lines+markers+text", marker_color="#e63946", text=df_tren["% Negatif"].apply(lambda v: f"{v}%"), textposition="bottom center", line=dict(width=3)))
            fig.update_layout(height=420, xaxis=dict(title="Tahun", tickmode="linear", dtick=1), yaxis=dict(title="Persentase (%)", range=[0, 110]), margin=dict(t=20, b=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
            
        else:
            fig = go.Figure()
            fig.add_trace(go.Scatter(name="Positif", x=df_tren["Tahun"], y=df_tren["Positif"], fill="tonexty", mode="lines", marker_color="#2a9d8f", fillcolor="rgba(42,157,143,0.3)"))
            fig.add_trace(go.Scatter(name="Negatif", x=df_tren["Tahun"], y=df_tren["Negatif"], fill="tozeroy", mode="lines", marker_color="#e63946", fillcolor="rgba(230,57,70,0.3)"))
            fig.update_layout(height=420, xaxis=dict(title="Tahun", tickmode="linear", dtick=1), yaxis_title="Jumlah Tweet", margin=dict(t=20, b=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("##### 📋 Tabel Distribusi Sentimen Per Tahun")
        num_cols_T3 = [c for c in df_tren.columns if c != 'Tahun']
        styler_T3 = df_tren.style \
            .set_properties(subset=num_cols_T3, **{'text-align': 'center'}) \
            .set_table_styles([{'selector': 'th', 'props': [('text-align', 'center'), ('font-weight', 'bold')]}]) \
            .background_gradient(subset=["% Positif"], cmap="Greens") \
            .background_gradient(subset=["% Negatif"], cmap="Reds") \
            .background_gradient(subset=["% Netral"], cmap="Greys") \
            .format({"% Positif":"{:.1f}%","% Negatif":"{:.1f}%","% Netral":"{:.1f}%","Total": format_indo, "Positif": format_indo, "Negatif": format_indo, "Netral": format_indo})
        st.dataframe(styler_T3, use_container_width=True, hide_index=True)

    else:
        opsi_tahun = [str(y) for y in range(2016, 2026)]
        tahun_pilih_str = st.selectbox("📅 Pilih Tahun:", options=opsi_tahun, index=8, key="sentimen_dropdown")
        tahun_pilih = int(tahun_pilih_str)
        
        data_tahun = SENTIMEN_PER_TAHUN[tahun_pilih]
        total_t = data_tahun["positif"] + data_tahun["negatif"] + data_tahun["netral"]
        
        pct_pos = f"{data_tahun['positif']/total_t*100:.1f}%"
        pct_neg = f"{data_tahun['negatif']/total_t*100:.1f}%"
        pct_net = f"{data_tahun['netral']/total_t*100:.1f}%"

        col_chart, col_detail = st.columns([1.2, 1])
        
        with col_chart:
            max_val = max(data_tahun["positif"], data_tahun["negatif"], data_tahun["netral"])
            fig_bar_detail = go.Figure(go.Bar(
                x=["Positif", "Negatif", "Netral"],
                y=[data_tahun["positif"], data_tahun["negatif"], data_tahun["netral"]],
                marker_color=["#2a9d8f", "#e63946", "#adb5bd"],
                text=[format_indo(data_tahun["positif"]), format_indo(data_tahun["negatif"]), format_indo(data_tahun["netral"])],
                textposition="outside",
                textfont=dict(size=14, color="black"),
                hovertemplate="<b>%{x}</b><br>Jumlah: %{text} tweet<extra></extra>"
            ))
            fig_bar_detail.update_layout(
                title=f"Distribusi Sentimen Tahun {tahun_pilih}",
                height=400,
                yaxis=dict(title="Jumlah Tweet", range=[0, max_val * 1.2], showgrid=True, gridcolor="#f0f0f0"),
                xaxis=dict(title=""),
                margin=dict(t=50, b=20, l=10, r=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig_bar_detail, use_container_width=True)

        with col_detail:
            st.markdown(f"<h5 style='margin-bottom: 1rem;'>📊 Detail Tahun {tahun_pilih}</h5>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background-color:#ffffff;border:1px solid #e0e0e0;border-radius:8px;padding:1.2rem;margin-bottom:1rem;border-left:5px solid #0f3460;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
            <div style="font-size:0.95rem;color:#666;font-weight:500;">Total Tweet</div>
            <div style="font-size:2.2rem;font-weight:800;color:#1a202c;line-height:1.2;">{format_indo(total_t)}</div>
            </div>
            <div style="display:flex;gap:1rem;margin-bottom:1rem;">
            <div style="flex:1;background-color:#ffffff;border:1px solid #e0e0e0;border-radius:8px;padding:1.2rem;border-left:5px solid #2a9d8f;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
            <div style="font-size:0.9rem;color:#666;font-weight:500;">😊 Positif</div>
            <div style="font-size:1.8rem;font-weight:800;color:#2a9d8f;line-height:1.2;margin:0.2rem 0;">{format_indo(data_tahun['positif'])}</div>
            <div style="display:inline-block;background-color:#e8f5e9;color:#2e7d32;padding:0.2rem 0.6rem;border-radius:4px;font-size:0.85rem;font-weight:600;">{pct_pos}</div>
            </div>
            <div style="flex:1;background-color:#ffffff;border:1px solid #e0e0e0;border-radius:8px;padding:1.2rem;border-left:5px solid #e63946;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
            <div style="font-size:0.9rem;color:#666;font-weight:500;">😠 Negatif</div>
            <div style="font-size:1.8rem;font-weight:800;color:#e63946;line-height:1.2;margin:0.2rem 0;">{format_indo(data_tahun['negatif'])}</div>
            <div style="display:inline-block;background-color:#ffebee;color:#c62828;padding:0.2rem 0.6rem;border-radius:4px;font-size:0.85rem;font-weight:600;">{pct_neg}</div>
            </div>
            </div>
            <div style="background-color:#ffffff;border:1px solid #e0e0e0;border-radius:8px;padding:1rem 1.2rem;border-left:5px solid #adb5bd;box-shadow:0 2px 4px rgba(0,0,0,0.05);display:flex;justify-content:space-between;align-items:center;">
            <div>
            <div style="font-size:0.9rem;color:#666;font-weight:500;">😐 Netral</div>
            <div style="font-size:1.5rem;font-weight:800;color:#6c757d;">{format_indo(data_tahun['netral'])}</div>
            </div>
            <div style="background-color:#f8f9fa;color:#495057;padding:0.2rem 0.6rem;border-radius:4px;font-size:0.85rem;font-weight:600;border:1px solid #dee2e6;">{pct_net}</div>
            </div>
            """, unsafe_allow_html=True)

# =========================================================================
# TAB 4: PEMODELAN TOPIK LDA 
# =========================================================================
with tab4:
    st.subheader("Pemodelan Topik Isu Kritis - Latent Dirichlet Allocation (LDA)")
    st.caption("6 klaster topik dominan yang merepresentasikan ketidakpuasan publik terhadap DPR RI.")

    mode_lda = st.radio("🖼️ Tampilan:", ["Grafik Interaktif (Semua Tahun)", "Detail Per Tahun"], horizontal=True, key="lda_mode")

    topik_keys = ["T1","T2","T3","T4","T5","T6"]
    short_labels = [f"Topik {k[1]}" for k in topik_keys]
    
    # Menentukan Palet Warna untuk tiap Topik agar Legend seragam
    COLOR_MAP_LDA = {
        "Topik 1": "#1f77b4", # Biru
        "Topik 2": "#ff7f0e", # Oranye
        "Topik 3": "#2ca02c", # Hijau
        "Topik 4": "#d62728", # Merah
        "Topik 5": "#9467bd", # Ungu
        "Topik 6": "#8c564b"  # Coklat
    }

    if mode_lda == "Grafik Interaktif (Semua Tahun)":
        fig_heat = go.Figure(go.Heatmap(
            z=[[TOPIK_PER_TAHUN[t][k] for k in topik_keys] for t in sorted(TOPIK_PER_TAHUN.keys())], 
            x=short_labels, 
            y=[str(t) for t in sorted(TOPIK_PER_TAHUN.keys())], 
            colorscale="Blues", 
            text=[[f"{v:.1f}%" for v in row] for row in [[TOPIK_PER_TAHUN[t][k] for k in topik_keys] for t in sorted(TOPIK_PER_TAHUN.keys())]], 
            texttemplate="%{text}", 
            showscale=True
        ))
        
        fig_heat.update_layout(
            title="Heatmap Distribusi 6 Topik LDA per Tahun", 
            height=420, 
            margin=dict(t=50, b=40, l=60, r=20), 
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_heat, use_container_width=True)
        
        # Keterangan tetap dimunculkan di bawah jika mode Heatmap
        st.markdown("""
        <div style="background-color: #f8f9fa; border: 1px solid #e0e0e0; border-left: 5px solid #0f3460; border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem;">
            <h5 style="margin-top: 0; margin-bottom: 1rem; color: #1a202c; font-size: 1.1rem;">📖 Keterangan Deskripsi Topik:</h5>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 12px; font-size: 0.95rem; color: #444;">
                <div><strong style="color: #1f77b4;">Topik 1:</strong> Pembahasan Kebijakan, Komisi, dan Sidang DPR</div>
                <div><strong style="color: #ff7f0e;">Topik 2:</strong> Kebijakan dan Representasi Wakil Rakyat</div>
                <div><strong style="color: #2ca02c;">Topik 3:</strong> Politik Partai dan Proses Legislasi DPR</div>
                <div><strong style="color: #d62728;">Topik 4:</strong> Reses dan Aktivitas Kelembagaan DPR</div>
                <div><strong style="color: #9467bd;">Topik 5:</strong> Aspirasi Rakyat dan Fungsi Perwakilan DPR</div>
                <div><strong style="color: #8c564b;">Topik 6:</strong> Korupsi dan Kritik terhadap Elite Politik</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        opsi_tahun = [str(y) for y in range(2016, 2026)]
        tahun_lda_str = st.selectbox("📅 Pilih Tahun:", options=opsi_tahun, index=8, key="lda_dropdown")
        tahun_lda = int(tahun_lda_str)
        
        data_lda = TOPIK_PER_TAHUN[tahun_lda]
        col_lda_chart, col_lda_info = st.columns([2.5, 1])

        with col_lda_chart:
            df_lda_bar = pd.DataFrame({
                "Topik_Pendek": [f"Topik {k[1]}" for k in data_lda.keys()], 
                "Label_Lengkap": [LABEL_TOPIK[k] for k in data_lda.keys()],
                "Persentase": list(data_lda.values())
            }).sort_values("Persentase", ascending=False)
            
            fig_lda = go.Figure()
            
            for idx, row in df_lda_bar.iterrows():
                fig_lda.add_trace(go.Bar(
                    x=[row["Topik_Pendek"]], 
                    y=[row["Persentase"]], 
                    name=row["Label_Lengkap"], 
                    marker_color=COLOR_MAP_LDA[row["Topik_Pendek"]],
                    text=[f"{row['Persentase']:.1f}%"], 
                    textposition="outside",
                    hovertemplate="<b>%{x}</b><br>Persentase: %{y:.1f}%<extra></extra>"
                ))
                
            fig_lda.update_layout(
                title=f"Distribusi 6 Topik LDA - Tahun {tahun_lda}", 
                height=550, 
                yaxis=dict(title="Persentase (%)", range=[0, max(data_lda.values())*1.2]), 
                xaxis=dict(title=""), 
                margin=dict(t=50, b=10, l=10, r=10), 
                paper_bgcolor="rgba(0,0,0,0)", 
                plot_bgcolor="rgba(0,0,0,0)",
                legend=dict(
                    title="Keterangan Deskripsi Topik (Legend):",
                    orientation="h",       
                    yanchor="top",
                    y=-0.15,
                    xanchor="center",
                    x=0.5,
                    font=dict(size=11)
                )
            )
            st.plotly_chart(fig_lda, use_container_width=True)

        with col_lda_info:
            dominan_key = max(data_lda, key=data_lda.get)
            dominan_label_pendek = f"Topik {dominan_key[1]}"
            
            st.markdown(f"""
            <div style="margin-top: 3.5rem;" class="insight-box">
                <span style="font-size:0.9rem;color:#666;">Total tweet negatif:</span><br>
                <span style="font-size:1.4rem;font-weight:700;">{format_indo(SENTIMEN_PER_TAHUN[tahun_lda]["negatif"])}</span>
                <hr style="margin: 10px 0; border-color: #bee3f8;">
                <span style="font-size:0.9rem;color:#666;">Topik Dominan:</span><br>
                <b style="color:{COLOR_MAP_LDA[dominan_label_pendek]};font-size:1.1rem;">{LABEL_TOPIK[dominan_key]}</b><br>
                <span style="font-size:2rem;font-weight:800;color:#1a202c;">{data_lda[dominan_key]:.1f}%</span>
            </div>
            """, unsafe_allow_html=True)

    # --- BAGIAN BARU: KESIMPULAN TOPIK DOMINAN ---
    # Hitung Topik Paling Dominan Secara Keseluruhan (Rata-rata 2016-2025)
    avg_topik = {}
    for k in topik_keys:
        avg_topik[k] = sum(TOPIK_PER_TAHUN[t][k] for t in TOPIK_PER_TAHUN) / len(TOPIK_PER_TAHUN)
    
    dominan_overall_key = max(avg_topik, key=avg_topik.get)
    dominan_overall_val = avg_topik[dominan_overall_key]
    dominan_overall_label = LABEL_TOPIK[dominan_overall_key]
    dominan_overall_color = COLOR_MAP_LDA[f"Topik {dominan_overall_key[1]}"]

    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #0f3460 0%, #1a1a2e 100%); 
                padding: 2.5rem 2rem; 
                border-radius: 12px; 
                color: white; 
                text-align: center; 
                margin-top: 1.5rem; 
                margin-bottom: 1rem;
                box-shadow: 0 8px 16px rgba(0,0,0,0.15);
                border: 1px solid #16213e;">
        <h3 style="color: #FFD700; margin-bottom: 0.8rem; font-size: 1.6rem;">📢 Kesimpulan Isu Kritis Dominan</h3>
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem; opacity: 0.9;">
            Secara keseluruhan dari tahun 2016 hingga 2025, ketidakpuasan publik paling banyak terpusat pada:
        </p>
        <h2 style="color: #ffffff; font-size: 2.2rem; font-weight: 800; margin: 0.8rem 0; letter-spacing: 1px;">
            {dominan_overall_label}
        </h2>
        <div style="display: inline-block; background-color: rgba(255, 255, 255, 0.1); padding: 0.5rem 1.5rem; border-radius: 30px; margin-top: 0.5rem; border: 1px solid rgba(255, 255, 255, 0.2);">
            <span style="font-size: 1.1rem; color: {dominan_overall_color}; font-weight: 600;">✨ Rata-rata persentase kemunculan: {dominan_overall_val:.1f}%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div style="text-align:center;color:#888;font-size:0.8rem;padding:1rem;margin-top:2rem;">
    Dashboard ini dikembangkan sebagai bagian dari Tugas Akhir Siti Aminatuzzuhriyah (10221014) | Institut Teknologi Kalimantan | 2026
</div>
""", unsafe_allow_html=True)