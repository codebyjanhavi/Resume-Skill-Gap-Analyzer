SKILL_RECOMMENDATIONS = {
    "Python": "Learn Python programming, functions, OOP, and practical problem solving.",
    "SQL": "Practice SQL queries, joins, subqueries, aggregation, and database operations.",
    "Pandas": "Learn Pandas for data cleaning, manipulation, filtering, grouping, and analysis.",
    "NumPy": "Learn NumPy arrays, mathematical operations, indexing, and numerical computing.",
    "Machine Learning": "Study supervised and unsupervised learning algorithms and model evaluation.",
    "Deep Learning": "Learn neural networks, CNNs, RNNs, and deep learning model training.",
    "TensorFlow": "Learn TensorFlow for building, training, and evaluating machine learning models.",
    "PyTorch": "Learn PyTorch tensors, neural networks, model training, and deep learning workflows.",
    "Scikit-learn": "Practice machine learning algorithms, preprocessing, pipelines, and evaluation using Scikit-learn.",
    "Docker": "Learn Docker images, containers, Dockerfiles, and containerized application deployment.",
    "Linux": "Practice Linux commands, file management, permissions, processes, and shell usage.",
    "REST API": "Learn REST API concepts, HTTP methods, endpoints, JSON, and API development.",
    "Git": "Practice Git repositories, branching, commits, merging, and collaboration workflows.",
    "GitHub": "Learn GitHub repositories, pull requests, issues, and collaborative development.",
    "Java": "Practice Java OOP, collections, exception handling, and application development.",
    "JavaScript": "Learn JavaScript fundamentals, DOM manipulation, events, and asynchronous programming.",
    "React": "Learn React components, props, state, hooks, and frontend application development.",
    "Node.js": "Learn Node.js, Express, REST APIs, middleware, and backend development.",
    "MongoDB": "Learn MongoDB documents, collections, queries, indexing, and database design.",
    "AWS": "Learn AWS core services, cloud deployment, storage, networking, and security basics.",
    "Azure": "Learn Azure services, cloud deployment, storage, networking, and resource management.",
    "Kubernetes": "Learn Kubernetes pods, deployments, services, configuration, and container orchestration.",
    "Terraform": "Learn infrastructure as code using Terraform, providers, resources, and state management.",
    "Jenkins": "Learn Jenkins pipelines, CI/CD automation, builds, testing, and deployment.",
    "Selenium": "Practice browser automation, locators, test cases, and automated web testing.",
    "JUnit": "Learn JUnit test cases, assertions, test suites, and unit testing practices.",
    "Power BI": "Learn data modeling, dashboards, visualizations, and reporting using Power BI.",
    "Tableau": "Learn Tableau data connections, dashboards, charts, and interactive visualizations.",
    "Excel": "Practice Excel formulas, data cleaning, pivot tables, charts, and analysis.",
    "Networking": "Study networking fundamentals, protocols, IP addressing, routing, and network security.",
    "Cryptography": "Learn encryption, hashing, digital signatures, keys, and cryptographic fundamentals.",
    "Firewalls": "Learn firewall rules, network filtering, traffic control, and security configurations.",
    "SIEM": "Learn security event collection, monitoring, log analysis, and incident detection.",
    "OWASP": "Study common web application security risks and secure development practices."
}


def generate_recommendations(missing_skills):
    recommendations = []

    for skill in missing_skills:
        recommendation = SKILL_RECOMMENDATIONS.get(
            skill,
            f"Learn the fundamentals and practice {skill} through hands-on projects."
        )

        recommendations.append({
            "skill": skill,
            "recommendation": recommendation
        })

    return recommendations