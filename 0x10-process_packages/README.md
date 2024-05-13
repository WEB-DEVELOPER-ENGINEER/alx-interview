# Network Packet Processing Simulation

This program simulates the processing of network packets received in a series. It considers a single processor and a fixed-size buffer.

## Problem Description

The task is to simulate the processing of incoming network packets. Each packet has an arrival time and a processing time. Packets are processed in the order of their arrival (queue data structure). If the buffer is full when a packet arrives, it is dropped.

## Input Format
The first line of the input contains the size S of the buffer and the number n of incoming network packets. Each of the next n lines contains two numbers. i-th line contains the time of arrival Ai and the processing time Pi (both in milliseconds) of the i-th packet. It is guaranteed that the sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).

## Output Format

For each packet, output either the moment of time (in milliseconds) when the processor began processing it or -1 if the packet was dropped.

## Description of Solution

1. **process_packets function**: This function simulates the processing of network packets based on the given buffer size and a list of packets. It iterates through each packet, checking if it can be processed immediately or needs to wait in the buffer. If the buffer is full, the packet is dropped. Otherwise, the start time of packet processing is recorded, and the packet is added to the buffer. The function returns a list of start times for each packet, or -1 if the packet was dropped.

2. **main function**: This function handles the input/output operations. It reads the buffer size and the number of packets from the input, then processes each packet using the `process_packets` function. Finally, it prints the start times for each packet.
