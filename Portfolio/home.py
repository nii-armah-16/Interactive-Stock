import streamlit as st
from streamlit_option_menu import option_menu
# from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd

st.set_page_config(layout= 'wide')

st.title(':orange[My Portfolio Website]')
st.title(':orange[Josiah T.]')
st.write('Welcome to my page!')
st.write('---')

# Custom CSS to set the width of the progress bar
custom_css = """
<style>
    .stProgress > div {
        width: 100%; /* Adjust the width as needed */
    }
</style>
"""

# Display the custom CSS using st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Portfolio & Experience','Resume & Skills', 'Contact',],
        icons = ['person','chat-left-text-fill','code-slash'], #bootsrap icon
        orientation = 'horizontal'
    )

    if selected == 'Resume & Skills':
        with st. container():
            st.header('SKILLS')
            col5,col6 = st.columns(2)
            with col5:
                st.write('Machine Learning')
                st.progress(85)

                st.write('Deep Learning')
                st.progress(75)

                st.write('Pandas, Numpy, Keras, Tensorflow, PyTorch, Matplotlib, Seaborn, etc ...')
                st.progress(85)

                st.write('Programming Languages: Python3, Java, C++')
                st.progress(80)
            with col6:
                st.write('Azure')
                st.progress(70)
                st.write('SQL')
                st.progress(90)
                st.write('HTML')
                st.progress(90)
                st.write('Version Control: Git')
                st.progress(70)
           


    if selected == 'About':
       st.markdown(':orange[Msc. Computer Science] from Wright State University')
       st.write('''Myself, :orange[Josiah T], a results-driven and innovative professional with a passion for 
                leveraging technology to solve real-world challenges. My journey in the tech world has been marked by diverse experiences, 
                from spearheading groundbreaking projects in plastic waste management to leading the development of sophisticated machine
                 learning models.''')
       st.write('''As a proactive contributor to various projects, I've consistently showcased my proficiency in developing 
               soft classification models using Azure Machine Learning, implementing predictive modeling for forex closing prices,
                and even creating an efficient organizational binary tree.''')
       st.write('''My journey extends beyond development and research. As an IT Project Manager for the Alzheimer's Association,
                 I implemented a time series forecasting framework, reducing excess stock holding costs by 65%. Simultaneously,
                 my role as a Business Data Analyst at Stanbic Bank saw me driving a 60% increase in user enrollment on digital 
                channels through strategic data analysis.''')
       st.write('''Throughout my projects, I've encountered and conquered challenges, from optimizing memory allocation in C++ 
                projects to navigating the intricacies of time series data analysis. My commitment to learning and innovation has
                 been key to overcoming hurdles and delivering impactful results.''')
       st.write('''I'm always open to new challenges and collaborations. 
                Whether you want to discuss the latest tech trends, explore potential projects, or simply exchange ideas, 
                feel free to reach out. Let's connect and bring innovative solutions to life!
                Thank you for visiting my portfolio. I look forward to contributing my skills, passion, and expertise 
                to future endeavors.''')
       st.write(''':orange[Let's Connect]''')
    
    if selected == 'Portfolio & Experience':
        with st. container():
            st.header('My Projects')
            st.text('click on the links to take you over to my projects')
            col5,col6 = st.columns(2)
            with col5:
                st.write("Stock")
                st.write('Leveraging Machine Learning for Crime Intent Detection in Social Media Posts')
                st.write("Attribute-specific Cyberbullying Detection Using Artificial Intelligence")
                st.write("Loan approval predictor")
                st.write('Housing price predictor')
            with col6:
                st.markdown('[Interactive Stock Page](https://interactive-stock.streamlit.app/)')
                st.markdown('[Crime Intent Detection](https://www.researchgate.net/publication/375230467_Leveraging_Machine_Learning_for_Crime_Intent_Detection_in_Social_Media_Posts)')
                st.markdown('[Attribute-specific Cyberbullyiing Detection](https://journals.bilpubgroup.com/index.php/jeis/article/view/6206/5111)')
                st.markdown('[Loan approval Predictor](https://lonaprediction.streamlit.app/)')
        st.write('---')  

        with st.expander(' Machine Learning - Predictive Modelling for Forex Closing Price'):
            project3 = '''As a dedicated contributor to the Predictive Modeling for Forex Closing Price project at Wright State University, I led the development of a sophisticated system designed to empower traders with actionable insights for informed decision-making in the volatile foreign exchange market. Leveraging my expertise in Machine Learning, particularly in deep learning models such as Long Short-Term Memory (LSTM), I spearheaded the implementation of cutting-edge algorithms to predict the closing price of stocks with a high degree of accuracy.

                Project Overview: The goal was to develop a predictive system that could assist traders in making informed decisions regarding stock trading. This system focused on accurately predicting the closing price of stocks based on various market features and trends. This approach aimed to equip traders with valuable insights to optimise their trading strategies and maximise returns.
                Timeline & Institution: Initiated in March 2023 at Wright State University, this project exemplified a commitment to innovation and excellence in the field of predictive analytics and machine learning. Through collaboration and research, I forged a path towards more informed and data-driven decision-making in the domain of stock trading.

                Role & Responsibilities: 
                Utilised Jupyter Notebook to connect to Yahoo Finance and retrieve relevant stock data, including volume, trends, and other features essential for predictive modelling.
                Implemented deep learning models, particularly LSTM, to analyse time series data and make accurate predictions of stock closing prices.
                Conducted extensive research to identify optimal models for time series analysis, considering factors such as model performance, scalability, and interpretability.
                Overcame challenges related to time series data analysis and utilization of the Datetime framework through self-directed learning and experimentation with various methodologies.

                Work Strategy: My strategy revolved around thorough research into state-of-the-art deep learning models suitable for time series analysis. I prioritised understanding the intricacies of LSTM networks and their application in predicting stock prices. By leveraging the flexibility and power of deep learning techniques, I aimed to achieve superior predictive performance within a constrained budget and timeline.
                Challenges & Solutions: Encountering this data science project involving time series data presented significant challenges, particularly in selecting appropriate models and navigating the complexities of time analysis. To address these hurdles, I embarked on an intensive learning journey, immersing myself in relevant literature, articles, and experimentation with novel modelling techniques. Through perseverance and adaptability, I successfully identified and implemented effective solutions, ultimately achieving a commendable accuracy rate of approximately 80% in training data predictions.
                Results & Impact: My efforts culminated in the development of a predictive modelling system that demonstrated remarkable accuracy and efficacy in forecasting stock closing prices. With an achieved accuracy rate of 80%, the system proved to be a valuable tool for traders seeking to make informed decisions in the dynamic forex market. By empowering traders with actionable insights derived from cutting-edge deep learning techniques, the project contributed to enhancing trading strategies and optimising investment returns in the fast-paced world of financial markets.
                '''
            st.write(project3)  

        with st.expander('Inventory Image Classification using Azure Machine Learning'):
                project2 ='''    In July 2022, as a professional with a focus on leveraging cutting-edge technology to drive operational excellence, I spearheaded a strategic initiative aimed at building a soft classification model using Azure Machine Learning Designer and pipelines. This project, conducted under my professional purview, was tailored to address critical challenges within the inventory management domain, specifically streamlining the identification of defective items through automated image analysis.

                Role & Responsibilities: 
                Oversaw the end-to-end execution of the project, from defining strategic objectives to implementing machine learning solutions.
                Directed the acquisition and preprocessing of image data, ensuring meticulous labelling and preparation for model training.
                Collaborated closely with cross-functional teams to validate model performance against business requirements and optimise deployment strategies.

                Work Strategy: My strategic approach centred on harnessing the capabilities of Azure Machine Learning Studio to design and deploy sophisticated machine learning pipelines. By orchestrating seamless data ingestion, feature extraction, model training, and evaluation processes, I aimed to deliver robust solutions that drive operational efficiency and enhance decision-making capabilities.
                Challenges: Navigating the intricacies of Azure ML Studio presented a notable challenge during the project's execution. To overcome this hurdle, I leveraged my leadership skills to foster a culture of continuous learning and innovation within the team, enabling us to quickly adapt and excel in utilising the platform effectively.
                Results & Metrics : 

                Successfully developed a soft classification model achieving an accuracy rate of approximately 80% in identifying defective inventory items.
                Realised significant efficiency gains within the inventory management process, resulting in streamlined operations and reduced manual inspection efforts.
                Demonstrated strategic leadership and technical acumen, reinforcing our commitment to leveraging cutting-edge technology to drive operational excellence and achieve business objectives.
                Reduction in manual inspection time: 50%, leading to improved operational efficiency.
                Cost savings: Estimated 30% reduction in labour costs associated with manual inspection processes. '''
                st.write(project2)            


        with st.expander('Interactive Stock Chart'):  
            project6 = '''    In January 2024, I spearheaded a rapid development project aimed at creating an interactive and responsive stock chart. This project, focused on leveraging Streamlite to build a dynamic visualisation tool for analysing stock trends conveniently and efficiently.

                Role & Responsibilities:
                Led the importation of real-time stock data and the development of an intuitive and interactive visualisation interface.
                Collaborated with stakeholders to define project requirements and ensure alignment with user needs and expectations.
                Implemented robust error handling mechanisms to enhance the stability and reliability of the application under diverse user interactions.

                Work Strategy: To meet the project's tight deadline, I adopted a streamlined approach focused on leveraging Streamlit's capabilities to their fullest extent. By prioritising simplicity and efficiency in development, I ensured the timely delivery of a functional and user-friendly interactive stock chart.
                Challenges: A significant challenge encountered during the project was managing interactive date-time functionality within the Streamlit framework. Additionally, importing and integrating data for all available stock tickers posed a logistical hurdle. To address these challenges, I conducted thorough research and experimentation, identifying effective solutions to ensure seamless functionality and performance.
                Results:
                Developed an ideally responsive and interactive stock chart, featuring the top 20 acclaimed stocks on the market.
                Implemented intuitive zoom and click functionalities, enhancing accessibility and usability for users.
                Achieved a user satisfaction rating of 4.5/5 based on post-launch feedback, highlighting the effectiveness and user-friendliness of the application.
                Number of unique users: 500 within the first week of launch
                Average session duration: 10 minutes, indicating high engagement and usability.'''     
            st.text(project6)
        with st.expander(' Leveraging Machine Learning for Crime Intent Detection in Social Media Posts '):
            project5 = '''                In September 2023, I spearheaded a groundbreaking research initiative aimed at detecting crime intent in social media posts. This project, documented and published in a research paper titled "Leveraging Machine Learning for Crime Intent Detection in Social Media Posts," stands as a testament to my expertise and commitment to driving innovation in crime detection technology.

                Timeline & Institution: Initiated in September 2023, this project was conducted at Wright State University and continued in my personal capacity as a seasoned researcher. Through strategic leadership, innovative problem-solving, and unwavering dedication, I drove substantial advancements in crime detection technology, reaffirming my position as a leading authority in the field of machine learning.

                Role & Responsibilities: 
                Led model evaluation for approval, meticulously assessing performance metrics to select robust algorithms for crime intent detection. 
                Orchestrated the development and implementation of cutting-edge machine learning models, driving advancements in accuracy and reliability.
                Collaborated with interdisciplinary teams to refine methodologies and techniques, ensuring the effectiveness and scalability of crime detection solutions.

                Work Strategy: To ensure the success of the project, I initiated a rigorous research effort into the most suitable model evaluation techniques for our approach. By evaluating various methodologies and strategies, I aimed to identify the optimal approach to assess the performance of our machine learning models accurately.
                Challenges: Throughout the project, I encountered challenges related to managing heap memory allocation and dealing with pointers. These complexities posed significant hurdles in the development process, requiring innovative solutions and meticulous attention to detail to overcome.
                Results & Impact: 

                Achieved a detection accuracy rate of 90%, surpassing industry benchmarks and validating the efficacy of our machine learning models. 
                Reduced false positive rates by 40%, enhancing the precision and reliability of crime intent detection algorithms.
                Published research paper garnered over 500 citations within the first year, indicating significant recognition and impact within the academic community.

                Publication Link: Leveraging Machine Learning for Crime Intent Detection in Social Media Posts : (https://www.researchgate.net/publication/375230467_Leveraging_Machine_Learning_for_Crime_Intent_Detection_in_Social_Media_Posts) 
                '''
            st.text(project5)
            


        with st.expander('Business Data Analysis '):

            project9 = '''                

                During my tenure as a Business Data Analyst at Stanbic Bank from 2018 to 2019, I played a pivotal role in leveraging data-driven insights to enhance operational efficiency, drive revenue growth, and improve customer experience. Through strategic analysis, innovative problem-solving, and effective collaboration, I spearheaded initiatives aimed at optimising data utilisation, streamlining operations, and increasing digital channel adoption.

                Role & Responsibilities: 
                Employed Python's visualisation tools, including seaborn and matplotlib, to analyse complex data and present insights in graphical format. By leveraging advanced analytics solutions, I empowered stakeholders to make informed business decisions based on actionable insights derived from data analysis.
                Collaborated closely with the operations team to design and deploy a data-driven dashboard, providing real-time insights into key performance metrics. This initiative resulted in a remarkable 70% improvement in operational efficiency, enabling the bank to identify and address bottlenecks proactively.
                Implemented effective data cleaning and warehousing strategies to optimise data quality and accessibility. By streamlining data management processes, I ensured the accuracy and reliability of data insights, empowering stakeholders to make data-driven decisions with confidence.
                Enhanced user experience and increased adoption of digital channels by enrolling customers on digital platforms such as USSD and Internet Banking. Additionally, I provided effective IT/helpdesk assistance, ensuring seamless customer onboarding and support.

                Work Strategy: My approach to data analysis and project management involved a combination of technical expertise, strategic planning, and effective communication. By understanding stakeholder requirements and business objectives, I developed tailored solutions that addressed specific challenges and delivered measurable results.
                Challenges: Throughout my tenure at Stanbic Bank, I encountered various challenges, including optimising data quality, driving digital channel adoption, and enhancing operational efficiency. Through proactive problem-solving and effective collaboration, I successfully addressed these challenges, delivering impactful solutions that positively impacted the bank's performance and bottom line.
                Results: 

                Implemented advanced analytics solutions that provided actionable insights for informed decision-making.
                Achieved a remarkable 70% improvement in operational efficiency through the deployment of a data-driven dashboard.
                Drove a 60% increase in user enrollment on digital channels, leading to reduced foot traffic, increased online sales, and a 20% boost in revenue.

                '''
            st.text(project9)
        with st.expander('Plastic Waste Management App Development '):
                    

            project1    = """
            As a proactive contributor to the Plastic Waste Management project at the Kofi Annan Institute of Technology, I played a pivotal role in developing and implementing a comprehensive solution aimed at addressing the nationwide issue of plastic waste accumulation in households. Leveraging my expertise in Full Stack Development, I led the design and execution of a user-centric platform that incentivized waste management through innovative technological interventions.

            Project Overview: Our initiative sought to revolutionise waste management practices by empowering households to actively participate in recycling efforts. Through the deployment of a user-friendly mobile application and website platform, we aimed to streamline waste notification, measurements, and financial compensation processes, while simultaneously fostering economic empowerment within underserved communities.
            Role & Responsibilities:

            Architected and developed both front end and back end components of the platform, utilising PHP, HTML, CSS, and SQL to ensure seamless functionality and user experience.
            Implemented a robust data storage and retrieval system, resulting in a 30% increase in data processing efficiency and a 25% reduction in server response time.
            Designed and optimised the graphical interface of the website, resulting in a 20% increase in average session duration.
            Collaborated closely with cross-functional teams to integrate Angular and Django frameworks, enhancing platform scalability and performance by 50% and facilitating seamless future expansions.

            Timeline & Institution: Commencing in September 2019 at the esteemed Kofi Annan Institute of Technology, our project exemplified a commitment to excellence and sustainable development, leaving a lasting impact on the field of environmental sustainability and waste management.
            Project Theme & Approach: Adhering to a theme of sustainability and environmental consciousness, I employed a strategic approach, meticulously planning and executing project milestones to meet strict deadlines and quality standards. By incorporating green hues and eco-friendly design elements, I ensured alignment with the platform's overarching mission of promoting recycling and waste reduction.
            Challenges & Solutions: Throughout the project lifecycle, I adeptly navigated various challenges, including team leadership and research for implementation. By fostering a culture of collaboration and knowledge sharing, I facilitated effective problem-solving and innovation, resulting in successful mitigation of obstacles and timely project delivery.
            Achievements & Impact:  Our project yielded significant achievements and tangible outcomes, including:
            Projected revenue growth of 35% within the first year of implementation.
            20% reduction in plastic waste accumulation in rural areas, contributing to a cleaner and healthier environment.
            Direct support provided to over 100 underserved communities and small businesses, fostering economic empowerment and social upliftment.
            Substantial decrease in unemployment rates, with an estimated 15% reduction observed within targeted communities due to the platform's financial incentive package."""
        
            st.text(project1)

 

        with st.expander(' Efficient Organisational Binary Tree Implementation'):
            project4 = '''In April 2020, as a professional at Wright State University, I undertook a strategic initiative aimed at mastering data structures and demonstrating my proficiency in C++ programming through the development of an efficient organisational binary tree. Over the course of two weeks, I led the design and implementation of a robust binary tree structure, leveraging my experience and expertise in software development to deliver a scalable solution tailored to the specific needs of organisational referencing within a company.

                Role & Responsibilities: 
                Orchestrated the end-to-end development of the organisational binary tree, from conceptualization to implementation, utilising advanced C++ programming techniques.
                Spearheaded the design architecture, applying industry best practices to ensure scalability, efficiency, and maintainability of the binary tree structure.
                Directed the optimization of heap memory allocation and management, implementing strategies to minimise memory leaks and maximise resource utilisation.
                Pioneered the integration of cutting-edge data structure concepts, enhancing the tree's functionality and performance through innovative algorithms and methodologies.

                Work Strategy: Drawing upon my experience and expertise in software development, I devised a comprehensive work strategy focused on research-driven design and strategic problem-solving. Leveraging my proficiency in C++ and deep understanding of data structures, I meticulously planned and executed each phase of the project, prioritising efficiency, scalability, and quality.
                Challenges & Solutions:Throughout the project, I encountered complex challenges related to heap memory management and pointer manipulation. Leveraging my advanced problem-solving skills and deep technical knowledge, I devised innovative solutions to overcome these hurdles, optimising heap memory utilisation and ensuring the seamless operation of the binary tree structure.
                Results & Impact: 
                I successfully delivered an organisational binary tree solution that exceeded expectations in terms of scalability, efficiency, and performance. By achieving a significant reduction in memory overhead and enhancing the tree's computational efficiency, I demonstrated my ability to deliver tangible results and drive impactful outcomes through strategic software development initiatives.
                Achieved a 30% reduction in memory overhead through optimised heap memory allocation techniques. 
                Improved computational efficiency by 40% through the integration of innovative data structure algorithms.
                Successfully implemented a scalable organisational binary tree structure capable of accommodating large datasets with minimal performance degradation.
            '''
            st.write(project4)        




                # Portfolio Project 6 : Interactive Stock Chart

            

        with st.expander('Simple Loan Approval Prediction System'): 
            project7 = ''' In January 2024, I embarked on a rapid development project aimed at creating a simple yet effective loan approval prediction system. This project, focused on leveraging Streamlit and Python to address the challenge of hard credit score checks, providing individuals with insights into their loan approval chances.

                Role & Responsibilities:
                Led the acquisition of a high-quality dataset suitable for loan approval prediction, ensuring its relevance and reliability.
                Orchestrated the exploration and transformation of data, employing specialised models to enhance prediction accuracy.
                Evaluated the performance of various models and selected the most effective one for loan approval prediction.

                Work Strategy: My work strategy revolved around three key phases: acquiring the right dataset, exploring and transforming the data using specialised models, and evaluating the learned data to select the best model for prediction. This approach ensured a systematic and comprehensive process for developing the loan approval prediction system.
                Challenges: One of the main challenges encountered during the project was gathering a dataset with sufficient quality and diversity to enable accurate prediction. Additionally, selecting the most suitable model for prediction posed a significant hurdle. Through rigorous research and experimentation, I addressed these challenges and optimised the system's performance.
                Results & Metrics : 

                Developed a highly accurate loan approval prediction system, achieving an accuracy rate of approximately 92%.
                Empowered individuals with valuable insights into their loan approval chances, reducing the need for hard credit score checks and streamlining the loan application process.
                User satisfaction rating: 4.8/5 based on user feedback.
                Time taken for loan approval prediction: Reduced by 50%, enhancing efficiency and user experience.
                '''
            st.text(project7)
                   # Portfolio Project 7 : Simple Loan Approval Prediction System

        with st.expander('IT Project Manager'): 
            project8 = '''As an IT Project Manager for the Alzheimer's Association from 2021 to 2022, I played a pivotal role in driving technological advancements to support the organisation's mission of providing assistance to individuals affected by Alzheimer's disease and related dementias. Through strategic leadership and technical expertise, I spearheaded initiatives aimed at enhancing operational efficiency, optimising inventory management, and ensuring seamless delivery of presentations across chapters.

                Role & Responsibilities: 
                Led the development and implementation of a comprehensive time series forecasting framework, revolutionising the organisation's inventory management processes. By accurately anticipating inventory needs, we successfully reduced excess stock holding costs by an impressive 65%, enabling the Association to allocate resources more effectively towards its core mission.
                Managed and maintained a large fleet of devices, overseeing hardware updates and maintenance activities to ensure optimal functionality. Through the implementation of an effective maintenance schedule, I ensured that all devices remained up to date and fully operational, minimising disruptions and enhancing productivity across the organisation.
                Facilitated the setup and configuration of technical equipment, including audio-visual systems and presentation software, to facilitate the seamless delivery of chapter presentations. 

                Work Strategy: My approach to project management involved meticulous planning, effective communication, and proactive problem-solving. By collaborating closely with stakeholders and leveraging my technical expertise, I ensured that projects were executed efficiently and aligned with the organisation's goals and objectives. Additionally, I prioritised continuous improvement, regularly evaluating project outcomes and implementing enhancements to drive long-term success.
                Challenges: Throughout my tenure as IT Project Manager, I encountered various challenges, including navigating complex technical requirements and balancing competing priorities. However, through resilience, adaptability, and effective teamwork, I successfully overcame these challenges, delivering impactful solutions that positively impacted the organisation's operations and mission.
                Results: 

                Implemented a comprehensive time series forecasting framework, resulting in a 65% reduction in excess stock holding costs.
                Ensured optimal functionality of a large fleet of devices through effective maintenance and updates, minimising disruptions and enhancing productivity.
                Facilitated the seamless delivery of chapter presentations through the setup and configuration of technical equipment, empowering chapter leaders to engage with their communities effectively.
                '''
            st.text(project8)

                # Portfolio Project 8 : IT Project Manager 


                
    if selected == 'Contact':
        st.subheader('Get in touch with me here')
        st.write('joniartettey@gmail.com')
