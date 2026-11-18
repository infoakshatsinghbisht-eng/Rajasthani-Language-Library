# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Presumptive & Epistemic Modality
=============================================================
Expresses presumption, deduction, and inferential conjecture:
- Imperfective participle + होसी (e.g. 'वो पढ़तो होसी' - He must be studying)
- Perfective participle + होसी (e.g. 'ऊँ घर गयो होसी' - He must have gone home)
"""

from typing import Dict
from rajasthani.constants import Gender, GrammaticalNumber


def presumptive_clause(subject: str, verb_root: str, aspect: str = "imperfective", gender: Gender = Gender.MASCULINE) -> str:
    """
    Constructs an epistemic presumptive sentence in Rajasthani.
    """
    if aspect == "imperfective":
        participle = f"{verb_root}ती" if gender == Gender.FEMININE else f"{verb_root}तो"
    else:  # perfective
        participle = f"{verb_root}ी" if gender == Gender.FEMININE else f"{verb_root}यो"

    copula = "होसी"
    return f"{subject} {participle} {copula}।"
