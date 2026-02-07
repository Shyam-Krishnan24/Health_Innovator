Health Innovators – AI-Based IVR Healthcare Triage System
 Project Overview

  Health Innovators is an AI-powered Interactive Voice Response (IVR) simulation system designed to efficiently triage healthcare requests.
This project is temporarily implemented as a locally running service for development and testing purposes and does not operate through real phone calls.
The system simulates IVR interactions via a local interface (CLI / local server) and classifies cases as Emergency or Non-Emergency, providing appropriate actions such as appointment booking or medical guidance.

 Objectives

  --->Simulate healthcare IVR call triaging
  --->Prioritize emergency cases using AI logic
  --->Reduce manual workload through automation
  --->Validate decision-making flow in a local environment

 System Features

  --->Locally simulated IVR interaction
  --->Emergency and non-emergency classification
  --->AI-driven decision engine
  --->Token-based appointment confirmation
  --->Guided symptom and patient detail collection
  --->Fully automated decision flow (no real telephony)

Interaction Flow (Local IVR Simulation)
System Start

  1. Display a greeting message
  2. Prompt user options:
          --->Press 1 – Emergency
          --->Press 2 – Non-Emergency

 Emergency Flow (Option 1)

The system performs the following steps:
  1. Collect patient issue (text or keypad-style input)
  2. Collect personal details:
          --->Name
          --->Phone number
  3. Automatically prioritize appointment booking
  4. Confirm entered details
  5. Generate a unique token number
  6. Display and store the token for the patient
  7. End the session

 Non-Emergency Flow (Option 2)

The system collects:

  1. Issue description
  2. Symptoms (preloaded list: 1–9)
  3. Age
  4. Gender:
      --->Press 1 – Male
      --->Press 2 – Female
  5. Patient Status:
      --->Press 1 – Normal
      --->Press 2 – Child
      --->Press 3 – Pregnant
  6. Medication background details

 AI Decision Engine

The AI module analyzes all collected inputs and classifies the case as:
      --->Emergency
      --->Non-Emergency

(This classification is based on predefined rules or AI logic implemented for local execution.)

 If Classified as Emergency

  1. Clearly explain why the case is considered an emergency
  2. Provide options:
      --->Press 1 – Book Appointment
      --->Press 2 – End Session

  3. If booking is selected:
      --->Collect remaining details
      --->Confirm appointment
      --->End session

 If Classified as Non-Emergency

  1. Provide appropriate guidance or next steps
  2. Suggest self-care or follow-up recommendations
  3. End session
