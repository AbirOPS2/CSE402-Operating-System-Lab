# Lab 07

## Experiment
Disk Scheduling Algorithms - SSTF (Shortest Seek Time First) and FCFS (First Come First Serve)

## Objective
- To implement SSTF and FCFS Disk Scheduling Algorithms
- To calculate total head movement and the seek sequence for each
- To compare the performance of SSTF and FCFS

## Given Data
- Request Queue: [3, 60, 10, 25, 30, 4]
- Initial Head Position: 41

## Result
| Algorithm | Seek Sequence | Total Head Movement |
|-----------|---------------|---------------------|
| SSTF | 30, 25, 10, 4, 3, 60 | 95 |
| FCFS | 3, 60, 10, 25, 30, 4 | 191 |

SSTF reduces head movement by 96 tracks (approx. 50.26%).

## Files
- Source Code
- Lab Report

## Language
Python

## Submitted
Week 7
