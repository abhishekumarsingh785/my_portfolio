import streamlit as st
from base64 import b64encode
import os

# Page configuration must be the first Streamlit command
st.set_page_config(page_title="Abhishek Kumar Singh's Portfolio", page_icon="⭐", layout="wide")

def load_css(file_name):
    """Load CSS from a file."""
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"CSS file '{file_name}' not found.")

def load_image(image_path):
    """Load and encode an image from a file."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = b64encode(img_file.read()).decode()
            # Determine image type based on extension
            ext = os.path.splitext(image_path)[1].lower()
            if ext == '.png':
                mime = 'image/png'
            elif ext in ['.jpg', '.jpeg']:
                mime = 'image/jpeg'
            elif ext == '.gif':
                mime = 'image/gif'
            else:
                mime = 'image/png'  # Default fallback
            return f"data:{mime};base64,{encoded}"
    else:
        st.error(f"Image file '{image_path}' not found.")
        return ""

def web_portfolio():
    # Load CSS from external file
    load_css("styles.css")
    
    # Navigation Bar
    #st.markdown("""
    #<div class="navbar">
    #    <a href="#about">About Me</a>
    #    <a href="#work-experience">Work Experience</a>
    #    <a href="#projects">Projects</a>
    #    <a href="#certifications">Certifications</a>
    #    <a href="#education">Education</a>
    #    <a href="#skills">Skills</a>
    #    <a href="#download-resume">Download Resume</a>
    #    <a href="#contact-me">Contact Me</a>
    #</div>
   # """, unsafe_allow_html=True)
    
    # Main Content
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Title Section
    profile_img = load_image("profile-pic.png")
    social_icons_data = {
        "LinkedIn": ["https://www.linkedin.com/in/abhishekkumarsingh108/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "GitHub": ["https://github.com/abhishekumarsingh785", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
        "Gmail": ["mailto:abhishekumarsingh785@gmail.com","https://cdn-icons-png.flaticon.com/128/732/732200.png"]
    }
    
    social_icons_html = ''.join([
        f"<a href='{social_icons_data[platform][0]}' target='_blank'>"
        f"<img src='{social_icons_data[platform][1]}' alt='{platform}' class='social-icon'></a>"
        for platform in social_icons_data
    ])
    
    # Prepare download link with base64-encoded PDF
    pdf_path = "resume_abhishek_kumar_singh.pdf"
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()
        b64_pdf = b64encode(pdf_data).decode()
        download_href = f'data:application/octet-stream;base64,{b64_pdf}'
        download_link = f'<a href="{download_href}" download="resume_abhishek_kumar_singh.pdf" class="btn-download">📄 Download My Resume</a>'
    else:
        download_link = "Resume not found."
    
    # Centered Layout using HTML
    st.markdown(f"""
    <div class="title">
        <span style='font-size: 32px;'>Hello! I'm Abhishek Kumar Singh</span> 👋
    </div>
    <div class="subtitle">Data Science and GenAI Engineer</div>
    <div class="centered-container">
        <img src="{profile_img}" class="profile-pic">
        <div class="social-icons">{social_icons_html}</div>
        <div class="cv-download">
            {download_link}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # About Me Section
    st.markdown('<h2 id="about">About Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    - 🧑‍💻 **Seasoned Data Scientist** with over **5+ years of experience** in building machine learning models, statistical forecasting, Generative AI solutions, and deploying scalable data solutions using Python, R, and cloud platforms like Azure.
    - ❤️ **Passionate** about Machine Learning/Deep Learning, MLOps, Data Science, Generative AI, Data Analytics, Data Engineering, Automation, and more!
    - 🪧 **Contact**: Reach me at [abhishekumarsingh785@gmail.com](mailto:abhishekumarsingh785@gmail.com).
    """)
    
    st.markdown("---")
      


    # Work Experience Section
    st.markdown('<h2 id="work-experience">Work Experience</h2>', unsafe_allow_html=True)
    
    # LatentView Analytics Experience
    with st.container():
        st.subheader("Senior Analyst, LatentView Analytics")
        st.write("📍 Chennai, India | 🗓️ Oct 2021 - Jul 2023")
        st.markdown("""
        - Developed and deployed a chatbot using an LLM, hosted on Azure Functions, to convert natural language input into SQLqueries for database retrieval. Built the frontend with Power Platform and integrated it into Power BI.
        - Gathered, extracted, and compiled data from various sources, enhancing data quality through cleaning and linking complex datasets with an 88.5% matching accuracy using Python's fuzzy matching library.
        - Communicated findings and recommendations through detailed reports and interactive dashboards, enhancing stakeholder understanding and driving data-informed decisions.
        - Implemented statistical time series forecasting models (ARIMA, SARIMA, Prophet, Theta) to predict website and app footfall with 94% accuracy, visualizing these forecasts in a Tableau dashboard.
        - Developed K-means clustering models to identify regions with similar customer behaviors, leading to targeted marketing campaigns that increased user engagement by 10%.
        - Analyzed survey data with NLP-based topic modeling techniques and calculated monthly Net Promoter Scores (NPS), identifying key factors that improved customer satisfaction by 8%.
        - Automated data quality monitoring and extraction processes using Hive within the Hadoop ecosystem, saving approximately one week of manual efforts.
        """)
    
    # Cognizant Experience
    with st.container():
        st.subheader("Data Engineer, Cognizant Technology Solutions")
        st.write("📍 Chennai, India | 🗓️ Apr 2019 - Sep 2021")
        st.markdown("""
        - Developed data mapping logics in SQL for data extraction and transformation, implementing a CI/CD pipeline to automate testing and deployment.
        - Built an automated ETL pipeline to handle over 1 billion records, ensuring data integrity and readiness for analysis using Informatica and Azure Data Lake.
        - Collaborated with cross-functional teams worldwide, leveraging Jira for efficient work tracking and project management.
        - Designed and implemented a real-time data health monitoring system to ensure continuous data quality and availability.
        """)
    
    st.markdown("---")
    
    # Projects Section
    st.markdown('<h2 id="projects">Projects</h2>', unsafe_allow_html=True)
    
    projects = [
         {
            "title": "DeepSeek R1: AI That Thinks",
            "description": "DeepSeek R1 Chatbot is a personal AI assistant using the DeepSeek R1 model on Ollama. Built with Streamlit and LangChain, it features an intuitive interface, logical response handling, and advanced reasoning.",
            "github_link": "https://github.com/abhishekumarsingh785/deepseekr1-chatbot",
            "image": "deepseekr1.png"
        },
        {
            "title": "Calorie Calculator App using multimodel LLM deployed on Azure",
            "description": "A multimodal LLM-powered app that calculates calorie intake from food images, provides dietary suggestions, and is deployed on Azure via docker and Azure Container Registry for easy accessibility.",
            "github_link": "https://github.com/abhishekumarsingh785/Calorie_Counter",
            "deployed_link": "https://caloriecalculatorv1.azurewebsites.net/",
            "image": "calorie_calculator.png"
        },
        {
            "title": "A/B Testing for promotional in app notification",
            "description": "The objective of this experiment is to determine if sending an in-app notification promoting the Lamp category leads to an increase in purchases from this category, while monitoring other important metrics like uninstall rate.",
            "github_link": "https://github.com/abhishekumarsingh785/Decco_AB_Testing",
            "image": "ab_testing.png"
        },
        {
            "title": "DataVision - Chat with your data using Agentic RAG",
            "description": "Developed an Agentic RAG-based on a tabular database enabling user interaction for data queries, visualizations, and future predictions.",
            "github_link": "https://github.com/abhishekumarsingh785/DataVision",
            "image": "datavision.png"
        },
        {
            "title": "End-to-End Game Recommendation System",
            "description": "Built an end-to-end game recommendation system using Azure services and deployed the web app via Docker and Azure Container.",
            "github_link": "https://github.com/abhishekumarsingh785/steam-game-recommendation",
            "deployed_link": "https://steamgamerecommend.azurewebsites.net/",
            "image": "end-to-end-flow.png"
        },
        {
            "title": "Agentic Stock Analysis System with AutoGen",
            "description": "This project showcases an Agentic Stock Analysis System, built using Microsoft's AutoGen framework. The system leverages a team of autonomous AI agents to collaboratively analyze stock performance, generate financial reports, and visualize data—all with minimal human intervention.",
            "github_link": "https://github.com/abhishekumarsingh785/financial-analysis-with-agents",
            "image": "autogen.png"
        },
        {
            "title": "Shakesperean Text generator",
            "description": "Built a GPT-2 architecture from scratch, pre-trained on the complete works of Shakespeare using Python and PyTorch.",
            "github_link": "https://github.com/abhishekumarsingh785/llm-from-scratch",
            "image": "llm-from-scratch.png"
        },
        {
            "title": "Job hunting using Agents",
            "description": "This project leverages the power of Large Language Models (LLMs) and APIs to streamline the job-hunting process using agents and crewAI to manage them, making it smarter and more efficient. Designed for individuals looking to save time while exploring opportunities, this system combines intelligent job searching with interview preparation.",
            "github_link": "https://github.com/abhishekumarsingh785/job-hunter",
            "image": "agents.png"
        }


    ]
    
    for project in projects:
        with st.container():
            # Use columns to layout image and description
            col1, col2 = st.columns([1, 3])
            
            with col1:
                project_img = load_image(project["image"])
                if project_img:
                    st.markdown(f'<img src="{project_img}" class="project-img">', unsafe_allow_html=True)
            
            with col2:
                st.subheader(project["title"])
                st.write(project["description"])
                if project.get("github_link"):
                    st.markdown(f"[🔗 GitHub Repository]({project['github_link']})")
                if project.get("deployed_link"):
                    st.markdown(f"[🚀 Live Demo]({project['deployed_link']})")
        st.markdown("")  # Add space between projects
    
    st.markdown("---")
    
    # Certifications Section (Original Layout)
    st.markdown('<h2 id="certifications">Certifications</h2>', unsafe_allow_html=True)
    certifications = [
        {
            "title": "Microsoft Azure Data Scientist Associate",
            "image": "DP-100.png",
            "auth_link": "https://learn.microsoft.com/en-us/users/26182533/credentials/b51113813fc2b17f?ref=https%3A%2F%2Fwww.linkedin.com%2F",
        },
        {
            "title": "Microsoft Power BI Data Analyst Associate",
            "image": "PL-300.png",
            "auth_link": "https://learn.microsoft.com/en-us/users/26182533/credentials/ee5576e9c17a9dc3?ref=https%3A%2F%2Fwww.linkedin.com%2F",
        },
        # Add more certifications as needed
    ]
    
    cols_per_row = 3
    for i in range(0, len(certifications), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, cert in enumerate(certifications[i:i+cols_per_row]):
            with cols[j]:
                cert_img = load_image(cert["image"])
                if cert_img:
                    st.markdown(f"""
                    <a href="{cert['auth_link']}" target="_blank">
                        <img src="{cert_img}" class="certificate-img" alt="{cert['title']}">
                    </a>
                    """, unsafe_allow_html=True)
                    st.caption(cert["title"])
                else:
                    st.write("Image not available")
    
    st.markdown("---")
    
    # Education Section
    st.markdown('<h2 id="education">Education</h2>', unsafe_allow_html=True)
    
    # University at Buffalo, The State University of New York
    with st.container():
        st.subheader("Master's in Data Science")
        st.write("📍 University at Buffalo, The State University of New York | 🗓️ Aug 2023 - Dec 2024")
        st.write("**GPA:** 3.93/4")
    
    # SRM Institute of Science and Technology (SRM IST)
    with st.container():
        st.subheader("Bachelor's in Mechanical Engineering")
        st.write("📍 SRM Institute of Science and Technology, India | 🗓️ Aug 2014 - May 2018")
        st.write("**GPA:** 3.78/4")
    
    st.markdown("---")


    # Skills Section
    st.markdown('<h2 id="skills">Skills</h2>', unsafe_allow_html=True)
    
    skills = {
        "Programming Languages": ["Python", "SQL", "R"],
        "Machine Learning": ["Deep Learning", "Supervised & Unsupervised ML", "Time Series Forecasting", "A/B Testing", "Causal Inference", "NumPy", "Pandas"],
        "Data Engineering": ["Data Pipeline Development", "ETL/ELT Pipelines", "PySpark", "Distributed Data Processing"],
        "Data Visualization": ["Power BI", "Tableau"],
        "Cloud Computing": ["Azure", "AWS", "Git", "Docker", "CI/CD"]
    }
    
    for category, items in skills.items():
        st.markdown(f"<h3>{category}</h3>", unsafe_allow_html=True)
        cols = st.columns(len(items))
        for idx, item in enumerate(items):
            with cols[idx % len(cols)]:
                st.markdown(f"<div class='skill-box'>{item}</div>", unsafe_allow_html=True)
        st.markdown("")
    
    st.markdown("---")
    
    # Download Resume Section (for Navigation)
    st.markdown('<h2 id="download-resume">Download Resume</h2>', unsafe_allow_html=True)
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        # Use the same btn-download class for consistency
        b64_pdf = b64encode(pdf_bytes).decode()
        download_href = f'data:application/octet-stream;base64,{b64_pdf}'
        download_link = f'<a href="{download_href}" download="resume_abhishek_kumar_singh.pdf" class="btn-download">📄 Download My Resume</a>'
        st.markdown(download_link, unsafe_allow_html=True)
    else:
        st.write("Resume not available for download.")
    
    st.markdown("---")
    
    # Contact Me Section
    st.markdown('<h2 id="contact-me">Contact Me</h2>', unsafe_allow_html=True)
    
    contact_info = {
        "Email": {
            "icon": "https://cdn-icons-png.flaticon.com/128/732/732200.png",
            "link": "mailto:abhishekumarsingh785@gmail.com",
            "display": "abhishekumarsingh785@gmail.com"
        },
        "GitHub": {
            "icon": "https://cdn-icons-png.flaticon.com/128/25/25231.png",
            "link": "https://github.com/abhishekumarsingh785",
            "display": "GitHub Profile"
        },
        "LinkedIn": {
            "icon": "https://cdn-icons-png.flaticon.com/128/3536/3536505.png",
            "link": "https://www.linkedin.com/in/abhishekkumarsingh108/",
            "display": "LinkedIn Profile"
        },
    }
    
    for platform, info in contact_info.items():
        st.markdown(f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="{info['icon']}" alt="{platform}" style="width:30px; height:30px; margin-right:10px;">
            <a href="{info['link']}" target="_blank" style="font-size:18px; color: var(--text-color);">{info['display']}</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="subtitle" style="text-align: center; margin-top: 50px;">🌟 Have A Wonderful Day!!! 🌟</div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-content div

if __name__ == "__main__":
    web_portfolio()
