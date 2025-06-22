from agents.summarizer_agent import summarize

def synthesize(paper_summaries):
    # Step 1: Create a prompt that encourages synthesis
    combined_input = (
        "The following are summaries of research papers on a similar topic:\n\n"
    )
    for i, summary in enumerate(paper_summaries, 1):
        combined_input += f"Paper {i} Summary:\n{summary}\n\n"

    combined_input += (
        "Please synthesize the above summaries into a coherent overview that highlights:\n"
        "- The main shared contributions\n"
        "- Key differences (if any)\n"
        "- Overall insights or trends\n"
        "Avoid repeating the same points. Provide a unified synthesis."
    )

    # Step 2: Use summarizer to process the smart synthesis
    final_synthesis = summarize(combined_input, max_len=2048)
    return final_synthesis
