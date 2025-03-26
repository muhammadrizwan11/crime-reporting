# import json
# import streamlit as st
# from datetime import datetime

# class CrimeReporting:
#     @staticmethod
#     def load_reports():
#         """Load crime reports from JSON file."""
#         try:
#             with open('crime_reports.json', 'r') as f:
#                 content = f.read().strip()
#                 # If file is empty, return an empty list
#                 if not content:
#                     return []
#                 return json.loads(content)
#         except (FileNotFoundError, json.JSONDecodeError):
#             # Create an empty file if it doesn't exist or is invalid
#             with open('crime_reports.json', 'w') as f:
#                 json.dump([], f)
#             return []
    
#     @staticmethod
#     def save_report(report):
#         """Save a new crime report to JSON file."""
#         reports = CrimeReporting.load_reports()
        
#         # Add timestamp to the report
#         report['timestamp'] = datetime.now().isoformat()
        
#         # Generate a unique ID
#         report['id'] = len(reports) + 1
        
#         reports.append(report)
        
#         with open('crime_reports.json', 'w') as f:
#             json.dump(reports, f, indent=4)
        
#         st.success("Crime report submitted successfully!")
    
#     @staticmethod
#     def view_reports():
#         """View all crime reports."""
#         reports = CrimeReporting.load_reports()
        
#         if not reports:
#             st.info("No crime reports found.")
#             return
        
#         st.header("Crime Reports")
        
#         # Create columns for report details
#         for report in reports:
#             with st.expander(f"Report #{report['id']} - {report.get('crime_type', 'Unknown Crime')}"):
#                 col1, col2 = st.columns(2)
                
#                 with col1:
#                     st.write(f"**Crime Type:** {report.get('crime_type', 'N/A')}")
#                     st.write(f"**Location:** {report.get('location', 'N/A')}")
#                     st.write(f"**Date of Incident:** {report.get('incident_date', 'N/A')}")
                
#                 with col2:
#                     st.write(f"**Description:** {report.get('description', 'N/A')}")
#                     st.write(f"**Reported At:** {report['timestamp']}")
                
#                 st.divider()



import json
import streamlit as st
from datetime import datetime

class CrimeReporting:
    @staticmethod
    def load_reports():
        """Load crime reports from JSON file."""
        try:
            with open('crime_reports.json', 'r') as f:
                content = f.read().strip()
                # If file is empty, return an empty list
                if not content:
                    return []
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            # Create an empty file if it doesn't exist or is invalid
            with open('crime_reports.json', 'w') as f:
                json.dump([], f)
            return []
    
    @staticmethod
    def save_report(report):
        """Save a new crime report to JSON file."""
        reports = CrimeReporting.load_reports()
        
        # Add timestamp to the report
        report['timestamp'] = datetime.now().isoformat()
        
        # Generate a unique ID
        report['id'] = len(reports) + 1
        
        reports.append(report)
        
        with open('crime_reports.json', 'w') as f:
            json.dump(reports, f, indent=4)
        
        st.success("Crime report submitted successfully!")
    
    @staticmethod
    def view_reports():
        """View all crime reports with enhanced display."""
        reports = CrimeReporting.load_reports()
        
        if not reports:
            st.info("No crime reports found.")
            return
        
        st.header("Crime Reports")
        
        # Create columns for report details
        for report in reports:
            # Color-code based on severity
            severity = report.get('severity', 5)
            if severity <= 3:
                color = "green"
            elif severity <= 6:
                color = "orange"
            else:
                color = "red"
            
            with st.expander(f"Report #{report['id']} - {report.get('crime_type', 'Unknown Crime')}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Crime Type:** {report.get('crime_type', 'N/A')}")
                    st.write(f"**Location:** {report.get('location', 'N/A')}")
                    st.write(f"**Date of Incident:** {report.get('incident_date', 'N/A')}")
                
                with col2:
                    st.write(f"**Description:** {report.get('description', 'N/A')}")
                    st.write(f"**Reported At:** {report['timestamp']}")
                    st.markdown(f"**Severity:** <span style='color:{color}'>{severity}/10</span>", unsafe_allow_html=True)
                
                st.divider()
