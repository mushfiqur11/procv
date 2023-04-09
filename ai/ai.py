import openai
from starlette.config import Config

config = Config('.env')
config_dict = config.__dict__.get('file_values')

access_key = str(config_dict['OPENAI_ACCESS_KEY'])

prompt = '''The following is a description of my work followed by a job description. Summarize my work description fitting this job's description. 
""

"Required:
Demonstrated proficiency working with data collection, processing, and statistical analysis in Python, with preference for experience using SQL and Python Pandas library.
Experience using Tableau, Looker, D3, Python or similar tools to visualize complex data for both fellow data scientists and non-technical audiences.
Commitment to advancing racial and gender equity in work
Curiosity about emerging research and advocacy in the criminal justice space
Wrestles with creative and concrete ways to use data to shift power and advance equity and inclusion

Preferred:
Professional, personal or academic engagement with issues of mass incarceration and mass criminalization"
'''

model = "text-davinci-002"
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.5,
)

summary = response.choices[0].text
print(summary)