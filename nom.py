import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="NomineeVault: DPDP Section 14 Engine", page_icon="🏛️", layout="wide")

# --- CUSTOM DARK TECH-LEGAL THEME STYLING ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc !important;
        font-family: 'Inter', sans-serif;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {
        background-color: #1e293b;
        color: #f1f5f9;
        border: 1px solid #334155;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 6px;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ NomineeVault: DPDP Section 14 Digital Estate & Privacy Engine")
st.markdown("A specialized legal-tech application addressing **Section 14 of India's DPDPA 2023** (Right to Nominate), managing digital survivorship and proxy statutory execution.")
st.caption("⚖️ **Statutory & Legal Disclaimer:** All names, nomination records, and entity data utilized within this demonstration environment are entirely hypothetical mock records.")

# --- CONCISE RECRUITER & LEGAL ARCHITECT OVERVIEW ---
with st.expander("⚖️ About NomineeVault & Market Gap (For Recruiters & Reviewers)", expanded=False):
    st.markdown("""
    * **The Market Gap:** While global compliance platforms like OneTrust handle standard GDPR DSARs, they completely lack native workflows for **India's DPDPA Section 14 (Right to Nominate)**—the statutory "digital will" provision governing digital survivorship upon death or incapacity.
    * **My Role as Legal Architect & Product Owner:** Conceptualized the multi-gate verification architecture, differentiating objective proof (Death Certificates) from complex legal thresholds (Incapacity/Guardianship) to prevent unauthorized account takeovers while ensuring strict regulatory compliance.
    * **The Solution:** An interactive multi-portal simulation bridging escrowed nominee registration, simulated DigiLocker/Aadhaar e-KYC authentication, sequential compliance gates, and Section 32 grievance adjudication.
    """)

st.divider()

# Initialize Session State with realistic default records (Anonymized Names)
if "nomination_records" not in st.session_state:
    current_date = datetime.now().date()
    st.session_state.nomination_records = [
        {
            "Nomination_ID": "NOM-3001",
            "Principal_Name": "Ashok Kumar",
            "Principal_Email": "ashok.kumar@privacyvault.in",
            "Nominee_Name": "Sunita Kumar",
            "Nominee_Email": "sunita.kumar@privacyvault.in",
            "Nominee_Relationship": "Spouse",
            "Trigger_Status": "Active (Principal Living - Escrowed)",
            "Trigger_Event_Details": "None. Principal is active.",
            "Authorized_Scope": "Full Account Erasure & RoPA Access",
            "Verification_State": "Not Triggered",
            "Proof_Submitted": False,
            "Denial_Reason": "",
            "Registration_Date": (current_date - timedelta(days=120)).strftime("%d-%m-%Y")
        },
        {
            "Nomination_ID": "NOM-3002",
            "Principal_Name": "Ramesh Menon",
            "Principal_Email": "ramesh.m@enterprise.in",
            "Nominee_Name": "Arjun Menon",
            "Nominee_Email": "arjun.m@enterprise.in",
            "Nominee_Relationship": "Son",
            "Trigger_Status": "Death Triggered",
            "Trigger_Event_Details": "Reported Death of Data Principal on 15-10-2026.",
            "Authorized_Scope": "Right to Erasure (Deceased Estate Purge)",
            "Verification_State": "Verified (Death Certificate Validated)",
            "Proof_Submitted": True,
            "Denial_Reason": "",
            "Registration_Date": (current_date - timedelta(days=200)).strftime("%d-%m-%Y")
        }
    ]

# --- LEFT SIDEBAR DIRECTORY CLIPBOARD NAVIGATION ---
st.sidebar.header("📁 Digital Estate Directory")
st.sidebar.markdown("Select a portal view to load the corresponding interactive workspace on the right panel.")

portal_selection = st.sidebar.radio(
    "Navigation Clipboard", 
    [
        "📝 1. Data Principal Portal", 
        "🏛️ 2. Nominee Portal (Proxy Claims)", 
        "🛡️ 3. Enterprise Privacy Manager"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.info("💡 **Architectural Note:** This simulator enforces strict DPDPA Section 14 compliance gates, separating Principal escrow, DigiLocker nominee verification, and Privacy Manager adjudication.")


# ==========================================
# PORTAL 1: DATA PRINCIPAL PORTAL
# ==========================================
if portal_selection == "📝 1. Data Principal Portal":
    st.subheader("Data Principal Portal: Digital Will & Nomination Registry")
    st.markdown("Manage your personal privacy settings and register your designated nominee under **Section 14 of the DPDPA 2023**.")
    
    logged_in_email = "ashok.kumar@privacyvault.in"
    logged_in_name = "Ashok Kumar"
    
    st.info(f"👤 **Active User Session:** {logged_in_name} ({logged_in_email})")
    
    existing_nomination = next((n for n in st.session_state.nomination_records if n["Principal_Email"].lower() == logged_in_email.lower()), None)
    
    if existing_nomination:
        st.success("✅ **Active Section 14 Nomination Found in Digital Estate Vault:**")
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Nomination ID", value=existing_nomination["Nomination_ID"], disabled=True, key="p_id_view")
            st.text_input("Registered Nominee Name", value=existing_nomination["Nominee_Name"], disabled=True, key="p_name_view")
            st.text_input("Nominee Email", value=existing_nomination["Nominee_Email"], disabled=True, key="p_email_view")
        with col_b:
            st.text_input("Relationship", value=existing_nomination["Nominee_Relationship"], disabled=True, key="p_rel_view")
            st.text_input("Pre-Authorized Scope", value=existing_nomination["Authorized_Scope"], disabled=True, key="p_scope_view")
            st.text_input("Current Estate Status", value=existing_nomination["Trigger_Status"], disabled=True, key="p_status_view")
            
        st.divider()
        st.markdown("#### ⚖️ Statutory Modification & Revocation Controls")
        st.markdown("Modifying or replacing an established statutory nomination alters active digital estate escrow rights. This action is logged for regulatory compliance audit trails.")
        
        if "show_revocation_form" not in st.session_state:
            st.session_state["show_revocation_form"] = False
            
        if not st.session_state["show_revocation_form"]:
            if st.button("⚠️ Initiate Revocation / Replacement of Nomination", key="init_rev_btn"):
                st.session_state["show_revocation_form"] = True
                st.rerun()
        else:
            with st.form("revocation_guardrail_form"):
                st.warning(
                    "**STATUTORY WARNING & COMPLIANCE NOTICE:**\n"
                    "You are attempting to modify or revoke a registered Section 14 DPDPA nomination. "
                    "In accordance with data fiduciary governance standards, revoking an active nomination terminates the nominee's contingent legal standing."
                )
                
                revocation_action = st.radio("Select Action", ["Revoke Nomination Entirely", "Replace with New Nominee"], key="rev_action_radio")
                
                new_n_name, new_n_email, new_n_rel = "", "", ""
                if revocation_action == "Replace with New Nominee":
                    st.markdown("##### Enter Replacement Nominee Details:")
                    new_n_name = st.text_input("Replacement Nominee Full Name", placeholder="e.g., Meena Kumar")
                    new_n_email = st.text_input("Replacement Nominee Email", placeholder="meena@privacyvault.in")
                    new_n_rel = st.text_input("Relationship", placeholder="e.g., Daughter")
                
                confirm_checkbox = st.checkbox("I legally affirm that I am the authorized Data Principal executing this change under free will.")
                
                col_sub1, col_sub2 = st.columns(2)
                with col_sub1:
                    commit_btn = st.form_submit_button("🔒 Execute Statutory Change", type="primary")
                with col_sub2:
                    cancel_btn = st.form_submit_button("❌ Cancel")
                    
                if cancel_btn:
                    st.session_state["show_revocation_form"] = False
                    st.rerun()
                    
                if commit_btn:
                    if not confirm_checkbox:
                        st.error("You must check the legal affirmation checkbox to proceed.")
                    else:
                        if revocation_action == "Revoke Nomination Entirely":
                            st.session_state.nomination_records = [n for n in st.session_state.nomination_records if n["Nomination_ID"] != existing_nomination["Nomination_ID"]]
                            st.success("Nomination successfully revoked and purged from active digital estate escrow.")
                        else:
                            if not new_n_name.strip() or not new_n_email.strip():
                                st.error("Please fill in the replacement nominee's name and email.")
                            else:
                                existing_nomination["Nominee_Name"] = new_n_name
                                existing_nomination["Nominee_Email"] = new_n_email
                                existing_nomination["Nominee_Relationship"] = new_n_rel
                                existing_nomination["Verification_State"] = "Not Triggered (Replacement Nominee)"
                                existing_nomination["Trigger_Status"] = "Active (Principal Living - Escrowed)"
                                st.success("Nomination successfully updated with replacement nominee details. Audit trail updated.")
                        st.session_state["show_revocation_form"] = False
                        st.rerun()
    else:
        st.warning("⚠️ No active Section 14 nominee registered under your account. Configure your digital estate preference below.")
        
        with st.form("principal_reg_form"):
            col1, col2 = st.columns(2)
            with col1:
                new_id = f"NOM-300{len(st.session_state.nomination_records)+1}"
                n_name = st.text_input("Nominee Full Name", placeholder="e.g., Sunita Kumar")
                n_email = st.text_input("Nominee Email Address", placeholder="sunita.kumar@privacyvault.in")
            with col2:
                n_relation = st.text_input("Relationship to Principal", placeholder="e.g., Spouse")
                scope = st.selectbox("Pre-Authorized Statutory Scope", [
                    "Full Account Erasure & RoPA Access", 
                    "Right to Erasure (Deceased Estate Purge)", 
                    "Correction & Financial Record Access"
                ])
                
            submitted = st.form_submit_button("🔒 Securely Register Nomination to Vault")
            if submitted:
                if not n_name.strip() or not n_email.strip():
                    st.warning("Please complete your nominee's name and email address.")
                else:
                    new_entry = {
                        "Nomination_ID": new_id,
                        "Principal_Name": logged_in_name,
                        "Principal_Email": logged_in_email,
                        "Nominee_Name": n_name,
                        "Nominee_Email": n_email,
                        "Nominee_Relationship": n_relation,
                        "Trigger_Status": "Active (Principal Living - Escrowed)",
                        "Trigger_Event_Details": "None. Principal is active.",
                        "Authorized_Scope": scope,
                        "Verification_State": "Not Triggered",
                        "Proof_Submitted": False,
                        "Denial_Reason": "",
                        "Registration_Date": datetime.now().strftime("%d-%m-%Y")
                    }
                    st.session_state.nomination_records.append(new_entry)
                    st.success(f"Success! Nomination ID **{new_id}** registered securely to your digital estate account.")
                    st.rerun()


# ==========================================
# PORTAL 2: NOMINEE PORTAL
# ==========================================
elif portal_selection == "🏛️ 2. Nominee Portal (Proxy Claims)":
    st.subheader("Nominee Portal: Proxy Dashboard & Statutory Claims Execution")
    st.markdown("Authenticate your session via **DigiLocker / Aadhaar e-KYC Intermediary Verification** to access your designated nominee dashboard and execute pre-authorized rights.")
    
    nominee_options = {f"{n['Nomination_ID']} — {n['Nominee_Name']} (Nominee for {n['Principal_Name']})": n for n in st.session_state.nomination_records}
    nominee_select_list = ["-- Select Nominee Profile --"] + list(nominee_options.keys())
    
    chosen_nom_label = st.selectbox("Select Nominee Profile for Authentication", nominee_select_list, key="nom_dropdown_sel")
    
    digilocker_id_input = st.text_input(
        "Enter Nominee Aadhaar Number / Virtual ID (Mock) (e.g., type any 4+ digits for mock verification)", 
        placeholder="e.g., 123456789012", 
        type="password", 
        key="digilocker_input"
    )
    
    if st.button("🔗 Authenticate via DigiLocker Service Provider", key="auth_digilocker_btn"):
        if chosen_nom_label == "-- Select Nominee Profile --":
            st.error("Please select a valid nomination profile from the dropdown.")
            if "active_nominee" in st.session_state:
                del st.session_state["active_nominee"]
        elif not digilocker_id_input.strip() or len(digilocker_id_input.strip()) < 4:
            st.error("Invalid or empty DigiLocker credential format. Please input simulated verification credentials.")
        else:
            matched_rec = nominee_options[chosen_nom_label]
            st.session_state["active_nominee"] = matched_rec
            st.success(f"✅ **DigiLocker Verification Successful:** Identity cryptographically verified for **{matched_rec['Nominee_Name']}**. Session token issued.")

    if "active_nominee" in st.session_state:
        current_nom_id = st.session_state["active_nominee"]["Nomination_ID"]
        m = next(n for n in st.session_state.nomination_records if n["Nomination_ID"] == current_nom_id)
        
        st.divider()
        st.info(f"🏛️ **Active Verified Session:** Acting as **{m['Nominee_Name']}** (`{m['Nominee_Email']}`) | Nomination ID: **{m['Nomination_ID']}**\n*(Verified via Government Intermediary Service Provider: DigiLocker API)*")
        
        # --- DYNAMIC STREAMLINED VIEW BASED ON STATUS ---
        if "Verified" in m["Verification_State"]:
            st.success("🎉 **Proxy Authorization Active:** Your evidentiary proof has been fully validated and adjudicated. You are legally authorized to exercise your pre-authorized proxy rights conferred by the Data Principal.")
            
            st.markdown(f"### 📊 Active Estate Profile: {m['Principal_Name']}")
            c_v1, c_v2 = st.columns(2)
            with c_v1:
                st.metric("Adjudication State", m["Verification_State"])
                st.metric("Nomination ID", m["Nomination_ID"])
            with c_v2:
                st.metric("Pre-Authorized Scope", m["Authorized_Scope"])
                st.metric("Estate Status", "Authorized Proxy Access")
                
            st.divider()
            st.markdown("### ⚡ Execution of Conferred Rights (Section 12 & Section 14 Mandates)")
            st.markdown("Pursuant to the legal authority established under DPDPA Section 14, you may now formally exercise the specific data rights conferred by the Data Principal.")
            
            selected_right_to_execute = st.selectbox("Select Statutory Right to Exercise on Behalf of Principal", [
                "Execute Section 12 Right to Erasure / Deceased Estate Purge",
                "Request RoPA & Data Transparency Record Access",
                "Withdraw All Active Consents Granted by Principal"
            ], key="proxy_act_sel")
            
            execution_reason = st.text_area("Statutory Invocation Note / Context", value=f"Exercising {selected_right_to_execute} pursuant to Section 14 Digital Estate Nomination ID {m['Nomination_ID']}.", key="exec_note_input")
            
            if st.button("🚀 Transmit Formal Statutory Mandate to Data Fiduciary", type="primary", key="exec_mandate_btn"):
                st.success(f"✅ **Mandate Successfully Executed & Logged:** **{selected_right_to_execute}** has been formally processed and transmitted for Data Principal **{m['Principal_Name']}** under DPDPA Section 14 read with Section 12 mandates. Audit cryptographic receipt generated.")
                
        elif "Rejected" in m["Verification_State"]:
            # DIRECT DENIAL NOTICE REFLECTION AT TOP OF NOMINEE VIEW
            st.error("❌ **Claim Notice: Formal Statutory Denial Notice Issued**")
            st.markdown(f"> **Official Denial Reason & Legal Adjudication Pleading:**\n> {m['Denial_Reason']}")
            st.warning(f"⚖️ **Grievance Redressal Notice (Section 32 DPDPA):** Pursuant to the statutory grievance framework under the DPDPA 2023, if you believe this adjudication is erroneous or wish to adduce supplementary evidence, you may formally file an appeal with our designated **Enterprise Grievance Officer** at `grievance.officer@enterprise.in` citing Nomination ID **{m['Nomination_ID']}**.")
            
        else:
            st.markdown(f"### 📊 Estate Overview & Incident Log: {m['Principal_Name']}")
            
            c_m1, c_m2 = st.columns(2)
            with c_m1:
                st.metric("Current Estate Status", m["Trigger_Status"])
                st.markdown(f"**Recorded Incident / Trigger:**\n> {m['Trigger_Event_Details']}")
            with c_m2:
                st.metric("Verification State", m["Verification_State"])
                st.metric("Nomination ID", m["Nomination_ID"])
                
            st.divider()
            st.markdown("#### 🔄 Sequential Statutory Workflow & Compliance Gates")
            
            if "Active" in m["Trigger_Status"]:
                st.info("🟢 **Gate 1 Status:** The Data Principal is currently active and living. Nomination rights remain held securely in escrow under Section 14.")
                st.markdown("If an unfortunate event (Death or Incapacity) has occurred, you may initiate the statutory trigger sequence below.")
                
                trigger_type = st.selectbox("Select Statutory Trigger Event", ["Death of Data Principal", "Incapacity / Medical Incompetence"], key="trig_type_sel")
                if st.button("📤 File Statutory Incident Notification", type="primary", key="file_trig_btn"):
                    m["Trigger_Status"] = f"Triggered ({trigger_type} - Pending Review)"
                    m["Trigger_Event_Details"] = f"Initiated by nominee on {datetime.now().strftime('%d-%m-%Y')} for {trigger_type}."
                    m["Verification_State"] = "Pending Evidentiary Proof Upload"
                    st.success("Incident notification recorded in audit logs. Proceed to Gate 2 (Evidentiary Upload).")
                    st.rerun()
                    
            elif "Pending" in m["Verification_State"] or "Triggered" in m["Trigger_Status"]:
                st.warning("⚠️ **Gate 2 Action Required:** Incident registered. Please upload statutory proof (e.g., Death Certificate or Medical Board Certificate) for adjudication.")
                
                uploaded_file = st.file_uploader("Upload Statutory Document (PDF, JPG, PNG)", type=["pdf", "jpg", "png"], key="proof_upload")
                if uploaded_file is not None:
                    st.info(f"File attached: `{uploaded_file.name}`")
                    if st.button("🚀 Transmit Proof to Enterprise Adjudication Officer", key="trans_proof_btn"):
                        m["Proof_Submitted"] = True
                        m["Verification_State"] = "Pending Compliance Officer Review"
                        st.success("📤 **TRANSMISSION SUCCESSFUL:** Statutory evidentiary document has been securely routed via DigiLocker bridge to the concerned Adjudication Officer. A formal statutory determination will be rendered within 3 to 5 business days.")
                elif m["Proof_Submitted"]:
                    st.info("📋 Proof successfully transmitted and logged. Awaiting adjudication review from the Enterprise Compliance Manager.")


# ==========================================
# PORTAL 3: ENTERPRISE PRIVACY MANAGER
# ==========================================
else:
    st.subheader("Enterprise Compliance Manager: Adjudication & Access Control Gateway")
    st.markdown("Review incoming Section 14 claims, examine DigiLocker-transmitted evidentiary proofs, and issue legally binding determinations or statutory denial notices.")
    
    df_audit = pd.DataFrame(st.session_state.nomination_records)
    st.dataframe(df_audit[["Nomination_ID", "Principal_Name", "Nominee_Name", "Trigger_Status", "Verification_State", "Proof_Submitted"]], use_container_width=True)
    
    st.divider()
    st.subheader("⚖️ Adjudication Workbench")
    
    mgr_options = {f"{n['Nomination_ID']} — Principal: {n['Principal_Name']} (Nominee: {n['Nominee_Name']})": n for n in st.session_state.nomination_records}
    mgr_select_list = ["-- Select Nomination Record to Adjudicate --"] + list(mgr_options.keys())
    
    mgr_selected_label = st.selectbox("Select Nomination Record to Adjudicate", mgr_select_list, key="mgr_sel_box")
    
    if mgr_selected_label != "-- Select Nomination Record to Adjudicate --":
        mgr_rec = mgr_options[mgr_selected_label]
        
        st.write(f"**Data Principal:** {mgr_rec['Principal_Name']} (`{mgr_rec['Principal_Email']}`)")
        st.write(f"**Nominee:** {mgr_rec['Nominee_Name']} (`{mgr_rec['Nominee_Email']}`)")
        st.write(f"**Current Status:** {mgr_rec['Trigger_Status']} | **Trigger Details:** {mgr_rec['Trigger_Event_Details']}")
        st.write(f"**Verification State:** {mgr_rec['Verification_State']}")
        st.write(f"**Evidentiary Proof Uploaded:** {'Yes ✅ (Transmitted via DigiLocker Bridge)' if mgr_rec['Proof_Submitted'] else 'No ❌'}")
        
        st.divider()
        
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("✅ Approve Proof & Unlock Nominee Scope", type="primary", key="mgr_approve_btn"):
                mgr_rec["Verification_State"] = "Verified (Death Certificate Validated)"
                mgr_rec["Trigger_Status"] = "Death Triggered & Authorized"
                mgr_rec["Denial_Reason"] = ""
                st.success(f"Nomination {mgr_rec['Nomination_ID']} approved! Sequential gates are now automatically cleared, and nominee proxy rights execution is unlocked.")
                st.rerun()
                
        with col_btn2:
            st.markdown("#### ❌ Issue Statutory Denial Notice")
            default_denial_draft = (
                "The adjudicating authority has reviewed the submission under Section 14 of the DPDPA 2023 and determined that the evidentiary documentation provided lacks sufficient legal verification (such as a certified government-issued Death Certificate or valid judicial guardianship order) establishing valid statutory nexus. "
                "Consequently, the claim stands rejected. In accordance with the statutory grievance redressal mechanism under Section 32 of the DPDPA 2023, if the claimant disputes this determination or wishes to adduce additional evidence, they may formally escalate the matter to the designated Enterprise Grievance Officer at grievance.officer@enterprise.in."
            )
            denial_reason_input = st.text_area(
                "Draft Legal Reason for Denial", 
                value=default_denial_draft,
                key="denial_text_area"
            )
            
            if st.button("📨 Issue Formal Denial Notice to Nominee", key="mgr_reject_btn"):
                mgr_rec["Verification_State"] = "Rejected"
                mgr_rec["Trigger_Status"] = "Claim Rejected by Compliance"
                mgr_rec["Denial_Reason"] = denial_reason_input
                
                st.error(f"✅ **Statutory Denial Notice Successfully Issued & Dispatched!**\n- **Recipient Nominee Email:** `{mgr_rec['Nominee_Email']}`\n- **Status:** Formal denial record and grievance escalation path transmitted to nominee portal.")
    else:
        st.info("👆 Please select a nomination record from the dropdown above to load the adjudication workbench.")
