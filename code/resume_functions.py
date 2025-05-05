import prompter
import os

from open_interface import ask_gpt, ask_gpt_context
from hacker_news_scraper import get_jobs, scrape_web


def gap_finder(resume, job_desc):
    # Interact with chatGPT
    promt = prompter.focusAreas((job_desc, resume))
    result = ask_gpt_context(promt)

    context = promt + result
    promt = prompter.idGaps3(result)
    result = ask_gpt_context(context, promt)

    context = context + promt + result
    promt = prompter.actAdv3()
    result = ask_gpt_context(context, promt)
    
    path_to_folder = "uploads"
    filename = "gap.txt"
    filename = os.path.join(path_to_folder, filename)
    with open(filename, 'w') as gaps:
       gaps.write(result) 

    return filename
    

def get_recommendations(resume):
    description = ""
    result = []
    n = 0
    for job in get_jobs(): 
        # Retrieve the job data
        if "text" in job.keys():
            content = job["text"] 
        elif "url" in job.keys():
            content = scrape_web(job["url"]) 
        else:
            continue
        answer = ask_gpt(prompter.match((resume, content))) 
        if answer[-4:] == "TRUE":
            description = ask_gpt(f"Please provide me with a description of the following job data: {content}") 
            result.append({
                "title": job["title"],
                "url": job["url"] if "url" in job.keys() else None,
                "description": description,
            })
            if len(result) == 5:
               break
    return (result, n)

def write_cover(resume, job_desc):
    # Interact with chatGPT
    promt = prompter.coverLetter((job_desc, resume))
    result = ask_gpt(promt)
    
    path_to_folder = "uploads"
    filename = "cover_letter.txt"
    filename = os.path.join(path_to_folder, filename)
    with open(filename, 'w') as cover:
       cover.write(result) 

    return filename


def get_projects(resume, job_desc):
    # Interact with chatGPT
    promt = prompter.proposeProject((job_desc, resume))
    result = ask_gpt(promt)
    
    path_to_folder = "uploads"
    filename = "proposed_projects.txt"
    filename = os.path.join(path_to_folder, filename)
    with open(filename, 'w') as cover:
       cover.write(result) 

    return filename

def get_interview_questions_prompt(resume, job_desc):

    # Interact with chatGPT
    promt = prompter.interview((job_desc, resume))
    result = ask_gpt(promt)
    
    path_to_folder = "uploads"
    filename = "interview_q.txt"
    filename = os.path.join(path_to_folder, filename)
    with open(filename, 'w') as cover:
       cover.write(result) 

    return (promt, filename)

def get_interview_performance(context, questions, answers):
    # Interact with chatGPT
    promt = prompter.performance(context, questions, answers)
    result = ask_gpt(promt)
    
    path_to_folder = "uploads"
    filename = "interview_perf.txt"
    filename = os.path.join(path_to_folder, filename)
    with open(filename, 'w') as cover:
       cover.write(result) 

    return filename

    
