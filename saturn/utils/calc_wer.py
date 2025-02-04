#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import logging
import saturn.utils.set_logging
logger = logging.getLogger(__name__.split('.')[-1])

import numpy as np

def align_text_and_calculate_edit_distance(ref, hyp):
    """
    Aligns the reference and hypothesis texts, highlights insertions, deletions, and substitutions,
    and calculates the Levenshtein distance along with the number of insertions, deletions, and substitutions.
    """
    ref_words = ref.split()
    hyp_words = hyp.split()
    dp = np.zeros((len(ref_words) + 1, len(hyp_words) + 1), dtype=int)
    insertions, deletions, substitutions = 0, 0, 0

    # Fill the dp table
    for i in range(len(ref_words) + 1):
        dp[i][0] = i
    for j in range(len(hyp_words) + 1):
        dp[0][j] = j

    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # Backtrack to align text and highlight insertions, deletions, and substitutions
    i, j = len(ref_words), len(hyp_words)
    ref_aligned, hyp_aligned = [], []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref_words[i - 1] == hyp_words[j - 1]:
            ref_aligned.append(ref_words[i - 1])
            hyp_aligned.append(hyp_words[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == 1 + dp[i - 1][j - 1]:
            # Substitution (change)
            substitutions += 1
            ref_aligned.append(f"<span style='color: red;'><del>{ref_words[i - 1]}</del></span>")
            hyp_aligned.append(f"<span style='color: blue;'>{hyp_words[j - 1]}</span>")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == 1 + dp[i - 1][j]:
            # Deletion (in reference)
            deletions += 1
            ref_aligned.append(f"<span style='color: red;'><del>{ref_words[i - 1]}</del></span>")
            hyp_aligned.append("")
            i -= 1
        elif j > 0 and dp[i][j] == 1 + dp[i][j - 1]:
            # Insertion (in hypothesis)
            insertions += 1
            ref_aligned.append("")
            hyp_aligned.append(f"<span style='color: green;'>{hyp_words[j - 1]}</span>")
            j -= 1

    ref_aligned.reverse()
    hyp_aligned.reverse()

    # Total edit distance
    edit_distance = dp[len(ref_words)][len(hyp_words)]
    error_rate = edit_distance / len(ref_words)

    logger.info(f"Words in reference: {len(ref_words)}")
    logger.info(f"Words in hypothesis: {len(hyp_words)}")
    logger.info(f"Edit distance: {edit_distance}")
    logger.info(f"Error rate: {error_rate:.3f}")
    logger.info(f"Insertions: {insertions}")
    logger.info(f"Deletions: {deletions}")
    logger.info(f"Substitutions: {substitutions}")

    return (' '.join(ref_aligned), ' '.join(hyp_aligned)), (error_rate, insertions, deletions, substitutions)


# Function to calculate edit distance with insertion, deletion, and substitution counts
def edit_distance_detailed(ref, hyp):
    """Calculates the Levenshtein distance between reference and hypothesis
    and returns the number of insertions, deletions, and substitutions.
    """
    dp = np.zeros((len(ref) + 1, len(hyp) + 1), dtype=int)
    insertions, deletions, substitutions = 0, 0, 0

    for i in range(len(ref) + 1):
        dp[i][0] = i
    for j in range(len(hyp) + 1):
        dp[0][j] = j

    for i in range(1, len(ref) + 1):
        for j in range(1, len(hyp) + 1):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # Backtracking to find insertions, deletions, substitutions
    i, j = len(ref), len(hyp)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref[i - 1] == hyp[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == 1 + dp[i - 1][j - 1]:
            substitutions += 1
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == 1 + dp[i - 1][j]:
            deletions += 1
            i -= 1
        elif j > 0 and dp[i][j] == 1 + dp[i][j - 1]:
            insertions += 1
            j -= 1

    return dp[len(ref)][len(hyp)], insertions, deletions, substitutions

# Function to calculate Word Error Rate (WER) and return detailed info
def wer_detailed(ref, hyp):
    """Calculate the Word Error Rate and return details of insertions, deletions, substitutions."""
    ref_words = ref.split()
    hyp_words = hyp.split()
    distance, insertions, deletions, substitutions = edit_distance_detailed(ref_words, hyp_words)
    total_words = len(ref_words)
    wer_value = distance / total_words
    return wer_value, total_words, insertions, deletions, substitutions

# Function to calculate Character Error Rate (CER) and return detailed info
def cer_detailed(ref, hyp):
    """Calculate the Character Error Rate and return details of insertions, deletions, substitutions."""
    distance, insertions, deletions, substitutions = edit_distance_detailed(ref, hyp)
    total_chars = len(ref)
    cer_value = distance / total_chars
    return cer_value, total_chars, insertions, deletions, substitutions
