# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Deliberative & Hortative Subjunctive
=================================================================
Consultative deliberative questions and collective proposals:
- 'म्हूँ के करूँ?' (What shall I do?)
- 'चालो, घर चालां!' (Come, let us go home! - Hortative)
"""

from typing import Dict


def deliberative_question(subject: str, verb_root: str) -> str:
    """
    Constructs a consultative deliberative question.
    """
    if "म्हूँ" in subject:
        if verb_root.endswith("ा"):
            return f"{subject} के {verb_root[:-1]}ाऊँ?"
        return f"{subject} के {verb_root}ूँ?"
    return f"{subject} के {verb_root}वै?"


def hortative_proposal(verb_root: str) -> str:
    """
    Constructs an inclusive hortative proposal ('Let us do X!').
    Examples:
        >>> hortative_proposal("चाल")
        'चालो, चालां!'
    """
    return f"चालो, {verb_root}ां!"
