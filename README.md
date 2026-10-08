# LangChain App with LangSmith Tracing

A simple LangChain application that sends multiple prompts to OpenAI using `ChatOpenAI` and automatically tracks each run with LangSmith.

This project demonstrates how LangSmith can record:

* Prompts sent to the model
* Model responses
* Latency
* Token usage
* Individual application runs
* Project-level run history

The application uses **environment variables** to enable LangSmith tracing. No LangSmith tracing code is included in the Python application.

---

## 1. Project Overview

### Objective

Build a small LangChain application that:

1. Uses LangChain's `ChatOpenAI`.
2. Sends at least three different prompts.
3. Prints each model response.
4. Enables LangSmith tracing using environment variables.
5. Groups all runs under the LangSmith project `caie-week2`.
6. Allows the runs to be inspected in the LangSmith dashboard.
7. Shows the exact prompt, response, latency, and token usage for a run.

### Technologies

* Python
* LangChain
* LangChain OpenAI integration
* OpenAI
* LangSmith
* Git / GitHub
* Windows Command Prompt

---

# 2. Project Structure

```text
traced-app/
│
├── traced_app.py
├── README.md
├── .gitignore
├── .env.example
└── venv/
```

> The `venv/` directory should not be uploaded to GitHub.

---

# 3. Prerequisites

Make sure Python is installed.

Check the Python version:

```cmd
python --version
```

Example:

```text
Python 3.11.0
```

You also need:

* An OpenAI API key
* A LangSmith account
* A LangSmith API key
* Git, if uploading the project to GitHub

---

# 4. Create the Project

Open **Windows Command Prompt**.

Create the project directory:

```cmd
mkdir traced-app
cd traced-app
```

---

# 5. Create a Virtual Environment

Create the virtual environment:

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

After activation, the command prompt should show:

```text
(venv)
```

Example:

```text
(venv) C:\Users\YourName\traced-app>
```

---

# 6. Install Required Packages

Install LangChain, LangChain OpenAI integration, and LangSmith:

```cmd
pip install langsmith langchain langchain-openai
```

After installation, verify the packages:

```cmd
pip list
```

You should see packages related to:

```text
langchain
langchain-openai
langsmith
```

---

# 7. Create a LangSmith Account

Open:

https://smith.langchain.com/

Create or sign in to your LangSmith account.

Create an API key from your LangSmith settings.

Keep this API key private.

---

# 8. Get an OpenAI API Key

You also need an OpenAI API key to use `ChatOpenAI`.

Keep your OpenAI API key private.

Never commit your API key to GitHub.

---

# 9. Configure Environment Variables

This project uses environment variables for configuration.

Because this project is being run from **Windows Command Prompt**, use the `set` command.

Set LangSmith tracing:

```cmd
set LANGSMITH_TRACING=true
```

Set your LangSmith API key:

```cmd
set LANGSMITH_API_KEY=YOUR_LANGSMITH_API_KEY
```

Set the LangSmith project:

```cmd
set LANGSMITH_PROJECT=caie-week2
```

Set your OpenAI API key:

```cmd
set OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Replace the placeholder values with your actual keys.

---

# 10. Verify the Environment Variables

Before running the application, verify that tracing is enabled.

Check LangSmith tracing:

```cmd
echo %LANGSMITH_TRACING%
```

Expected result:

```text
true
```

Check the project:

```cmd
echo %LANGSMITH_PROJECT%
```

Expected result:

```text
caie-week2
```

You can also check that the API key variables exist:

```cmd
echo %LANGSMITH_API_KEY%
echo %OPENAI_API_KEY%
```

Do not share the output of these commands because they contain secret API keys.

---

# 11. Create `traced_app.py`

Create a file named:

```text
traced_app.py
```

The application uses LangChain's `ChatOpenAI`.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain LangChain in one simple paragraph.",
    "Explain how LangSmith helps developers debug AI applications.",
    "Explain why tracking latency and token usage is important when building an AI application. Give three practical examples."
]

for i, prompt in enumerate(prompts, 1):
    response = llm.invoke(prompt)

    print(f"\n--- Run {i} ---")
    print(f"Prompt: {prompt}")
    print(f"Answer: {response.content}")
```

---

# 12. Important: No LangSmith Code in `traced_app.py`

The Python file does not contain LangSmith tracing code.

There is no:

```python
from langsmith import ...
```

There is no:

```python
os.environ["LANGSMITH_TRACING"] = "true"
```

There is no:

```python
@traceable
```

Tracing is enabled only through environment variables.

This satisfies the assignment requirement:

> Turn tracing on with environment variables only. No tracing code in the file.

---

# 13. Run the Application

Make sure the virtual environment is active:

```cmd
venv\Scripts\activate
```

Then run:

```cmd
python traced_app.py
```

The application sends three different prompts to OpenAI.

Example output:

```text
--- Run 1 ---
Prompt: Explain LangChain in one simple paragraph.
Answer: ...

--- Run 2 ---
Prompt: Explain how LangSmith helps developers debug AI applications.
Answer: ...

--- Run 3 ---
Prompt: Explain why tracking latency and token usage is important when building an AI application. Give three practical examples.
Answer: ...
```

The exact responses will vary.

---

# 14. Verify LangSmith Tracing

Open:

https://smith.langchain.com/

Find the project:

```text
caie-week2
```

The three application runs should appear in the project.

You should see something similar to:

```text
caie-week2

Run 1
Run 2
Run 3
```

If the three runs appear, LangSmith tracing is working.

---

# 15. Inspect an Individual Run

Open one of the runs in LangSmith.

Inspect the run details.

You should be able to find:

### Input

The exact prompt sent to the model.

### Output

The model's response.

### Model

The model used by the application:

```text
gpt-4o-mini
```

### Latency

The amount of time taken by the model request.

### Token Usage

The run's token information, such as:

```text
Input tokens
Output tokens
Total tokens
```

The exact values depend on the actual responses generated during the run.

---

# 16. Compare the Three Runs

Compare the three runs in LangSmith.

Look at:

* Latency
* Input tokens
* Output tokens
* Total tokens

The run with the highest token usage is generally the most expensive of the three.

For example:

```text
Run 1 → lower token usage
Run 2 → medium token usage
Run 3 → highest token usage
```

If the third prompt requests a detailed answer and multiple examples, a higher token count can be reasonable.

---

# 17. Assignment Questions

## How do you check that tracing is actually on?

Before checking LangSmith, verify the environment variables:

```cmd
echo %LANGSMITH_TRACING%
```

It should return:

```text
true
```

Also verify:

```cmd
echo %LANGSMITH_PROJECT%
```

It should return:

```text
caie-week2
```

After running the application, confirm that the three runs appear inside the `caie-week2` LangSmith project.

If the runs appear, tracing is working.

---

## Which prompt is the expensive one?

Compare the token usage of all three runs in LangSmith.

The prompt with the highest token usage is the most expensive of the three.

If the prompt requests a longer explanation or multiple examples, the additional token usage may be justified.

The actual answer should be based on the token counts shown in your LangSmith project.

---

# 18. Screenshots Required

The assignment requires two screenshots.

## Screenshot 1 — LangSmith Project

Open the:

```text
caie-week2
```

project in LangSmith.

Capture a screenshot showing all three runs.

The screenshot should demonstrate that:

```text
Run 1
Run 2
Run 3
```

were successfully recorded.

---

## Screenshot 2 — Individual Run

Open one of the runs.

Capture a screenshot showing:

* Exact prompt
* Model response
* Latency
* Token usage

This demonstrates that LangSmith is recording the details of the model request.

---

# 19. `.env.example`

A `.env.example` file can be used as a safe template.

Example:

```text
OPENAI_API_KEY=your-openai-api-key
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=caie-week2
```

Do **not** put real API keys in this file.

The `.env.example` file is only a template.

---

# 20. `.gitignore`

Create a `.gitignore` file:

```text
venv/
__pycache__/
*.pyc
.env
```

This prevents the virtual environment, Python cache files, and `.env` secrets from being uploaded to GitHub.

---

# 21. Security

Never upload API keys to GitHub.

Do not put real keys inside:

```text
traced_app.py
```

Do not put real keys inside:

```text
.env.example
```

If you use a `.env` file locally, make sure it is included in `.gitignore`.

Example:

```text
.env
```

should be ignored by Git.

---

# 22. GitHub Upload

Initialize Git:

```cmd
git init
```

Add the required files:

```cmd
git add traced_app.py README.md .gitignore .env.example
```

Commit the project:

```cmd
git commit -m "Add LangChain LangSmith tracing app"
```

Create a GitHub repository and connect the local repository to it using the GitHub commands provided when creating the repository.

Push the project to GitHub.

The repository should contain:

```text
traced-app/
│
├── traced_app.py
├── README.md
├── .gitignore
└── .env.example
```

The `venv/` directory should not be uploaded.

---

# 23. Final Workflow

The complete workflow is:

```text
Windows CMD
     |
     v
Create traced-app
     |
     v
Create Python virtual environment
     |
     v
Activate venv
     |
     v
Install LangChain packages
     |
     v
Create OpenAI API key
     |
     v
Create LangSmith API key
     |
     v
Set environment variables
     |
     v
Verify LANGSMITH_TRACING=true
     |
     v
Create traced_app.py
     |
     v
Use ChatOpenAI
     |
     v
Send 3 different prompts
     |
     v
Run python traced_app.py
     |
     v
Open LangSmith
     |
     v
Open caie-week2
     |
     +----------------------+
     |                      |
     v                      v
  3 runs               Open one run
                            |
                            v
                 Prompt / Response
                 Latency / Tokens
                            |
                            v
                      Take screenshots
                            |
                            v
                      Upload GitHub
```

---

# 24. Final Submission Checklist

Before submitting, verify everything:

* [ ] Python installed
* [ ] Virtual environment created
* [ ] Required packages installed
* [ ] OpenAI API key configured
* [ ] LangSmith API key configured
* [ ] `LANGSMITH_TRACING=true`
* [ ] `LANGSMITH_PROJECT=caie-week2`
* [ ] `traced_app.py` created
* [ ] `traced_app.py` uses `ChatOpenAI`
* [ ] Three different prompts are used
* [ ] Three answers are printed
* [ ] Three runs appear in LangSmith
* [ ] One run shows the exact prompt
* [ ] One run shows the response
* [ ] One run shows latency
* [ ] One run shows token counts
* [ ] Most expensive run identified
* [ ] LangSmith project screenshot taken
* [ ] Individual run screenshot taken
* [ ] `.gitignore` created
* [ ] No API keys committed
* [ ] `traced_app.py` uploaded to GitHub
* [ ] `README.md` uploaded to GitHub
* [ ] GitHub link ready for submission
* [ ] WhatsApp link ready
* [ ] Community video completed

---

# 25. Key Learning

The main lesson from this assignment is that LangSmith tracing can be enabled without adding tracing logic to the application.

The application only needs to use LangChain:

```python
from langchain_openai import ChatOpenAI
```

and:

```python
llm = ChatOpenAI(model="gpt-4o-mini")
```

Tracing is enabled externally through:

```text
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=...
LANGSMITH_PROJECT=caie-week2
```

This allows developers to inspect prompts, responses, latency, token usage, and errors without changing the application's core logic.
