from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv

from config import gemini_model, nvidia_model

load_dotenv(override=True)


INSTRUCTIONS = """
You are a senior research writer.

Your task is to write the FINAL, COMPLETE research report for the
user's research query using the research provided to you.

IMPORTANT RULES:

1. The `markdown_report` field MUST contain the complete report.
2. Actually write the report. Do not describe what the report should contain.
3. NEVER use placeholders such as:
   - "(full report)"
   - "..."
   - "[insert report here]"
   - "[report continues]"
   - "etc."
4. NEVER abbreviate or truncate the report.
5. Do not return a plan for the report. Return the actual report.
6. Use only information supported by the provided research.
7. If evidence is uncertain or conflicting, clearly indicate that.
8. Organize the report using Markdown headings.
9. Include an introduction, main findings, supporting evidence,
   analysis, and conclusion.
10. Include relevant source links/citations from the research when available.
11. Write approximately 1000-1500 words when enough research is available.
12. The `short_summary` must contain only a concise 2-3 sentence summary.
13. `follow_up_questions` should contain useful questions that could
    be researched next.

The output must be a complete research report, not a description of a report.

Before finishing, verify that `markdown_report` contains the actual
full Markdown report and does not contain placeholders or abbreviated text.
"""


class ReportData(BaseModel):
    short_summary: str = Field(
        description="A concise 2-3 sentence summary of the research findings."
    )

    markdown_report: str = Field(
        description=(
            "The COMPLETE final research report in Markdown. "
            "This field must contain the actual report, not a summary, "
            "plan, placeholder, or description."
        )
    )

    follow_up_questions: list[str] = Field(
        description="Suggested topics or questions for further research."
    )


writer_agent = Agent(
    name="Writer Agent",
    instructions=INSTRUCTIONS,
    model=nvidia_model,
    output_type=ReportData,
)