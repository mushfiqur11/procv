import openai
from starlette.config import Config
import os

openai.api_key = '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'

# config = Config('../.env')
# config_dict = config.__dict__.get('file_values')

# access_key = str(config_dict['OPENAI_ACCESS_KEY'])

abstract = '''Video captioning, ie, the task of generating captions from video sequences creates a bridge between the Natural Language Processing and Computer Vision domains of computer science. The task of generating a semantically accurate description of a video is quite complex. Considering the complexity, of the problem, the results obtained in recent research works are praiseworthy. However, there is plenty of scope for further investigation. This paper addresses this scope and proposes a novel solution. Most video captioning models comprise two sequential/recurrent layers—one as a video-to-context encoder and the other as a context-to-caption decoder. This paper proposes a novel architecture, namely Semantically Sensible Video Captioning (SSVC) which modifies the context generation mechanism by using two novel approaches—“stacked attention” and “spatial hard pull”. As there are no exclusive metrics for evaluating video captioning models, we emphasize both quantitative and qualitative analysis of our model. Hence, we have used the BLEU scoring metric for quantitative analysis and have proposed a human evaluation metric for qualitative analysis, namely the Semantic Sensibility (SS) scoring metric. SS Score overcomes the shortcomings of common automated scoring metrics. This paper reports that the use of the aforementioned novelties improves the performance of state-of-the-art architectures.'''

job_desc = '''Required:
Demonstrated proficiency working with data collection, processing, and statistical analysis in Python, with preference for experience using SQL and Python Pandas library.
Experience using Tableau, Looker, D3, Python or similar tools to visualize complex data for both fellow data scientists and non-technical audiences.
Commitment to advancing racial and gender equity in work
Curiosity about emerging research and advocacy in the criminal justice space
Wrestles with creative and concrete ways to use data to shift power and advance equity and inclusion

Preferred:
Professional, personal or academic engagement with issues of mass incarceration and mass criminalization'''


prompt = f'''The following is an abstract of my research work followed by a job description from a company. Summarize my research work for a CV fitting this job's description. Use strong active words that are good for resume and goes with this experience. Use first person where necessary. Do not make up new skills that has not been mentioned.
"{abstract}"
"{job_desc}"
'''

model = "text-davinci-002"
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

summary = response.choices[0].text
print(summary)