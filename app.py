from flask import Flask, render_template
import os

app = Flask(__name__)

# Projects data
projects = [
    {
        'title': 'Ryanair Passenger Reviews Analysis',
        'description': 'Leveraging Natural Language Processing (NLP) techniques to analyze Ryanair passenger reviews from 2012 to 2024. Employing sentiment analysis, topic modeling, and root cause analysis to identify key areas of satisfaction and dissatisfaction.',
        'technologies': ['Python', 'NLP', 'Machine Learning', 'Sentiment Analysis', 'Graph Networks'],
        'report_link': 'https://github.com/jbanerje/jbanerje.github.io/blob/master/projects/Ryain_Air_Passenger_Review/report_and_presentatation/Term_Project_114.pdf',
        'project_link': 'https://github.com/jbanerje/jbanerje.github.io/tree/master/projects/Ryain_Air_Passenger_Review'
    },
    {
        'title': 'Amazon Product Bundling and Recommendation',
        'description': 'Comprehensive analysis of Amazon sales data using data mining techniques for product bundling strategy and customer recommendations. Includes exploratory analysis, clustering, association mining, and predictive modeling.',
        'technologies': ['Data Mining', 'Clustering', 'Association Rules', 'Predictive Modeling'],
        'report_link': 'https://github.com/jbanerje/jbanerje.github.io/blob/master/projects/Amazon_Product_Bundling/report_and_presentatation/ISYE_7406_DSML_Project_Group_115_Final_Report.pdf',
        'project_link': 'https://github.com/jbanerje/jbanerje.github.io/tree/master/projects/Amazon_Product_Bundling'
    },
    {
        'title': 'IntelliFraud: Bank Account Fraud Detection',
        'description': 'An innovative online tool for detecting fraudulent bank account applications, featuring dashboard analytics, graph network analysis, and advanced machine learning techniques.',
        'technologies': ['Machine Learning', 'Graph Networks', 'SHAP', 'ELI5', 'Dashboard Development'],
        'report_link': 'https://github.com/jbanerje/jbanerje.github.io/blob/master/projects/Intellifraud_Bank_Account_Fraud_Detection/final_submission_docs/team028report.pdf',
        'project_link': 'https://github.com/jbanerje/jbanerje.github.io/tree/master/projects/Intellifraud_Bank_Account_Fraud_Detection'
    }
]

# Case Studies data
case_studies = [
    {
        'title': 'Optimizing cancer patient care with advanced analytics',
        'description': 'A comprehensive case study of the Oscar Lambret Center\'s initiative to establish personalized care pathways for cancer patients using advanced analytics.',
        'highlights': [
            'Personalized care pathway development',
            'Multidisciplinary collaboration enhancement',
            'Resource optimization and workforce allocation',
            'Treatment time benchmarking'
        ],
        'report_link': 'https://github.com/jbanerje/jbanerje.github.io/tree/master/case_studies/Optimizing cancer patient care with advanced analytics.pdf',
        'reference_link': 'https://www.sas.com/en_us/customers/oscar-lambret-center.html'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, case_studies=case_studies)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/case_studies')
def case_studies_page():
    return render_template('case_studies.html', case_studies=case_studies)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 