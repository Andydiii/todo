smtpClient change depdens on envs -> build app -> publish -> backup old folder -> replace server files with bin/dev_armsclient -> test before notify clients 

first one is for PROD.
smtpClient.Host = "eesrelay.gov.on.ca";
//smtpClient.Host = "eesUATrelay.gov.on.ca";
/smtpClient.Host = "eesDEVrelay.gov.on.ca";



CICD
yml file to set up the task and base branch and target folder
as our app is on the server and devOps cannot copy changed files onto our app folder on the server
so we have a self_hosted agent hosted in our server, and configured in Azure Devops so that once developers commit to the base branch, it triggers the CICD pipeline automatically to the arms_dev folder on server