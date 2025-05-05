## Different prompts to be fed into Llama to generate the comparisons
prompts = [
    'Analyze the following job posting and attached resume. Identify key skills mentioned in the job posting, compare the applicant''s job history with the job requirements, and assess to what extent the applicant''s education aligns with the position. Provide insights into how relevant relevant the applicant''s experiences and qualifications are.',
    'Given the mentioned job posting and resume, as well as the following focus areas, try to match the skills mentioned in the job posting with those on the resume. Identify any gaps in the applicant''s skills based on the job requirements. Additionally, assess if the applicant''s past experiences cover the required tasks and responsibilities, pinpointing areas where the experience falls short.',
    'Based on the insights you just shared, provide actionable advice based on the job posting and the applicant''s resume. Clearly identify the applicant''s strengths and shortcomings. Offer constructive suggestions for addressing identified skills and experience gaps. Additionally, recommend specific courses, certifications and resume optimization strategies to enhance the applicant''s chances.',
    'You are now an expert career counselor. Given the applicant''s resume, as well as the job description, execute these 2 steps: 1) {Summarize the applicant''s main strengths and relevant experience} 2) {Write a cover letter for this job opening that strongly conveys the applicant''s skills, passions, and fit for the job. Make sure it is a memorable letter that will catch the recruiter''s eye.',
    'We are analyzing a job applicant''s resume, as well as the description of their target job. You have decades of experience working in this job''s industry. Based on the applicant''s resume, as well as the job description, {identify the applicant''s main strengths, as well as their shortcomings}. Having learned of these strengths and shortcomings, {propose 3 projects that the applicant could add to their portfolio. Each project should be relevant to the job opening and add diversity to the applicant''s experience, helping them meet the job requirements. For each project, make sure to: {include a brief description}, {define at least 5 necessary steps to complete it} and {state the skills and experience the project will demonstrate.}}.',
    'You are an expert career counselor, tasked with analyzing the following job posting and attached resume. Let''s think step by step. You will 1) {In one sentence, identify key skills mentioned in the job posting}, 2) {In two sentences, compare the applicant''s qualifications with the job requirements}, and 3) {Without further explanation: say TRUE if the applicant''s qualifications align with the job description, and FALSE  otherwise}',
    'You are interviewing a job applicant, whose resume is attached, for a job posting whose description is also attached. You have decades of experience in your industry and need to filter out unqualified applicants. Ask the applicant 3 questions that will help you discriminate whether they are a good fit: {1) Technical Question 1; 2) Technical Question 2; 3) Behaviorial Question}. All 3 questions must be specific and relate directly to qualifications stated in the job posting. ',
    'Given the CONTEXT, the INTERVIEWER QUESTIONS, and the APPLICANT ANSWERS, {assess the applicant''s performance answering each question from the point of view of the interviewer.} {Provide actionable advice to the applicant on how to improve their interview performance for next time.}'
]

md_formatting = "\n\n<Output Format> Format the output so the text is markdown-friendly \n<Output Format/>"

# For 3-prompt architecture
def focusAreas(jobPost_resume):
    return prompts[0] + "\n\n<Job Post>" + jobPost_resume[0] + "\n<Job Post/> " + "\n\n<Resume>" + jobPost_resume[1] + "\n<Resume/>"

def idGaps3(areas):
    return prompts[1] + "\n\n<Areas>" + areas[0] + "\n<Areas/>"

def actAdv3():
    return prompts[2] + md_formatting

# For cover letters. The UI should incite users to use this functionality after skills & gaps identification
def coverLetter(jobPost_resume):
    return prompts[3] + "\n\n<Job Post>" + jobPost_resume[0] + "\n<Job Post/> " + "\n\n<Resume>" + jobPost_resume[1] + "\n<Resume/>"

# For the proposal of projects for the applicant's portfolio
def proposeProject(jobPost_resume):
    return prompts[4] + "\n\n<Job Post>" + jobPost_resume[0] + "\n<Job Post/> " + "\n\n<Resume>" + jobPost_resume[1] + "\n<Resume/>" + md_formatting

# To identify if a candidate should apply to a job
def match(jobPost_resume):
    return prompts[5] + "\n\n<Job Post>" + jobPost_resume[0] + "\n<Job Post/> " + "\n\n<Resume>" + jobPost_resume[1] + "\n<Resume/>"

# Challenge with interview questions
def interview(jobPost_resume):
    return prompts[6] + "\n\n<Job Post>" + jobPost_resume[0] + "\n<Job Post/> " + "\n\n<Resume>" + jobPost_resume[1] + "\n<Resume/>"

# Assess interview performance
#   context: the prompt that generated the interview questions, itself generated by the interview() function
#   questions: the questions asked by the interviewer: ChatGPT's output when prompted by the context
#   answers: the answers given by the applicant to each one of the questions
def performance(context, questions, answers):
    return prompts[7] + "\nCONTEXT: {" + context + "}\nINTERVIEWER''S QUESTIONS: {" + questions + "}\nAPPLICANT ANSWERS: {" + answers + "}"
