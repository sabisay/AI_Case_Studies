from langchain_core.messages import HumanMessage, SystemMessage
from embeddings import llm_json_mode
from ragPrompt import docs_txt, generation
import json

### Hallucination Grader

hallucination_grader_instructions = """
You are a teacher grading a quiz about *Alice in Wonderland*. 

You will be given FACTS from *Alice in Wonderland* and a STUDENT ANSWER.

Grading criteria:
1. Ensure the STUDENT ANSWER is grounded in the FACTS provided.
2. Ensure the STUDENT ANSWER does not contain "hallucinated" information outside the scope of the FACTS.

Return a JSON object with:
- 'binary_score': 'yes' or 'no' indicating if the STUDENT ANSWER is grounded in the FACTS.
- 'explanation': A detailed step-by-step explanation justifying the score, mentioning any hallucinations or correct alignments.
"""

hallucination_grader_prompt = """FACTS: \n\n {documents} \n\n STUDENT ANSWER: {generation}. 

Return a JSON object with:
1. "binary_score": 'yes' or 'no'.
2. "explanation": Detailed step-by-step reasoning for the score.
"""

# Format the hallucination grader prompt with documents and generation
hallucination_grader_prompt_formatted = hallucination_grader_prompt.format(
    documents=docs_txt, generation=generation.content
)

# Invoke the LLM to evaluate hallucination
result = llm_json_mode.invoke(
    [SystemMessage(content=hallucination_grader_instructions)]
    + [HumanMessage(content=hallucination_grader_prompt_formatted)]
)

# Parse and print the JSON result
try:
    graded_output = json.loads(result.content)
    print("Binary Score:", graded_output["binary_score"])
    print("Explanation:", graded_output["explanation"])
except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
except KeyError as e:
    print(f"Missing key in response: {e}")
