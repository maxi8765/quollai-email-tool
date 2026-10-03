# App Portfolio Summary

**Comprehensive human-readable edition · Ian Maxwell · 3 October 2026**

This catalogue documents 83 deployed applications, prototypes, research systems, supporting tools and specification-stage projects. It is written for a reader who has never seen the software before: each entry explains what the app is, why it exists and what a user actually does with it. Sources appear directly beneath each entry.

## AI, LLM and reasoning systems

### Workflow Wizard
Workflow Wizard was an early environment for experimenting with structured ways of instructing large language models. Instead of simply typing a question into ChatGPT and hoping for a good answer, it allowed prompts to be broken into controlled elements such as role, tone, format and constraints. It was primarily a research and testing tool: the purpose was to determine whether deliberately structured prompts produced better and more repeatable results than ordinary conversational prompting. The work became an important precursor to PromptSmith.

**Source:** R&D project record; historical deployment: https://workflow-wizard-maxwellian.replit.app/

### QuollAI v1
QuollAI v1 was an experimental writing assistant designed to analyse human communication rather than simply rewrite it. A user could give it an email or other piece of writing and the system would examine characteristics such as cognitive bias, tone, personal voice and cultural sensitivity, then suggest or generate an improved version. The project was also used as a practical test of whether general-purpose LLMs could be wrapped in enough software and structured prompting to perform a specialised commercial task. It included browser-interface work, API integrations and supporting Python analysis tools.

**Source:** Uploaded QuollAI project material within PromptSmith App.zip; R&D project record.

### QuollAI v2 / Sales Email Tool
QuollAI v2 narrowed the original idea to a more specific commercial problem: improving sales emails. A salesperson could enter an email and have the app assess it against a structured set of psychological, tonal and cultural parameters, then rewrite it according to those controls. Rather than asking an LLM vaguely to “make this email better”, QuollAI attempted to make the variables controlling the rewrite explicit. It became a useful testbed for the structured-prompt concepts that later developed into PromptSmith.

**Source:** GitHub: https://github.com/maxi8765/quollai-email-tool ; uploaded QuollAI source material.

### QuollAI data tooling
QuollAI also produced a collection of supporting software for preparing and evaluating email data. This included programs for extracting emails, validating datasets and scoring material for characteristics such as bias. These were not user-facing products, but they were important research infrastructure because they provided repeatable data on which the QuollAI concepts could be developed and tested.

**Source:** Uploaded QuollAI data/tooling material within PromptSmith App.zip.

### PromptSmith v1
PromptSmith v1 was designed to help an ordinary user create a much more precise instruction for an LLM without needing to understand prompt engineering. The user described what they wanted, then selected explicit controls such as the desired role, tone, audience, framing, constraints and output format. PromptSmith assembled those choices into a structured prompt which could then be copied into ChatGPT, Claude or another model. Its purpose was to move prompt construction from an informal writing exercise towards a repeatable engineering process.

**Source:** Replit: https://replit.com/@maxwellian/PromptSmith ; PromptSmith App.zip.

### PromptSmith v2
PromptSmith v2 moved beyond being a prompt generator and became an LLM application in its own right. Instead of generating a prompt for the user to copy elsewhere, the system could build the structured prompt, send it directly to an OpenAI model and display the resulting answer. This made it possible to record prompts and outputs, repeat tests, change individual controls and compare results systematically. The version was therefore both a practical application and a research platform for measuring whether different prompt structures actually changed model performance.

**Source:** Replit: https://replit.com/@maxwellian/PromptSmith-v2 ; PromptSmith App.zip.

### PromptSmith v3
PromptSmith v3 extended the system towards testing prompting techniques across different models and external AI services rather than treating one OpenAI model as the target. The underlying idea remained the same: describe the desired behaviour explicitly, construct a structured instruction and observe the result. The wider purpose was to determine whether the PromptSmith control framework represented a general method for directing LLMs rather than a collection of tricks that worked with one particular model.

**Source:** Replit: https://replit.com/@maxwellian/PromptSmith-v3 ; PromptSmith App.zip.

### Image PromptSmith
Image PromptSmith applied the same structured-control philosophy to generative images. Instead of relying on a loose visual description, the proposed application separated an image request into explicit elements such as subject, composition, style, lighting, viewpoint and other visual constraints. An LLM could preprocess those choices into a carefully constructed prompt for an image generator. The project reached detailed specification stage and was intended to test whether the PromptSmith method transferred from language generation to visual generation.

**Source:** Image PromptSmith specification in PromptSmith App.zip.

### Meta-Cognitive Prompting benchmark harness
This was experimental software built to test prompting methods quantitatively rather than relying on subjective impressions. It repeatedly sent the same underlying tasks to an LLM using different prompting strategies, recorded the results and allowed those results to be compared on measures such as precision, compliance, accuracy and clarity. One major experiment involved thousands of individual API runs. Its purpose was to determine experimentally whether structured prompting methods produced statistically meaningful improvements.

**Source:** PromptSmith App.zip experiment code and results; Meta-Cognitive Prompting paper.

### The Half-Life of Truth experimental system
The Half-Life of Truth software investigated what happens when information is repeatedly processed by an LLM. Material was generated or summarised, then that output was fed into another generation or summarisation step, and the process was repeated. The system allowed changes in factual content and meaning to be tracked across generations. The research was intended to distinguish simple factual errors from the more subtle loss or mutation of meaning that occurs as machine-generated information is repeatedly transformed.

**Source:** Half-Life project and code in PromptSmith App.zip; published research paper.

### Innovation Engine
Innovation Engine was an experimental system intended to use LLMs for structured invention rather than ordinary brainstorming. It explored several approaches, including starting with a known technology and looking for new applications, starting with a problem and looking across unrelated technologies for solutions, and identifying opportunities by comparing functions across industries. The aim was to turn innovation into a defined process that software could repeatedly execute rather than simply asking a chatbot for ideas.

**Source:** Innovation Engine project, structured design and framework paper in PromptSmith App.zip.

### Prompt Intelligence Loop
The Prompt Intelligence Loop was a feedback mechanism developed around the Innovation Engine and PromptSmith work. Instead of treating every LLM interaction as an isolated event, the system recorded prompts, responses and assessments of those responses and used that information to influence later prompts. Its purpose was to investigate whether an application could gradually improve the way it asked questions without retraining the underlying model. It is best understood as a component of the broader research program rather than a standalone consumer application.

**Source:** Innovation Engine source material and PromptSmith R&D record.

### Time Enough to Think
Time Enough to Think is an experimental reasoning architecture built around an LLM. Its central idea is that a model should not simply receive a difficult question and immediately produce an answer. Software around the model maintains an explicit working state, constructs provisional explanations, identifies assumptions, seeks evidence, challenges conclusions, revises models and decides when enough reasoning has been performed. Later versions introduced competing hypotheses, evidence provenance, Bayesian belief updates, explicit stopping rules and reusable experience. Previous reasoning lessons are stored in a heuristics database known as the bank, allowing subsequent problems to benefit from earlier ones without changing the underlying LLM.

**Source:** Uploaded Time Enough to Think.zip; project whitepaper and source code.

### Judgement Layer prototype series
The Judgement Layer is the main executable implementation of the Time Enough to Think architecture. Successive versions added more of the machinery needed to turn a single LLM into a controlled reasoning system: explicit models, challenges, quantitative analysis, alternative hypotheses, evidence handling, contradiction detection, Bayesian updating and stopping criteria. Version 0.8.5 represents one of the more developed versions of this experimental line. The series is valuable because it records the evolution of the architecture in working software rather than only as a theoretical proposal.

**Source:** Time Enough to Think.zip, including judgement_layer_v085.py and earlier versions.

### Sequential Evidence Test harness
This is a testing environment for one specific question within Time Enough to Think: whether the reasoning system changes its beliefs sensibly as new evidence arrives. Evidence is introduced sequentially rather than all at once, allowing the system's hypotheses and confidence to be examined after each new item. The harness makes it possible to detect problems such as double-counting correlated evidence, overreacting to weak evidence or failing to revise an earlier conclusion.

**Source:** Time Enough to Think.zip, including sequential_evidence_test_v03.py.

### Experience Cache / reasoning fingerprints
The Experience Cache is the persistent-memory component of Time Enough to Think. It stores compact records of reasoning patterns, successful or unsuccessful approaches and reusable heuristics derived from previous problems. Those records, sometimes represented as reasoning fingerprints, can be consulted when a later problem resembles an earlier one. The purpose is to give an otherwise stateless LLM-based system a primitive form of accumulated experience.

**Source:** Time Enough to Think.zip, including experience_cache_v071 and reasoning_fingerprints_v2.json.

### WordPress Crawl
WordPress Crawl was developed to collect material from the Offshore Westerly blog for experiments in reasoning and precedent. Rather than using the writing simply as text for a language model, the project treats it as a corpus containing many examples of arguments, decisions, assumptions and ways of analysing problems. The crawler automates acquisition of that material so it can be processed systematically.

**Source:** Time Enough to Think.zip, WordPress Crawl source folder.

### WordPress Download
WordPress Download is a supporting utility that retrieves and normalises material collected from the WordPress site. Its job is largely infrastructural: get the source material into a consistent local form that other programs can analyse. It sits between web acquisition and the reasoning-analysis stages of the Time Enough work.

**Source:** Time Enough to Think.zip, WordPress Download source folder.

### WordPress Reasoning
WordPress Reasoning processes the collected blog material to identify useful reasoning artefacts and precedents. The broader objective is to extract reusable patterns such as “when this type of situation occurs, this line of reasoning proved useful” rather than merely storing passages of prose. These artefacts can then contribute to the Time Enough precedent and heuristic systems.

**Source:** Time Enough to Think.zip, WordPress Reasoning source folder.

### Gertrude - R&D Tax
Gertrude is an AI-assisted system for preparing R&D tax documentation. A user creates an R&D project, uploads technical material and other supporting documents and then asks the system to help complete the structured descriptions required for an R&D claim. The LLM is given the project material rather than being asked to invent generic answers, so the aim is to turn a messy collection of engineering work into a coherent, evidence-based R&D record. It was built to reduce the substantial manual effort involved in converting real technical development into formal regulatory documentation.

**Source:** Replit: https://replit.com/@maxwellian/Gertrude-RandD-Tax ; uploaded Gertrude.zip.

### Gertrude - National Phase
This version of Gertrude applies the same document-centred architecture to a broader structured-document workflow. Users organise project and reference documents, retrieve relevant information from them and generate editable formal material grounded in those sources. The project demonstrates the general Gertrude idea: use an LLM inside a controlled document process rather than simply asking a chatbot to draft from scratch.

**Source:** Replit: https://replit.com/@maxwellian/Gertrude-National-Phase

### Limpid Logic
Limpid Logic exists as a Replit project, but the surviving material available through the current connector does not establish its function with enough confidence to describe it accurately. It remains in the catalogue so the project is not lost, but no purpose has been invented from the name alone.

**Source:** Replit: https://replit.com/@maxwellian/Limpid-Logic

### Stakeholder Sync
Stakeholder Sync helps prepare regular investor or stakeholder updates. A user provides company information and can bring in information from connected business systems such as Slack, accounting or email sources; the app then uses Claude to turn that material into a coherent update. Individual sections can be regenerated or edited before the update is sent. Its purpose is to reduce the work required to convert scattered operational information into a useful recurring communication.

**Source:** Replit: https://replit.com/@maxwellian/Stakeholder-Sync

### Slack Triage Bot
Slack Triage Bot is designed for people who receive more Slack traffic than they can reasonably monitor. It watches messages and mentions, removes obvious noise and uses an LLM to decide whether a message appears to require action, how urgent it is and why. Important items can then be surfaced as direct alerts rather than requiring the user to read every channel. The app also keeps enough state to avoid repeatedly alerting the user about the same unresolved conversation.

**Source:** Replit: https://replit.com/@maxwellian/Slack-Triage-Bot

### Travel Itinerary Calendar Converter
This app converts travel confirmations into usable calendar entries. A traveller can provide an airline itinerary, PDF or pasted confirmation; the software extracts flight numbers, airports, dates and times, presents them for checking and then creates an ICS calendar file. LLM processing and verification are used to handle the inconsistent formats found in real airline documents. Its purpose is to eliminate manual re-entry of travel details into a calendar.

**Source:** Replit: https://replit.com/@maxwellian/Travel-Itinerary-Calendar-Converter

### Paper Calendar
Paper Calendar is a mobile-oriented calendar application intended to make getting events into a calendar as easy as forwarding the original information. In addition to normal event creation and ICS import/export, a user can give it emails, images or PDFs containing event details and Claude extracts the relevant date, time, place and description. The user can verify the result before it becomes a calendar event. The aim is to bridge the gap between how events arrive in real life and the rigid data fields conventional calendar apps require.

**Source:** Uploaded Paper Calendar.zip; Replit project papercalendar.win: https://replit.com/@maxwellian/papercalendarwin

### Adaptive LLM Education Platform
This project proposes a general education system in which the user begins with a subject rather than a fixed pre-written course. The application would assemble an appropriate curriculum from available material, teach the subject interactively and alter the sequence or depth depending on the learner's demonstrated understanding. The purpose is to use an LLM as the engine of a course while retaining an explicit educational structure around it. The surviving version reached detailed build-plan stage.

**Source:** Uploaded Apps Built with Claude.docx.

### RTT-HLLM: Testing your Humanity
RTT-HLLM is an interactive browser questionnaire presented as a test of human characteristics. Users answer a sequence of questions and receive a result based on those responses, with information panels providing additional context during the test. It is a conventional self-contained web application rather than an LLM-backed questionnaire.

**Source:** GitHub: https://github.com/maxi8765/quiz

## Accordia IP patent pipeline

### Module 0 - Integrated Drafter
The Integrated Drafter turns technical source material into formal patent documents. A user can provide inventor notes, existing patents or technical documents and the system uses Claude to construct a U.S.-style patent application with the expected sections and structure. It can also work in the opposite direction, converting patent material into a more readable white paper or academic paper. Its purpose is to automate much of the repetitive transformation between technical information and highly structured patent documentation.

**Source:** Replit: https://replit.com/@maxwellian/Module-0-integrated-drafter

### Module 0b - Paper Drafter
Paper Drafter is the patent-to-publication part of the drafting system separated into a standalone application. A user uploads patent material and chooses whether the desired result is a white paper or an academic paper, including the relevant academic discipline. Claude then restructures the patent's technical content into the selected form and the result can be exported as a normal document. The app is intended to make technically valuable patent material usable for communication and publication without manually rewriting it.

**Source:** Replit: https://replit.com/@maxwellian/Module-0b-Paper-Drafter

### Module 1 - Patent Infringement Value Assessor
This application answers a commercial question that occurs before expensive patent enforcement work begins: is this patent worth pursuing? A patent is assessed across a structured set of commercial, legal and patent-quality dimensions, including factors affecting enforceability and potential economic value. The system combines LLM analysis, external patent information and deterministic scoring to produce a comparable Commercial Enforcement Score. It is intended to help prioritise a large portfolio so human effort is concentrated on the patents with the strongest apparent enforcement opportunity.

**Source:** Replit: https://replit.com/@maxwellian/Module-1-Patent-Infringement-Value-Assessor

### Module 2 - Potential Infringer Detector
Module 2 tries to determine which real companies and products are worth investigating against a patent. The user supplies a patent and the system analyses what the invention actually covers, searches the relevant technology market and produces a ranked list of candidate companies and products with supporting evidence. It does not attempt to decide infringement conclusively. Its job is to shrink an enormous search space into a manageable list for deeper analysis.

**Source:** Replit: https://replit.com/@maxwellian/Module-2-Potential-Infringer-Detector

### Module 3 - Smoke Detector
Smoke Detector is the next triage stage after candidate discovery. It compares selected patent claims with publicly available information about a candidate product and asks whether there is enough evidence of overlap to justify further investigation. The result is a structured “smoke” assessment rather than a legal conclusion, including element-level evidence and gaps. The objective is to discard weak candidates cheaply before spending time and money constructing full claim charts.

**Source:** Replit: https://replit.com/@maxwellian/Module-3-Smoke-Detector

### Module 23 - Candidate Finder & Infringement Triage
Module 23 combines Modules 2 and 3 into a continuous workflow. It first discovers companies and products that appear relevant to the patent and then automatically passes the promising candidates into preliminary claim analysis. This avoids manually moving information between separate tools and preserves the evidence collected during discovery. Its purpose is to produce a shorter, evidence-backed list of candidates deserving serious infringement analysis.

**Source:** Replit: https://replit.com/@maxwellian/Module-23-Candidate-Finder-and-Infringement-Triage

### Module 4 - Claim Charting
Module 4 performs the detailed evidence organisation required once a candidate has survived initial triage. Each element of a patent claim is compared with evidence about the candidate product and presented in a structured claim chart, including where evidence was found and where it remains missing. Human reviewers can inspect and amend the analysis before exporting formal reports and audit data. The app is designed to turn scattered product evidence into the structured element-by-element analysis required for serious patent enforcement work.

**Source:** Replit: https://replit.com/@maxwellian/Module-4-Claim-Charting

### Accordia SaaS Update
Accordia SaaS Update is the web front end presenting the Accordia patent-analysis service and its individual modules. It explains the patent brokering and IP strategy offering and provides a client-facing path into drafting, valuation, candidate discovery, infringement triage and claim-charting tools. It is primarily the service and portal layer rather than the analytical engine itself.

**Source:** Replit: https://replit.com/@maxwellian/Accordia-SaaS-Update

### Accordia Aggregator
The Aggregator is intended to sit at the end of the Accordia pipeline. Rather than forcing an analyst to read separate exports from patent valuation, candidate discovery, infringement triage and claim charting, it combines those results into a reconciled report. Its purpose is to give a decision-maker a single view of the patent, likely targets, evidence quality and commercial opportunity. The surviving material describes it as a system under development rather than a finished application.

**Source:** Uploaded Apps Built with Claude.docx.

## Quantum computing and education

### Quokka Quantum
Quokka Quantum is an interactive course intended to teach quantum computing by combining explanations with actual computation. It covers the mathematical foundations and major quantum concepts, includes quizzes and exercises and can run quantum programs through Qiskit. An OpenAI-powered tutor can explain material at an appropriate level when the learner becomes stuck. The purpose is to make quantum computing something students can experiment with rather than only read about.

**Source:** GitHub: https://github.com/maxi8765/Quokka

### Quokka
Quokka is a courseware application built around Eigensystems' quantum education material. Students work through a sequence of lectures, coding exercises and assessments while the software records their progress. An AI tutor can answer questions using the course material as context, reducing the need for an instructor to be present for every question. The application is intended to provide a structured educational experience rather than simply exposing a general chatbot to students.

**Source:** Replit: https://replit.com/@maxwellian/Quokka

### Quokka v2
Quokka v2 is a later iteration of the learning platform with improved course navigation, searching, progress management and integrated coding exercises. Its GPT-4o tutor retrieves relevant sections from a local quantum-computing knowledge base before answering, helping keep explanations connected to the curriculum. The objective is a self-contained teaching environment in which course material, practice and tutoring all sit in one system.

**Source:** Replit: https://replit.com/@maxwellian/Quokka-v2

### Quokka Programming App
The Quokka Programming App is closer to a small quantum programming IDE than a course. Users can create or edit quantum programs, inspect a visual representation of the circuit, choose execution parameters and request that the program be run against a device or simulator. The inspected version contains simulated device/execution behaviour as well as the interface. Its purpose is to give students a simple place to experiment with quantum programs without the complexity of a full professional development environment.

**Source:** Replit: https://replit.com/@maxwellian/Quokka-Programming-App

### Quokka Mobile App
The Quokka Mobile App is a Flutter application for setting up and managing physical Quokka devices. A user can discover a device, pair with it, configure Wi-Fi and maintain a list of previously connected Quokkas. It therefore solves the hardware-management part of the Quokka experience rather than providing the main educational course itself.

**Source:** GitHub: https://github.com/maxi8765/Quokka-iOS-

### ZooBall Quantum
ZooBall Quantum teaches quantum concepts through a game rather than through equations alone. Players interact with moving objects and controls representing ideas such as classical state, superposition, entanglement and measurement, progressing through increasingly quantum stages. Scores, lives and explanations provide normal game feedback while the mechanics illustrate the underlying concepts. The objective is to give beginners an intuitive feel for otherwise abstract quantum behaviour.

**Source:** Replit: https://replit.com/@maxwellian/Zooball-Quantum

### ZooBall multistage
This is the conventional game from which the quantum teaching variants developed. The player changes the colour of a bar to match incoming bouncing balls, progressing through ten stages of increasing difficulty. The game records scores, completion times and records. It provided a simple interactive framework that could later be adapted to illustrate quantum concepts.

**Source:** Replit: https://replit.com/@maxwellian/Zooball-multistage

### ZooBall multistage - two player
This version converts ZooBall into a same-device competitive game. Two players independently control their colour-matching bars, accumulate scores across stages and compete for the overall result. It extends the original game mechanics rather than adding an AI or quantum-computing component.

**Source:** Replit: https://replit.com/@maxwellian/Zooball-multistage-two-player

### Foundations of Quantum Computing
Foundations of Quantum Computing is a complete introductory course package created for Eigensystems. It consists of a structured curriculum and 14 interactive HTML teaching modules intended for delivery through the Wix platform. Rather than being a single simulation, it is the educational content layer through which a student can progress from basic concepts towards practical quantum understanding.

**Source:** Uploaded Apps Built with Claude.docx.

### Eigensystems Website
The Eigensystems website is the public-facing site for the company's quantum education, security and consulting activities. It explains the products and research, introduces the team and partners and provides access to product material and purchasing or enquiry routes. Its job is commercial communication rather than quantum computation itself.

**Source:** Replit: https://replit.com/@maxwellian/Eigensystems-Website

### Eigensystems Pipeline
The Eigensystems Pipeline is an internal sales-management system. Staff and partners can record organisations, contacts, products, deal values, sales stages, owners, follow-up dates and notes and then view or export the resulting pipeline. Its purpose is to provide a lightweight CRM tailored to the actual Eigensystems sales process rather than adapting a large general-purpose CRM.

**Source:** Replit: https://replit.com/@maxwellian/Eigensystems-Pipeline

## Race timing and RFID systems

### ScoreHound
ScoreHound is a lightweight race-management and timing application. An organiser creates a race, enters participants and records their finishes; the software calculates elapsed times, pace and placings and can export the resulting data. Early versions included simulated RFID reader connections so the complete workflow could be developed before relying on production hardware. The purpose is to give a small race organiser a much simpler timing system than traditional specialist timing software.

**Source:** Replit: https://replit.com/@maxwellian/ScoreHound

### ScoreHound v2
ScoreHound v2 develops the original concept into a more complete RFID timing system. Participants can be associated with RFID tags and live reads from timing hardware are converted into race finishes and real-time results. Race setup, participant administration and timing therefore take place in the same application. It represents the transition from the original timing demo towards a functioning event system.

**Source:** Replit: https://replit.com/@maxwellian/ScoreHound-v2

### ScoreHound v3
ScoreHound v3 extends the platform for running, cycling and swimming events and supports live RFID timing information delivered over WebSockets. It can manage participants, calculate results and export timing data, while a Capacitor wrapper allows the web application to operate as an Android app. The aim is to provide the functionality of conventional race-timing software in a lightweight mobile-first product.

**Source:** Replit: https://replit.com/@maxwellian/ScoreHound-v3 ; GitHub: https://github.com/maxi8765/ScoreHound-v3

### ScoreHound AWS only
This version deliberately simplifies the timing architecture by using the AWS WebSocket connection as the sole live timing-data path. Organisers can manage the race and participants, receive RFID finishes, add manual finishes where necessary and import or export CSV data. Removing alternative reader paths reduces configuration complexity and makes the software easier to deploy against the ONETIME cloud infrastructure.

**Source:** Replit: https://replit.com/@maxwellian/ScoreHound-AWS-only

### Trident Replay
Trident Replay is a diagnostic and operational tool for looking backwards at timing data as well as watching it live. An operator can request historical reads for selected readers and time periods or connect to the WebSocket feed to capture new reads. The resulting data can be stored locally or exported as CSV or JSON. It is useful for investigating timing problems, reconstructing races and testing the cloud timing infrastructure.

**Source:** Replit project Replay: https://replit.com/@maxwellian/Replay

### ONETIME Status
ONETIME Status is a monitoring dashboard for deployed RFID readers. Rather than waiting for a timer to report that a device has stopped working, the application displays information such as last contact time, firmware, battery and power state, clock information, tag counts, cellular signal and temperature. The purpose is remote operational awareness: an operator should be able to see whether readers in the field are alive and healthy before or during an event.

**Source:** Replit project Status: https://replit.com/@maxwellian/Status

### Onetime Reader Management
Onetime Reader Management is the configuration and control application for the Decoder2 RFID reader. It allows an operator to connect to a reader, inspect its condition, change settings and collect timing reads using either local communications or the ONETIME cloud architecture. Race information and reader telemetry can be handled in the same mobile-oriented interface. It is effectively the field-management console for the timing hardware.

**Source:** Replit: https://replit.com/@maxwellian/Onetime-Reader-Management ; GitHub: https://github.com/maxi8765/Onetime-Reader-Management

### ONETIME/Trident RFID WebSocket Testing Application
This is a developer and diagnostic utility rather than an end-user timing product. It lets a user enter WebSocket credentials and device information, establish a connection and inspect the messages being received in real time. Connection logs and raw timing data make it useful when commissioning readers or diagnosing communications problems between the hardware and cloud services.

**Source:** GitHub: https://github.com/maxi8765/rfid-websocket-app

### TinyTag
TinyTag is an RFID timing prototype combining reader control, participant registration and timing processing in one browser interface. Users can associate RFID tags with bib numbers and participant information, import and export those records as CSV and inspect live tag reads and calculated results. Some reader behaviours are simulated, showing that the project was also used to prototype the workflow before final hardware integration.

**Source:** GitHub: https://github.com/maxi8765/tinytag

### Trident Homepage
The Trident Homepage is the public product site for Trident race-timing equipment. It explains the available equipment, compares products, presents technical specifications and provides an enquiry mechanism. Its role is to help potential timing customers understand and purchase the hardware rather than to perform race timing itself.

**Source:** Replit: https://replit.com/@maxwellian/Trident-Homepage ; GitHub: https://github.com/maxi8765/Trident-Homepage

### Quadrant Sports Website
The Quadrant Sports site presents the newer range of UHF and active-HF race-timing equipment. Visitors can browse and filter products, examine specifications and compatibility information and submit quote or support enquiries. It functions as the commercial catalogue and customer-information layer for the timing business.

**Source:** Replit: https://replit.com/@maxwellian/Quadrant-Sports-Website

### Onetime/Trident Pipeline
This application is a purpose-built sales CRM for the ONETIME and Trident businesses. Users create opportunities, associate them with customers and contacts, add products, quantities, pricing and discounts and move the deals through defined sales stages. Notes, attachments and reporting keep the sales history together. It was designed to make the actual timing-equipment sales pipeline visible without the complexity of a large CRM platform.

**Source:** Replit: https://replit.com/@maxwellian/OnetimeTrident-Pipeline

### Onemanager
The Replit project named Onemanager contains a race-timing application closely related to ScoreHound rather than a distinct generic management system. It manages races, participants and RFID timing data and produces elapsed times, progress information and CSV results. It is retained separately in the catalogue because it exists as a distinct project even though its functionality substantially overlaps the ScoreHound line.

**Source:** Replit: https://replit.com/@maxwellian/Onemanager

## Web apps, PWAs and practical utilities

### Container Log - Replit version
Container Log solves the mundane problem of remembering what is stored in boxes and containers. A user attaches a numbered or QR-coded label to a container, scans it with the phone and records a description, photograph and optional expiry information. Later, the code can be scanned again to retrieve the contents without opening the box. Backup and reminder features make it suitable for ordinary household or small-business storage rather than formal warehouse management.

**Source:** Replit: https://replit.com/@maxwellian/Container-Log

### Container Log - GitHub Pages version
The GitHub Pages version applies the same idea as a lightweight offline-first PWA that does not require a user account. A phone can scan QR or barcode labels and associate them with stored-container information, with much of the application operating locally. The design deliberately avoids the overhead of a conventional cloud inventory system for a task that should be quick and simple.

**Source:** GitHub: https://github.com/maxi8765/containerlog ; live app: https://maxi8765.github.io/containerlog/

### ChargerGuard Android App
ChargerGuard is intended to stop people leaving phone chargers behind in hotel rooms, airports and other temporary locations. A small Bluetooth beacon stays with the charger; after the phone is unplugged, the app watches for that beacon and alerts the user if it disappears for longer than the configured delay. Home Wi-Fi and other settings can suppress unnecessary warnings. The product idea is deliberately about separation detection rather than tracking the charger's location.

**Source:** Replit: https://replit.com/@maxwellian/ChargerGuard-Android-App

### Image Merger PDF
Image Merger PDF is a small utility for turning a folder of images into a single A4 PDF. It accepts common image formats, lays them out as document pages and, when necessary, progressively adjusts JPEG quality and resolution to keep the finished PDF below a target file size. It was built to automate a repetitive document-preparation task rather than provide a general PDF editor.

**Source:** Replit: https://replit.com/@maxwellian/Image-Merger-Pdf

### House Visitor Companion
House Visitor Companion is a mobile-friendly instruction manual for guests staying at a particular house. Instead of sending separate messages about entry, parking, Wi-Fi, nearby shops and household details, the host can put everything into one simple web app containing text, photographs and map links. Its purpose is to answer the routine questions a visitor has before and during a stay.

**Source:** Replit: https://replit.com/@maxwellian/House-Visitor-Companion

### Corona Finder
Corona Finder is a deliberately specialised venue finder: it helps locate bars that serve Corona beer and records whether they have it bottled, on tap, both or neither. Users can search by location or name, apply amenity filters, add or correct venues and view them on an OpenStreetMap map. It demonstrates the useful simplicity of building a dedicated app for one very specific preference instead of depending on generic venue-review services.

**Source:** Replit: https://replit.com/@maxwellian/CoronaFinder

### Calendar
Calendar is a deliberately simple browser-based calendar. Users can move between months, add and remove events and import existing events from CSV or ICS files. Data is handled locally in the browser, keeping the application lightweight. It is useful where a basic personal calendar is preferable to the account, syncing and interface complexity of a large calendar service.

**Source:** GitHub: https://github.com/maxi8765/Calendar

### CompMax
CompMax is a compensation-negotiation calculator for jobs where the package contains both salary and equity. Rather than treating an offer as a fixed salary number, the application lets the parties explore different combinations of cash and ownership while preserving the overall economic logic of the offer. It is particularly relevant to startups and technology companies where equity can be a material part of employee compensation.

**Source:** GitHub: https://github.com/maxi8765/CompMax2

### PaintScape
PaintScape is a straightforward marketing website for a residential and commercial painting business. It explains the services and geographical coverage, shows previous projects and testimonials and gives prospective customers a way to understand the business before making contact. It is a conventional business website rather than an application with significant backend logic.

**Source:** Replit: https://replit.com/@maxwellian/PaintScape

### Kin Kin fire permit app / PyroCheck
This application digitises the process of applying for a local burn permit. The applicant enters their identity and contact details, the property address, the purpose of the burn and supporting photographs; the information is then assembled and delivered to the responsible fire warden. A static web/PWA front end and a Python Flask email backend were explored in different versions. The objective is to replace an informal paper, telephone or email process with a consistent application form that works well on a phone.

**Source:** GitHub backend: https://github.com/maxi8765/pyrocheck ; uploaded Robs Form.zip and Apps Built with Claude.docx.

### Turtleman
Turtleman is the publishing site for the Turtleman satirical comic series. It organises the comics into browsable volumes and provides printable PDF issues covering subjects such as AI, business, travel, language and technology. The website also includes the normal indexing, metadata and SEO work required to make the archive discoverable. Its purpose is primarily publishing and preserving the growing comic collection.

**Source:** GitHub: https://github.com/maxi8765/turtleman ; live site: https://maxi8765.github.io/turtleman/

### Vivian Control
Vivian Control is an experimental browser-based control-console interface styled like an industrial equipment panel. It contains status indicators, numerical readouts, sliders, toggles and a prominent stasis control, allowing different control concepts and interface behaviours to be explored in a single screen. The surviving version demonstrates the console itself; integration with an external machine or service was not verified.

**Source:** GitHub: https://github.com/maxi8765/Vivian

### Semonides Classifier
The Semonides Classifier is an interactive humorous questionnaire based on the ancient poet Semonides' taxonomy of women. A user answers a sequence of questions and the software maps those responses to one of the classifications, then displays the associated result and explanation. It is a self-contained entertainment and literary-history web application rather than an AI system.

**Source:** GitHub: https://github.com/maxi8765/Semonides-

## Games and interactive experiments

### CrypticA
CrypticA is a word-transformation puzzle influenced by the combination mechanics of games such as Infinite Craft. The player begins with one word and must reach a target word in a limited number of moves by combining it with words from a small bank, with only predefined transformations accepted. Later versions introduced shuffled banks, daily puzzle data, undo and clear win/loss feedback. The challenge is to infer the hidden semantic pathway rather than simply guess a word.

**Source:** GitHub: https://github.com/maxi8765/CrypticA ; Apps Built with Claude.docx.

### PoopQuest
PoopQuest turns bowel tracking into a simple game for a child. It combines a toilet timer and bowel-movement record with quizzes, streaks, badges and scores so that an otherwise tedious health routine feels more like a game. Records can be stored and exported for later review. The practical objective is to encourage consistent participation in the routine rather than provide medical diagnosis.

**Source:** Replit: https://replit.com/@maxwellian/PoopQuest

### Norwich Quest
Norwich Quest is a location-aware walking game built around visiting five Norwich landmarks. The phone uses GPS and orientation sensors to show how far away the next destination is and which direction to walk, and the user checks in when close enough. Progress is saved locally. The app turns a day of sightseeing into a simple physical quest rather than a conventional guided tour.

**Source:** Replit: https://replit.com/@maxwellian/Norwich-Quest

### Amsterdam Quest
Amsterdam Quest applies the same idea to Amsterdam. A family follows a sequence of landmarks from Amsterdam Centraal, using live GPS distance, compass directions and check-ins rather than a prescribed guided-tour interface. The purpose is to make walking around the city into a small self-directed game.

**Source:** Replit: https://replit.com/@maxwellian/Amsterdam-Quest

### Istanbul Quest
Istanbul Quest is the Istanbul version of the location-based walking game. It guides a child or family between selected landmarks, shows live distance and direction and records completed visits. As with the other Quest apps, the software provides enough structure to make exploration engaging without trying to replace a map or detailed travel guide.

**Source:** Replit: https://replit.com/@maxwellian/Istanbul-Quest

### ZooBall specification
The ZooBall specification describes the broader educational concept behind the playable ZooBall implementations. The idea is to use familiar game mechanics to teach progressively less intuitive quantum behaviours, allowing a learner to experience differences between classical and quantum rules rather than merely reading definitions. The specification records the educational intent that sits behind the working game prototypes.

**Source:** Apps Built with Claude.docx; playable ZooBall Replit projects above.

## Additional experimental and specification-stage systems

### Atomix Lab
Atomix Lab is a proposed chemistry-learning application for roughly school-age learners. Students drag atoms from an interactive periodic table onto a workspace and attempt to construct molecules, while the software checks concepts such as valency, charge balance and bonding and reports whether the result is stable, unstable or unknown. Challenges and quizzes turn the chemical rules into an exploratory game. The aim is to let students learn molecular structure by building things and receiving immediate feedback.

**Source:** Atomix Lab specification in uploaded Apps.zip.

### Deterministic LDV Converter
The Deterministic LDV Converter explores whether complex English can be represented using the restricted Longman Defining Vocabulary without losing the ability to reconstruct the original text. Words outside the permitted vocabulary are encoded with reversible tags while punctuation, whitespace and other information are carefully preserved. Because conversion is deterministic, the same input should always produce the same output and the source can be reconstructed exactly. Potential uses include controlled-language research, patent processing and experiments measuring how much linguistic complexity an LLM actually requires.

**Source:** Uploaded LDV LLM.zip, including LDV Converter.docx and Deterministic LDV converter.docx.

### LDV Patent Translation Pipeline
This project applies the reversible LDV concept specifically to patent documents, where losing a chemical name, number, claim term or other precise expression would be unacceptable. The proposed pipeline first identifies and protects critical entities, rewrites only the surrounding connective language into the restricted vocabulary and maintains an explicit alignment with the source. A decoder reconstructs the original document and automated validation tests whether anything has changed. The purpose is to investigate whether legally and technically dense patent language can be simplified for machine processing without destroying the information needed to recover the original text.

**Source:** Uploaded LDV LLM.zip, Ldv Patent Pipeline Plan.docx.
