import streamlit as st
from auth import Authentication
from crime_report import CrimeReporting

def login_page():
    """Login page interface."""
    st.title("Crime Reporting System - Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
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
    """User registration interface."""
    st.title("Crime Reporting System - Registration")
    
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Create a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
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
    """Crime reporting interface."""
    st.title(f"Crime Reporting - Welcome, {st.session_state.username}")
    
    # Crime reporting form
    with st.form("crime_report_form"):
        crime_type = st.selectbox("Type of Crime", [
            "Theft", "Assault", "Burglary", "Fraud", 
            "Cybercrime", "Other"
        ])
        
        location = st.text_input("Location of Incident")
        incident_date = st.date_input("Date of Incident")
        description = st.text_area("Detailed Description")
        
        submitted = st.form_submit_button("Submit Report")
        
        if submitted:
            # Prepare report dictionary
            report = {
                "crime_type": crime_type,
                "location": location,
                "incident_date": str(incident_date),
                "description": description
            }
            
            # Save the report
            CrimeReporting.save_report(report)

def view_reports_page():
    """Page to view existing crime reports."""
    st.title("Existing Crime Reports")
    CrimeReporting.view_reports()

def main():
    """Main application controller."""
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'show_registration' not in st.session_state:
        st.session_state.show_registration = False
    
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
    # Page configuration
    st.set_page_config(
        page_title="Crime Reporting System", 
        page_icon="🚨",
        layout="wide"
    )
    
    main()