ArchiShield

by ArchiTechs — Where Architecture meets Technology

AI-powered tool that detects and fixes data loss in IFC BIM models across 5 integrity levels, with NBC 2016 compliance checking and a Groq-powered assistant.


What it does

Every IFC export silently loses data — walls lose their type, properties vanish, geometry disappears. ArchiShield scans any IFC file and measures this loss across 5 levels, scores the model's quality, checks NBC 2016 compliance, and answers natural-language questions about the model using AI.

Features


5-level data loss analysis — semantic, property, quantity, relationship, geometry
Quality scoring — 0-100 weighted score with severity classification
13 analysis modules — proxy classification, Pset analysis, storey quality, 3D viewer, issue heatmap, rule validation, NBC 2016 compliance, correction suggestions, BCF export, version comparison, geometry integrity
AI assistant — ask plain-English questions about your model, grounded in live-scanned data (powered by Groq / Llama 3.3 70B), with voice input
Role-adaptive interface — 5 distinct dashboards for Architect, BIM Manager, Contractor, Facility Manager, and Student — same data, different layout and language for each
Technical / Business / Full view modes — switch between IFC jargon and plain English on any page
Cloud storage — private per-user IFC file storage via Supabase


Tech stack

LayerTechnologyFrontendStreamlitIFC parsingifcopenshellAIGroq API (Llama 3.3 70B)StorageSupabaseReportsfpdf, pandas

Setup

See GROQ_SETUP.md for AI assistant setup (free, no credit card).

bashpip install streamlit ifcopenshell pandas fpdf groq supabase
streamlit run Back.py

A sample IFC file (sample_model.ifc) is included for quick testing.

Project structure

ArchiShield/
├── Back.py / Home.py        — entry points
├── theme.py                 — role-based theming
├── role_ui.py                — role-adaptive UI components
├── view_mode.py               — Technical/Business/Full toggle
├── supabase_storage.py         — cloud storage
├── page_runner.py               — multipage routing
├── pages/                        — Streamlit native pages
└── legacy_pages/                  — 13 analysis modules + AI assistant

Roadmap


ML-based proxy classifier (LightGBM)
Team / collaborative workspaces
BIM Clash Detector and Quantity Extractor (next ArchiTechs products)
Public API



Built for a hackathon as a working MVP — not just a concept.
