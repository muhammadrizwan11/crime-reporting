# import streamlit as st
# from auth import Authentication
# from crime_report import CrimeReporting

# def login_page():
#     """Login page interface."""
#     st.title("Crime Reporting System - Login")
    
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if st.button("Login"):
#             if Authentication.login_user(username, password):
#                 st.session_state.logged_in = True
#                 st.session_state.username = username
#                 st.rerun()
    
#     with col2:
#         if st.button("Register New Account"):
#             st.session_state.show_registration = True
#             st.rerun()

# def registration_page():
#     """User registration interface."""
#     st.title("Crime Reporting System - Registration")
    
#     new_username = st.text_input("Choose a Username")
#     new_password = st.text_input("Create a Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if st.button("Create Account"):
#             if new_password != confirm_password:
#                 st.error("Passwords do not match!")
#             elif not new_username or not new_password:
#                 st.error("Username and password cannot be empty!")
#             else:
#                 if Authentication.register_user(new_username, new_password):
#                     st.session_state.show_registration = False
#                     st.rerun()
    
#     with col2:
#         if st.button("Back to Login"):
#             st.session_state.show_registration = False
#             st.rerun()

# def crime_reporting_page():
#     """Crime reporting interface."""
#     st.title(f"Crime Reporting - Welcome, {st.session_state.username}")
    
#     # Crime reporting form
#     with st.form("crime_report_form"):
#         crime_type = st.selectbox("Type of Crime", [
#             "Theft", "Assault", "Burglary", "Fraud", 
#             "Cybercrime", "Other"
#         ])
        
#         location = st.text_input("Location of Incident")
#         incident_date = st.date_input("Date of Incident")
#         description = st.text_area("Detailed Description")
        
#         submitted = st.form_submit_button("Submit Report")
        
#         if submitted:
#             # Prepare report dictionary
#             report = {
#                 "crime_type": crime_type,
#                 "location": location,
#                 "incident_date": str(incident_date),
#                 "description": description
#             }
            
#             # Save the report
#             CrimeReporting.save_report(report)

# def view_reports_page():
#     """Page to view existing crime reports."""
#     st.title("Existing Crime Reports")
#     CrimeReporting.view_reports()

# def main():
#     """Main application controller."""
#     # Initialize session state variables
#     if 'logged_in' not in st.session_state:
#         st.session_state.logged_in = False
#     if 'show_registration' not in st.session_state:
#         st.session_state.show_registration = False
    
#     # Sidebar for navigation when logged in
#     if st.session_state.logged_in:
#         menu = st.sidebar.radio("Navigation", 
#             ["Report Crime", "View Reports", "Logout"]
#         )
        
#         if menu == "Report Crime":
#             crime_reporting_page()
#         elif menu == "View Reports":
#             view_reports_page()
#         elif menu == "Logout":
#             st.session_state.logged_in = False
#             st.rerun()
#     else:
#         # Show login or registration page
#         if st.session_state.show_registration:
#             registration_page()
#         else:
#             login_page()

# if __name__ == "__main__":
#     # Page configuration
#     st.set_page_config(
#         page_title="Crime Reporting System", 
#         page_icon="🚨",
#         layout="wide"
#     )
    
#     main()



import streamlit as st
from auth import Authentication
from crime_report import CrimeReporting

def login_page():
    """Login page interface with enhanced styling."""
    st.markdown("""
    <style>
    .login-title {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #3498db;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #bdc3c7;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='login-title'>🚨 Crime Reporting System - Login</h1>", unsafe_allow_html=True)
    
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Login"):
            if Authentication.login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
    
    with col2:
        if st.button("Register New Account"):
            st.session_state.show_registration = True
            st.rerun()

def registration_page():
    """User registration interface with enhanced styling."""
    st.markdown("""
    <style>
    .registration-title {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2ecc71;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #27ae60;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #bdc3c7;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='registration-title'>🔐 Crime Reporting System - Registration</h1>", unsafe_allow_html=True)
    
    new_username = st.text_input("Choose a Username", placeholder="Enter a unique username")
    new_password = st.text_input("Create a Password", type="password", placeholder="Enter a strong password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Create Account"):
            if new_password != confirm_password:
                st.error("Passwords do not match!")
            elif not new_username or not new_password:
                st.error("Username and password cannot be empty!")
            else:
                if Authentication.register_user(new_username, new_password):
                    st.session_state.show_registration = False
                    st.rerun()
    
    with col2:
        if st.button("Back to Login"):
            st.session_state.show_registration = False
            st.rerun()

def crime_reporting_page():
    """Enhanced crime reporting interface with additional resources."""
    st.markdown(f"<h1 style='color: #2c3e50;'>🚨 Crime Reporting - Welcome, {st.session_state.username}</h1>", unsafe_allow_html=True)
    
    # Government Reporting Resources
    st.markdown("### 🏛️ Official Crime Reporting Resources")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Federal Investigation Agency (FIA)")
        st.markdown("[Report to FIA Online](https://www.fia.gov.pk/complaints_dept)", unsafe_allow_html=True)
        st.info("Official portal for reporting federal-level crimes")
    
    with col2:
        st.markdown("#### Bahawalnagar Police District")
        st.markdown("""
        **Contact Details:**
        - Phone: 063-9240053
        - Fax: 063-9240077
        - E-mail: dpo.bwn@punjabpolice.gov.pk
        """)
    
    st.divider()
    
    # Crime reporting form
    with st.form("crime_report_form"):
        st.markdown("## 📝 Submit Crime Report")
        
        crime_type = st.selectbox("Type of Crime", [
            "Theft", "Assault", "Burglary", "Fraud", 
            "Cybercrime", "Other"
        ])
        
        location = st.text_input("Location of Incident")
        incident_date = st.date_input("Date of Incident")
        description = st.text_area("Detailed Description")
        
        # Optional: Severity rating
        severity = st.slider("Incident Severity", 1, 10, 5, help="1 being least severe, 10 being most severe")
        
        submitted = st.form_submit_button("Submit Report")
        
        if submitted:
            # Prepare report dictionary with severity
            report = {
                "crime_type": crime_type,
                "location": location,
                "incident_date": str(incident_date),
                "description": description,
                "severity": severity
            }
            
            # Save the report
            CrimeReporting.save_report(report)

def view_reports_page():
    """Enhanced page to view existing crime reports."""
    st.markdown("<h1 style='color: #2c3e50;'>📋 Existing Crime Reports</h1>", unsafe_allow_html=True)
    
    CrimeReporting.view_reports()
    
    # Optional: Filter or search functionality can be added here
    st.sidebar.header("Filter Reports")
    filter_type = st.sidebar.selectbox("Filter by Crime Type", 
        ["All", "Theft", "Assault", "Burglary", "Fraud", "Cybercrime", "Other"]
    )

def main():
    """Main application controller."""
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'show_registration' not in st.session_state:
        st.session_state.show_registration = False
    
    # Sidebar styling
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f1f2f6;
    }
    .sidebar .sidebar-content .stRadio>div {
        background-color: white;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar for navigation when logged in
    if st.session_state.logged_in:
        menu = st.sidebar.radio("Navigation", 
            ["Report Crime", "View Reports", "Logout"]
        )
        
        if menu == "Report Crime":
            crime_reporting_page()
        elif menu == "View Reports":
            view_reports_page()
        elif menu == "Logout":
            st.session_state.logged_in = False
            st.rerun()
    else:
        # Show login or registration page
        if st.session_state.show_registration:
            registration_page()
        else:
            login_page()

if __name__ == "__main__":
    # Page configuration with enhanced styling
    st.set_page_config(
        page_title="Crime Reporting System", 
        page_icon="🚨",
        layout="wide"
    )
    
    main()
