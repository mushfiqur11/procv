import openai
from starlette.config import Config
import os

openai.api_key = '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'

# config = Config('../.env')
# config_dict = config.__dict__.get('file_values')

# access_key = str(config_dict['OPENAI_ACCESS_KEY'])

# abstracts = ['''Video captioning, ie, the task of generating captions from video sequences creates a bridge between the Natural Language Processing and Computer Vision domains of computer science. The task of generating a semantically accurate description of a video is quite complex. Considering the complexity, of the problem, the results obtained in recent research works are praiseworthy. However, there is plenty of scope for further investigation. This paper addresses this scope and proposes a novel solution. Most video captioning models comprise two sequential/recurrent layers—one as a video-to-context encoder and the other as a context-to-caption decoder. This paper proposes a novel architecture, namely Semantically Sensible Video Captioning (SSVC) which modifies the context generation mechanism by using two novel approaches—“stacked attention” and “spatial hard pull”. As there are no exclusive metrics for evaluating video captioning models, we emphasize both quantitative and qualitative analysis of our model. Hence, we have used the BLEU scoring metric for quantitative analysis and have proposed a human evaluation metric for qualitative analysis, namely the Semantic Sensibility (SS) scoring metric. SS Score overcomes the shortcomings of common automated scoring metrics. This paper reports that the use of the aforementioned novelties improves the performance of state-of-the-art architectures.''',
#              '''Image restoration deals with the removal of noise, blurriness, missing patches, and other kinds of distortions in broken images. Traditional reconstruction and restoration approaches suffer from different kinds of limitations. In our work, we have improved upon those models by introducing novel structure loss that emphasizes the overall image structure rather than individual pixels. Our proposed model StructGAN can achieve a higher SSIM (Structural Similarity Index Measure) score while not massively compromising other noise metrics. Overall, our proposed model uses generative adversarial networks with a two-step generator network, a dual discriminator network, and coherent semantic attention (CSA) layer. The two-step generator helps refine the output. The dual discriminator ensures local and global correctness. The CSA layer ensures semantic consistency. Along with these, our model incorporates the novel structure loss. The structure loss is based on the Laplacian filter that calculates the overall structure-map of the image and tries to replicate the structure-map in the generation step. The results obtained by our model are qualitatively comparable to the performance of the state-of-the-art models. For certain metrics, e.g. SSIM, StructGAN quantitatively outperforms other models.'''

# ]
# job_desc = '''Required:
# Demonstrated proficiency working with data collection, processing, and statistical analysis in Python, with preference for experience using SQL and Python Pandas library.
# Experience using Tableau, Looker, D3, Python or similar tools to visualize complex data for both fellow data scientists and non-technical audiences.
# Commitment to advancing racial and gender equity in work
# Curiosity about emerging research and advocacy in the criminal justice space
# Wrestles with creative and concrete ways to use data to shift power and advance equity and inclusion

# Preferred:
# Professional, personal or academic engagement with issues of mass incarceration and mass criminalization'''


# prompt = f'''The following is a list of abstracts of my research work followed by a job description from a company. For each of these work experiences, generate separate concise summaries with active words so that I can put them in my CV for this job. Use first person where necessary. Also provide a generaal summary. Your response should be a python dictionary
# "{abstracts}"
# "{job_desc}"
# '''






def get_workexp_summary(work_exp, job_prompt):
    model = "text-davinci-003"
    prompt = f'''The following is a list of abstracts of my research work followed by a job description from a company. For each of these work experiences, generate separate concise summaries with active words so that I can put them in my CV for this job (Choose the most relevant experiences only). Use first person where necessary. Also provide a generaal summary. Your response should be a python dictionary.
    "{work_exp}"
    "{job_prompt}"
    '''
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    summary = response.choices[0].text
    print(summary)
    return summary

def generate_pdf(summary):
    model = "text-davinci-003"
    prompt = f'''From the following summary, generate an HTML with portfolio format {summary}
    '''
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    html = response.choices[0].text

    return html