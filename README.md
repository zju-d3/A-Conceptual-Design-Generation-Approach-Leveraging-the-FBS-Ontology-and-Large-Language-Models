# FBS

## Introduction

Recent research in the field of design engineering is more or less focusing on using AI technologies such as Large Language Models (LLMs) to assist early stage design. The engineer or designer can use LLMs to explore, validate and compare thousands of generated conceptual stimuli and make final choices. This was seen as a significant stride in advancing the status of the generative approach in computer-aided design. However, it is often difficult to instruct LLMs to obtain conceptual solutions been novel and requirement-compliant in real design tasks, due to the lack of transparency and insufficient controllability of LLMs. This paper presents an approach to leverage LLMs to infer Function-Behavior-Structure (FBS) ontology for high-quality design concepts. Prompting design based on the FBS model decomposes the design task into three sub-tasks including functional, behavioral, and structural reasoning. In each sub-task, prompting templates and specification signifiers are specified to guide the LLMs to generate concepts. Human can determine the selected concepts by judging and evaluating the generated function-structure pairs. A comparative experiment has been conducted to evaluate the concept generation approach. The results indicate that our approach achieves the highest scores in concept evaluation. Generated concepts are more reasonable and creative compared to the baseline.

## Usage

1. clone project
2. cd test
3. python run.py
