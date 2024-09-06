import os
import json
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from postmortem_data_processor import PostmortemDataProcessor
from postmortem_analysis_model import PostmortemAnalysisModel

load_dotenv()

def save_to_file(content, file_type):
    if not os.path.exists('results'):
        os.makedirs('results')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/{file_type}_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return filename

def save_to_json(content, file_type):
    if not os.path.exists('results'):
        os.makedirs('results')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/{file_type}_{timestamp}.json"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=2)
    return filename

def create_adaptive_agent(role, goal, backstory, recommendations):
    adjusted_goal = adjust_goal(goal, recommendations)
    adjusted_backstory = adjust_backstory(backstory, recommendations)
    
    agent = Agent(
        role=role,
        goal=adjusted_goal,
        backstory=adjusted_backstory,
        verbose=True,
        allow_delegation=True
    )
    
    apply_tool_recommendations(agent, recommendations)
    apply_behavior_recommendations(agent, recommendations)
    
    return agent

def adjust_goal(goal, recommendations):
    # Placeholder for goal adjustment logic
    return goal

def adjust_backstory(backstory, recommendations):
    # Placeholder for backstory adjustment logic
    return backstory

def apply_tool_recommendations(agent, recommendations):
    # Placeholder for tool recommendation logic
    pass

def apply_behavior_recommendations(agent, recommendations):
    # Placeholder for behavior recommendation logic
    pass

def get_latest_recommendations(role):
    # Placeholder for fetching latest recommendations
    return {}

def run_crew(user_request):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

    search_tool = SerperDevTool()

    researcher = create_adaptive_agent(
        role='Senior Research Analyst',
        goal='Conduct thorough research based on the given request',
        backstory="""You work at a leading tech think tank. Your expertise lies in identifying emerging trends and analyzing complex topics.""",
        recommendations=get_latest_recommendations('researcher')
    )

    writer = create_adaptive_agent(
        role='Tech Content Strategist',
        goal='Craft compelling content based on the research and analysis',
        backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles. You transform complex concepts into compelling narratives.""",
        recommendations=get_latest_recommendations('writer')
    )

    analyst = create_adaptive_agent(
        role='Research Evaluator and Writing Advisor',
        goal='Evaluate search results and provide suggestions to improve the written content',
        backstory="""You are an expert at analyzing research data and providing valuable insights to writers. Your expertise lies in identifying key information from search results and suggesting ways to enhance written content.""",
        recommendations=get_latest_recommendations('analyst')
    )
    
    task1 = Task(
        description=f"Conduct comprehensive research based on the following request: {user_request}",
        expected_output="Detailed research findings with relevant data and trends",
        agent=researcher
    )

    task2 = Task(
        description="Review the search results and provide suggestions for improvement.",
        expected_output="Analysis of research findings with improvement suggestions",
        agent=analyst
    )

    task3 = Task(
        description="Develop an engaging article based on the research findings.",
        expected_output="Draft of an engaging article summarizing key insights",
        agent=writer
    )

    task4 = Task(
        description="Revise and finalize the article based on the analyst's suggestions.",
        expected_output="Final polished article incorporating feedback",
        agent=writer
    )

    crew = Crew(
        agents=[researcher, writer, analyst],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential
    )

    result = crew.kickoff()
    
    analysis_file = save_to_file(str(result), "analysis")
    print(f"Analysis results saved to {analysis_file}")
    
    return result

def parse_postmortem_content(content):
    sections = content.split('###')[1:]  # Split by section headers
    structured_content = {}
    for section in sections:
        lines = section.strip().split('\n')
        header = lines[0].strip()
        content = '\n'.join(lines[1:]).strip()
        structured_content[header] = content
    return structured_content

def run_postmortem(postmortem_request, previous_result):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

    postmortem_analyst = create_adaptive_agent(
        role='Postmortem Analyst',
        goal='Conduct a thorough postmortem analysis of the team\'s performance',
        backstory="""You are an experienced project manager and analyst specializing in team performance and process improvement.""",
        recommendations=get_latest_recommendations('postmortem_analyst')
    )

    postmortem_task = Task(
        description=f"""Analyze the team's performance based on the following request and the previous result:
        Request: {postmortem_request}
        Previous Result: {previous_result}
        
        Provide insights on what went well, what could be improved, and specific recommendations for future tasks.""",
        expected_output="Detailed postmortem analysis with actionable insights and recommendations",
        agent=postmortem_analyst
    )

    postmortem_crew = Crew(
        agents=[postmortem_analyst],
        tasks=[postmortem_task],
        verbose=True,
        process=Process.sequential
    )

    postmortem_result = postmortem_crew.kickoff()
    
    # Extract the content from the CrewOutput object
    content = str(postmortem_result)
    
    # Parse the content into a structured format
    structured_content = parse_postmortem_content(content)
    
    # Neural network analysis
    data_processor = PostmortemDataProcessor()
    df = data_processor.collect_data([postmortem_result])
    processed_data = data_processor.preprocess_data(df)
    
    # Temporarily comment out the model prediction part until we have a trained model
    # model = PostmortemAnalysisModel.load_model('path/to/saved/model')
    # predictions = model.predict(processed_data)
    # recommendations = interpret_predictions(predictions)
    
    # For now, let's use a placeholder for recommendations
    recommendations = "Placeholder for AI-generated recommendations based on postmortem analysis"
    
    # Create a structured dictionary for the postmortem results
    postmortem_dict = {
        'structured_result': structured_content,
        'ai_recommendations': recommendations
    }
    
    # Save the results as a JSON file for better readability
    postmortem_file = save_to_json(postmortem_dict, "postmortem")
    print(f"Postmortem results saved to {postmortem_file}")
    
    return postmortem_dict

def interpret_predictions(predictions):
    # Placeholder for prediction interpretation logic
    return "AI-generated recommendations based on postmortem analysis"

if __name__ == "__main__":
    test_request = "Analyze the latest advancements in AI in 2024. Identify key trends, breakthrough technologies, and potential industry impacts."
    result = run_crew(test_request)
    print("######################")
    print(result)
    
    test_postmortem_request = "Conduct a postmortem on the team's performance. How did we do and what could we improve for next time?"
    postmortem_result = run_postmortem(test_postmortem_request, str(result))
    print("######################")
    print(json.dumps(postmortem_result, indent=2))