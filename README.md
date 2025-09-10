📑 Project Report

Task Automation with Microsoft Teams, Google Sheets, and n8n
Timeline: May 2025 – July 2025

🎯 Objective

To design and implement an automated workflow that:

-Logs into Microsoft Teams reliably.

-Sends notifications and messages automatically to groups or individuals.

-Integrates Google Sheets updates as workflow triggers.

-Uses n8n as the orchestration platform, running locally in Docker.

🛠 Work Completed
1. Automation Foundations (May 2025)

-Built and refined Python scripts for automatic Microsoft Teams login.

-Transitioned from undetected_chromedriver to standard Selenium + ChromeDriver for stability.

-Implemented cookie-based session management to reduce repeated logins and 2FA prompts.

-Debugged and stabilized core scripts (get_report.py, get_message.py, botMSTeam.py).

-Ported scripts to Google Colab for cloud-based execution.

2. Workflow Integrations (June 2025)

-Google Services

-Connected n8n with Google Drive and Google Sheets.

-Configured authentication and API access.

-Added Gmail notifications on Google Sheets updates.

-Microsoft Teams

-Initial experiments with webhooks (found not feasible with personal accounts).

-Created Azure app for OAuth2, enabling n8n → MS Teams integration.

-Automated group chat notifications from Google Sheets via n8n.

Other Tests

-Evaluated Trello as an alternative integration (rolled back after testing).

-Debugged HTTPS node and cookie handling in n8n workflow.

3. Advanced Messaging Features (Late June – July 2025)

-Enhanced automation to send private messages to individuals instead of group chats.

-Developed Python scripts to:

-Create new chats, enter recipient emails, and send messages.

-Improve reliability of input handling (navigating MS Teams’ JavaScript-driven UI).

-Iterated multiple times on handling recipient identification:

-From email entry → name-based search → suggestion box selection.

-Verified direct message sending (tested with user “Ray”).

-Finalized end-to-end integration:

-Google Sheets update → triggers n8n workflow → runs Python scripts → sends MS Teams messages automatically.

✅ Results

-Stable Login Automation: One-time login with cookies successfully replaces repeated authentications.

-Google Sheets Integration: Every new line in Sheets triggers an automated workflow.

-MS Teams Integration: Messages can now be sent automatically to group chats or individuals (condition: prior connection in MS Teams).

-Workflow Reliability: n8n workflow remains continuously active and operational, orchestrating the process.

🔮 Next Steps

-Expand User Targeting

- handling of new recipients who are not yet connected on MS Teams.

-Optimize Error Handling

-Add retry logic and error logging for Selenium-based scripts.

-Production Deployment

-Move from local Docker to a server/VM for 24/7 availability.

-Security & Maintainability

-Store credentials and secrets using environment variables or a secure vault.

-Replace cookie/session hacks with official Microsoft Graph API (long-term).



To activate:
#download Docker and run this in terminal before every run
docker run -it \
  -v ~/.n8n:/home/node/.n8n \
  -v ~/Desktop:/scripts \
  -p 5678:5678 \
  n8nio/n8n

#run this in terminal every time to start or saved the changes.
python3 /Users/vietnguyen/Desktop/send_teams_message.py --host=0.0.0.0 --port=5001


#links to workflow ( has to be activate steps above)
http://localhost:5678
http://localhost:5678/webhook-test/send-teams-task
