def judge(question: str, expects: str, answer: str, results) -> bool:
    """
    Check whether the expected answer appears in the generated answer.

    Args:
        question: The question that was asked.
        expects: The expected answer or text to look for.
        answer: The generated answer to evaluate.
        results: Retrieval results associated with the question.

    Returns:
        True if the expected answer appears in the generated answer,
        ignoring leading/trailing whitespace and capitalization.
        False if no expected answer is provided or the expected answer
        is not found.
    """
    if not expects:
        return False

    return expects.strip().lower() in (answer or "").strip().lower()