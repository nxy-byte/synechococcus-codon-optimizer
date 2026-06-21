# Codon Optimizer for Synechococcus elongatus

## What is this?
A Python script that optimizes any DNA sequence for expression in 
*Synechococcus elongatus* — a cyanobacterium widely used in photosynthesis 
and carbon fixation research.

## Motivation
RuBisCO (Ribulose-1,5-bisphosphate carboxylase/oxygenase) is the primary 
enzyme responsible for carbon fixation in photosynthesis. Despite being the 
most abundant enzyme on Earth, RuBisCO is notoriously inefficient — it evolved 
billions of years ago and is poorly adapted to current atmospheric CO₂ levels.

*Synechococcus elongatus* is a model cyanobacterium used in research aimed at 
engineering more efficient RuBisCO variants and carbon fixation pathways. 
This tool was built to optimize RuBisCO gene sequences for expression in 
*S. elongatus* as part of exploring computational approaches to photosynthesis 
engineering.

## Background
Different organisms prefer different codons to encode the same amino acid. 
When expressing a foreign gene in a new organism, using that organism's 
preferred codons significantly improves protein expression efficiency. 
This tool replaces each codon in an input sequence with the preferred 
codon for *S. elongatus*.

## Features
- Translates input DNA sequence to amino acids
- Optimizes each codon using *S. elongatus* codon preference table
- Outputs optimized sequence with length comparison

## Built with
Python 3

## Author
Kritika | B.Tech Biotechnology, GGSIPU  
Inspired by Dr. Dave Savage's work on CO₂ fixation engineering — IGI, UC Berkeley
## Author
Kritika | B.Tech Biotechnology, GGSIPU  
Inspired by Dr. Dave Savage's work on CO₂ fixation engineering — IGI, UC Berkeley
