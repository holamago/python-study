#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022 SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import re
from typing import Dict, Text

SPECIALCHARS="‘’“”!@#$^&*()\[\]{};:,./<>|?`~\-=_+\"\\\\"
ENG_LANG_PACK="[\u0021-\u007E|1-9|'|\n]+"

def normalize_english_text(
    text: Text,
)-> Text:
    """
    Text normalization for movie english
    """
    text = ' '.join(text.split())
    text = text.replace("’", "'").replace("`","'").replace("′", "'").lower()
    text = re.sub("[" + SPECIALCHARS + "]", " ", text)
    return ' '.join(re.findall(ENG_LANG_PACK, text))

def compute_wer(
    ref: Text,
    hyp: Text,
    debug=False,
    mode="wer",
)-> Dict:
    """
    Compute WER/CER

    Parameters
    ----------
    ref: Text
        Reference text
    hyp: Text
        Hypothesis text
    debug: bool
        Debug mode
    mode: Text
        Mode for computing WER/CER
    """
    if mode == "wer":
        r = normalize_english_text(ref).split()
        h = hyp.split()
    else:
        r = list(normalize_english_text(ref))
        h = list(hyp)

    #costs will holds the costs, like in the Levenshtein distance algorithm
    costs = [[0 for inner in range(len(h)+1)] for outer in range(len(r)+1)]
    # backtrace will hold the operations we've done.
    # so we could later backtrace, like the WER algorithm requires us to.
    backtrace = [[0 for inner in range(len(h)+1)] for outer in range(len(r)+1)]

    OP_OK = 0
    OP_SUB = 1
    OP_INS = 2
    OP_DEL = 3

    DEL_PENALTY=1 # Tact
    INS_PENALTY=1 # Tact
    SUB_PENALTY=1 # Tact
    # First column represents the case where we achieve zero
    # hypothesis words by deleting all reference words.
    for i in range(1, len(r)+1):
        costs[i][0] = DEL_PENALTY*i
        backtrace[i][0] = OP_DEL

    # First row represents the case where we achieve the hypothesis
    # by inserting all hypothesis words into a zero-length reference.
    for j in range(1, len(h) + 1):
        costs[0][j] = INS_PENALTY * j
        backtrace[0][j] = OP_INS

    # computation
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                costs[i][j] = costs[i-1][j-1]
                backtrace[i][j] = OP_OK
            else:
                substitutionCost = costs[i-1][j-1] + SUB_PENALTY # penalty is always 1
                insertionCost    = costs[i][j-1] + INS_PENALTY   # penalty is always 1
                deletionCost     = costs[i-1][j] + DEL_PENALTY   # penalty is always 1

                costs[i][j] = min(substitutionCost, insertionCost, deletionCost)
                if costs[i][j] == substitutionCost:
                    backtrace[i][j] = OP_SUB
                elif costs[i][j] == insertionCost:
                    backtrace[i][j] = OP_INS
                else:
                    backtrace[i][j] = OP_DEL

    # back trace though the best route:
    i = len(r)
    j = len(h)
    numSub = 0
    numDel = 0
    numIns = 0
    numCor = 0

    ref_status = []

    if debug:
        print("OP\tREF\tHYP")
        lines = []
    while i > 0 or j > 0:
        if backtrace[i][j] == OP_OK:
            numCor += 1
            i-=1
            j-=1
            if mode == "wer":
                ref_status.append({
                    "status": "OK",
                    "ref": r[i],
                    "hyp": h[j],
                    "ref_index": i,
                    "hyp_index": j,
                })
            if debug:
                lines.append("OK\t" + r[i]+"\t"+h[j])
        elif backtrace[i][j] == OP_SUB:
            numSub +=1
            i-=1
            j-=1
            if mode == "wer":
                ref_status.append({
                    "status": "SUB",
                    "ref": r[i],
                    "hyp": h[j],
                    "ref_index": i,
                    "hyp_index": j,
                })
            if debug:
                lines.append("SUB\t" + r[i]+"\t"+h[j])
        elif backtrace[i][j] == OP_INS:
            numIns += 1
            j-=1
            if mode == "wer":
                ref_status.append({
                    "status": "INS",
                    "ref": "",
                    "hyp": h[j],
                    "ref_index": -1,
                    "hyp_index": j,
                })
            if debug:
                lines.append("INS\t" + "****" + "\t" + h[j])
        elif backtrace[i][j] == OP_DEL:
            numDel += 1
            i-=1
            if mode == "wer":
                ref_status.append({
                    "status": "DEL",
                    "ref": r[i],
                    "hyp": "",
                    "ref_index": -i,
                    "hyp_index": -1,
                })
            if debug:
                lines.append("DEL\t" + r[i]+"\t"+"****")
    if debug:
        lines = reversed(lines)
        for line in lines:
            print(line)
        print("Ncor " + str(numCor))
        print("Nsub " + str(numSub))
        print("Ndel " + str(numDel))
        print("Nins " + str(numIns))
    # return (numSub + numDel + numIns) / (float) (len(r))
    wer_result = round( (numSub + numDel + numIns) / (float) (len(r)), 3)

    ref_status.reverse()
    return {
        'wer':wer_result,
        'cor':numCor,
        'sub':numSub,
        'ins':numIns,
        'del':numDel,
        "status": ref_status,
    }
