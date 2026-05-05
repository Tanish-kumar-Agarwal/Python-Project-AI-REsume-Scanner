"""
STAR question bank: pre-written behavioral interview questions tagged by role and skill.
Used by Feature 6 (STAR Questions).
~40 questions with S/T/A/R hint labels.
"""

STAR_BANK = [
    # --- SOFTWARE ENGINEERING ---
    {"question": "Tell me about a time you debugged a critical production issue under pressure.",
     "role_tags": ["software engineer", "backend engineer", "devops engineer"],
     "skill_tags": ["problem solving", "python", "sql"],
     "s": "A major API outage affected 10K+ users during peak hours.",
     "t": "I was the on-call engineer and needed to restore service within our 30-min SLA.",
     "a": "I triaged logs, identified a deadlock in the database connection pool, and deployed a hotfix.",
     "r": "Service restored in 22 minutes; post-mortem led to connection pool monitoring that prevented 3 future incidents."},

    {"question": "Describe a time you refactored legacy code to improve performance.",
     "role_tags": ["software engineer", "backend engineer", "full stack developer"],
     "skill_tags": ["python", "java", "sql", "problem solving"],
     "s": "Our report generation module took 45 seconds, frustrating internal users.",
     "t": "I was tasked with reducing load time to under 5 seconds without breaking existing functionality.",
     "a": "I profiled the code, replaced N+1 queries with batch fetches, and added Redis caching.",
     "r": "Load time dropped to 2.3 seconds — an 18x improvement; team adopted the caching pattern across 4 other modules."},

    {"question": "Tell me about a time you had to learn a new technology quickly for a project.",
     "role_tags": ["software engineer", "web developer", "full stack developer"],
     "skill_tags": ["react", "javascript", "typescript"],
     "s": "Client pivoted from jQuery to React mid-project with a hard 3-week deadline.",
     "t": "I needed to rebuild the dashboard UI in React while maintaining feature parity.",
     "a": "I spent weekends on React docs, built small prototypes, and paired with a React-experienced colleague.",
     "r": "Delivered on time with zero regressions; became the team's go-to React resource."},

    {"question": "Describe a situation where you disagreed with a technical decision and how you handled it.",
     "role_tags": ["software engineer", "backend engineer", "frontend engineer"],
     "skill_tags": ["communication", "leadership", "problem solving"],
     "s": "The lead proposed using a NoSQL database for a heavily relational data model.",
     "t": "I needed to voice my concerns without undermining the lead's authority.",
     "a": "I prepared a comparison document with benchmarks, presented trade-offs in a team meeting, and proposed a hybrid approach.",
     "r": "Team adopted PostgreSQL for core data and MongoDB for analytics — query performance improved 3x."},

    {"question": "Tell me about a time you mentored a junior developer.",
     "role_tags": ["software engineer", "backend engineer", "frontend engineer"],
     "skill_tags": ["leadership", "communication", "teamwork"],
     "s": "A new hire was struggling with code reviews and getting PRs rejected repeatedly.",
     "t": "As the senior on the team, I took responsibility for their onboarding.",
     "a": "I set up weekly 1:1 pairing sessions, created a PR checklist, and reviewed their code with explanations rather than just fixes.",
     "r": "Their PR approval rate went from 30% to 90% in 6 weeks; they later mentored another new hire."},

    # --- FRONTEND ---
    {"question": "Tell me about a time you optimized a slow React application.",
     "role_tags": ["frontend engineer", "web developer", "full stack developer"],
     "skill_tags": ["react", "javascript", "performance optimization"],
     "s": "Our React dashboard had a 4-second initial load and frequent re-renders.",
     "t": "I was assigned to improve perceived performance to under 1.5 seconds.",
     "a": "I implemented React.memo, code splitting with lazy loading, and virtualized long lists with react-window.",
     "r": "First paint dropped to 1.1 seconds, bundle size reduced by 40%, and user engagement increased 25%."},

    {"question": "Describe a time you had to make a website fully accessible.",
     "role_tags": ["frontend engineer", "web developer"],
     "skill_tags": ["html", "css", "accessibility"],
     "s": "An audit revealed our app failed WCAG 2.1 AA compliance, risking a government contract.",
     "t": "I led the accessibility remediation effort across 30+ pages.",
     "a": "I added ARIA labels, fixed color contrast ratios, implemented keyboard navigation, and set up automated axe testing.",
     "r": "Passed WCAG 2.1 AA audit with zero critical issues; secured the $2M government contract."},

    {"question": "Tell me about building a complex responsive layout.",
     "role_tags": ["frontend engineer", "web developer"],
     "skill_tags": ["css", "html", "responsive design"],
     "s": "The marketing team needed a landing page that worked flawlessly on 15+ device sizes.",
     "t": "I was responsible for the entire front-end implementation with a 1-week deadline.",
     "a": "I used CSS Grid with mobile-first approach, created fluid typography, and tested on BrowserStack across 20 devices.",
     "r": "Zero layout bugs reported post-launch; page achieved 98 Lighthouse performance score."},

    # --- DATA SCIENCE / ML ---
    {"question": "Tell me about a machine learning model you built and deployed.",
     "role_tags": ["data scientist", "machine learning engineer"],
     "skill_tags": ["machine learning", "python", "tensorflow"],
     "s": "Customer churn was at 18% and the business lacked predictive capabilities.",
     "t": "I was tasked with building a churn prediction model with >85% accuracy.",
     "a": "I engineered 40+ features from usage data, trained XGBoost and neural network models, and deployed via Flask API.",
     "r": "Model achieved 91% accuracy; proactive retention outreach reduced churn by 6 percentage points."},

    {"question": "Describe a time you had to clean and preprocess messy data.",
     "role_tags": ["data scientist", "data analyst"],
     "skill_tags": ["data analysis", "python", "sql"],
     "s": "Inherited a dataset with 30% missing values, duplicates, and inconsistent date formats across 5 sources.",
     "t": "I needed to create a clean, unified dataset for quarterly business reporting.",
     "a": "I built an ETL pipeline using pandas, standardized schemas, imputed missing values with KNN, and wrote validation tests.",
     "r": "Reduced data quality issues by 95%; pipeline was adopted as the team standard for all future integrations."},

    {"question": "Tell me about a time your analysis influenced a major business decision.",
     "role_tags": ["data scientist", "data analyst"],
     "skill_tags": ["data analysis", "communication", "data visualization"],
     "s": "Marketing was split on whether to invest in SEO or paid ads for Q4.",
     "t": "I was asked to provide data-driven guidance within 1 week.",
     "a": "I analyzed 12 months of funnel data, built attribution models, and presented ROI comparisons in a stakeholder deck.",
     "r": "Team shifted 60% of budget to SEO based on my analysis; organic traffic grew 45% over the next quarter."},

    # --- DEVOPS ---
    {"question": "Tell me about a CI/CD pipeline you designed from scratch.",
     "role_tags": ["devops engineer", "software engineer"],
     "skill_tags": ["ci/cd", "docker", "git", "jenkins"],
     "s": "The team was doing manual deployments that took 2 hours and caused frequent rollbacks.",
     "t": "I was tasked with automating the entire build-test-deploy pipeline.",
     "a": "I set up GitHub Actions with Docker builds, automated testing, staging deployments, and Slack notifications.",
     "r": "Deployment time dropped to 8 minutes, rollback rate fell from 20% to 3%, and team shipped 2x more frequently."},

    {"question": "Describe a time you handled a security incident in production.",
     "role_tags": ["devops engineer", "cybersecurity analyst"],
     "skill_tags": ["security", "linux", "monitoring"],
     "s": "Our monitoring detected unusual traffic patterns suggesting a potential DDoS attack.",
     "t": "I needed to mitigate the attack while keeping services available.",
     "a": "I enabled rate limiting, configured WAF rules, scaled up infrastructure, and coordinated with the ISP.",
     "r": "Services maintained 99.5% uptime during the attack; implemented permanent DDoS protection that blocked 15 subsequent attempts."},

    {"question": "Tell me about migrating an application to the cloud.",
     "role_tags": ["devops engineer", "cloud architect"],
     "skill_tags": ["aws", "docker", "kubernetes", "terraform"],
     "s": "Our on-premise servers were reaching capacity and costing $50K/month in maintenance.",
     "t": "I led the migration of 12 microservices to AWS with zero downtime.",
     "a": "I containerized apps with Docker, set up EKS clusters, used Terraform for IaC, and implemented a blue-green deployment strategy.",
     "r": "Reduced infrastructure costs by 40%, achieved 99.99% uptime, and enabled auto-scaling for peak traffic."},

    # --- TEAMWORK & LEADERSHIP ---
    {"question": "Tell me about a time you led a cross-functional team.",
     "role_tags": ["software engineer", "product manager", "data scientist"],
     "skill_tags": ["leadership", "communication", "project management"],
     "s": "A product launch required coordination between engineering, design, marketing, and sales.",
     "t": "I volunteered to lead the cross-functional team through a 6-week sprint.",
     "a": "I set up daily standups, created a shared Notion board, resolved blockers proactively, and facilitated weekly demos.",
     "r": "Launched on time with all features; post-launch survey showed 95% team satisfaction with the process."},

    {"question": "Describe a time you had to manage conflicting priorities.",
     "role_tags": ["software engineer", "product manager", "full stack developer"],
     "skill_tags": ["problem solving", "communication", "agile"],
     "s": "Two VPs requested urgent features for the same sprint, and both were 'P0'.",
     "t": "I needed to find a resolution without damaging either stakeholder relationship.",
     "a": "I quantified the business impact of each feature, presented data to both VPs, and proposed a staggered release plan.",
     "r": "Both features shipped within 3 weeks; the prioritization framework I created was adopted company-wide."},

    {"question": "Tell me about receiving tough feedback and how you responded.",
     "role_tags": ["software engineer", "frontend engineer", "data scientist"],
     "skill_tags": ["communication", "problem solving", "teamwork"],
     "s": "During a performance review, my manager said my code reviews were too harsh and demoralizing juniors.",
     "t": "I needed to adjust my approach while still maintaining code quality standards.",
     "a": "I adopted the 'sandwich' feedback model, started highlighting what was done well before suggesting improvements, and asked questions instead of making demands.",
     "r": "Team morale improved, PR review turnaround time decreased by 30%, and I was nominated for a mentorship award."},

    {"question": "Describe a time you failed and what you learned from it.",
     "role_tags": ["software engineer", "data scientist", "web developer", "devops engineer"],
     "skill_tags": ["problem solving", "communication"],
     "s": "I deployed a database migration without proper testing that caused 2 hours of downtime.",
     "t": "I needed to fix the issue, communicate to stakeholders, and prevent recurrence.",
     "a": "I rolled back the migration, wrote a detailed incident report, and implemented a mandatory staging-first migration policy.",
     "r": "Zero migration-related incidents in the following 12 months; the policy became an engineering standard."},

    # --- PROBLEM SOLVING ---
    {"question": "Tell me about solving a problem that no one else could figure out.",
     "role_tags": ["software engineer", "backend engineer", "machine learning engineer"],
     "skill_tags": ["problem solving", "python", "sql"],
     "s": "Intermittent 500 errors appeared randomly, and 3 engineers had spent 2 weeks without finding the cause.",
     "t": "I was pulled in as a fresh set of eyes to diagnose and fix the issue.",
     "a": "I added granular logging, correlated errors with memory usage, and discovered a memory leak in a third-party library during garbage collection.",
     "r": "Fixed the leak with a workaround, reported the bug upstream, and built a memory monitoring dashboard that caught 2 similar issues later."},

    {"question": "Describe a time you automated a tedious manual process.",
     "role_tags": ["software engineer", "devops engineer", "data analyst"],
     "skill_tags": ["python", "scripting", "problem solving"],
     "s": "The QA team spent 4 hours daily manually testing API endpoints after each deployment.",
     "t": "I wanted to free up QA time for exploratory testing by automating regression tests.",
     "a": "I built a pytest suite with 200+ API tests, integrated it with our CI pipeline, and added Slack reporting.",
     "r": "Manual testing time dropped to 30 minutes; QA found 3x more edge-case bugs through exploratory testing."},

    # --- AGILE / PROJECT MANAGEMENT ---
    {"question": "Tell me about a time you improved a team's development process.",
     "role_tags": ["software engineer", "product manager", "devops engineer"],
     "skill_tags": ["agile", "scrum", "communication", "leadership"],
     "s": "Our sprint completion rate was only 60%, with constant scope creep and unclear requirements.",
     "t": "As scrum master, I needed to improve delivery predictability.",
     "a": "I introduced story point estimation, enforced a 'definition of ready' checklist, limited WIP, and started retrospectives.",
     "r": "Sprint completion rate improved to 88%, velocity became predictable, and stakeholder satisfaction scores increased by 40%."},

    # --- ADDITIONAL QUESTIONS ---
    {"question": "Tell me about building an API from scratch.",
     "role_tags": ["backend engineer", "software engineer", "full stack developer"],
     "skill_tags": ["api", "rest", "python", "sql"],
     "s": "The company needed a public API for third-party integrations but had none.",
     "t": "I was responsible for designing, building, and documenting the REST API.",
     "a": "I designed RESTful endpoints following OpenAPI spec, implemented rate limiting, auth with JWT, versioning, and comprehensive docs.",
     "r": "API launched with 50+ endpoints; adopted by 15 partners in the first month with zero breaking changes."},

    {"question": "Describe a time you worked with a tight deadline.",
     "role_tags": ["software engineer", "web developer", "frontend engineer"],
     "skill_tags": ["problem solving", "agile", "communication"],
     "s": "A client demo was moved up by 2 weeks, and we had 60% of the features built.",
     "t": "I needed to prioritize which features to polish and which to defer.",
     "a": "I created a priority matrix with the PM, cut non-essential features, and led the team through focused daily sprints.",
     "r": "Demo went flawlessly with the core features; client signed a $500K contract on the spot."},

    {"question": "Tell me about implementing a microservices architecture.",
     "role_tags": ["backend engineer", "software engineer", "devops engineer"],
     "skill_tags": ["microservices", "docker", "kubernetes", "api"],
     "s": "Our monolithic app had 500K lines of code and deployments took 4 hours with high failure rates.",
     "t": "I was part of the team tasked with breaking the monolith into microservices.",
     "a": "I identified service boundaries using domain-driven design, extracted the user service first as a pilot, set up inter-service communication with gRPC.",
     "r": "Deployment time dropped to 15 minutes per service, team velocity increased 3x, and we could scale individual services independently."},

    {"question": "Describe setting up monitoring and observability for a system.",
     "role_tags": ["devops engineer", "software engineer", "backend engineer"],
     "skill_tags": ["monitoring", "linux", "docker", "aws"],
     "s": "Production issues were only discovered when customers complained — we had no proactive monitoring.",
     "t": "I was tasked with building a comprehensive observability stack.",
     "a": "I set up Prometheus for metrics, Grafana dashboards, ELK stack for logs, and PagerDuty for alerting with runbooks.",
     "r": "MTTD (mean time to detect) dropped from 45 minutes to 2 minutes; MTTR improved by 70%."},

    {"question": "Tell me about a time you improved application security.",
     "role_tags": ["software engineer", "backend engineer", "cybersecurity analyst"],
     "skill_tags": ["security", "api", "testing"],
     "s": "A penetration test revealed 12 critical vulnerabilities including SQL injection and XSS.",
     "t": "I led the security remediation effort with a 2-week deadline before the next audit.",
     "a": "I parameterized all SQL queries, implemented CSP headers, added input sanitization, and set up SAST/DAST in CI.",
     "r": "All 12 vulnerabilities fixed; next pen test showed zero critical findings and earned SOC 2 compliance."},

    {"question": "Describe a data pipeline you built end-to-end.",
     "role_tags": ["data scientist", "data analyst", "backend engineer"],
     "skill_tags": ["python", "sql", "data analysis", "etl"],
     "s": "Business analytics relied on manually exported spreadsheets that were always outdated.",
     "t": "I needed to build an automated pipeline from raw data to executive dashboards.",
     "a": "I built an ETL pipeline with Airflow, transformed data with dbt, stored in a data warehouse, and connected Tableau dashboards.",
     "r": "Reports went from weekly manual exports to real-time dashboards; saved the analytics team 20 hours per week."},

    {"question": "Tell me about handling a difficult stakeholder.",
     "role_tags": ["product manager", "software engineer", "data scientist"],
     "skill_tags": ["communication", "leadership", "stakeholder management"],
     "s": "A VP kept changing requirements mid-sprint, causing the team to miss deadlines.",
     "t": "I needed to align the VP's expectations with our delivery capacity without conflict.",
     "a": "I set up bi-weekly prioritization meetings, introduced a change request process, and showed the cost of context switching with data.",
     "r": "Mid-sprint changes dropped by 80%; the VP praised the new process as 'the first time I actually know what's happening'."},

    {"question": "Describe a time you used data to drive a product decision.",
     "role_tags": ["product manager", "data analyst", "data scientist"],
     "skill_tags": ["data analysis", "a/b testing", "communication"],
     "s": "The team debated between two checkout flow designs with strong opinions on each side.",
     "t": "I proposed running a data-driven experiment instead of relying on opinion.",
     "a": "I set up an A/B test with clear success metrics, ran it for 2 weeks with statistical significance, and presented results.",
     "r": "Design B won with 23% higher conversion; the A/B testing culture I initiated saved $200K in the first year."},

    {"question": "Tell me about a time you contributed to open source.",
     "role_tags": ["software engineer", "frontend engineer", "backend engineer"],
     "skill_tags": ["git", "python", "javascript", "communication"],
     "s": "I found a performance bug in a popular open-source library our team depended on.",
     "t": "I wanted to fix it upstream rather than maintain a fork.",
     "a": "I diagnosed the issue, wrote a fix with tests, submitted a PR with detailed explanation, and responded to maintainer feedback.",
     "r": "PR was merged and released in v2.3; fix improved performance for thousands of users and I became a recognized contributor."},

    {"question": "Describe building a feature that required learning an unfamiliar domain.",
     "role_tags": ["software engineer", "full stack developer", "data scientist"],
     "skill_tags": ["problem solving", "communication", "api"],
     "s": "I was assigned to build a financial reporting module but had no finance background.",
     "t": "I needed to understand GAAP accounting rules well enough to implement correct calculations.",
     "a": "I shadowed the finance team for a week, read accounting documentation, built a prototype, and iterated based on CFO feedback.",
     "r": "Module passed financial audit with zero errors; finance team adopted it as their primary reporting tool."},

    {"question": "Tell me about implementing real-time features.",
     "role_tags": ["software engineer", "backend engineer", "full stack developer"],
     "skill_tags": ["javascript", "node", "api", "microservices"],
     "s": "Users complained about stale data — our dashboard only refreshed on page reload.",
     "t": "I was tasked with adding real-time updates without a full rewrite.",
     "a": "I implemented WebSocket connections with Socket.io, added event-driven updates for key metrics, and ensured graceful degradation.",
     "r": "Data freshness went from minutes to milliseconds; user session duration increased by 35%."},

    {"question": "Describe a time you reduced cloud costs significantly.",
     "role_tags": ["devops engineer", "cloud architect", "backend engineer"],
     "skill_tags": ["aws", "docker", "kubernetes", "cost optimization"],
     "s": "AWS bill was $80K/month and growing 15% each quarter with no visibility into waste.",
     "t": "Leadership asked me to reduce cloud spend by at least 25% without impacting performance.",
     "a": "I audited all resources, right-sized instances, implemented spot instances for batch jobs, set up cost alerts, and terminated orphaned resources.",
     "r": "Reduced monthly bill to $52K (35% savings), implemented ongoing cost governance, and performance actually improved with right-sizing."},

    {"question": "Tell me about designing a database schema for a complex application.",
     "role_tags": ["backend engineer", "software engineer", "data analyst"],
     "skill_tags": ["sql", "postgresql", "data analysis"],
     "s": "We were building a multi-tenant SaaS platform and needed a schema that could scale to 10K+ tenants.",
     "t": "I was responsible for designing the core database architecture.",
     "a": "I evaluated shared vs isolated schemas, chose row-level security with tenant_id partitioning, designed indexes based on query patterns, and load tested.",
     "r": "Schema handled 15K tenants with sub-100ms query times; became the reference architecture for all new projects."},

    {"question": "Describe a time you improved test coverage and code quality.",
     "role_tags": ["software engineer", "frontend engineer", "backend engineer"],
     "skill_tags": ["testing", "python", "javascript", "ci/cd"],
     "s": "Our codebase had 12% test coverage and bugs were making it to production weekly.",
     "t": "I championed a quality initiative to get coverage above 70% within one quarter.",
     "a": "I set up coverage reporting in CI, wrote a testing guide, led testing workshops, and blocked merges below coverage thresholds.",
     "r": "Coverage reached 78% in 10 weeks; production bugs dropped by 65% and developer confidence in deployments soared."},

    {"question": "Tell me about managing technical debt.",
     "role_tags": ["software engineer", "backend engineer", "frontend engineer"],
     "skill_tags": ["problem solving", "agile", "communication"],
     "s": "Years of feature-first development left our codebase with significant tech debt slowing feature delivery.",
     "t": "I needed to convince leadership to allocate sprint time for debt reduction.",
     "a": "I cataloged tech debt items with business impact scores, proposed a '20% rule' (1 day per sprint for debt), and tracked velocity improvements.",
     "r": "Feature delivery speed increased 40% over 2 quarters; leadership made the 20% rule permanent."},
]


def get_questions_for_role(role, skills=None, limit=8):
    """
    Filter STAR questions by role and optionally by skills.
    Returns up to `limit` questions.
    """
    role_lower = role.lower()
    results = []

    for q in STAR_BANK:
        role_match = any(role_lower in tag for tag in q["role_tags"])
        if role_match:
            if skills:
                skill_match = any(s.lower() in [t.lower() for t in q["skill_tags"]] for s in skills)
                q_copy = dict(q)
                q_copy["relevance"] = 2 if skill_match else 1
                results.append(q_copy)
            else:
                q_copy = dict(q)
                q_copy["relevance"] = 1
                results.append(q_copy)

    # Sort by relevance (skill-matched first)
    results.sort(key=lambda x: x.get("relevance", 0), reverse=True)
    return results[:limit]
