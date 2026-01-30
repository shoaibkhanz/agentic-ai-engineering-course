# Continuous Deployment Guidelines

## Global Context of the Lesson

### What We Are Planning to Share

In this lesson, we complete the DevOps journey for AI agents by deploying our research agent to the cloud and setting up Continuous Deployment (CD). We will cover:

- **Infrastructure as Code with gcloud**: Provisioning cloud resources using documented commands rather than clicking through UIs.
- **GCP Services Setup**: Creating Artifact Registry, Cloud SQL, Secret Manager, and configuring Workload Identity Federation.
- **Manual Deployment Pipeline**: A GitHub Actions workflow for controlled, on-demand deployments.
- **Cloud Run Concepts**: Understanding services, revisions, autoscaling, and zero-downtime deployments.
- **Continuous Deployment Pipeline**: Automatically deploying to production after CI passes.

### Why We Think It's Valuable

This lesson completes the production infrastructure that makes AI agents deployable and maintainable:

1. **Closes the CI/CD loop**: Lesson 31 established CI for quality; this lesson adds CD for automated releases.
2. **Enables rapid iteration**: Prompt engineering is iterative. Manual deployment creates friction; CD removes it.
3. **Production-ready infrastructure**: Learners need to know how to deploy, not just build.
4. **Practical cloud skills**: GCP, Docker, and GitHub Actions are industry-standard tools.

### Expected Length of the Lesson

**5,500–6,500 words** (main instructional content, excluding code examples).

### Theory / Practice Ratio

40% theory - 60% real-world examples and infrastructure code

---

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 4 parts, each with multiple lessons.

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in their journey. You will be careful to consider the following:
- The points of view
- To not reintroduce concepts already taught in the previous lessons.
- To be careful when talking about concepts introduced only in future lessons
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is lesson 34 (from Part 3) of the course on AI agents.

**In scope:**
- gcloud CLI setup and configuration
- GCP infrastructure provisioning (Artifact Registry, Cloud SQL, Secret Manager, Workload Identity Federation)
- Manual deployment workflow with GitHub Actions
- Cloud Run concepts (services, revisions, autoscaling, health checks, zero-downtime deployments)
- Continuous deployment workflow triggered by CI success
- Feature flags for deployment control

**Out of scope (mention briefly, point forward):**
- Full Terraform/Pulumi IaC (acknowledge as more sophisticated alternative)
- Multi-region deployments
- Advanced monitoring and alerting beyond basics
- Kubernetes (Cloud Run is the focus)

### Point of View

The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

### Who Is the Intended Audience

Aspiring AI engineers who have built agent systems and are now learning to deploy them professionally.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:

**Part 3 (Production Engineering):**

- **Lesson 31 - Continuous Integration**: Pre-commit hooks, Ruff linting/formatting, unit tests with mocked LLMs, GitHub Actions CI pipelines, three-tier testing model.
- **Lesson 32 - Authentication & Docker**: Containerizing the research agent with Docker, implementing OAuth 2.0 authentication with Descope.
- **Lesson 33 - Database & Files**: Replacing file-based storage with PostgreSQL, database migrations with Alembic, rate limiting for API protection.

The reader already knows:
- How CI pipelines work and why they matter
- Docker containerization basics
- PostgreSQL database setup and migrations
- The research agent (Nova) architecture

### Concepts That Will Be Introduced in Future Lessons

**Part 4 (Capstone Project):**

- **Lesson 35 - Capstone Project**: The final project where learners apply everything from the course.

This is the final theory lesson before the capstone, so there are no new technical concepts to introduce after this.

### Anchoring the Reader in the Educational Journey

The reader has completed the full agent-building journey (Parts 1-2) and is now finishing the production engineering track (Part 3). They understand CI from Lesson 31, Docker and authentication from Lesson 32, and databases from Lesson 33. This lesson completes their DevOps knowledge by adding deployment.

Do not re-explain:
- What CI is or why it matters (covered in Lesson 31)
- Docker basics or Dockerfile structure (covered in Lesson 32)
- OAuth 2.0 or Descope authentication (covered in Lesson 32)
- PostgreSQL or Alembic migrations (covered in Lesson 33)

Reference these lessons when connecting concepts, but assume familiarity.

---

## Narrative Flow of the Lesson

Follow this story arc:

1. **Connection**: "We built CI, containerized our agent, and set up the database. Now we deploy it."
2. **Infrastructure Foundation**: Why command-line infrastructure matters over clicking through UIs.
3. **GCP Setup**: Step-by-step provisioning of all required cloud services.
4. **Manual Deployment**: A controlled deployment pipeline for initial setup and testing.
5. **Cloud Run Understanding**: The concepts needed to operate and monitor the deployed agent.
6. **Continuous Deployment**: Automating the full pipeline from commit to production.
7. **Completion**: The full CI/CD picture and transition to the capstone project.

---

## Lesson Outline

1. **Introduction: From CI to CD**
   - Connection to Lessons 31-33
   - What CD adds to the pipeline
   - Lesson scope and objectives

2. **Infrastructure as Code with gcloud**
   - Why command-line over UI
   - gcloud CLI setup
   - Our pragmatic approach (documented commands vs. Terraform)

3. **Setting Up GCP Services**
   - Architecture overview
   - Enabling APIs
   - Artifact Registry
   - Cloud SQL
   - Secret Manager
   - Workload Identity Federation
   - Cloud Run service account permissions

4. **The Manual Deployment Pipeline**
   - GitHub repository variables
   - Pipeline structure walkthrough
   - Step-by-step explanation
   - Triggering manual deployments

5. **Understanding Cloud Run**
   - Services and revisions
   - Autoscaling and cold starts
   - Health checks
   - Zero-downtime deployments
   - Monitoring and logging

6. **The Continuous Deployment Pipeline**
   - Automatic trigger after CI
   - Feature flag control
   - Conditional execution
   - Pros and cons of CD

7. **Conclusion**
   - The complete CI/CD picture
   - Summary of Lessons 31-34
   - Transition to capstone project

---

## Section-by-Section Writing Instructions

### Section 1 — Introduction: From CI to CD

**Source reference:** Use the opening paragraphs of `source.md` (lines 1-17) for the introduction and lesson overview.

**Content to cover:**

- **Quick reference to Lessons 31-33:** Summarize the journey so far in one paragraph:
  - Lesson 31: CI foundation (tests, linting, formatting)
  - Lesson 32: Docker containerization and OAuth authentication
  - Lesson 33: PostgreSQL database and rate limiting
  
- **What CD adds:** Explain that CI answers "does this code work?" while CD answers "can we ship it?" Use the explanation from `source.md` lines 5-7.

- **Why CD matters for AI agents:** Emphasize the prompt iteration benefit from `source.md` line 7: "Prompt engineering is inherently iterative... A manual deployment process creates friction."

- **Lesson scope:** List the four main topics from `source.md` lines 9-15.

**Transition to Section 2:** "Before we can deploy our agent, we need to provision cloud infrastructure. Let's start by understanding why we use command-line tools instead of web consoles."

**Section length:** 400-500 words

---

### Section 2 — Infrastructure as Code with gcloud

**Source reference:** Use Section 1 of `source.md` titled "Infrastructure as Code with gcloud" (lines 18-79).

**Content to cover:**

- **Why command-line infrastructure:** Cover the three drawbacks of UI-based configuration from `source.md` lines 24-29:
  - Not reproducible
  - Not version-controlled
  - Not automatable

- **Brief mention of Terraform:** Acknowledge Terraform/Pulumi as the "most sophisticated form of IaC" from `source.md` lines 33-37, but explain why we take a pragmatic middle ground.

- **Installing gcloud:** Show the authentication and configuration commands from `source.md` lines 52-67.

- **Our documented approach:** Explain the benefits listed in `source.md` lines 71-77:
  - Reproducibility
  - Documentation
  - Reviewability
  - Simplicity

- **Acknowledge the tradeoff:** Mention idempotency concerns from `source.md` line 78.

**Transition to Section 3:** "With gcloud configured, we can now provision the infrastructure our research agent needs. Let's walk through each component."

**Section length:** 600-700 words

---

### Section 3 — Setting Up GCP Services

**Source reference:** Use Section 2 of `source.md` titled "Setting Up GCP Services" (lines 80-381).

**Content to cover:**

- **Architecture overview:** Include the mermaid diagram from `source.md` lines 88-108 showing how GitHub Actions, Artifact Registry, Secret Manager, Cloud Run, and Cloud SQL connect.

- **Environment variables:** Show the setup commands from `source.md` lines 112-123.

- **Enabling APIs:** Explain each API and its purpose from `source.md` lines 127-148.

- **Artifact Registry:** Explain its role as the bridge between build and deployment from `source.md` lines 149-162.

- **Cloud SQL:** Walk through the instance creation and configuration options from `source.md` lines 164-216.

- **Secret Manager:** Explain why it's essential (runtime injection, rotation, audit trail) from `source.md` lines 218-242.

- **Workload Identity Federation:** This is the most complex subsection. Explain:
  - What service accounts are (from `source.md` lines 250-251)
  - What Workload Identity Federation does (from `source.md` lines 252-254)
  - The three components: pool, provider, service account
  - Walk through each command with explanations from `source.md` lines 257-345

- **Cloud Run service account:** Brief coverage from `source.md` lines 347-367.

- **Getting values for GitHub:** The output commands from `source.md` lines 371-379.

**Transition to Section 4:** "With infrastructure provisioned, we can deploy our agent. We start with a manual deployment pipeline that gives explicit control over when deployments happen."

**Section length:** 1,200-1,400 words

---

### Section 4 — The Manual Deployment Pipeline

**Source reference:** Use Section 3 of `source.md` titled "The Manual Deployment Pipeline" (lines 383-695).

**Content to cover:**

- **GitHub repository variables:** Show the table from `source.md` lines 393-399 explaining what variables to configure.

- **Full pipeline file:** Include the complete YAML from `source.md` lines 405-521. This is the reference implementation.

- **Key components explained:**
  - Workflow trigger (`workflow_dispatch`) from `source.md` lines 525-540
  - Environment variables from `source.md` lines 542-554
  - Permissions block from `source.md` lines 556-568

- **Step-by-step explanation:** Walk through each pipeline step:
  - Authentication with GCP (lines 572-583)
  - Docker configuration (lines 585-593)
  - Build Docker image (lines 595-608)
  - Push to Artifact Registry (lines 610-617)
  - Deploy to Cloud Run (lines 619-665) — explain the key flags
  - Smoke test (lines 667-679)

- **How to trigger:** The GitHub UI steps from `source.md` lines 683-695.

**Transition to Section 5:** "After your first deployment, you need to understand Cloud Run to effectively monitor and operate your agent in production."

**Section length:** 900-1,000 words

---

### Section 5 — Understanding Cloud Run

**Source reference:** Use Section 4 of `source.md` titled "Understanding Cloud Run" (lines 697-867).

**Content to cover:**

- **What is a Cloud Run service:** Basic definition from `source.md` lines 700-708.

- **Revisions and version management:** Explain the immutable snapshot concept from `source.md` lines 710-741. Include the mermaid diagram showing revisions.

- **Autoscaling:** Cover the scaling parameters from `source.md` lines 743-768:
  - `min-instances` and scale-to-zero
  - `max-instances` for cost control
  - `concurrency` for scaling triggers

- **Cold starts:** Explain the tradeoff from `source.md` lines 760-765.

- **Health checks:** Brief coverage from `source.md` lines 772-779.

- **Service URL and load balancing:** Explain the URL format and what the load balancer handles from `source.md` lines 781-804.

- **Monitoring and logging:** Cover Cloud Logging and Cloud Monitoring from `source.md` lines 806-822.

- **Zero-downtime deployments:** Explain the gradual traffic migration from `source.md` lines 824-867. Include the sequence diagram.

**Transition to Section 6:** "The manual pipeline gives control, but it requires human intervention. Continuous Deployment automates this: every change that passes CI is automatically deployed to production."

**Section length:** 800-900 words

---

### Section 6 — The Continuous Deployment Pipeline

**Source reference:** Use Section 5 of `source.md` titled "The Continuous Deployment Pipeline" (lines 869-1072).

**Content to cover:**

- **Connection to Lesson 31:** Explicitly reference that this is the final step in the CI/CD chain from `source.md` line 871.

- **Full auto-deploy pipeline:** Include the YAML from `source.md` lines 877-956.

- **Automatic trigger after CI:** Explain `workflow_run` from `source.md` lines 962-980. Include the mermaid diagram showing the deployment chain.

- **Feature flag (AUTO_DEPLOY_ENABLED):** Explain the kill switch from `source.md` lines 984-1008.

- **Conditional execution:** The `if` conditions from `source.md` lines 1010-1024.

- **Referencing the triggering commit:** The `head_sha` explanation from `source.md` lines 1026-1037.

- **Pros and cons of CD:** Cover both sides from `source.md` lines 1039-1072:
  - Advantages: faster iteration, smaller releases, reduced manual work, continuous feedback
  - Disadvantages: requires strong CI, requires monitoring, not suitable for all changes, blast radius
  - When to use and when not to use

**Transition to Section 7:** "With continuous deployment in place, we have completed the full DevOps pipeline for AI agents."

**Section length:** 800-900 words

---

### Section 7 — Conclusion

**Source reference:** Use the Conclusion section of `source.md` (lines 1074-1121).

**Content to cover:**

- **The complete CI/CD picture:** Include the final mermaid diagram from `source.md` lines 1078-1113 showing the full pipeline from code to production.

- **Summary of Lessons 31-34:** Recap what was built across all four lessons from `source.md` lines 1115-1119:
  - Lesson 31: CI foundation
  - Lesson 32: Docker and authentication
  - Lesson 33: PostgreSQL and rate limiting
  - Lesson 34: Deployment and CD

- **Key takeaways:** The practical benefits of the infrastructure we built from `source.md` lines 1119-1120.

- **Transition to capstone:** Reference that this concludes the theory portion and the next lesson introduces the capstone project from `source.md` lines 1121.

**Section length:** 400-500 words

---

## Article Code

Files to reference explicitly throughout the article:

- `source.md` — The comprehensive source document covering all CD topics (primary reference for each section)

## Sources

1. [Google Cloud - Infrastructure as Code with Terraform](https://cloud.google.com/docs/terraform)
2. [Terraform Introduction](https://www.terraform.io/)
3. [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install)
4. [Artifact Registry documentation](https://cloud.google.com/artifact-registry/docs)
5. [Secret Manager documentation](https://cloud.google.com/secret-manager/docs)
6. [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)
7. [GitHub Actions - workflow_dispatch](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch)
8. [GitHub - OpenID Connect security hardening](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
9. [Cloud Run documentation](https://cloud.google.com/run/docs)
10. [Cloud Run autoscaling](https://cloud.google.com/run/docs/about-instance-autoscaling)
11. [Cloud Run health checks](https://cloud.google.com/run/docs/configuring/healthchecks)
12. [Cloud Run logging](https://cloud.google.com/run/docs/logging)
13. [Cloud Run monitoring](https://cloud.google.com/run/docs/monitoring)
14. [Cloud Run rollouts and traffic migration](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)
15. [GitHub Actions - workflow_run](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_run)
