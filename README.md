<div align="center">


# **SYZYGI**

 Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

<h3>

[Homepage]AI HIVE  (https://www.ai-hive.net/syzygi)

</h3>

(https://opensource.org/licenses/MIT)

</div>

## Table of contents

## Introduction
The next generation AI foundation models will achieve reasoning and logic abilities equivalent to PhD level. And while AI doctors, AI lawyers, and AI engineers are not ready to hang out their shingles, every doctor, lawyer, and engineer will want a specialized AI partner to assist them in delivering premium service to their clients. 
​
## The Problem
AI agent teams partnering with professionals face poor coordination, limited adaptability, and inconsistent performance. Trust issues and integration hurdles hinder adoption. AI needs better collaboration mechanisms, adaptive learning, and robust feedback loops to improve. Enhancing communication skills and ethical decision-making is crucial. The goal is to create transparent, flexible AI agent teams that learn continuously, providing reliable assistance across various professional fields.
 
## The Solution
We are developing an AI Agent Team Architecture called Syzygi (pronounced SIZ-in-jee) that mimics some features of the neural net Transformer Architecture used to train LLMs. Syzygi architecture provides power and flexibility for AI agents to synchronize their tasks on one project and train as a team over many projects. As they perform more varied tasks, they become more versatile and efficient as an organization - they learn to become a better team.
 
## Syzygi - AI Agent Team Architecture
In the rapidly evolving landscape of artificial intelligence, we are witnessing a convergence of multi-agent systems and transformer-based language models. Syzygi presents a novel architecture that synergizes the strengths of specialized AI agents with the powerful mechanisms found in transformer models. It is centered around a large language model (LLM) acting as a neural transformer. This approach aims to enhance collaborative problem-solving, adaptability, and scalability in AI systems.

## Why use CrewAI as base?

The power of AI collaboration has too much to offer.
CrewAI is designed to enable AI agents to assume roles, share goals, and operate in a cohesive unit - much like a well-oiled crew. Whether you're building a smart assistant platform, an automated customer service ensemble, or a multi-agent research team, CrewAI provides the backbone for sophisticated multi-agent interactions.

## Getting Started

To get started follow these simple steps:

### 1. Installation

```shell
pip install crewai
```

If you want to install the 'crewai' package along with its optional features that include additional tools for agents, you can do so by using the following command: pip install 'crewai[tools]'. This command installs the basic package and also adds extra components which require more dependencies to function."

```shell
pip install 'crewai[tools]'
```

### 2. Setting Up Your Crew

``` pip install -r requirements.txt
```
### add new file 

app.py

### UI Streamlit

```shell
pip install streamlit 
```
### add file 

streamlit_app.py

### Run

```shell
streamlit run streamlit_app.py
```

### Key Features

- **Role-Based Agent Design**: Customize agents with specific roles, goals, and tools.
- **Autonomous Inter-Agent Delegation**: Agents can autonomously delegate tasks and inquire amongst themselves, enhancing problem-solving efficiency.
- **Flexible Task Management**: Define tasks with customizable tools and assign them to agents dynamically.
- **Processes Driven**: Currently only supports `sequential` task execution and `hierarchical` processes, but more complex processes like consensual and autonomous are being worked on.
- **Save output as file**: Save the output of individual tasks as a file, so you can use it later.
- **Parse output as Pydantic or Json**: Parse the output of individual tasks as a Pydantic model or as a Json if you want to.
- **Works with Open Source Models**: Run your crew using Open AI or open source models refer to the [Connect crewAI to LLMs](https://docs.crewai.com/how-to/LLM-Connections/) page for details on configuring your agents' connections to models, even ones running locally!

### Examples

You can test different real life examples of AI crews in the [crewAI-examples repo](https://github.com/joaomdmoura/crewAI-examples?tab=readme-ov-file):

- [Landing Page Generator](https://github.com/joaomdmoura/crewAI-examples/tree/main/landing_page_generator)


### How Syzygi and CrewAI Compares

- **Autogen**: While Autogen does good in creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows.

- **ChatDev**: ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications.

- **CrewAI's Advantage**: CrewAI is built with production in mind. It offers the flexibility of Autogen's conversational agents and the structured process approach of ChatDev, but without the rigidity. CrewAI's processes are designed to be dynamic and adaptable, fitting seamlessly into both development and production workflows.

### Syzygi - AI Agent Team Architecture
In the rapidly evolving landscape of artificial intelligence, we are witnessing a convergence of multi-agent systems and transformer-based language models. Syzygi presents a novel architecture that synergizes the strengths of specialized AI agents with the powerful mechanisms found in transformer models. It is centered around a large language model (LLM) acting as a neural transformer. This approach aims to enhance collaborative problem-solving, adaptability, and scalability in AI systems.
​
### Core Components
At the heart of this architecture lies a team of specialized AI agents, each designed to excel in specific tasks or domains. These agents span a wide range of capabilities, from natural language processing and computer vision to data analysis and logical reasoning. Each agent has clearly defined roles and responsibilities, not only executing tasks within their domain of expertise but also providing domain-specific knowledge to other agents and collaborating on complex tasks that span multiple domains.
​
### The inter-agent communication
 is facilitated through a robust set of protocols. These include standardized calls for direct interactions, shared memory spaces for collaborative tasks, and message passing systems for asynchronous communication. 
​
### Central 
to the architecture is a large language model, instructed and given system prompts to act as a transformer-like coordinator. This "Neural Transformer" is fine-tuned with specific instructions to emulate key transformer functionalities, with custom prompts designed to trigger attention-like mechanisms and information integration. The Neural Transformer plays a crucial role in coordinating and integrating agent outputs, acting as a central hub for information flow between agents, synthesizing outputs from multiple agents into coherent solutions, and managing task allocation and prioritization based on agent capabilities and task requirements.
​
### Key
 innovations in this architecture is the adaptive prompting based on task context. The central LLM dynamically generates prompts for agents based on the current task and context, and adjusts its own internal prompts to optimize coordination and integration processes. This adaptability allows the system to flexibly respond to a wide range of tasks and scenarios.

### Task Decomposition Module
 is another critical component, responsible for breaking down complex problems into manageable subtasks for efficient ste-by-step processing. It utilizes hierarchical task network (HTN) planning techniques and employs semantic analysis to identify key components of a task. This module also considers dependencies and parallelization opportunities in subtask creation, ensuring optimal distribution of work across the agent team.
​
### Transformer-Inspired Mechanisms
The architecture incorporates several mechanisms inspired by transformer models, adapting them for agent and task management. The attention mechanism, crucial in transformer models, is reimagined for task-agent relevance scoring and dynamic agent prioritization. The system computes relevance scores between tasks and agents based on historical performance and current capabilities, utilizing embedding techniques to represent tasks and agent skills in a shared vector space. This allows for real-time adjustment of agent priorities based on task urgency and agent performance.
​
### Multiple feedback loops 
ensure continuous improvement and adaptation. These include inter-agent feedback, where agents provide performance ratings and suggestions to each other, central LLM to agent feedback for guidance and correction, and user to system feedback for real-time adjustments based on user interactions. This multi-layered feedback system creates a dynamic, self-improving ecosystem of agents and processes.
​
### The weight parameter
 system dynamically adjusts the influence of different components. It tracks comprehensive performance metrics for each agent, assigns weights to tasks based on user priorities and system goals, and dynamically adjusts the impact of each agent's output on the final solution. This system implements a learning rate to balance stability and adaptability, ensuring that the architecture can evolve without becoming unstable.


### Contribution

Syzygi is open-source and we welcome contributions. If you're looking to contribute, please:

- Fork the repository.
- Create a new branch for your feature.
- Add your feature or improvement.
- Send a pull request.
- We appreciate your input!




### License

Syzygi is released under the MIT License.
