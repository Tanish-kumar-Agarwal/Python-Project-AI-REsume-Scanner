"""
Mock learning resources database: {skill: [{title, platform, hours, url}]}
Used by Feature 5 (Learning Path).
"""

LEARNING_DB = {
    "python": [
        {"title": "Python for Everybody Specialization", "platform": "Coursera", "hours": 60, "url": "https://www.coursera.org/specializations/python"},
        {"title": "Automate the Boring Stuff with Python", "platform": "YouTube", "hours": 15, "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
        {"title": "Python Official Tutorial", "platform": "Docs", "hours": 10, "url": "https://docs.python.org/3/tutorial/"},
    ],
    "java": [
        {"title": "Java Programming and Software Engineering", "platform": "Coursera", "hours": 50, "url": "https://www.coursera.org/specializations/java-programming"},
        {"title": "Java Full Course for Beginners", "platform": "YouTube", "hours": 12, "url": "https://www.youtube.com/watch?v=eIrMbAQSU34"},
    ],
    "javascript": [
        {"title": "The Complete JavaScript Course", "platform": "Coursera", "hours": 40, "url": "https://www.coursera.org/learn/javascript"},
        {"title": "JavaScript Crash Course", "platform": "YouTube", "hours": 8, "url": "https://www.youtube.com/watch?v=hdI2bqOjy3c"},
        {"title": "MDN JavaScript Guide", "platform": "Docs", "hours": 15, "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"},
    ],
    "react": [
        {"title": "React Basics by Meta", "platform": "Coursera", "hours": 25, "url": "https://www.coursera.org/learn/react-basics"},
        {"title": "React JS Full Course", "platform": "YouTube", "hours": 12, "url": "https://www.youtube.com/watch?v=bMknfKXIFA8"},
        {"title": "React Official Docs", "platform": "Docs", "hours": 10, "url": "https://react.dev/learn"},
    ],
    "sql": [
        {"title": "SQL for Data Science", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/sql-for-data-science"},
        {"title": "SQL Full Course - FreeCodeCamp", "platform": "YouTube", "hours": 4, "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},
    ],
    "machine learning": [
        {"title": "Machine Learning by Andrew Ng", "platform": "Coursera", "hours": 60, "url": "https://www.coursera.org/learn/machine-learning"},
        {"title": "Machine Learning Full Course", "platform": "YouTube", "hours": 10, "url": "https://www.youtube.com/watch?v=Gv9_4yMHFhI"},
        {"title": "Scikit-learn User Guide", "platform": "Docs", "hours": 15, "url": "https://scikit-learn.org/stable/user_guide.html"},
    ],
    "deep learning": [
        {"title": "Deep Learning Specialization", "platform": "Coursera", "hours": 80, "url": "https://www.coursera.org/specializations/deep-learning"},
        {"title": "Deep Learning Crash Course", "platform": "YouTube", "hours": 6, "url": "https://www.youtube.com/watch?v=VyWAvY2CF9c"},
    ],
    "docker": [
        {"title": "Docker Essentials", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/docker-essentials"},
        {"title": "Docker Full Course", "platform": "YouTube", "hours": 5, "url": "https://www.youtube.com/watch?v=pTFZFxd4hOI"},
        {"title": "Docker Official Getting Started", "platform": "Docs", "hours": 4, "url": "https://docs.docker.com/get-started/"},
    ],
    "kubernetes": [
        {"title": "Kubernetes for Developers", "platform": "Coursera", "hours": 30, "url": "https://www.coursera.org/learn/kubernetes"},
        {"title": "Kubernetes Course - TechWorld", "platform": "YouTube", "hours": 4, "url": "https://www.youtube.com/watch?v=X48VuDVv0do"},
    ],
    "aws": [
        {"title": "AWS Cloud Practitioner Essentials", "platform": "Coursera", "hours": 20, "url": "https://www.coursera.org/learn/aws-cloud-practitioner-essentials"},
        {"title": "AWS Certified Cloud Practitioner", "platform": "YouTube", "hours": 14, "url": "https://www.youtube.com/watch?v=SOTamWNgDKc"},
    ],
    "git": [
        {"title": "Version Control with Git", "platform": "Coursera", "hours": 10, "url": "https://www.coursera.org/learn/version-control-with-git"},
        {"title": "Git & GitHub Crash Course", "platform": "YouTube", "hours": 2, "url": "https://www.youtube.com/watch?v=RGOj5yH7evk"},
    ],
    "typescript": [
        {"title": "Understanding TypeScript", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/typescript"},
        {"title": "TypeScript Handbook", "platform": "Docs", "hours": 8, "url": "https://www.typescriptlang.org/docs/handbook/"},
    ],
    "tensorflow": [
        {"title": "TensorFlow Developer Certificate", "platform": "Coursera", "hours": 40, "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice"},
        {"title": "TensorFlow Tutorials", "platform": "Docs", "hours": 15, "url": "https://www.tensorflow.org/tutorials"},
    ],
    "pytorch": [
        {"title": "Deep Neural Networks with PyTorch", "platform": "Coursera", "hours": 30, "url": "https://www.coursera.org/learn/deep-neural-networks-with-pytorch"},
        {"title": "PyTorch Getting Started", "platform": "Docs", "hours": 12, "url": "https://pytorch.org/tutorials/beginner/basics/intro.html"},
    ],
    "data analysis": [
        {"title": "Google Data Analytics Certificate", "platform": "Coursera", "hours": 50, "url": "https://www.coursera.org/professional-certificates/google-data-analytics"},
        {"title": "Data Analysis with Python", "platform": "YouTube", "hours": 5, "url": "https://www.youtube.com/watch?v=r-uOLxNrNk8"},
    ],
    "ci/cd": [
        {"title": "CI/CD Pipelines with Jenkins", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/cicd-jenkins"},
        {"title": "GitHub Actions Full Course", "platform": "YouTube", "hours": 3, "url": "https://www.youtube.com/watch?v=R8_veQiYBjI"},
    ],
    "api": [
        {"title": "APIs and RESTful Services", "platform": "Coursera", "hours": 12, "url": "https://www.coursera.org/learn/apis"},
        {"title": "REST API Crash Course", "platform": "YouTube", "hours": 3, "url": "https://www.youtube.com/watch?v=qbLc5a9jdXo"},
    ],
    "rest": [
        {"title": "Building RESTful APIs", "platform": "Coursera", "hours": 10, "url": "https://www.coursera.org/learn/restful-apis"},
        {"title": "RESTful API Tutorial", "platform": "Docs", "hours": 3, "url": "https://restfulapi.net/"},
    ],
    "communication": [
        {"title": "Improving Communication Skills", "platform": "Coursera", "hours": 10, "url": "https://www.coursera.org/learn/wharton-communication-skills"},
    ],
    "leadership": [
        {"title": "Inspirational Leadership", "platform": "Coursera", "hours": 12, "url": "https://www.coursera.org/specializations/inspirational-leadership"},
    ],
    "problem solving": [
        {"title": "Creative Problem Solving", "platform": "Coursera", "hours": 8, "url": "https://www.coursera.org/learn/creative-problem-solving"},
    ],
    "agile": [
        {"title": "Agile with Atlassian Jira", "platform": "Coursera", "hours": 10, "url": "https://www.coursera.org/learn/agile-atlassian-jira"},
        {"title": "Agile Manifesto", "platform": "Docs", "hours": 1, "url": "https://agilemanifesto.org/"},
    ],
    "html": [
        {"title": "HTML, CSS, and JavaScript for Web Developers", "platform": "Coursera", "hours": 20, "url": "https://www.coursera.org/learn/html-css-javascript-for-web-developers"},
        {"title": "MDN HTML Guide", "platform": "Docs", "hours": 6, "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML"},
    ],
    "css": [
        {"title": "Advanced CSS and Sass", "platform": "Coursera", "hours": 20, "url": "https://www.coursera.org/learn/advanced-css"},
        {"title": "MDN CSS Guide", "platform": "Docs", "hours": 8, "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS"},
    ],
    "node": [
        {"title": "Server-side Development with NodeJS", "platform": "Coursera", "hours": 30, "url": "https://www.coursera.org/learn/server-side-nodejs"},
        {"title": "Node.js Documentation", "platform": "Docs", "hours": 10, "url": "https://nodejs.org/en/docs/guides/"},
    ],
    "linux": [
        {"title": "Linux Fundamentals", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/linux-fundamentals"},
        {"title": "Linux Full Course", "platform": "YouTube", "hours": 5, "url": "https://www.youtube.com/watch?v=sWbUDq4S6Y8"},
    ],
    "testing": [
        {"title": "Software Testing and Automation", "platform": "Coursera", "hours": 20, "url": "https://www.coursera.org/specializations/software-testing-automation"},
        {"title": "Pytest Documentation", "platform": "Docs", "hours": 5, "url": "https://docs.pytest.org/en/stable/"},
    ],
    "microservices": [
        {"title": "Microservices Architecture", "platform": "Coursera", "hours": 20, "url": "https://www.coursera.org/learn/microservices"},
        {"title": "Microservices.io Patterns", "platform": "Docs", "hours": 8, "url": "https://microservices.io/patterns/"},
    ],
    "mongodb": [
        {"title": "MongoDB University - M001", "platform": "Coursera", "hours": 10, "url": "https://www.coursera.org/learn/introduction-mongodb"},
        {"title": "MongoDB Manual", "platform": "Docs", "hours": 12, "url": "https://www.mongodb.com/docs/manual/"},
    ],
    "nlp": [
        {"title": "NLP Specialization", "platform": "Coursera", "hours": 40, "url": "https://www.coursera.org/specializations/natural-language-processing"},
        {"title": "spaCy Documentation", "platform": "Docs", "hours": 8, "url": "https://spacy.io/usage"},
    ],
    "c++": [
        {"title": "C++ for C Programmers", "platform": "Coursera", "hours": 25, "url": "https://www.coursera.org/learn/c-plus-plus-a"},
        {"title": "cppreference.com", "platform": "Docs", "hours": 15, "url": "https://en.cppreference.com/w/"},
    ],
    "azure": [
        {"title": "Microsoft Azure Fundamentals", "platform": "Coursera", "hours": 20, "url": "https://www.coursera.org/learn/microsoft-azure-fundamentals"},
        {"title": "Azure Documentation", "platform": "Docs", "hours": 15, "url": "https://learn.microsoft.com/en-us/azure/"},
    ],
    "gcp": [
        {"title": "Google Cloud Fundamentals", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/gcp-fundamentals"},
        {"title": "Google Cloud Docs", "platform": "Docs", "hours": 12, "url": "https://cloud.google.com/docs"},
    ],
    "statistics": [
        {"title": "Statistics with Python", "platform": "Coursera", "hours": 30, "url": "https://www.coursera.org/specializations/statistics-with-python"},
    ],
    "data visualization": [
        {"title": "Data Visualization with Python", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/python-for-data-visualization"},
        {"title": "Matplotlib Documentation", "platform": "Docs", "hours": 6, "url": "https://matplotlib.org/stable/tutorials/"},
    ],
    "redis": [
        {"title": "Redis for Developers", "platform": "Coursera", "hours": 10, "url": "https://www.coursera.org/learn/redis"},
        {"title": "Redis Documentation", "platform": "Docs", "hours": 6, "url": "https://redis.io/docs/"},
    ],
    "security": [
        {"title": "Introduction to Cybersecurity", "platform": "Coursera", "hours": 20, "url": "https://www.coursera.org/learn/intro-cyber-security"},
        {"title": "OWASP Top 10", "platform": "Docs", "hours": 4, "url": "https://owasp.org/www-project-top-ten/"},
    ],
    "terraform": [
        {"title": "HashiCorp Terraform", "platform": "Coursera", "hours": 15, "url": "https://www.coursera.org/learn/terraform"},
        {"title": "Terraform Documentation", "platform": "Docs", "hours": 8, "url": "https://developer.hashicorp.com/terraform/docs"},
    ],
}


def get_resources(skill):
    """Return learning resources for a given skill (case-insensitive)."""
    return LEARNING_DB.get(skill.lower(), [])
