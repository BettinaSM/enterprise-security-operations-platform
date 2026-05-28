import streamlit as st

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Enterprise SOC Platform",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# DATABASE
# ---------------------------

from parsers.database_engine import (
    create_tables
)

create_tables()

# ---------------------------
# SECURITY
# ---------------------------

from security.auth import (
    login
)

from security.session import (
    create_session,
    logout,
    is_authenticated
)

# ---------------------------
# LOGIN
# ---------------------------

if "authenticated" not in st.session_state:

    st.session_state["authenticated"] = False

if not is_authenticated():

    st.title(
        "🛡️ Enterprise Security Operations Platform"
    )

    st.subheader(
        "Authentication Required"
    )

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button(
        "Login",
        key="login_button"
    ):

        role = login(
            username,
            password
        )

        if role:

            create_session(
                username,
                role
            )

            st.success(
                f"Authenticated as {role}"
            )

            st.rerun()

        else:

            st.error(
                "Invalid credentials"
            )

    st.stop()

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title(
    "SOC Navigation"
)

st.sidebar.success(
    f"Authenticated as: {st.session_state['role']}"
)

menu = st.sidebar.radio(

    "Select Section",

    [

        "Dashboard",
        "Detections",
        "Threat Intelligence",
        "Realtime Monitoring",
        "Incidents",
        "Analytics",
        "Cloud Security",
        "Threat Hunting",
        "Compliance",
        "Executive",
        "SOAR",
        "Automation",
        "Enterprise Audit",
        "Reporting"

    ]
)

if st.sidebar.button(
    "Logout",
    key="logout_button"
):

    logout()

    st.rerun()

# ---------------------------
# COLLECTORS
# ---------------------------

from collectors.linux_collector import (
    collect_linux_logs
)

from collectors.aix_collector import (
    collect_aix_logs
)

from collectors.windows_collector import (
    collect_windows_logs
)

from collectors.cloud_collector import (
    collect_cloud_logs
)

linux_logs = collect_linux_logs()

aix_logs = collect_aix_logs()

windows_logs = collect_windows_logs()

events = (
    linux_logs +
    aix_logs +
    [str(event) for event in windows_logs]
)

# ---------------------------
# PARSERS
# ---------------------------

from parsers.detection_engine import (
    run_detections
)

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from parsers.mitre_mapper import (
    map_to_mitre
)

from parsers.analytics_engine import (
    detection_analytics,
    incident_analytics
)

from parsers.threat_intelligence import (
    enrich_iocs
)

from parsers.threat_feed import (
    load_threat_feed,
    correlate_threat_feed
)

from parsers.cve_mapper import (
    enrich_cves
)

# ---------------------------
# DATA PROCESSING
# ---------------------------

ioc_matches = [

    "185.220.101.1",
    "malicious-domain.com"

]

detections = run_detections(
    events
)

yaml_detections = run_yaml_detections(
    events
)

mitre_events = map_to_mitre(
    events
)

detection_stats = detection_analytics()

incident_stats = incident_analytics()

threat_feed = load_threat_feed(
    "threat-intelligence/threat-feed.json"
)

feed_correlations = correlate_threat_feed(
    ioc_matches,
    threat_feed
)

enriched_iocs = enrich_iocs(
    ioc_matches
)

cve_findings = enrich_cves(
    ioc_matches
)

# ---------------------------
# SECTIONS
# ---------------------------

from sections.dashboard import (
    render_dashboard
)

from sections.detections import (
    render_detections
)

from sections.threat_intelligence import (
    render_threat_intelligence
)

from sections.realtime import (
    render_realtime
)

from sections.incidents import (
    render_incidents
)

from sections.analytics import (
    render_analytics
)

from sections.cloud_security import (
    render_cloud_security
)

from sections.compliance import (
    render_compliance
)

from sections.executive import (
    render_executive
)

from sections.hunting import (
    render_hunting
)

from sections.soar import (
    render_soar
)

from sections.automation import (
    render_automation
)

from sections.enterprise_audit import (
    render_enterprise_audit
)

# ---------------------------
# HEADER
# ---------------------------

st.title(
    "🛡️ Enterprise Security Operations Platform"
)

# ---------------------------
# ROUTING
# ---------------------------

if menu == "Dashboard":

    render_dashboard()

elif menu == "Detections":

    render_detections(
        detections,
        yaml_detections,
        mitre_events
    )

elif menu == "Threat Intelligence":

    render_threat_intelligence(
        enriched_iocs,
        feed_correlations,
        cve_findings
    )

elif menu == "Realtime Monitoring":

    render_realtime()

elif menu == "Incidents":

    render_incidents()

elif menu == "Analytics":

    render_analytics(
        detection_stats,
        incident_stats
    )

elif menu == "Cloud Security":

    render_cloud_security()

elif menu == "Threat Hunting":

    render_hunting(
        events
    )

elif menu == "Compliance":

    render_compliance()

elif menu == "Executive":

    render_executive()

elif menu == "SOAR":

    render_soar()

elif menu == "Automation":

    render_automation()

elif menu == "Enterprise Audit":

    render_enterprise_audit()

elif menu == "Reporting":

    from reporting.pdf_generator import (
        generate_security_report
    )

    st.subheader(
        "Security Reporting"
    )

    if st.button(
        "Generate Executive PDF Report",
        key="pdf_button"
    ):

        report_file = generate_security_report(
            detections,
            incident_stats.to_dict("records"),
            feed_correlations
        )

        st.success(
            f"Report generated: {report_file}"
        )

        with open(
            report_file,
            "rb"
        ) as pdf_data:

            st.download_button(
                label="Download PDF",
                data=pdf_data,
                file_name=report_file.name,
                mime="application/pdf",
                key="download_pdf"
            )

# ---------------------------
# FOOTER
# ---------------------------

st.divider()

st.caption(
    "Enterprise Security Operations Platform | SOC Engineering Lab"
)
