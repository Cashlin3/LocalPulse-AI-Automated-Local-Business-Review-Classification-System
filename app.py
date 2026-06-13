import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="LocalPulse AI",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp { background-color: #f0f2f6; }

    [data-testid="stSidebar"] {
        background-color: #1a1d27;
        border-right: 1px solid #2d3748;
        padding-top: 1rem;
    }
    [data-testid="stSidebar"] * { color: #ffffff !important; }
    [data-testid="stSidebar"] .stRadio label {
        color: #cbd5e1 !important;
        font-size: 0.95rem;
        padding: 0.4rem 0;
    }

    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .metric-label {
        color: #000000;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.4rem;
    }
    .metric-value {
        color: #000000;
        font-size: 1.9rem;
        font-weight: 700;
        line-height: 1.2;
    }

    .stTextInput input {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        color: #1e293b !important;
        font-size: 0.95rem !important;
        padding: 0.75rem 1rem !important;
    }
    .stTextInput input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
    }

    .page-title {
        color: #1e293b;
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 0.25rem;
    }
    .page-subtitle {
        color: #64748b;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }
    .section-header {
        color: #1e293b;
        font-size: 1rem;
        font-weight: 600;
        margin: 1.5rem 0 0.75rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }

    .critical-card {
        background-color: #fff5f5;
        border: 1px solid #fed7d7;
        border-left: 4px solid #ef4444;
        border-radius: 10px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }
    .warning-card {
        background-color: #fffbeb;
        border: 1px solid #fde68a;
        border-left: 4px solid #f59e0b;
        border-radius: 10px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }
    .card-meta {
        color: #94a3b8;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.4rem;
    }
    .card-text {
        color: #334155;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .info-box {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 2.5rem;
        text-align: center;
        color: #64748b;
        font-size: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .sidebar-stat {
        color: #94a3b8 !important;
        font-size: 0.82rem;
        line-height: 1.8;
    }

    hr { border-color: #e2e8f0 !important; margin: 1.5rem 0 !important; }
</style>
""", unsafe_allow_html=True)


def metric_card(label, value):
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)


@st.cache_data
def load_data():
    alerts  = pd.read_csv("review_alerts.csv")
    summary = pd.read_csv("business_summary.csv")
    return alerts, summary


alerts_df, summary_df = load_data()


# Sidebar
with st.sidebar:
    st.markdown("## 📍 LocalPulse AI")
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["Home - Overview", "Search Business", "All Critical Alerts"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    total      = len(alerts_df)
    businesses = alerts_df["business_id"].nunique()
    critical_n = (alerts_df["alert_level"] == "CRITICAL").sum()
    st.markdown(
        f"<div class='sidebar-stat'>"
        f"Reviews analyzed: {total:,}<br>"
        f"Businesses: {businesses:,}<br>"
        f"Critical alerts: {critical_n:,}"
        f"</div>",
        unsafe_allow_html=True
    )


BASE_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#1e293b"),
    margin=dict(t=30, b=60, l=20, r=20)
)


# PAGE 1 — OVERVIEW
if "Overview" in page:
    st.markdown('<div class="page-title">Dashboard Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Platform-wide review intelligence summary</div>', unsafe_allow_html=True)


    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Total Reviews", f"{len(alerts_df):,}")
    with c2:
        metric_card("Businesses Monitored", f"{alerts_df['business_id'].nunique():,}")
    with c3:
        metric_card("Critical Alerts", f"{(alerts_df['alert_level']=='CRITICAL').sum():,}")
    with c4:
        metric_card("Warnings", f"{(alerts_df['alert_level']=='WARNING').sum():,}")


    st.markdown("---")
    col_l, col_r = st.columns(2)


    with col_l:
        st.markdown('<div class="section-header">Sentiment Distribution</div>', unsafe_allow_html=True)
        sc = alerts_df["sentiment"].value_counts().reset_index()
        sc.columns = ["sentiment", "count"]
        color_map = {"positive": "#22c55e", "negative": "#ef4444", "neutral": "#f59e0b"}
        fig = go.Figure(data=[go.Pie(
            labels=sc["sentiment"],
            values=sc["count"],
            hole=0.45,
            marker=dict(colors=[color_map.get(s, "#94a3b8") for s in sc["sentiment"]]),
            textinfo="label+percent",
            textposition="outside",
            textfont=dict(size=13, color="#1e293b"),
            insidetextorientation="radial",
            pull=[0.03] * len(sc)
        )])
        fig.update_layout(
            **BASE_LAYOUT,
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5,
                font=dict(size=12, color="#1e293b")
            )
        )
        st.plotly_chart(fig, use_container_width=True)


    with col_r:
        st.markdown('<div class="section-header">Alert Level Breakdown</div>', unsafe_allow_html=True)
        ac = alerts_df["alert_level"].value_counts().reset_index()
        ac.columns = ["alert_level", "count"]
        bar_colors = {"CRITICAL": "#ef4444", "WARNING": "#f59e0b", "normal": "#22c55e"}
        fig2 = go.Figure(data=[go.Bar(
            x=ac["alert_level"],
            y=ac["count"],
            marker_color=[bar_colors.get(l, "#6366f1") for l in ac["alert_level"]],
            text=[f"{v:,}" for v in ac["count"]],
            textposition="outside",
            textfont=dict(size=13, color="#1e293b"),
            width=0.5
        )])
        fig2.update_layout(
            **BASE_LAYOUT,
            showlegend=False,
            xaxis=dict(
                showgrid=False,
                color="#1e293b",
                tickfont=dict(size=13, color="#1e293b"),
                title=dict(text="Alert Level", font=dict(size=13, color="#64748b"))
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor="#e2e8f0",
                color="#1e293b",
                tickfont=dict(size=12, color="#64748b"),
                title=dict(text="Number of Reviews", font=dict(size=13, color="#64748b")),
                tickformat=","
            ),
            bargap=0.4
        )
        st.plotly_chart(fig2, use_container_width=True)


# PAGE 2 — SEARCH BUSINESS
elif "Search" in page:
    st.markdown('<div class="page-title">Search Your Business</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Enter your Business ID to see your personalised review report</div>', unsafe_allow_html=True)


    business_id = st.text_input("", placeholder="e.g. XQfwVwDr-v0ZS3_CbbE5Xw")


    if business_id.strip():
        biz = alerts_df[alerts_df["business_id"] == business_id.strip()]


        if len(biz) == 0:
            st.error("Business ID not found. Please check and try again.")
        else:
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                metric_card("Total Reviews", len(biz))
            with c2:
                metric_card("Avg Stars", f"{biz['stars'].mean():.1f}")
            with c3:
                metric_card("Critical", (biz["alert_level"]=="CRITICAL").sum())
            with c4:
                metric_card("Warnings", (biz["alert_level"]=="WARNING").sum())
            with c5:
                metric_card("Normal", (biz["alert_level"]=="normal").sum())


            st.markdown("---")
            col_l, col_r = st.columns(2)


            with col_l:
                st.markdown('<div class="section-header">Sentiment Breakdown</div>', unsafe_allow_html=True)
                sc = biz["sentiment"].value_counts().reset_index()
                sc.columns = ["sentiment", "count"]
                color_map = {"positive": "#22c55e", "negative": "#ef4444", "neutral": "#f59e0b"}
                fig = go.Figure(data=[go.Pie(
                    labels=sc["sentiment"],
                    values=sc["count"],
                    hole=0.45,
                    marker=dict(colors=[color_map.get(s, "#94a3b8") for s in sc["sentiment"]]),
                    textinfo="label+percent",
                    textposition="outside",
                    textfont=dict(size=13, color="#1e293b"),
                    pull=[0.03] * len(sc)
                )])
                fig.update_layout(
                    **BASE_LAYOUT,
                    showlegend=True,
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.2,
                        xanchor="center",
                        x=0.5,
                        font=dict(size=12, color="#1e293b")
                    )
                )
                st.plotly_chart(fig, use_container_width=True)


            with col_r:
                st.markdown('<div class="section-header">Star Rating Distribution</div>', unsafe_allow_html=True)
                sr = biz["stars"].value_counts().sort_index().reset_index()
                sr.columns = ["stars", "count"]
                fig3 = go.Figure(data=[go.Bar(
                    x=sr["stars"],
                    y=sr["count"],
                    marker_color="#6366f1",
                    text=[f"{v:,}" for v in sr["count"]],
                    textposition="outside",
                    textfont=dict(size=13, color="#1e293b"),
                    width=0.5
                )])
                fig3.update_layout(
                    **BASE_LAYOUT,
                    showlegend=False,
                    xaxis=dict(
                        showgrid=False,
                        tickfont=dict(size=13, color="#1e293b"),
                        title=dict(text="Stars", font=dict(size=13, color="#64748b"))
                    ),
                    yaxis=dict(
                        showgrid=True,
                        gridcolor="#e2e8f0",
                        tickfont=dict(size=12, color="#64748b"),
                        title=dict(text="Number of Reviews", font=dict(size=13, color="#64748b")),
                        tickformat=","
                    )
                )
                st.plotly_chart(fig3, use_container_width=True)


            st.markdown("---")


            critical = biz[biz["alert_level"] == "CRITICAL"]
            st.markdown('<div class="section-header">Critical Alerts — Act Immediately</div>', unsafe_allow_html=True)
            if len(critical) > 0:
                st.error(f"You have {len(critical)} critical reviews flagging hygiene or safety issues!")
                show_all_biz_critical = st.session_state.get("show_all_biz_critical", False)
                critical_to_show = critical if show_all_biz_critical else critical.head(10)
                for _, row in critical_to_show.iterrows():
                    stars_display = "⭐" * int(row["stars"])
                    text_preview  = str(row["text"])[:300] + ("..." if len(str(row["text"])) > 300 else "")
                    st.markdown(f"""
                        <div class="critical-card">
                            <div class="card-meta">{stars_display} {row['stars']} stars</div>
                            <div class="card-text">{text_preview}</div>
                        </div>""", unsafe_allow_html=True)
                if not show_all_biz_critical and len(critical) > 10:
                    if st.button(f"Show all {len(critical):,} critical alerts", key="biz_more_critical"):
                        st.session_state["show_all_biz_critical"] = True
                        st.rerun()
            else:
                st.success("No critical alerts for this business!")


            warnings = biz[biz["alert_level"] == "WARNING"]
            st.markdown('<div class="section-header">Warning Alerts</div>', unsafe_allow_html=True)
            if len(warnings) > 0:
                st.warning(f"You have {len(warnings)} reviews flagging service issues.")
                show_all_biz_warn = st.session_state.get("show_all_biz_warn", False)
                warnings_to_show = warnings if show_all_biz_warn else warnings.head(10)
                for _, row in warnings_to_show.iterrows():
                    stars_display = "⭐" * int(row["stars"])
                    text_preview  = str(row["text"])[:300] + ("..." if len(str(row["text"])) > 300 else "")
                    st.markdown(f"""
                        <div class="warning-card">
                            <div class="card-meta">{stars_display} {row['stars']} stars</div>
                            <div class="card-text">{text_preview}</div>
                        </div>""", unsafe_allow_html=True)
                if not show_all_biz_warn and len(warnings) > 10:
                    if st.button(f"Show all {len(warnings):,} warnings", key="biz_more_warn"):
                        st.session_state["show_all_biz_warn"] = True
                        st.rerun()
            else:
                st.success("No warnings for this business!")
    else:
        st.markdown("""
            <div class="info-box">
                Enter a Business ID above to see your full review intelligence report
            </div>""", unsafe_allow_html=True)


# PAGE 3 — ALL CRITICAL ALERTS
elif "Critical" in page:
    st.markdown('<div class="page-title">All Critical Alerts</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Reviews flagging serious hygiene or safety issues across all businesses</div>', unsafe_allow_html=True)


    critical_all = alerts_df[alerts_df["alert_level"] == "CRITICAL"].copy()
    st.markdown(f'<div class="section-header">{len(critical_all):,} Critical Reviews Found</div>', unsafe_allow_html=True)


    show_all = st.session_state.get("show_all_critical", False)
    critical_to_show = critical_all if show_all else critical_all.head(50)


    for _, row in critical_to_show.iterrows():
        stars_display = "⭐" * int(row["stars"])
        text_preview  = str(row["text"])[:300] + ("..." if len(str(row["text"])) > 300 else "")
        st.markdown(f"""
            <div class="critical-card">
                <div class="card-meta">Business: {row['business_id']} &nbsp;|&nbsp; {stars_display} {row['stars']} stars</div>
                <div class="card-text">{text_preview}</div>
            </div>""", unsafe_allow_html=True)


    if not show_all:
        if st.button(f"Show all {len(critical_all):,} critical alerts", key="more_critical"):
            st.session_state["show_all_critical"] = True
            st.rerun()