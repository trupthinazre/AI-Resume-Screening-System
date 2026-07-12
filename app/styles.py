import streamlit as st

def load_css():
    st.markdown("""
<style>

/* =====================================================
   GLOBAL SETTINGS
===================================================== */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"]{
    font-family:'Segoe UI',sans-serif;
}

.stApp{
    background:#0D1117;
    color:white;
}

/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{

    background:#161B22;
    border-right:1px solid #30363D;

}

section[data-testid="stSidebar"] *{

    color:white;

}

/* =====================================================
   HERO
===================================================== */

.hero{

    background:linear-gradient(
    135deg,
    #2563EB,
    #7C3AED
    );

    padding:35px;

    border-radius:20px;

    text-align:center;

    margin-bottom:30px;

    box-shadow:0px 10px 30px rgba(0,0,0,.45);

}

.hero h1{

    color:white;

    font-size:42px;

    margin-bottom:15px;

    font-weight:700;

}

.hero p{

    color:#F3F4F6;

    font-size:18px;

    line-height:1.7;

}

/* =====================================================
   TEXT AREA
===================================================== */

textarea{

    background:#2A2F3A !important;

    color:white !important;

    border-radius:15px !important;

    border:1px solid #4B5563 !important;

    font-size:16px !important;

    padding:15px !important;

}

/* =====================================================
   BUTTON
===================================================== */

.stButton>button{

    width:100%;

    height:58px;

    border:none;

    border-radius:15px;

    color:white;

    font-size:18px;

    font-weight:bold;

    background:linear-gradient(
    90deg,
    #2563EB,
    #7C3AED
    );

    transition:.35s;

}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:0px 10px 25px rgba(37,99,235,.45);

}

/* =====================================================
   METRIC CARDS
===================================================== */

[data-testid="stMetric"]{

    background:#2A2F3A;

    border:1px solid #4B5563;

    border-radius:18px;

    padding:22px;

    box-shadow:
    0 10px 20px rgba(0,0,0,.30);

}

[data-testid="stMetric"]:hover{

    border:1px solid #2563EB;

    transform:translateY(-4px);

    transition:.25s;

}

/* Metric label */

[data-testid="stMetricLabel"]{

    color:#D1D5DB;

    font-size:15px;

}

/* Metric value */

[data-testid="stMetricValue"]{

    color:white;

    font-size:34px;

    font-weight:bold;

}

/* =====================================================
   DATAFRAME
===================================================== */

[data-testid="stDataFrame"]{

    background:#2A2F3A;

    border:1px solid #4B5563;

    border-radius:18px;

    overflow:hidden;

}

/* =====================================================
   SUCCESS MESSAGE
===================================================== */

div[data-testid="stAlert"]{

    border-radius:15px;

}

/* =====================================================
   HEADINGS
===================================================== */

h1,h2,h3{

    color:white;

}

/* =====================================================
   HORIZONTAL LINE
===================================================== */

hr{

    border:1px solid #30363D;

}

/* =====================================================
   SCROLLBAR
===================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#4B5563;

    border-radius:30px;

}

::-webkit-scrollbar-track{

    background:#161B22;

}

/* =====================================================
   ANIMATION
===================================================== */

@keyframes fadeUp{

    from{

        opacity:0;
        transform:translateY(15px);

    }

    to{

        opacity:1;
        transform:translateY(0px);

    }

}

.hero,
[data-testid="stMetric"],
[data-testid="stDataFrame"]{

    animation:fadeUp .5s ease;

}

</style>
""", unsafe_allow_html=True)